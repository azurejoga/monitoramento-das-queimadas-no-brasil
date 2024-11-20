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

## Dados Diários - Página 15

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0d1d4759-e488-3837-a4e2-9eaa1f613616 | -0.18422 | -51.63098 | 2024-11-20 01:26:00 | TERRA_M-M | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 2294154f-8944-3144-b548-e8d56c503e65 | -1.45444 | -52.6812 | 2024-11-20 01:26:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 41.7 |
| 21f97f7e-6bfc-3374-b59a-26f72b13efb1 | -0.96168 | -51.72605 | 2024-11-20 01:26:00 | TERRA_M-M | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 24.0 |
| 99d00efd-793a-37db-ae4d-eb4058f68a72 | -1.415 | -54.92034 | 2024-11-20 01:26:00 | TERRA_M-M | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 3010e77c-4539-3b02-87a2-bd8efff3b3a0 | -0.30879 | -51.56514 | 2024-11-20 01:26:00 | TERRA_M-M | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 18.4 |
| 0170bc67-b3aa-3fd8-87a2-eaf2c8379155 | -1.63096 | -52.62923 | 2024-11-20 01:26:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 19.7 |
| f26d8901-1141-3859-86a1-0a323b49a736 | -1.38258 | -52.42353 | 2024-11-20 01:26:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 7da68cf0-5169-3fc3-a808-088f2f3b650e | -1.32454 | -52.41631 | 2024-11-20 01:26:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 17.3 |
| 29dbdb22-713c-3acf-b274-2009c0f52c9e | -0.94978 | -51.72778 | 2024-11-20 01:26:00 | TERRA_M-M | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 21.3 |
| 3d7adc67-c56b-3ce0-bcef-dca1a4686294 | -1.33308 | -52.23423 | 2024-11-20 01:26:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 5de5c4ab-eddc-35c6-baef-087d61334f57 | -1.54564 | -52.27664 | 2024-11-20 01:26:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 15.9 |
| b35836e9-84a8-3e57-84be-469ff4c0e368 | -1.63692 | -52.67066 | 2024-11-20 01:26:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 31080078-465c-3e2e-8230-5ab8d4c3c1bb | -1.54447 | -52.26741 | 2024-11-20 01:26:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 21.6 |
| 8c1265c2-5ea2-3a0f-94c1-d0ced5a1b6dd | -1.19704 | -53.67118 | 2024-11-20 01:26:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 110.1 |
| 0a9b9586-062b-3320-bf4f-c47691d0324d | -1.45244 | -52.66727 | 2024-11-20 01:26:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 64.2 |
| ddc8c72c-df6e-3795-8b63-9d45236f84dd | -1.30335 | -52.26905 | 2024-11-20 01:26:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 61f89ecb-5800-3a7c-a321-989c005d92c6 | -1.09951 | -51.7447 | 2024-11-20 01:26:00 | TERRA_M-M | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 13.6 |
| 3c2f2466-3301-3498-abae-a81b834e8faf | -1.3012 | -52.25409 | 2024-11-20 01:26:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 4bcbcbf1-7a0f-3ede-b336-99779996f3c4 | -1.14502 | -53.5115 | 2024-11-20 01:26:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 14.8 |
| 535a3358-f1fc-30f6-8341-96e9eb48724f | -1.06898 | -52.39722 | 2024-11-20 01:26:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 2c40d279-b20e-3857-985d-c85aa5c15ce6 | -0.10803 | -51.44217 | 2024-11-20 01:26:00 | TERRA_M-M | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 17.2 |
| b8031860-6568-3eef-bd07-55cba5897b06 | -1.25428 | -53.35755 | 2024-11-20 01:26:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 54f68df3-9ce1-31f6-a204-efa0e084a18f | -1.1993 | -53.67654 | 2024-11-20 01:26:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 95.8 |
| 84802903-579a-30df-b5c2-95c4202dd253 | -0.19072 | -51.64205 | 2024-11-20 01:26:00 | TERRA_M-M | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 11.3 |
| b00bd91e-592e-34fc-97c8-4f226d975f58 | -0.90334 | -51.79085 | 2024-11-20 01:26:00 | TERRA_M-M | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 4ea378ab-fd37-3e5d-b874-f5925ab0d68d | -2.0651 | -53.4229 | 2024-11-20 01:30:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 62.2 |
| d01e025e-6f0e-366b-bf63-0e6de349db1f | -3.0109 | -51.0236 | 2024-11-20 01:30:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 59.6 |
| fd2a8fa7-4dd0-34d0-b0cc-811d2a00b66a | -2.2996 | -48.4863 | 2024-11-20 01:30:00 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 65.1 |
| 155d2de5-b1fc-356a-a337-75447c6c0eda | -17.653 | -40.26 | 2024-11-20 01:30:00 | GOES-16 | LAJEDÃO | BAHIA | Brasil | 2918902 | 29 | 33 | nan | nan | nan | Mata Atlântica | 66.9 |
| 2579a474-3237-367e-a484-f59bc02799d6 | -3.2014 | -54.3243 | 2024-11-20 01:30:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 100.6 |
| d2b2aba5-fb0d-387d-ae9a-40c2a1f91579 | -2.9969 | -45.436 | 2024-11-20 01:30:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 164.3 |
| 9a0256e9-2c75-35c5-9e09-e0b95d501d2e | -3.8021 | -47.7887 | 2024-11-20 01:30:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 50.3 |
| 215df932-d545-388c-8b8d-bc2b5ff3164f | -2.7218 | -49.3295 | 2024-11-20 01:30:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 39.9 |
| 44a747e0-5c8a-3baa-b79f-6e799a30ea98 | -2.6212 | -51.7997 | 2024-11-20 01:30:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 83.6 |
| e5e4f6da-d6aa-381b-bb78-d1b257911b5c | -4.5614 | -48.0141 | 2024-11-20 01:30:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 52.4 |
| 10948021-7466-32d1-b91e-ceb7a31cda5f | -4.4592 | -46.5745 | 2024-11-20 01:30:00 | GOES-16 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 57.6 |
| 24dd3ed7-011f-3e12-b61a-b8e42188ed99 | -4.4404 | -46.5975 | 2024-11-20 01:30:00 | GOES-16 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 45.9 |
| 8c31fa86-0ade-3ac6-98cb-c8d2c1dfd522 | -3.8206 | -47.7879 | 2024-11-20 01:30:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 54.0 |
| 5a88d30d-2f7d-3293-a37b-d67f1fe75bf2 | -4.4405 | -46.5754 | 2024-11-20 01:30:00 | GOES-16 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 58.9 |
| 5c76449b-b577-388d-b602-98c36324b4d7 | -1.2017 | -53.6769 | 2024-11-20 01:30:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 123.1 |
| 4e74b144-d5ed-34ec-b357-def197518164 | -2.6212 | -51.8203 | 2024-11-20 01:30:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 39.6 |
| a97b3c78-d17b-3783-b9d2-946dd44f2d64 | -2.9968 | -45.4584 | 2024-11-20 01:30:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 74.7 |
| 39bfb74e-9740-341c-94e5-e80a4b08a0fd | -2.831 | -45.1267 | 2024-11-20 01:30:00 | GOES-16 | SÃO BENTO | MARANHÃO | Brasil | 2110500 | 21 | 33 | nan | nan | nan | Amazônia | 71.0 |
| f08e11c3-02f9-3866-bae3-d1432d49caf8 | -3.8205 | -47.8096 | 2024-11-20 01:30:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 64.8 |
| 52773c5f-cc84-3d82-8645-31ab93355706 | -17.6522 | -40.286 | 2024-11-20 01:30:00 | GOES-16 | LAJEDÃO | BAHIA | Brasil | 2918902 | 29 | 33 | nan | nan | nan | Mata Atlântica | 122.1 |
| 53e22091-0ce9-3609-9651-a1e9170a0910 | -2.7217 | -49.3508 | 2024-11-20 01:30:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 55.9 |
| 53ba7127-17de-3e76-938a-62b7f94d6d20 | -3.011 | -51.0028 | 2024-11-20 01:30:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 62.5 |
| b9b3d08e-5c76-3b77-8ce9-3a16fb4666b4 | -3.802 | -47.8104 | 2024-11-20 01:30:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 62.3 |
| 8539b15a-62d2-3662-a267-43b83123561b | -2.2725 | -45.4593 | 2024-11-20 01:30:00 | GOES-16 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 65.1 |
| 926df233-5905-3850-95d5-e9e379a4f670 | -1.2018 | -53.6568 | 2024-11-20 01:30:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 76.1 |
| de04de30-7419-344b-a8f1-d79929f03f82 | -2.6212 | -51.7997 | 2024-11-20 01:40:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 69.7 |
| 533df91a-140c-3512-bed3-0c1dacfd73a6 | -4.4405 | -46.5754 | 2024-11-20 01:40:00 | GOES-16 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 45.1 |
| b6f04195-8692-37a7-a3fb-0307c8e32f3c | -3.011 | -51.0028 | 2024-11-20 01:40:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 61.4 |
| fd01afcb-2fdf-37f0-9297-3b65825371c4 | -3.2014 | -54.3243 | 2024-11-20 01:40:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 62.3 |
| 8a55a729-e737-3050-9a7c-14e204efcd4b | -2.9969 | -45.436 | 2024-11-20 01:40:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 112.5 |
| af93d8e8-af78-3dc9-add3-e9428f52a12c | -3.0155 | -45.4353 | 2024-11-20 01:40:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 89.1 |
| eaed6ed7-0fea-3365-8364-0384d0047ce5 | -4.459 | -46.5966 | 2024-11-20 01:40:00 | GOES-16 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 52.8 |
| 15aff3b3-2a6f-3cfb-a2bc-6237a82d0151 | -1.2017 | -53.6769 | 2024-11-20 01:40:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 123.9 |
| 503b3814-57ff-3ac9-8bea-6024629ebf2a | -2.7217 | -49.3508 | 2024-11-20 01:40:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 101.9 |
| 09ac6daa-764f-3672-bbbe-bac8266b120c | -4.4592 | -46.5745 | 2024-11-20 01:40:00 | GOES-16 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 58.8 |
| e44ba3b0-00e6-351f-b9d2-545a277168e3 | -3.0109 | -51.0236 | 2024-11-20 01:40:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 64.8 |
| bee759f1-c5ee-3c4a-8af6-cc33a0f23144 | -4.4404 | -46.5975 | 2024-11-20 01:40:00 | GOES-16 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 43.6 |
| b9539880-7574-3d29-9110-8fdba4c4ba0f | -2.7218 | -49.3295 | 2024-11-20 01:40:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 49.5 |
| 0d1799a8-fe1b-3193-a046-481494dfa5a1 | -4.5614 | -48.0141 | 2024-11-20 01:40:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 51.3 |
| e38cc008-17e8-377b-b99a-20c56459c513 | -5.9556 | -48.0642 | 2024-11-20 01:40:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 48.4 |
| ee9b5878-88e6-37d5-86e8-4d89a3e4e519 | -3.2014 | -54.3243 | 2024-11-20 01:50:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 78.0 |
| c9ccfa36-8bc4-329a-99b3-5b7bffd15412 | -4.4405 | -46.5754 | 2024-11-20 01:50:00 | GOES-16 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 54.3 |
| ea2025ed-9292-33b2-abf1-f145873b7b1b | -4.459 | -46.5966 | 2024-11-20 01:50:00 | GOES-16 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 42.5 |
| ec67d42e-10ca-3f12-bb65-03ad8d74b1d7 | -2.9969 | -45.436 | 2024-11-20 01:50:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 109.9 |
| a7372ec8-73a4-3b17-affb-77a29a04e2f2 | -2.6212 | -51.7997 | 2024-11-20 01:50:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 49.1 |
| 437c2e97-d3f2-382c-a702-d46619f0c194 | -11.1109 | -54.6204 | 2024-11-20 01:50:00 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 97.2 |
| 0a5f1f1d-7eb0-3ced-ad46-c4a40e312dcd | -3.0155 | -45.4353 | 2024-11-20 01:50:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 66.0 |
| b728daa7-4a1b-317a-87c9-95cc504da51f | -3.011 | -51.0028 | 2024-11-20 01:50:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 58.4 |
| 7b7c6f17-b806-300a-95b8-111372f8914f | -11.092 | -54.6221 | 2024-11-20 01:50:00 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 75.8 |
| 104e6b07-4654-3678-bfc3-ec55aa224e5c | -1.1834 | -53.6771 | 2024-11-20 01:50:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 65.8 |
| 296cbdbb-3797-3495-a423-68849b2c0e0f | -4.4592 | -46.5745 | 2024-11-20 01:50:00 | GOES-16 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 48.9 |
| b6e876de-f8f9-3182-aa2e-45b8703a9fe3 | -1.4603 | -52.6812 | 2024-11-20 01:50:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 62.2 |
| fcab683a-2085-315e-8f1f-81b5f07b694f | -11.1106 | -54.6408 | 2024-11-20 01:50:00 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 69.8 |
| 57674588-c122-3e9a-8e52-af6e8995db75 | -1.2017 | -53.6769 | 2024-11-20 01:50:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 91.4 |
| 1f483f66-8970-3d25-baa4-1a71ae59735c | -11.0917 | -54.6425 | 2024-11-20 01:50:00 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 54.9 |
| bb5f22b8-3b24-3cc1-b446-2a7a0e08e2ac | -3.0109 | -51.0236 | 2024-11-20 01:50:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 57.9 |
| ec787dd9-e6c3-354e-9b0c-25e5de8a8651 | -3.1477 | -49.1251 | 2024-11-20 01:50:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 43.0 |
| f87055aa-db13-3e00-80a0-9458f28e152f | -5.9742 | -48.063 | 2024-11-20 01:50:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 52.0 |
| 18de5e4f-e50b-3168-848f-bddc6690fb05 | -4.4404 | -46.5975 | 2024-11-20 01:50:00 | GOES-16 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 47.6 |
| 90196f74-9911-31ee-8528-ef18c1e90f2a | -11.092 | -54.6221 | 2024-11-20 02:00:00 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 69.8 |
| c9314be2-b59a-3ad7-9bbc-efdbcf3e3bb4 | -5.9742 | -48.063 | 2024-11-20 02:00:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 59.6 |
| 07f0b817-eaf9-389f-8973-28bae1fef6c0 | -5.9556 | -48.0642 | 2024-11-20 02:00:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 72.0 |
| ca44a485-92f9-3183-b16b-8f0337051e4c | -4.5614 | -48.0141 | 2024-11-20 02:00:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 44.4 |
| f83773d1-b87a-3baa-b2b7-6ba5b6d4562d | -3.011 | -51.0028 | 2024-11-20 02:00:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 52.1 |
| a5fefe85-af0b-3319-b41c-1a30331965de | -4.4404 | -46.5975 | 2024-11-20 02:00:00 | GOES-16 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 49.5 |
| 848cf5f8-ba82-34d2-995f-02d8c6bcdc7e | -11.1106 | -54.6408 | 2024-11-20 02:00:00 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 72.4 |
| a4f77223-8d2a-3346-9f8f-c867371ccfd6 | -3.0109 | -51.0236 | 2024-11-20 02:00:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 52.4 |
| f8650426-e7a1-3c17-9281-47b846540f22 | -4.4592 | -46.5745 | 2024-11-20 02:00:00 | GOES-16 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 53.6 |
| 0cb6efbb-4639-3fbd-86bf-01e54736f350 | -3.0155 | -45.4353 | 2024-11-20 02:00:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 71.2 |
| 82771575-9af6-37d7-9daf-6d5fca5e73b5 | -1.2017 | -53.6769 | 2024-11-20 02:00:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 90.1 |
| ed5e4a69-3adc-343c-9048-19d2fbd1ca58 | -4.459 | -46.5966 | 2024-11-20 02:00:00 | GOES-16 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 52.0 |
| e442df0b-9ab4-3a07-b75b-909293cb9f38 | -4.4405 | -46.5754 | 2024-11-20 02:00:00 | GOES-16 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 47.9 |
| ff66c77f-2a81-3548-816c-0e55bbdc040a | -3.2014 | -54.3243 | 2024-11-20 02:00:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 64.0 |
| 109b340a-1aec-3574-9b7c-d90dc3ee2e93 | -4.3959 | -47.7618 | 2024-11-20 02:00:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 47.9 |
| d37d5edc-019b-37d3-b7fd-7653e8fd07d8 | -2.9969 | -45.436 | 2024-11-20 02:00:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 88.4 |


[Clique aqui para ver as próximas entradas](README16.md)
