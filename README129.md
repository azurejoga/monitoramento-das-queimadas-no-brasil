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

## Dados Diários - Página 129

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7cca617c-6320-3598-9ba4-ac89c5cc5418 | -12.7848 | -62.633 | 2024-09-27 06:46:19 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 81.6 |
| 8b8298c7-1552-3951-a953-f580b4ccf365 | -14.9228 | -51.4076 | 2024-09-27 06:46:30 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 122.9 |
| 83dffd38-e900-392f-b60e-8b723d37d3e6 | -14.8447 | -51.4401 | 2024-09-27 06:46:30 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 76.1 |
| 64e1e376-7261-388e-90a4-a98d32d48aba | -14.9224 | -51.4292 | 2024-09-27 06:46:30 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 159.8 |
| 03a2fe56-4d0a-3c86-8c5e-0e398c05cd86 | -16.0993 | -51.9465 | 2024-09-27 06:46:37 | GOES-16 | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 47.1 |
| 2005c273-fb60-3607-aade-d6cc644891f7 | -22.7442 | -44.7785 | 2024-09-27 06:47:11 | GOES-16 | SILVEIRAS | SÃO PAULO | Brasil | 3552007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 47.0 |
| 255d7f80-9ec2-3f62-9419-ca2839380dda | -22.7433 | -44.8035 | 2024-09-27 06:47:11 | GOES-16 | SILVEIRAS | SÃO PAULO | Brasil | 3552007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 76.5 |
| aa6334be-61a6-3933-b4b8-8254e40886b3 | -23.5816 | -47.3408 | 2024-09-27 06:47:15 | GOES-16 | VOTORANTIM | SÃO PAULO | Brasil | 3557006 | 35 | 33 | nan | nan | nan | Mata Atlântica | 85.3 |
| 2cb41378-8df3-3f51-8dc4-96a13347be1a | -6.8199 | -63.1651 | 2024-09-27 06:55:46 | GOES-16 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 49.7 |
| cd9ee3de-411f-377c-85bf-eea37fbbba8e | -8.9978 | -67.3724 | 2024-09-27 06:55:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 104.5 |
| 24e07866-743e-30e7-a366-8156a5f5bec8 | -8.9977 | -67.3909 | 2024-09-27 06:55:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 60.9 |
| 2c91f66d-eebd-3d4a-b8e5-a8e77c156484 | -12.4501 | -55.0063 | 2024-09-27 06:56:17 | GOES-16 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 71.1 |
| 7207e534-3067-358d-8cbd-23843a77315f | -12.7848 | -62.633 | 2024-09-27 06:56:19 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 99.4 |
| 60d8990c-e912-3468-9320-089349e5d406 | -12.7659 | -62.6342 | 2024-09-27 06:56:19 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 64.7 |
| b6cbab43-5f1b-3153-943c-343fe318c2eb | -12.7868 | -54.0275 | 2024-09-27 06:56:19 | GOES-16 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 88.9 |
| 4d620151-d3fb-36b7-af66-da7a11a8e9e2 | -12.7099 | -54.0769 | 2024-09-27 06:56:19 | GOES-16 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 86.4 |
| 6137df7b-5366-344d-8c77-1a0c9abd67e1 | -14.8443 | -51.4616 | 2024-09-27 06:56:30 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 66.8 |
| b5b52594-9bcc-383b-8601-2aa54e7fe1a2 | -14.8447 | -51.4401 | 2024-09-27 06:56:30 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 83.9 |
| 6b5646da-183c-3e2e-9b54-20e8b6375644 | -14.9224 | -51.4292 | 2024-09-27 06:56:30 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 61.5 |
| af8dafe2-ef22-34b5-af33-f02cc96f4a7c | -14.9418 | -51.4264 | 2024-09-27 06:56:31 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 55.4 |
| 1a670ba1-bf75-3fd8-84d4-b5e778bc06d7 | -15.6364 | -57.508 | 2024-09-27 06:56:35 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 65.3 |
| 36174ff7-bccb-3ad1-89a8-0f3f65207fdd | -15.6367 | -57.4877 | 2024-09-27 06:56:35 | GOES-16 | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 84.3 |
| a7c8fb82-05e9-36d4-bbea-9a7acc3629d9 | -16.0993 | -51.9465 | 2024-09-27 06:56:37 | GOES-16 | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 68.8 |
| ab493cd2-2f13-3a84-acd6-a44187d2c82d | -16.0989 | -51.968 | 2024-09-27 06:56:37 | GOES-16 | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 64.9 |
| b2bef2d7-b066-3c55-bff3-acee58ac1dbe | -21.9194 | -48.4799 | 2024-09-27 06:57:07 | GOES-16 | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 71.7 |
| c93efdd7-b394-3adb-b24e-2e9e87ade95f | -22.7433 | -44.8035 | 2024-09-27 06:57:11 | GOES-16 | SILVEIRAS | SÃO PAULO | Brasil | 3552007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 47.9 |
| 387f2d2d-037f-3a0b-86be-690c0922185b | -23.5816 | -47.3408 | 2024-09-27 06:57:15 | GOES-16 | VOTORANTIM | SÃO PAULO | Brasil | 3557006 | 35 | 33 | nan | nan | nan | Mata Atlântica | 72.7 |
| b40766f5-2849-3b9f-b591-6836b5261de9 | -7.327 | -61.1808 | 2024-09-27 07:05:49 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 63.5 |
| b24608fc-f1ed-3fec-9dcd-bd4b16db7e7a | -7.5888 | -60.5785 | 2024-09-27 07:05:50 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 70.7 |
| 45ab1a72-2c22-3eb7-ae92-0642070b5a7c | -7.5887 | -60.5976 | 2024-09-27 07:05:50 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 78.5 |
| 8870e438-3d07-37b7-92db-5cf2d07582f1 | -8.9978 | -67.3724 | 2024-09-27 07:05:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 150.3 |
| da916ef9-0690-38a8-949c-442ffcc5d3c4 | -8.9977 | -67.3909 | 2024-09-27 07:05:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 86.0 |
| 1153c979-0ab5-310a-aeba-df6443c170ad | -12.6824 | -54.6968 | 2024-09-27 07:06:18 | GOES-16 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 67.7 |
| c3454c1e-59a9-32ee-87ac-2e4d1df2cc14 | -12.7848 | -62.633 | 2024-09-27 07:06:19 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 53.9 |
| 4e75c441-71f3-3087-a47e-df9e8108ba33 | -12.7659 | -62.6342 | 2024-09-27 07:06:19 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 54.8 |
| 3fba79e3-386f-3109-8ad7-d8ddd067c681 | -12.7868 | -54.0275 | 2024-09-27 07:06:19 | GOES-16 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 100.0 |
| 03ad1e9b-0cdf-313b-b3ec-22755c2dcc00 | -12.7099 | -54.0769 | 2024-09-27 07:06:19 | GOES-16 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 95.9 |
| 005c4e05-e7b7-3a63-8fd4-9576dd857066 | -14.9224 | -51.4292 | 2024-09-27 07:06:30 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 40.2 |
| ecf35724-8a09-39a2-90cb-1e8aa26fa7f4 | -15.6173 | -57.4897 | 2024-09-27 07:06:35 | GOES-16 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 76.4 |
| ad29bc5a-56fd-3b46-942a-45e1844839eb | -19.6136 | -42.8159 | 2024-09-27 07:06:54 | GOES-16 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 61.6 |
| 1294bfb2-d721-381e-b7a6-06d539b63838 | -22.7433 | -44.8035 | 2024-09-27 07:07:11 | GOES-16 | SILVEIRAS | SÃO PAULO | Brasil | 3552007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 59.5 |
| 645038be-8fa4-3c68-a6ef-68d878cc3f52 | -7.5703 | -60.5984 | 2024-09-27 07:15:50 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 48.3 |
| 9599adda-35c3-31a3-8123-d03617cb5b69 | -7.5887 | -60.5976 | 2024-09-27 07:15:50 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 64.2 |
| a0e607d8-7b1e-305d-a593-b0b6ebd44b8e | -7.5888 | -60.5785 | 2024-09-27 07:15:50 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 56.2 |
| 7f45e278-5dc8-3301-bf4f-ef401b834ea6 | -9.0163 | -67.3719 | 2024-09-27 07:15:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 49.2 |
| aa4193c6-3fd5-3502-82eb-3c285f57fb09 | -8.9978 | -67.3724 | 2024-09-27 07:15:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 94.2 |
| 28c06774-f44d-30a9-9f1f-9163c7835666 | -8.9977 | -67.3909 | 2024-09-27 07:15:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 67.2 |
| 1c498653-cb5f-3208-8964-834c1a929203 | -11.2223 | -54.7735 | 2024-09-27 07:16:10 | GOES-16 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 70.0 |
| 14dba9ab-4f0b-36ea-af31-2e34a5ee87f2 | -11.1951 | -53.8965 | 2024-09-27 07:16:10 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 78.2 |
| df1d959a-efe8-3182-9ac8-4e15480037a2 | -12.7868 | -54.0275 | 2024-09-27 07:16:19 | GOES-16 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 87.1 |
| a2f4e07e-0098-3f1d-a587-6cf842d23306 | -12.7099 | -54.0769 | 2024-09-27 07:16:19 | GOES-16 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 81.2 |
| 83841b50-b2ac-30d7-93d8-bab58b49db7e | -14.8447 | -51.4401 | 2024-09-27 07:16:30 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 87.8 |
| 0a21aa24-14cf-34df-91fd-0b8d7668f5d3 | -14.8443 | -51.4616 | 2024-09-27 07:16:30 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 75.1 |
| a57e301e-cd5b-3fab-a116-7cdf691ba760 | -15.6367 | -57.4877 | 2024-09-27 07:16:35 | GOES-16 | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 84.5 |
| 7484a0e0-b8a2-335a-a716-fc2fa57aaacc | -18.4403 | -52.1801 | 2024-09-27 07:16:49 | GOES-16 | SERRANÓPOLIS | GOIÁS | Brasil | 5220504 | 52 | 33 | nan | nan | nan | Cerrado | 116.7 |
| 5e6a6387-9de8-3f93-b706-ad26655a4485 | -18.4603 | -52.1767 | 2024-09-27 07:16:50 | GOES-16 | SERRANÓPOLIS | GOIÁS | Brasil | 5220504 | 52 | 33 | nan | nan | nan | Cerrado | 205.0 |
| ad843ce5-4dd3-3a30-981c-7cffe33b7586 | -18.4598 | -52.1986 | 2024-09-27 07:16:50 | GOES-16 | SERRANÓPOLIS | GOIÁS | Brasil | 5220504 | 52 | 33 | nan | nan | nan | Cerrado | 74.2 |
| c09a3a6d-d1c6-3c16-81e1-cde31a8e3320 | -22.7433 | -44.8035 | 2024-09-27 07:17:11 | GOES-16 | SILVEIRAS | SÃO PAULO | Brasil | 3552007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 55.1 |
| 7d53e326-5d70-3d76-b8ac-de9a7db9c972 | -7.5887 | -60.5976 | 2024-09-27 07:25:50 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 54.2 |
| 62a32f6f-77a3-333d-a3a7-ccce232e34e7 | -9.0163 | -67.3719 | 2024-09-27 07:25:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 73.4 |
| c452bd23-79cb-381a-a9f4-9872b010ca59 | -8.9977 | -67.3909 | 2024-09-27 07:25:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 73.5 |
| 666eadeb-76f0-3703-8f2e-95a200dd9474 | -8.9978 | -67.3724 | 2024-09-27 07:25:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 122.9 |
| e9ca35e7-3996-3853-a80e-257eb53b3567 | -8.9978 | -67.3538 | 2024-09-27 07:25:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 52.7 |
| 9e18b1aa-f717-3bcc-bd4d-0b7732080c53 | -9.0162 | -67.3904 | 2024-09-27 07:25:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 50.4 |
| 617855ca-eab0-34d8-ab8e-1032390b1431 | -8.9793 | -67.3728 | 2024-09-27 07:25:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 52.0 |
| ebfbd1c7-d5c3-3468-a089-c8f34f1567fc | -11.1951 | -53.8965 | 2024-09-27 07:26:10 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 81.9 |
| 7c0cb4f5-3c7f-32bb-840e-3aace7c4d7ab | -12.7099 | -54.0769 | 2024-09-27 07:26:19 | GOES-16 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 80.3 |
| 0dba28e1-422e-3d23-a92a-b1e52d628770 | -12.7868 | -54.0275 | 2024-09-27 07:26:19 | GOES-16 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 91.8 |
| 86f75692-c92b-3c8e-9c27-7f169d450f7c | -12.8059 | -54.0255 | 2024-09-27 07:26:19 | GOES-16 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 73.5 |
| 314af2c4-5f54-35e6-a923-3f957128f40d | -14.8447 | -51.4401 | 2024-09-27 07:26:30 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 57.0 |
| b0494519-b496-3219-abed-bd1eb0cb6c14 | -15.6367 | -57.4877 | 2024-09-27 07:26:35 | GOES-16 | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 64.5 |
| b7b1e230-29fb-317f-9bb8-5ffd2446df39 | -22.1506 | -47.6716 | 2024-09-27 07:27:08 | GOES-16 | ANALÂNDIA | SÃO PAULO | Brasil | 3502002 | 35 | 33 | nan | nan | nan | Cerrado | 79.0 |
| 40246548-bed9-32eb-8a70-d7bb2f7843de | -22.7433 | -44.8035 | 2024-09-27 07:27:11 | GOES-16 | SILVEIRAS | SÃO PAULO | Brasil | 3552007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 64.1 |
| f764e0a6-a628-362c-beaa-e1a815dfbc1a | -7.5887 | -60.5976 | 2024-09-27 07:35:50 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 48.4 |
| f54258c9-0ac9-338d-8338-96c3ad5d9d5b | -7.5888 | -60.5785 | 2024-09-27 07:35:50 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 48.6 |
| 9bf98d25-f200-3dba-924f-edb693c50b60 | -8.9977 | -67.3909 | 2024-09-27 07:35:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 104.6 |
| 4b453623-130d-3c8d-83e2-62fea60ea265 | -8.9978 | -67.3724 | 2024-09-27 07:35:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 150.5 |
| 33cfbc51-8b79-3701-a2e1-7a156cf9f467 | -8.9978 | -67.3538 | 2024-09-27 07:35:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 47.4 |
| ba54fe90-543b-3f91-b4b8-220c415b158e | -9.0162 | -67.3904 | 2024-09-27 07:35:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 53.5 |
| 43c43623-7a00-3803-9819-74d278367cf2 | -9.0163 | -67.3719 | 2024-09-27 07:35:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 63.2 |
| 0bdd2d5f-071d-360b-b930-b0eff7590264 | -11.1951 | -53.8965 | 2024-09-27 07:36:10 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 72.1 |
| fbbd0e9c-68ed-393a-a936-a3fe65bf2f9a | -12.6824 | -54.6968 | 2024-09-27 07:36:18 | GOES-16 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 72.2 |
| 24b88e68-0c15-3cda-8cd6-84009ebc8578 | -12.7099 | -54.0769 | 2024-09-27 07:36:19 | GOES-16 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 90.0 |
| da97e99d-a65f-3008-9ac0-54d6afca6b44 | -12.7868 | -54.0275 | 2024-09-27 07:36:19 | GOES-16 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 105.1 |
| 225244b9-2067-359f-abb8-6ffa7ebef1ee | -12.8059 | -54.0255 | 2024-09-27 07:36:19 | GOES-16 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 72.0 |
| 4ddf2162-5941-3bf2-9997-323fe2729f0f | -15.6367 | -57.4877 | 2024-09-27 07:36:35 | GOES-16 | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 64.5 |
| dfe27229-3760-3b01-a281-7188c75195df | -22.7433 | -44.8035 | 2024-09-27 07:37:11 | GOES-16 | SILVEIRAS | SÃO PAULO | Brasil | 3552007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 63.6 |
| 413dcb2f-e2f0-3348-81b5-54e7b645a852 | -8.9977 | -67.3909 | 2024-09-27 07:45:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 133.7 |
| 301b9a5c-94ef-34ea-b82e-db9f3cc5a583 | -8.9978 | -67.3724 | 2024-09-27 07:45:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 192.5 |
| 70fe1816-0ca5-308b-b81e-fb5069b8f017 | -8.9978 | -67.3538 | 2024-09-27 07:45:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 67.3 |
| 64bd114e-e185-339a-b9ed-f68ff33e9c8d | -9.0162 | -67.3904 | 2024-09-27 07:45:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 60.6 |
| a3f694df-bed6-3ea8-a82c-449d98f92bcb | -9.0163 | -67.3719 | 2024-09-27 07:45:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 79.6 |
| 137d13c9-7092-37cf-92f2-29c97b2d93fc | -10.0139 | -53.4464 | 2024-09-27 07:46:03 | GOES-16 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 97.3 |
| e7db5d15-2004-37d3-aef2-b4bc2cbe40e7 | -10.0141 | -53.4258 | 2024-09-27 07:46:03 | GOES-16 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 40.1 |
| 7dd7bb28-c584-3ba3-aa23-7190b6e97e91 | -10.0324 | -53.4654 | 2024-09-27 07:46:04 | GOES-16 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 63.8 |
| 9fa65257-6ddc-3cac-815d-d7bc399fdcc1 | -10.0327 | -53.4448 | 2024-09-27 07:46:04 | GOES-16 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 247.3 |
| 4ea28e2e-7b24-3445-861d-275e414e6391 | -10.0329 | -53.4242 | 2024-09-27 07:46:04 | GOES-16 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 74.5 |
| 05a6e2bc-d477-359c-9615-223641dca696 | -12.7099 | -54.0769 | 2024-09-27 07:46:19 | GOES-16 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 82.1 |
| 8015aee2-ea1a-3c78-9a9a-de828574af8f | -12.7868 | -54.0275 | 2024-09-27 07:46:19 | GOES-16 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 90.8 |
| 96859bdb-97ea-3de4-bd0f-9080a2f22363 | -15.6367 | -57.4877 | 2024-09-27 07:46:35 | GOES-16 | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 64.2 |


[Clique aqui para ver as próximas entradas](README130.md)
