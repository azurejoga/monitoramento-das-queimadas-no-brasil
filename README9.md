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

## Dados Diários - Página 9

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4556e87d-0a49-3cce-93f7-fee37551ae3d | -15.03766 | -48.17418 | 2025-08-24 00:48:00 | TERRA_M-M | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 7.6 |
| e71bfc91-a7ac-3973-9d53-2869ebdf3ea5 | -16.79182 | -51.35411 | 2025-08-24 00:48:00 | TERRA_M-M | PALESTINA DE GOIÁS | GOIÁS | Brasil | 5215652 | 52 | 33 | nan | nan | nan | Cerrado | 196.1 |
| 67bdf345-f884-303d-9464-fab4ac0594ae | -20.34813 | -51.7105 | 2025-08-24 00:48:00 | TERRA_M-M | SELVÍRIA | MATO GROSSO DO SUL | Brasil | 5007802 | 50 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 49fb599c-9521-3e2a-87ed-b4048fc9bf4a | -22.0701 | -53.77586 | 2025-08-24 00:48:00 | TERRA_M-M | ANGÉLICA | MATO GROSSO DO SUL | Brasil | 5000856 | 50 | 33 | nan | nan | nan | Mata Atlântica | 9.7 |
| d94fb572-16a1-35ed-8955-5dc1cb47ad37 | -16.78286 | -51.35537 | 2025-08-24 00:48:00 | TERRA_M-M | PALESTINA DE GOIÁS | GOIÁS | Brasil | 5215652 | 52 | 33 | nan | nan | nan | Cerrado | 14.5 |
| 0d2d6fc2-7e89-3d52-be93-85d442b8994a | -22.0968 | -53.81693 | 2025-08-24 00:48:00 | TERRA_M-M | ANGÉLICA | MATO GROSSO DO SUL | Brasil | 5000856 | 50 | 33 | nan | nan | nan | Mata Atlântica | 9.4 |
| 6ceb6b43-3554-35ad-800c-7a797ae6c4ae | -18.84739 | -49.50076 | 2025-08-24 00:48:00 | TERRA_M-M | ITUIUTABA | MINAS GERAIS | Brasil | 3134202 | 31 | 33 | nan | nan | nan | Cerrado | 8.9 |
| fcfe9e00-cf9f-374b-9e84-4e86ec81b86b | -17.59279 | -46.09391 | 2025-08-24 00:48:00 | TERRA_M-M | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 0016a15f-9e0d-358c-9b64-f013bad41f22 | -21.72664 | -46.81565 | 2025-08-24 00:48:00 | TERRA_M-M | SÃO SEBASTIÃO DA GRAMA | SÃO PAULO | Brasil | 3550803 | 35 | 33 | nan | nan | nan | Mata Atlântica | 28.0 |
| a7c154e9-15e9-391b-a2a7-8cd0df8caf40 | -20.35347 | -51.67777 | 2025-08-24 00:48:00 | TERRA_M-M | SELVÍRIA | MATO GROSSO DO SUL | Brasil | 5007802 | 50 | 33 | nan | nan | nan | Cerrado | 24.9 |
| 557b9bcd-0779-325d-ae21-da338e04e29d | -20.36708 | -46.75977 | 2025-08-24 00:48:00 | TERRA_M-M | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 11.6 |
| d586c65a-a81a-32cc-a6c3-d69da4aaefee | -20.27999 | -50.89698 | 2025-08-24 00:48:00 | TERRA_M-M | TRÊS FRONTEIRAS | SÃO PAULO | Brasil | 3554904 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.2 |
| 4c32949a-51d5-3777-8919-3a21a143f8b8 | -20.20487 | -47.02856 | 2025-08-24 00:48:00 | TERRA_M-M | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 8090e9e9-3ddc-3feb-841f-7406044c5623 | -16.79057 | -51.34469 | 2025-08-24 00:48:00 | TERRA_M-M | PALESTINA DE GOIÁS | GOIÁS | Brasil | 5215652 | 52 | 33 | nan | nan | nan | Cerrado | 17.5 |
| 0692900d-e1a7-3438-894b-e4ab67d37d88 | -18.75572 | -45.09589 | 2025-08-24 00:48:00 | TERRA_M-M | FELIXLÂNDIA | MINAS GERAIS | Brasil | 3125705 | 31 | 33 | nan | nan | nan | Cerrado | 26.2 |
| bcdbb74f-9291-3ab0-a27d-7690b8b8711c | -22.07342 | -53.80538 | 2025-08-24 00:48:00 | TERRA_M-M | ANGÉLICA | MATO GROSSO DO SUL | Brasil | 5000856 | 50 | 33 | nan | nan | nan | Mata Atlântica | 38.5 |
| f5867f3f-3632-365c-8f09-31263f11386e | -14.93978 | -48.00867 | 2025-08-24 00:48:00 | TERRA_M-M | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 435407f8-b00b-36b3-b678-d6320afc9a63 | -15.23836 | -48.21629 | 2025-08-24 00:48:00 | TERRA_M-M | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 7171a6be-f1e1-393e-b534-d1c0368d57ea | -22.09847 | -53.83167 | 2025-08-24 00:48:00 | TERRA_M-M | ANGÉLICA | MATO GROSSO DO SUL | Brasil | 5000856 | 50 | 33 | nan | nan | nan | Mata Atlântica | 19.4 |
| cd176658-a6cb-341c-929c-c10f2041b38d | -15.11171 | -48.66383 | 2025-08-24 00:48:00 | TERRA_M-M | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 926ae8dd-81c8-382e-b15f-85d4e2e33191 | -16.79952 | -51.34344 | 2025-08-24 00:48:00 | TERRA_M-M | PALESTINA DE GOIÁS | GOIÁS | Brasil | 5215652 | 52 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 35f699f7-d7cd-312f-89ce-0a3892145bfd | -16.49042 | -52.5645 | 2025-08-24 00:48:00 | TERRA_M-M | BALIZA | GOIÁS | Brasil | 5203104 | 52 | 33 | nan | nan | nan | Cerrado | 6.9 |
| c43d9668-d60c-3b51-afcf-5361a7cfb954 | -22.29786 | -47.61317 | 2025-08-24 00:48:00 | TERRA_M-M | RIO CLARO | SÃO PAULO | Brasil | 3543907 | 35 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 6bd32da0-ea73-3740-a577-6848696b8374 | -15.22887 | -48.21791 | 2025-08-24 00:48:00 | TERRA_M-M | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 90.7 |
| 07517fb8-b3ab-3b77-a53a-46a593322c03 | -20.36279 | -51.67645 | 2025-08-24 00:48:00 | TERRA_M-M | SELVÍRIA | MATO GROSSO DO SUL | Brasil | 5007802 | 50 | 33 | nan | nan | nan | Cerrado | 6.8 |
| d2ef9f09-1afc-398d-81ab-4de5d4d042e2 | -14.80309 | -47.93044 | 2025-08-24 00:48:00 | TERRA_M-M | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 58.2 |
| 5b075376-2d30-3549-9f97-b4227015be33 | -20.3654 | -46.74904 | 2025-08-24 00:48:00 | TERRA_M-M | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 19.8 |
| 636948b7-3670-337d-9a13-514fb918e752 | -20.81085 | -50.12381 | 2025-08-24 00:48:00 | TERRA_M-M | NHANDEARA | SÃO PAULO | Brasil | 3532603 | 35 | 33 | nan | nan | nan | Mata Atlântica | 7.6 |
| 45b70158-50c6-3b47-a529-9527198c758f | -4.9605 | -55.8226 | 2025-08-24 00:50:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 120.9 |
| 81acb68d-7ec8-3b20-b0b2-8d1afc813985 | -5.4026 | -44.9952 | 2025-08-24 00:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 85.8 |
| 95ac43b5-d8d8-3a28-b9c6-e054a5fd19ca | -11.5055 | -51.8705 | 2025-08-24 00:50:00 | GOES-19 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 77.7 |
| 381d4922-c893-3c89-afaf-180312f3987b | -14.8153 | -47.9343 | 2025-08-24 00:50:00 | GOES-19 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 50.5 |
| a0fd0c83-a782-360f-ad75-d0a343e30219 | -22.0862 | -53.7763 | 2025-08-24 00:50:00 | GOES-19 | ANGÉLICA | MATO GROSSO DO SUL | Brasil | 5000856 | 50 | 33 | nan | nan | nan | Mata Atlântica | 238.5 |
| 39ed5fe9-a8f4-3fe0-bf18-a25022f88ff3 | -22.8039 | -54.0134 | 2025-08-24 00:50:00 | GOES-19 | NAVIRAÍ | MATO GROSSO DO SUL | Brasil | 5005707 | 50 | 33 | nan | nan | nan | Mata Atlântica | 89.6 |
| d5cebfba-8a96-3020-94c7-bb2ea37f4ad4 | -14.8157 | -47.9118 | 2025-08-24 00:50:00 | GOES-19 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 49.4 |
| 5bc67686-2ea5-319d-b4f0-23dd216e50a9 | -17.6183 | -44.2738 | 2025-08-24 00:50:00 | GOES-19 | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 59.6 |
| 623539ac-5d01-3052-9aeb-bd7fec876b9b | -22.065 | -53.8023 | 2025-08-24 00:50:00 | GOES-19 | ANGÉLICA | MATO GROSSO DO SUL | Brasil | 5000856 | 50 | 33 | nan | nan | nan | Mata Atlântica | 217.7 |
| b43b7ad8-b191-3cdb-8f18-5ada99405627 | -3.5083 | -47.212 | 2025-08-24 00:50:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 61.7 |
| fffa07ba-c2cb-358c-87d0-1464feb5b017 | -5.4364 | -60.1779 | 2025-08-24 00:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 92.0 |
| 85072412-49f3-36c8-94d1-c1098da8f4fc | -14.7962 | -47.915 | 2025-08-24 00:50:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 52.8 |
| 8a491df6-cc45-3136-945d-7300065ebcaf | -20.3599 | -51.68 | 2025-08-24 00:50:00 | GOES-19 | SELVÍRIA | MATO GROSSO DO SUL | Brasil | 5007802 | 50 | 33 | nan | nan | nan | Cerrado | 201.5 |
| 9fd43dba-d332-30a5-8fa8-5ae307475cdf | -5.4365 | -60.1588 | 2025-08-24 00:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 53.6 |
| 3fce2805-21af-3fcc-aa2c-dc9d9fb99eb5 | -11.9867 | -61.0214 | 2025-08-24 00:50:00 | GOES-19 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 64.1 |
| 9a64f02f-7c92-3b8b-bb0c-4007c91a83cb | -10.5819 | -50.1863 | 2025-08-24 00:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 65.5 |
| 3a80727d-df72-3b02-9819-7adee65fcaa9 | -22.0856 | -53.7984 | 2025-08-24 00:50:00 | GOES-19 | ANGÉLICA | MATO GROSSO DO SUL | Brasil | 5000856 | 50 | 33 | nan | nan | nan | Mata Atlântica | 191.1 |
| 99f97864-4541-36bf-99fa-2d5f7550b568 | -11.5245 | -51.8685 | 2025-08-24 00:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 77.7 |
| 332c9453-0596-31db-882a-0a64458bc8c2 | -10.6131 | -44.3051 | 2025-08-24 00:50:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 68.4 |
| f1921eba-d364-3bdc-a117-1008f23485e9 | -9.0061 | -65.3813 | 2025-08-24 00:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 65.5 |
| 2f4743e2-599c-3cbb-bc06-d34149924e60 | -10.6009 | -50.1843 | 2025-08-24 00:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 67.2 |
| 2191d510-cf16-3545-b4e1-02c7a9a3b754 | -5.4181 | -60.1784 | 2025-08-24 00:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 187.9 |
| 9bba81ef-704c-324e-992a-b7e630898996 | -4.9606 | -55.8028 | 2025-08-24 00:50:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 57.3 |
| 028a708a-910e-31fe-bca8-397f250246c0 | -9.0416 | -65.7163 | 2025-08-24 00:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 84.1 |
| 02005366-f994-32f8-b15f-b521ea0bb8d2 | -9.0045 | -65.7174 | 2025-08-24 00:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 76.5 |
| 0264761f-1949-3c81-ab73-1a337df268f7 | -20.339 | -51.7062 | 2025-08-24 00:50:00 | GOES-19 | SELVÍRIA | MATO GROSSO DO SUL | Brasil | 5007802 | 50 | 33 | nan | nan | nan | Cerrado | 92.1 |
| 5547fbda-443f-3d92-9f7c-a00187b53751 | -3.5994 | -47.5359 | 2025-08-24 00:50:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 74.7 |
| cdfc4d0f-51ab-3d96-a8ec-7ebb9d519431 | -10.8078 | -46.4083 | 2025-08-24 00:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 64.1 |
| cac62f6e-87ca-3408-a97f-67f16392054a | -22.8248 | -54.0094 | 2025-08-24 00:50:00 | GOES-19 | NAVIRAÍ | MATO GROSSO DO SUL | Brasil | 5005707 | 50 | 33 | nan | nan | nan | Mata Atlântica | 78.6 |
| 2b40a7f3-44b9-32b3-9f07-c0274abcd375 | -20.3396 | -51.6839 | 2025-08-24 00:50:00 | GOES-19 | SELVÍRIA | MATO GROSSO DO SUL | Brasil | 5007802 | 50 | 33 | nan | nan | nan | Cerrado | 96.8 |
| 25935060-d556-3e51-a0f9-0db244a5be14 | -3.5995 | -47.5142 | 2025-08-24 00:50:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 81.1 |
| 97773452-6026-3a75-bb28-0e567cedad7c | -16.7965 | -51.3637 | 2025-08-24 00:50:00 | GOES-19 | PALESTINA DE GOIÁS | GOIÁS | Brasil | 5215652 | 52 | 33 | nan | nan | nan | Cerrado | 78.0 |
| 527d2176-8502-321f-80a2-228ac4a189c1 | -9.1998 | -60.793 | 2025-08-24 00:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 77.5 |
| 376fa200-8aaa-3898-91b9-f19d494147b6 | -20.278 | -50.8948 | 2025-08-24 00:50:00 | GOES-19 | TRÊS FRONTEIRAS | SÃO PAULO | Brasil | 3554904 | 35 | 33 | nan | nan | nan | Mata Atlântica | 125.9 |
| bfb6496e-784a-3598-b097-e8d7a9dc39b5 | -5.4213 | -44.9939 | 2025-08-24 00:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 54.8 |
| 80b79519-44e0-36dc-ba1f-772a7c383c7d | -9.0246 | -65.3807 | 2025-08-24 00:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 52.6 |
| 1d2448ec-413e-399b-9760-77503bb2dd65 | -9.0231 | -65.7169 | 2025-08-24 00:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 139.4 |
| 35c38b19-d181-3130-a8ad-c14bd0f7d824 | -5.4182 | -60.1593 | 2025-08-24 00:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 106.8 |
| a269e09f-ea1e-338d-a8d3-9bb498755011 | -3.7847 | -47.5719 | 2025-08-24 00:50:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 46.0 |
| 9f665217-833e-3607-8725-0ad4be438eb6 | -17.5975 | -44.3027 | 2025-08-24 00:50:00 | GOES-19 | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 51.9 |
| 32f6ea12-e295-34f8-b1cc-e3dab6952ac3 | -22.0655 | -53.7802 | 2025-08-24 00:50:00 | GOES-19 | ANGÉLICA | MATO GROSSO DO SUL | Brasil | 5000856 | 50 | 33 | nan | nan | nan | Mata Atlântica | 282.5 |
| 4e10c693-4954-30f0-be3f-8353767621a6 | -20.3594 | -51.7023 | 2025-08-24 00:50:00 | GOES-19 | SELVÍRIA | MATO GROSSO DO SUL | Brasil | 5007802 | 50 | 33 | nan | nan | nan | Cerrado | 139.3 |
| dad02c1e-daa6-3ec3-af63-dc09e95e312c | -20.2775 | -50.9173 | 2025-08-24 00:50:00 | GOES-19 | TRÊS FRONTEIRAS | SÃO PAULO | Brasil | 3554904 | 35 | 33 | nan | nan | nan | Mata Atlântica | 52.1 |
| c8f8076d-2765-36a8-89d1-9f771b26a7e5 | -20.3701 | -46.7433 | 2025-08-24 00:50:00 | GOES-19 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 60.5 |
| 3cf96648-eef0-3520-9a45-b1889d219383 | -9.0232 | -65.6982 | 2025-08-24 00:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 138.7 |
| f48b1238-6665-3298-b5e3-5d5ab912d789 | -17.6176 | -44.298 | 2025-08-24 00:50:00 | GOES-19 | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 121.7 |
| 008686b4-1103-3210-9ded-bbf2dd549446 | -22.0851 | -53.8204 | 2025-08-24 00:50:00 | GOES-19 | ANGÉLICA | MATO GROSSO DO SUL | Brasil | 5000856 | 50 | 33 | nan | nan | nan | Mata Atlântica | 89.1 |
| 3978a300-c0ea-314d-9a19-4f9d5f19b546 | -17.4045 | -42.6186 | 2025-08-24 00:50:00 | GOES-19 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 46.1 |
| 56a0ad8f-2a09-3a98-a356-90cf7c39db7e | -17.3844 | -42.6235 | 2025-08-24 00:50:00 | GOES-19 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 60.4 |
| 8c7571f6-39dd-32be-aa1f-338ca8604b68 | -9.0046 | -65.6988 | 2025-08-24 00:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 107.4 |
| c369766e-74ed-3a42-b5cb-8a892b410d8b | -10.6128 | -44.3284 | 2025-08-24 00:50:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 75.6 |
| f1bf3ca2-b648-391f-882d-a3ad2a975bca | -5.4547 | -60.1964 | 2025-08-24 00:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 50.4 |
| 070b1c74-152f-3345-8dc8-a9f295f9b855 | -16.797 | -51.3419 | 2025-08-24 00:50:00 | GOES-19 | PALESTINA DE GOIÁS | GOIÁS | Brasil | 5215652 | 52 | 33 | nan | nan | nan | Cerrado | 131.0 |
| 5723d76e-c180-3cf3-a841-05b4c244460b | -14.7981 | -59.6343 | 2025-08-24 00:50:00 | GOES-19 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Amazônia | 43.1 |
| c21a0a6c-c998-352d-988f-110acbed1878 | -7.5534 | -63.8556 | 2025-08-24 00:50:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 53.2 |
| 47b99bec-09d6-3632-8361-a4b1c1f0eee9 | -20.2984 | -50.8908 | 2025-08-24 00:50:00 | GOES-19 | TRÊS FRONTEIRAS | SÃO PAULO | Brasil | 3554904 | 35 | 33 | nan | nan | nan | Mata Atlântica | 89.4 |
| 13576639-9135-3bb7-ab85-14801f0bbcad | -14.7984 | -59.6145 | 2025-08-24 00:50:00 | GOES-19 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Amazônia | 42.9 |
| cb536a49-22ec-382b-aa21-bb8a2c49d621 | -8.9106 | -62.4289 | 2025-08-24 00:50:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 53.1 |
| 48c14ef9-9216-3700-97c1-6f84af7ba6cd | -12.0055 | -61.0201 | 2025-08-24 00:50:00 | GOES-19 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 62.0 |
| 0b291ef2-c0ae-3683-9490-05366f8bc7da | -14.7958 | -47.9375 | 2025-08-24 00:50:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 55.3 |
| 27a0d8fa-44ff-3a6a-974b-f2a471dfc686 | -8.6131 | -62.5929 | 2025-08-24 00:50:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 62.9 |
| 45c820d1-d5c9-37fa-b65b-5e9cba6983ce | -4.93814 | -55.82469 | 2025-08-24 00:50:00 | TERRA_M-M | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 19.1 |
| 92dc6335-b0ec-3acd-b62f-cccee5b1f352 | -6.19626 | -45.43141 | 2025-08-24 00:50:00 | TERRA_M-M | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 52.3 |
| 0bb114bd-7b2c-367b-abc1-c7219f59b659 | -9.52249 | -60.55405 | 2025-08-24 00:50:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 31.7 |
| b15bbf97-68df-3985-844f-bfd435239499 | -6.43418 | -53.37622 | 2025-08-24 00:50:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| c6ad1b1f-14c7-3004-ad07-65f00164bf2c | -6.46636 | -53.40246 | 2025-08-24 00:50:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 9a17339c-0768-35a4-a997-7d74e442a39b | -13.49643 | -47.02979 | 2025-08-24 00:50:00 | TERRA_M-M | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 33.2 |
| 4d3362ef-90aa-3cee-9b09-0bc3f41ea419 | -11.51624 | -51.87938 | 2025-08-24 00:50:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 17.9 |
| 50bf9769-f156-3913-b80f-a989d0256aaa | -8.9224 | -62.43766 | 2025-08-24 00:50:00 | TERRA_M-M | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 41.5 |
| b5b5005a-b47b-3bc8-95a6-1b5ad5e97537 | -8.60227 | -62.6113 | 2025-08-24 00:50:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 51.8 |
| a0901590-769d-3b83-a813-a6651e2d4b91 | -11.13811 | -46.33931 | 2025-08-24 00:50:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 20.3 |
| 3dba6c6c-a676-3354-9d22-6b0a856b1ea9 | -6.42652 | -53.38644 | 2025-08-24 00:50:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 20.4 |


[Clique aqui para ver as próximas entradas](README10.md)
