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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f584c2c2-8ac3-3753-99e3-3896b59662a2 | -23.07579 | -50.35043 | 2025-05-16 04:12:00 | NOAA-21 | BANDEIRANTES | PARANÁ | Brasil | 4102406 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| dc9ae9b1-8583-321c-803d-c5f3258f54c8 | -23.98608 | -48.91746 | 2025-05-16 04:12:00 | NOAA-21 | ITAPEVA | SÃO PAULO | Brasil | 3522406 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 80c172da-7719-3171-b667-a32cb0fbfe35 | -23.40631 | -46.55808 | 2025-05-16 04:12:00 | NOAA-21 | SÃO PAULO | SÃO PAULO | Brasil | 3550308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 5bfce843-55fd-3627-a32d-6921b3f2a1af | -23.60698 | -48.29527 | 2025-05-16 04:12:00 | NOAA-21 | ITAPETININGA | SÃO PAULO | Brasil | 3522307 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 22cd4706-fe6c-3a2b-9d88-88d1bc4f4cb3 | -27.11535 | -50.57176 | 2025-05-16 04:14:00 | NOAA-21 | CURITIBANOS | SANTA CATARINA | Brasil | 4204806 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 578e05e4-ac89-3368-9681-712ece64d901 | -27.11902 | -50.57264 | 2025-05-16 04:14:00 | NOAA-21 | CURITIBANOS | SANTA CATARINA | Brasil | 4204806 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| ea06197b-3a25-306e-b87d-d58b67812ca8 | -28.587 | -49.44148 | 2025-05-16 04:14:00 | NOAA-21 | SIDERÓPOLIS | SANTA CATARINA | Brasil | 4217600 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| deb820af-ae25-3041-82ae-f2bc1ffb4652 | -28.74401 | -49.38519 | 2025-05-16 04:14:00 | NOAA-21 | CRICIÚMA | SANTA CATARINA | Brasil | 4204608 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 0f1c685c-744c-3d51-bd32-d6ed01f0bc1e | -28.5601 | -49.00563 | 2025-05-16 04:14:00 | NOAA-21 | JAGUARUNA | SANTA CATARINA | Brasil | 4208807 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 2e5adc84-0c87-32e2-8259-aac3d65611bc | -9.96059 | -49.8081 | 2025-05-16 04:34:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 871655dd-eb15-3989-b7bc-77bc6fa68089 | -10.06998 | -48.07946 | 2025-05-16 04:34:00 | NPP-375D | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| aba908c0-df8a-37bb-9503-2c9778e5c737 | -9.37088 | -48.40074 | 2025-05-16 04:34:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9ef96f7e-5fb2-3e40-aeca-2502f6007d6a | -9.58022 | -46.84538 | 2025-05-16 04:34:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 5c6059b2-9208-31f9-9501-542ebfae99a8 | -7.42386 | -43.46813 | 2025-05-16 04:34:00 | NPP-375D | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| dfc16fe4-de6e-3437-99b4-9db4c70c1ea1 | -7.54873 | -45.87496 | 2025-05-16 04:34:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 63ffadf6-8ccc-30f5-8e30-735e536a714e | -10.63644 | -48.09212 | 2025-05-16 04:34:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e75911d9-0879-3a9e-aea7-dc8a2e3bc72a | -7.54438 | -45.87534 | 2025-05-16 04:34:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 65c09894-c1ad-3aff-bc05-b9cef05c6b5e | -7.54787 | -45.87588 | 2025-05-16 04:34:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 8ee5bfd3-26b3-38c5-84fb-07800ad9807b | -10.35667 | -47.97891 | 2025-05-16 04:34:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c95d2636-5e0b-3428-a39f-a7cb59b9d42e | -9.66649 | -47.5602 | 2025-05-16 04:34:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 259f7984-c1ab-33f0-b9ba-cc73ca6fd261 | -9.367 | -48.40371 | 2025-05-16 04:34:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8a08c6cd-54af-3ae4-b6b8-56c964f9e7ab | -7.54906 | -45.86817 | 2025-05-16 04:34:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f7c84235-557e-3daf-a908-9c30b2c67dd5 | -7.54846 | -45.87204 | 2025-05-16 04:34:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1c9a6d1a-44bd-302d-a188-bd10f77100be | -9.45054 | -40.38984 | 2025-05-16 04:34:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 24c6eb1a-3ea9-3f04-98d2-fc8f5861d212 | -7.07836 | -44.39443 | 2025-05-16 04:34:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b7ed002a-30f2-3170-8032-9ced86395cf1 | -10.51966 | -48.55521 | 2025-05-16 04:34:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 65a141b4-8c78-3442-a714-b5deea6c539a | -10.34511 | -47.67659 | 2025-05-16 04:34:00 | NPP-375D | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 09b0b33c-cc70-3a3a-bee9-93c617e0b993 | -9.44901 | -40.40129 | 2025-05-16 04:34:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 3.8 |
| b16d3394-0741-3af7-a4ca-fad191d671ce | -10.34848 | -47.67713 | 2025-05-16 04:34:00 | NPP-375D | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9e08acb7-6fa0-38ee-82b6-1779134d3a93 | -9.58078 | -46.84165 | 2025-05-16 04:34:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| df2966fd-cdcd-37ea-b699-a5deb7f721ee | -7.0753 | -44.38945 | 2025-05-16 04:34:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c18f12b9-a281-3bc2-a40c-668966241639 | -9.2899 | -46.71469 | 2025-05-16 04:34:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 73a70852-0357-3f95-9e3f-3438a4bd8cfd | -9.44977 | -40.39556 | 2025-05-16 04:34:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 71fb0cda-20e5-311d-ae6b-2091a4a31e15 | -8.9002 | -44.78237 | 2025-05-16 04:34:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f4778fcd-6999-3922-898a-d06a9db11ece | -7.54582 | -45.87058 | 2025-05-16 04:34:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8d7e91c7-b4f7-3d2a-8132-21251b472680 | -7.54524 | -45.87443 | 2025-05-16 04:34:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 1b841306-ad73-3d32-9854-ca4060c2f975 | -9.95957 | -49.80839 | 2025-05-16 04:34:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| a05eebc2-8193-3dd1-bf61-d9b4bd5a92a8 | -11.0275 | -48.80323 | 2025-05-16 04:34:00 | NPP-375D | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 829c5fdc-295b-345c-8b68-e0d1db02290c | -6.71847 | -47.59152 | 2025-05-16 04:34:00 | NPP-375D | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d3f83e22-3f6c-3a4c-bb09-c86b76d01fb5 | -10.00607 | -47.84037 | 2025-05-16 04:34:00 | NPP-375D | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| cb8a3c43-2747-3612-8ea8-752f0319f7dd | -7.79871 | -45.34158 | 2025-05-16 04:34:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5257099e-8078-3314-8a49-b011729ce63f | -10.34613 | -51.69172 | 2025-05-16 04:34:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0eff67ce-decd-3a27-a311-65244a3ca3a2 | -10.34608 | -47.98086 | 2025-05-16 04:34:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 115a6a93-42f9-383b-b631-ca93a8c07956 | -8.42752 | -46.63448 | 2025-05-16 04:34:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 76fd6004-d47f-3b53-8e3e-0b011407825f | -7.23262 | -44.77845 | 2025-05-16 04:34:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8c4cd6ad-edd5-37a6-8aa6-20f3ef0e9960 | -9.5791 | -46.85277 | 2025-05-16 04:34:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b5050b0b-da11-397e-9962-55d3919f9f21 | -7.74215 | -46.32714 | 2025-05-16 04:34:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 428fe592-b0bf-3b75-9d4f-9de487bb797a | -11.16285 | -48.67649 | 2025-05-16 04:34:00 | NPP-375D | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 8b108a0b-307a-3872-bf09-3cf673dd171a | -9.36755 | -48.40021 | 2025-05-16 04:34:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 08c42ec1-2325-3460-b8aa-9cba9fab34f7 | -11.32591 | -46.50013 | 2025-05-16 04:34:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4e1911c6-afd0-33c0-adff-b651ad4e031c | -9.37143 | -48.39724 | 2025-05-16 04:34:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 192cbc74-371c-3e83-b2a4-fc3674f2acfa | -10.35778 | -47.97181 | 2025-05-16 04:34:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 65740b37-9adc-3909-83d4-2b94ec75a79e | -10.34544 | -51.69583 | 2025-05-16 04:34:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c8e12741-ab6b-30c9-8e02-83b090c80b3a | -10.34456 | -47.68018 | 2025-05-16 04:34:00 | NPP-375D | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 21b00b89-bf38-3eb7-9cb4-2c2375cee91f | -8.5134 | -49.13708 | 2025-05-16 04:34:00 | NPP-375D | COUTO MAGALHÃES | TOCANTINS | Brasil | 1706001 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fbb4ca67-806d-3dcf-a834-a2e492503067 | -10.34324 | -51.68699 | 2025-05-16 04:34:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d3cc6682-db29-3951-8a42-f63f9c1dc705 | -7.20382 | -43.10691 | 2025-05-16 04:34:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 9cb9e9f0-89f6-3eb3-ae53-0b6977e213f9 | -7.20338 | -43.10622 | 2025-05-16 04:34:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| e7c6237a-0118-3b01-a02b-67eb4b1b55cc | -6.7218 | -47.59205 | 2025-05-16 04:34:00 | NPP-375D | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| aa730d15-316c-3107-a983-bc3d54b4e28a | -7.54931 | -45.87111 | 2025-05-16 04:34:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 45c3fcb3-d5f4-3a89-ac85-9f80d6c9798d | -7.28092 | -43.28139 | 2025-05-16 04:34:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ec18e6e0-c007-363b-a76b-4f50e9900593 | -7.07156 | -44.38892 | 2025-05-16 04:34:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| daa9948b-2100-390e-97b1-70a952d3e6c5 | -10.3591 | -47.97617 | 2025-05-16 04:34:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7953ca4a-eb3b-3e6a-8ec1-e164db749a47 | -5.84801 | -42.59162 | 2025-05-16 04:34:00 | NPP-375D | OLHO D'ÁGUA DO PIAUÍ | PIAUÍ | Brasil | 2207108 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 959939b6-a640-38bb-9837-38d996ba937b | -10.06274 | -48.08197 | 2025-05-16 04:34:00 | NPP-375D | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b17499fe-d947-361a-ad9c-384580b8516e | -5.64062 | -48.60657 | 2025-05-16 04:34:00 | NPP-375D | SÃO DOMINGOS DO ARAGUAIA | PARÁ | Brasil | 1507151 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| d9477a63-7485-3b34-ba00-efb6dbaa1acc | -10.35965 | -47.97263 | 2025-05-16 04:34:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a0842b3f-5fea-3ae2-9332-e5a94812bde7 | -6.62226 | -48.00747 | 2025-05-16 04:34:00 | NPP-375D | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7885dc6d-22e5-37b0-817a-5356bedd9c34 | -7.32052 | -43.24132 | 2025-05-16 04:34:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2b080e7a-c468-3322-a006-f8ba48c984a6 | -5.65512 | -44.35485 | 2025-05-16 04:34:00 | NPP-375D | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a5095930-732a-37ac-8588-3b06e0f0d4db | -7.45713 | -49.77795 | 2025-05-16 04:34:00 | NPP-375D | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e55e8c12-8f1e-3935-829e-cafc69332d52 | -10.35723 | -47.97536 | 2025-05-16 04:34:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0988b3a9-1556-384c-ba70-7a17e5ad701f | -11.16618 | -48.67702 | 2025-05-16 04:34:00 | NPP-375D | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 2c86b63f-ae69-37fe-aa9a-b376bc93764d | -9.31104 | -44.83298 | 2025-05-16 04:34:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| b93b5df6-6044-3d33-ae16-3901ee9bb79a | -10.4621 | -49.0501 | 2025-05-16 04:34:00 | NPP-375D | NOVA ROSALÂNDIA | TOCANTINS | Brasil | 1715002 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5f2dace2-6cc0-3f5a-9d55-589efad7fe79 | -10.00551 | -47.84393 | 2025-05-16 04:34:00 | NPP-375D | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c70b034f-2119-3eb1-9d4b-6aaf0df9734c | -10.35333 | -47.97837 | 2025-05-16 04:34:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 42a83860-e5f6-3385-b284-37e32bc31f0b | -7.54498 | -45.8715 | 2025-05-16 04:34:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c5ab27e9-79fc-3e4b-a8e3-a5bb6d8e042f | -11.15286 | -48.67488 | 2025-05-16 04:34:00 | NPP-375D | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 52fc848d-459e-3214-b92f-ff21a1fd5c1a | -10.34273 | -47.98032 | 2025-05-16 04:34:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 01334c33-228a-318d-a423-6c8438ec4cde | -10.34943 | -47.98139 | 2025-05-16 04:34:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 69e41c6e-32d7-3fa3-a3e6-8b5bca445bba | -11.0656 | -47.41154 | 2025-05-16 04:34:00 | NPP-375D | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 891c12ca-ca2b-3833-9b47-e9fe49edf8f6 | -9.31171 | -44.82849 | 2025-05-16 04:34:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 9b062777-c66d-3ab5-97f5-d79d2e315971 | -10.3768 | -49.30708 | 2025-05-16 04:34:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4eb7b5bc-7f08-390c-aafa-842e7994e3c2 | -8.42695 | -46.63818 | 2025-05-16 04:34:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 36bd1904-da50-364d-bb5d-349ac83526d6 | -11.02695 | -48.80674 | 2025-05-16 04:34:00 | NPP-375D | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4f78d274-2409-326a-bdea-b9ec7a213e11 | -10.00216 | -47.84339 | 2025-05-16 04:34:00 | NPP-375D | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 10af696a-f2e1-3528-9c47-1b13f34a559b | -7.31978 | -43.2464 | 2025-05-16 04:34:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 19b439a1-67df-3903-aae2-4734951e6f2e | -11.15952 | -48.67595 | 2025-05-16 04:34:00 | NPP-375D | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4b5d8ef5-0087-340e-b3ed-d7bc5d7433ed | -9.36422 | -48.39968 | 2025-05-16 04:34:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8c136ca3-2a56-3a58-ac71-6b3b375cf5aa | -7.07755 | -44.91679 | 2025-05-16 04:34:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c0772973-b1cd-33d0-88a2-130a443593ee | -10.34998 | -47.97784 | 2025-05-16 04:34:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 68df62fd-1e0d-3d9e-80f8-d719c85bef40 | -11.1623 | -48.68002 | 2025-05-16 04:34:00 | NPP-375D | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| a64b13d0-e088-38eb-a86b-86114f6e210a | -10.27931 | -51.46515 | 2025-05-16 04:34:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 623ce419-329f-377c-b2c9-7b4c87c744ed | -10.34255 | -51.6911 | 2025-05-16 04:34:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1f047e4d-13db-34d7-9e86-7e87775bdbcc | -8.0031 | -49.70771 | 2025-05-16 04:34:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c7a09d40-a0d1-392c-9f45-5f105d8369de | -10.51633 | -48.55468 | 2025-05-16 04:34:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a03555bc-ad7d-3448-b4c7-5e824e0b33b5 | -7.07393 | -44.91621 | 2025-05-16 04:34:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fa0387bf-44ff-30be-9b44-8762c093a5d3 | -5.41651 | -47.56819 | 2025-05-16 04:34:00 | NPP-375D | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 412eabcd-7ee4-35b2-addc-a80f202df667 | -9.3681 | -48.39671 | 2025-05-16 04:34:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |


[Clique aqui para ver as próximas entradas](README7.md)
