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
| dd3d0990-f884-3ab9-9ad0-9354d92c5879 | -4.08949 | -41.62589 | 2024-12-18 12:44:00 | TERRA_M-T | BRASILEIRA | PIAUÍ | Brasil | 2201960 | 22 | 33 | nan | nan | nan | Caatinga | 23.4 |
| 2989e28a-6384-3872-b79a-0b843afea65d | -3.86278 | -47.03249 | 2024-12-18 12:44:00 | TERRA_M-T | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 10.9 |
| ba917bac-1d92-3f68-b947-f3b9f7652df8 | -2.13553 | -46.46573 | 2024-12-18 12:44:00 | TERRA_M-T | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 26893741-0584-332f-bfa8-2601c776b787 | -6.26688 | -42.16478 | 2024-12-18 12:44:00 | TERRA_M-T | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 17.5 |
| bbee440d-5a2c-379d-8e5d-2c8bac9ab26b | -5.09238 | -43.91052 | 2024-12-18 12:44:00 | TERRA_M-T | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 15.7 |
| afa606fd-cf70-3676-a892-729e31097b0c | -0.86567 | -47.85205 | 2024-12-18 12:44:00 | TERRA_M-T | CURUÇÁ | PARÁ | Brasil | 1502905 | 15 | 33 | nan | nan | nan | Amazônia | 13.7 |
| 78208034-1bb1-3b1a-b407-b805bb6a3e6b | -6.95263 | -42.99376 | 2024-12-18 12:44:00 | TERRA_M-T | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 49.5 |
| ae032eec-455e-3315-85b7-611df1a3438d | -3.51869 | -41.95893 | 2024-12-18 12:44:00 | TERRA_M-T | CAXINGÓ | PIAUÍ | Brasil | 2202653 | 22 | 33 | nan | nan | nan | Caatinga | 28.6 |
| 0709aff6-488a-3e13-b3f3-026af0b4df75 | -1.77076 | -46.05198 | 2024-12-18 12:44:00 | TERRA_M-T | JUNCO DO MARANHÃO | MARANHÃO | Brasil | 2105658 | 21 | 33 | nan | nan | nan | Amazônia | 13.4 |
| 6fb704c1-ccbe-3949-ac7f-a035e5ee07fe | -4.08336 | -44.59871 | 2024-12-18 12:44:00 | TERRA_M-T | SÃO MATEUS DO MARANHÃO | MARANHÃO | Brasil | 2111508 | 21 | 33 | nan | nan | nan | Cerrado | 8.4 |
| b6235a66-6a39-3849-ac0f-5eb82c695e9e | -1.74473 | -45.14146 | 2024-12-18 12:44:00 | TERRA_M-T | BACURI | MARANHÃO | Brasil | 2101301 | 21 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 7a74cdfd-395c-39e1-939a-9187e4ef34e3 | -8.04548 | -38.53522 | 2024-12-18 12:44:00 | TERRA_M-T | SERRA TALHADA | PERNAMBUCO | Brasil | 2613909 | 26 | 33 | nan | nan | nan | Caatinga | 111.8 |
| a7325444-1d73-358d-90ed-dc5833d6f0e1 | -0.75851 | -47.75278 | 2024-12-18 12:44:00 | TERRA_M-T | MARAPANIM | PARÁ | Brasil | 1504406 | 15 | 33 | nan | nan | nan | Amazônia | 16.3 |
| 88262064-0b66-3e06-b969-4543e855ba53 | -1.70819 | -45.77736 | 2024-12-18 12:44:00 | TERRA_M-T | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 20.6 |
| 3dcccaf5-b6ca-3ac5-8753-71ee11f2f7e4 | -2.85147 | -42.04541 | 2024-12-18 12:44:00 | TERRA_M-T | ARAIOSES | MARANHÃO | Brasil | 2100907 | 21 | 33 | nan | nan | nan | Cerrado | 29.8 |
| aa54bd31-bebc-3e0f-b638-0f2af3fa8bc4 | -5.59451 | -43.6987 | 2024-12-18 12:44:00 | TERRA_M-T | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 19.9 |
| 3f3ec136-118f-3eef-8565-8487566fde8d | -3.29783 | -43.11274 | 2024-12-18 12:44:00 | TERRA_M-T | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 22.8 |
| 4d31895d-89e8-34a8-afe0-ae5514eb1eb4 | -3.52846 | -41.97898 | 2024-12-18 12:44:00 | TERRA_M-T | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 93.3 |
| 3591f5e6-5529-3edd-8f48-f642f91f7572 | -2.85561 | -42.05179 | 2024-12-18 12:44:00 | TERRA_M-T | ARAIOSES | MARANHÃO | Brasil | 2100907 | 21 | 33 | nan | nan | nan | Cerrado | 47.8 |
| 327e5c4a-10a9-34a0-a98e-7862c4626478 | -3.77885 | -44.05724 | 2024-12-18 12:44:00 | TERRA_M-T | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 18.8 |
| bbba3705-868a-3131-82e2-7d1d0d6d3389 | -3.83024 | -46.67878 | 2024-12-18 12:44:00 | TERRA_M-T | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 18e18a4f-9025-380d-9650-effbe7962b1f | -1.61574 | -45.84539 | 2024-12-18 12:44:00 | TERRA_M-T | AMAPÁ DO MARANHÃO | MARANHÃO | Brasil | 2100550 | 21 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 8e2b5ebb-d2ce-39e0-b0bf-f1fd60f1f616 | -4.97341 | -43.70452 | 2024-12-18 12:44:00 | TERRA_M-T | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 44.8 |
| f4b1a7e6-cecd-395a-9085-4ca07ddf35c6 | -3.20276 | -43.45729 | 2024-12-18 12:44:00 | TERRA_M-T | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 61427c17-3f98-3ac1-b2a0-125584821890 | -1.47562 | -47.33976 | 2024-12-18 12:44:00 | TERRA_M-T | BONITO | PARÁ | Brasil | 1501600 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 9d0eb6d5-24a1-36cd-b9ed-5c7ba5e2a949 | -1.70684 | -45.78694 | 2024-12-18 12:44:00 | TERRA_M-T | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 16.6 |
| 9886284d-707b-3fb7-a5a8-15fb57931019 | -3.78228 | -44.0643 | 2024-12-18 12:44:00 | TERRA_M-T | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 16.6 |
| f096b01d-bc99-3d78-afd4-f377049816bf | -6.91278 | -42.82906 | 2024-12-18 12:44:00 | TERRA_M-T | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 92.4 |
| a21b2dea-3e85-3b53-ae3f-b48c23f57204 | -4.88898 | -45.34239 | 2024-12-18 12:44:00 | TERRA_M-T | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 7029e004-4826-3e92-bd13-d9c2f066cbe4 | -3.2261 | -45.23248 | 2024-12-18 12:44:00 | TERRA_M-T | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 16.0 |
| a4d1b8df-bc03-312a-be7b-7b17c0be3d0f | -3.07788 | -42.12981 | 2024-12-18 12:44:00 | TERRA_M-T | ARAIOSES | MARANHÃO | Brasil | 2100907 | 21 | 33 | nan | nan | nan | Cerrado | 77.7 |
| 285169f9-3cb0-33a7-9151-90e1234b93d1 | -1.5723 | -45.95842 | 2024-12-18 12:44:00 | TERRA_M-T | AMAPÁ DO MARANHÃO | MARANHÃO | Brasil | 2100550 | 21 | 33 | nan | nan | nan | Amazônia | 12.6 |
| e88d5a6e-bcab-3413-b048-de62c2eaf2ca | -3.53106 | -41.96067 | 2024-12-18 12:44:00 | TERRA_M-T | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 20.6 |
| 5950db86-c0d9-37c5-9771-fe7054436223 | -6.96467 | -42.99541 | 2024-12-18 12:44:00 | TERRA_M-T | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 36.8 |
| 8eafa915-cb1b-3cd7-830a-b7863626ad82 | -1.61439 | -45.85488 | 2024-12-18 12:44:00 | TERRA_M-T | AMAPÁ DO MARANHÃO | MARANHÃO | Brasil | 2100550 | 21 | 33 | nan | nan | nan | Amazônia | 20.0 |
| 491d2959-b73f-3372-b5db-61b356b0f6cc | -8.02801 | -38.53359 | 2024-12-18 12:44:00 | TERRA_M-T | SERRA TALHADA | PERNAMBUCO | Brasil | 2613909 | 26 | 33 | nan | nan | nan | Caatinga | 59.9 |
| 789e08e2-bb6f-30b2-a051-03cb7ce4edd6 | -4.64976 | -44.49161 | 2024-12-18 12:44:00 | TERRA_M-T | PEDREIRAS | MARANHÃO | Brasil | 2108207 | 21 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 56d0667a-8a90-3549-93fb-aea8dcfec476 | -5.83699 | -39.1648 | 2024-12-18 12:44:00 | TERRA_M-T | SOLONÓPOLE | CEARÁ | Brasil | 2313005 | 23 | 33 | nan | nan | nan | Caatinga | 24.2 |
| 8050a4a0-e959-3d22-a89a-dda1a4fdd15d | -4.66068 | -43.81396 | 2024-12-18 12:44:00 | TERRA_M-T | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 15.2 |
| ee230d13-dc3a-3ae2-9025-8cfc2d0c2754 | -11.7694 | -43.88132 | 2024-12-18 12:46:00 | TERRA_M-T | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 19.3 |
| e6db7d15-4398-32e6-9758-28243c4376ee | -13.9366 | -50.41911 | 2024-12-18 12:46:00 | TERRA_M-T | NOVA CRIXÁS | GOIÁS | Brasil | 5214838 | 52 | 33 | nan | nan | nan | Cerrado | 7.1 |
| fc3d0d7b-2917-354d-b117-cf3597a4c188 | -15.45717 | -51.81106 | 2024-12-18 12:48:00 | TERRA_M-T | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 3778fe4f-48c0-3921-a2a1-ab54c3cb0a89 | -19.80127 | -49.52018 | 2024-12-18 12:48:00 | TERRA_M-T | ITAPAGIPE | MINAS GERAIS | Brasil | 3133402 | 31 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 13e9578c-6fb3-35ef-9b65-52726cfc4cf5 | -20.11697 | -49.91066 | 2024-12-18 12:48:00 | TERRA_M-T | CARDOSO | SÃO PAULO | Brasil | 3510708 | 35 | 33 | nan | nan | nan | Mata Atlântica | 9.9 |
| 653081b1-922a-3e90-b53c-aaf76d7e7f22 | -19.32635 | -49.29935 | 2024-12-18 12:48:00 | TERRA_M-T | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 4276ad05-d5bf-3ed7-9dc4-282d2a60521e | -19.0609 | -50.82785 | 2024-12-18 12:48:00 | TERRA_M-T | CAÇU | GOIÁS | Brasil | 5204300 | 52 | 33 | nan | nan | nan | Cerrado | 9.3 |
| e15d5962-c620-3a6b-91f4-5e8bdc109ea4 | -18.52515 | -49.57603 | 2024-12-18 12:48:00 | TERRA_M-T | CACHOEIRA DOURADA | GOIÁS | Brasil | 5204250 | 52 | 33 | nan | nan | nan | Mata Atlântica | 9.6 |
| 73e69939-9289-3015-b902-4a85c1837f79 | -19.269 | -49.37504 | 2024-12-18 12:48:00 | TERRA_M-T | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 63ec35c0-acf2-3b13-a82f-ea5d36019e1f | -22.20989 | -49.65657 | 2024-12-18 12:48:00 | TERRA_M-T | GARÇA | SÃO PAULO | Brasil | 3516705 | 35 | 33 | nan | nan | nan | Mata Atlântica | 7.6 |
| ddda7a2d-08ad-3322-b122-cbf3807bef04 | -18.53386 | -49.30239 | 2024-12-18 12:48:00 | TERRA_M-T | ITUMBIARA | GOIÁS | Brasil | 5211503 | 52 | 33 | nan | nan | nan | Cerrado | 9.4 |
| f963ce24-9857-36e1-bcfb-4cbe1235fb55 | -15.90919 | -51.50755 | 2024-12-18 12:48:00 | TERRA_M-T | MONTES CLAROS DE GOIÁS | GOIÁS | Brasil | 5213707 | 52 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 0705e362-39d5-38e7-8cb9-9dce9444fc01 | -19.8969 | -48.70673 | 2024-12-18 12:48:00 | TERRA_M-T | PIRAJUBA | MINAS GERAIS | Brasil | 3150703 | 31 | 33 | nan | nan | nan | Cerrado | 13.5 |
| 93a64fe4-3192-3dbc-96ca-9eff7923c1c1 | -19.14489 | -49.54702 | 2024-12-18 12:48:00 | TERRA_M-T | ITUIUTABA | MINAS GERAIS | Brasil | 3134202 | 31 | 33 | nan | nan | nan | Cerrado | 10.5 |
| a5f536a8-d284-3474-8991-1f7ff8e32556 | -18.21858 | -49.73249 | 2024-12-18 12:48:00 | TERRA_M-T | BOM JESUS DE GOIÁS | GOIÁS | Brasil | 5203500 | 52 | 33 | nan | nan | nan | Cerrado | 7.1 |
| ba029c16-6eea-3d66-bab7-904223b760b0 | -19.06553 | -52.85781 | 2024-12-18 12:48:00 | TERRA_M-T | CHAPADÃO DO SUL | MATO GROSSO DO SUL | Brasil | 5002951 | 50 | 33 | nan | nan | nan | Cerrado | 9.5 |
| f9052d95-520c-31ba-a594-f6ed67b5ecd9 | -20.68939 | -51.54838 | 2024-12-18 12:48:00 | TERRA_M-T | CASTILHO | SÃO PAULO | Brasil | 3511003 | 35 | 33 | nan | nan | nan | Mata Atlântica | 8.9 |
| fc82872a-13d2-323b-b1f2-89efd44963b4 | -21.23261 | -51.36298 | 2024-12-18 12:48:00 | TERRA_M-T | GUARAÇAÍ | SÃO PAULO | Brasil | 3517802 | 35 | 33 | nan | nan | nan | Mata Atlântica | 8.9 |
| a42d5e47-9fd0-3fdb-85c9-f2626a881a81 | -18.5718 | -49.36952 | 2024-12-18 12:48:00 | TERRA_M-T | ITUMBIARA | GOIÁS | Brasil | 5211503 | 52 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 7cb93bff-6a6c-3455-bce1-d225364e1e89 | -21.69548 | -51.60303 | 2024-12-18 12:48:00 | TERRA_M-T | RIBEIRÃO DOS ÍNDIOS | SÃO PAULO | Brasil | 3543238 | 35 | 33 | nan | nan | nan | Mata Atlântica | 8.0 |
| 0d0dc5e5-a8ee-39d2-b9a2-25fe758e1a00 | -19.2354 | -52.34595 | 2024-12-18 12:48:00 | TERRA_M-T | CASSILÂNDIA | MATO GROSSO DO SUL | Brasil | 5002902 | 50 | 33 | nan | nan | nan | Cerrado | 15.6 |
| 362f3dc4-8781-3f0b-8ea3-56481432e879 | -18.68811 | -49.66261 | 2024-12-18 12:48:00 | TERRA_M-T | CAPINÓPOLIS | MINAS GERAIS | Brasil | 3112604 | 31 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 7469975f-b5ea-3d71-b062-478f9a96fd7c | -17.75365 | -52.79702 | 2024-12-18 12:48:00 | TERRA_M-T | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 716095f9-5d3d-3f85-8ff4-d06c19168429 | -6.9592 | -42.9994 | 2024-12-18 12:50:00 | GOES-16 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 100.8 |
| 399a9548-af00-3ae0-a033-322eb3c3bd04 | -4.9643 | -43.7182 | 2024-12-18 12:50:00 | GOES-16 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 119.8 |
| 10c66f88-2045-379a-9516-5d54e628fea6 | -24.79673 | -53.29669 | 2024-12-18 12:50:00 | TERRA_M-T | CORBÉLIA | PARANÁ | Brasil | 4106308 | 41 | 33 | nan | nan | nan | Mata Atlântica | 7.0 |
| fc9d5b18-2e92-35e2-95cd-5989d6bc95c6 | -24.5997 | -50.76124 | 2024-12-18 12:50:00 | TERRA_M-T | RESERVA | PARANÁ | Brasil | 4121703 | 41 | 33 | nan | nan | nan | Mata Atlântica | 6.1 |
| 8f557672-90f1-3332-a165-0cdebffced22 | -23.11823 | -46.56021 | 2024-12-18 12:50:00 | TERRA_M-T | ATIBAIA | SÃO PAULO | Brasil | 3504107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 14.9 |
| 86c9f03f-9531-328d-ae1e-1f6da9f2dd82 | -24.80938 | -50.22008 | 2024-12-18 12:50:00 | TERRA_M-T | CARAMBEÍ | PARANÁ | Brasil | 4104659 | 41 | 33 | nan | nan | nan | Mata Atlântica | 20.8 |
| 913f6c93-2895-3c4b-a492-e6e665d48962 | -30.38554 | -53.46882 | 2024-12-18 12:53:00 | TERRA_M-T | CAÇAPAVA DO SUL | RIO GRANDE DO SUL | Brasil | 4302808 | 43 | 33 | nan | nan | nan | Pampa | 9.8 |
| 5e7f628e-127f-350b-9130-5a0e405a2815 | -28.24289 | -49.87974 | 2024-12-18 12:53:00 | TERRA_M-T | SÃO JOAQUIM | SANTA CATARINA | Brasil | 4216503 | 42 | 33 | nan | nan | nan | Mata Atlântica | 5.4 |
| 1f421829-6e99-3210-b13a-335a1fdcee9d | -29.86976 | -51.24279 | 2024-12-18 12:53:00 | TERRA_M-T | NOVA SANTA RITA | RIO GRANDE DO SUL | Brasil | 4313375 | 43 | 33 | nan | nan | nan | Pampa | 6.6 |
| 30b51e1d-220b-3099-8eb4-fad95b37731d | -30.48495 | -53.54636 | 2024-12-18 12:53:00 | TERRA_M-T | CAÇAPAVA DO SUL | RIO GRANDE DO SUL | Brasil | 4302808 | 43 | 33 | nan | nan | nan | Pampa | 4.3 |
| 80e76ea8-0f9d-3b24-8306-d0a72ef766fd | -28.85056 | -51.89682 | 2024-12-18 12:53:00 | TERRA_M-T | GUAPORÉ | RIO GRANDE DO SUL | Brasil | 4309407 | 43 | 33 | nan | nan | nan | Mata Atlântica | 6.8 |
| d3ae43ae-679c-32db-b104-734348190b2c | -6.9613 | -42.8108 | 2024-12-18 13:00:00 | GOES-16 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 89.3 |
| f1c3a960-b429-3c10-b5fe-6314a405832c | -4.9643 | -43.7182 | 2024-12-18 13:00:00 | GOES-16 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 107.1 |
| f1d4d85f-9356-34d3-af0c-9655179e7a00 | -6.9613 | -42.8108 | 2024-12-18 13:10:00 | GOES-16 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 92.9 |
| 98627b6c-f8e2-3d15-8a08-f819755ad5ac | -4.983 | -43.7169 | 2024-12-18 13:20:00 | GOES-16 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 117.1 |
| 0d530ab4-0c49-3794-97ed-3db21b09023e | -4.9643 | -43.7182 | 2024-12-18 13:20:00 | GOES-16 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 139.5 |
| bd50bee1-3a31-3de0-a7b3-f39ae88197e6 | -6.9613 | -42.8108 | 2024-12-18 13:20:00 | GOES-16 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 96.4 |
| a414e474-446c-3dbc-a0fe-5e9197b760d9 | -4.9643 | -43.7182 | 2024-12-18 13:30:00 | GOES-16 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 148.5 |
| be0d1755-c438-38af-bc14-95810844f544 | -6.9613 | -42.8108 | 2024-12-18 13:30:00 | GOES-16 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 94.8 |
| 7797fbb6-3411-3420-9fb6-6642689806ae | -3.0311 | -42.1604 | 2024-12-18 13:40:00 | GOES-16 | ÁGUA DOCE DO MARANHÃO | MARANHÃO | Brasil | 2100154 | 21 | 33 | nan | nan | nan | Cerrado | 113.2 |
| 0846e2bf-63d1-3f66-83e0-b0e8ae0414ed | -6.9613 | -42.8108 | 2024-12-18 13:40:00 | GOES-16 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 97.7 |
| 24f9f7bf-d565-3854-9940-9879592f3a00 | -4.9022 | -42.1038 | 2024-12-18 13:40:00 | GOES-16 | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 79.1 |
| 62df70b5-11e3-37ef-a9da-ec111ce9bb20 | -4.9643 | -43.7182 | 2024-12-18 13:40:00 | GOES-16 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 143.6 |
| 6e79f145-3d7b-360e-b862-5aafc266474b | -4.9024 | -42.08 | 2024-12-18 13:40:00 | GOES-16 | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 79.5 |
| afc1273a-2abe-3ee5-9ea2-6d13d32c1778 | -6.961 | -42.8344 | 2024-12-18 13:40:00 | GOES-16 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 86.5 |
| 2f678d7a-cc1f-3d35-a18c-8b5256aa266e | -3.0124 | -42.1612 | 2024-12-18 13:40:00 | GOES-16 | ÁGUA DOCE DO MARANHÃO | MARANHÃO | Brasil | 2100154 | 21 | 33 | nan | nan | nan | Cerrado | 165.1 |
| 768c82c7-19ec-32a0-a753-ea962d402c68 | -4.1247 | -43.5601 | 2024-12-18 13:50:00 | GOES-16 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 76.4 |
| b2224877-7e84-3e46-af1b-a95d9b70482b | -6.9613 | -42.8108 | 2024-12-18 13:50:00 | GOES-16 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 91.0 |
| 6cc17364-4b5f-3117-98a5-21469c1c92b4 | -3.0124 | -42.1612 | 2024-12-18 13:50:00 | GOES-16 | ÁGUA DOCE DO MARANHÃO | MARANHÃO | Brasil | 2100154 | 21 | 33 | nan | nan | nan | Cerrado | 92.6 |
| e229a57f-7d4b-3ce8-b543-a74afee73d6e | -3.0311 | -42.1604 | 2024-12-18 13:50:00 | GOES-16 | ÁGUA DOCE DO MARANHÃO | MARANHÃO | Brasil | 2100154 | 21 | 33 | nan | nan | nan | Cerrado | 86.0 |
| bece7548-b490-3989-b598-22d3ec358fce | -4.9643 | -43.7182 | 2024-12-18 13:50:00 | GOES-16 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 139.0 |
| 61f18e85-bb18-3667-b395-aba9cd25b157 | -6.9424 | -42.8126 | 2024-12-18 13:50:00 | GOES-16 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 89.7 |
| 4abf3775-db80-3be0-b2f0-43a69af4e042 | -1.7698 | -46.0522 | 2024-12-18 14:00:00 | GOES-16 | JUNCO DO MARANHÃO | MARANHÃO | Brasil | 2105658 | 21 | 33 | nan | nan | nan | Amazônia | 76.7 |
| 4ed8556b-4a28-3dca-b647-1d536a07f8ef | -6.9422 | -42.8362 | 2024-12-18 14:00:00 | GOES-16 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 90.8 |
| b2324852-24ac-30ce-a954-8a2c31eeee49 | -4.9643 | -43.7182 | 2024-12-18 14:00:00 | GOES-16 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 142.2 |
| 139e03c5-a972-3068-b478-b514f8d6333f | -6.9424 | -42.8126 | 2024-12-18 14:00:00 | GOES-16 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 89.8 |
| 96ccd2cd-c65d-326d-8a20-7e09e839f3be | -6.961 | -42.8344 | 2024-12-18 14:00:00 | GOES-16 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 89.2 |
| b7d44255-57c1-3474-b224-28e1187f8b26 | -4.9022 | -42.1038 | 2024-12-18 14:00:00 | GOES-16 | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 78.3 |


[Clique aqui para ver as próximas entradas](README23.md)
