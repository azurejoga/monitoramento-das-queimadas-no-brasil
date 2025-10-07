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

## Dados Diários - Página 118

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 908dbbd4-f5c1-3ff1-8d3b-b3eaf021c521 | -13.3044 | -48.0575 | 2025-10-07 12:50:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 80.4 |
| 7cb8050d-3df5-3fa4-933e-c2a568be761b | -8.4824 | -46.2912 | 2025-10-07 12:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 82.9 |
| d119994e-2f52-3e9c-b71c-e0965b5b923c | -10.1939 | -45.5567 | 2025-10-07 12:50:00 | GOES-19 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 88.8 |
| 0783e31a-76f9-3989-9e70-d65b1e60480a | -10.456 | -48.3607 | 2025-10-07 12:50:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 335.6 |
| db43d82e-a339-3dc3-952c-e16eb8c2d864 | -18.9846 | -47.8282 | 2025-10-07 12:50:00 | GOES-19 | INDIANÓPOLIS | MINAS GERAIS | Brasil | 3130705 | 31 | 33 | nan | nan | nan | Cerrado | 83.8 |
| cb8b3c04-6469-32e7-b7a5-d56cb889fdc4 | -10.4746 | -48.3805 | 2025-10-07 12:50:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 353.5 |
| 6cdeb444-32ff-3237-b1cd-59fe03668a68 | -10.9109 | -47.1129 | 2025-10-07 12:50:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 112.0 |
| de776c58-1fbd-3476-9d42-671d4e013061 | -13.004 | -51.0195 | 2025-10-07 12:50:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 94.1 |
| 88979682-4268-3a06-8191-c6762ae8ed96 | -13.3241 | -48.0324 | 2025-10-07 12:50:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 95.8 |
| d70a853a-8223-332e-80fe-56f04c757f01 | -11.7409 | -45.371 | 2025-10-07 12:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 67.1 |
| 4630113c-998b-3732-b88a-fa04ec436f54 | -14.3148 | -45.8348 | 2025-10-07 12:50:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 89.3 |
| b78f3b26-7f79-339f-aee5-c574d02e0b64 | -8.4525 | -47.2067 | 2025-10-07 12:50:00 | GOES-19 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 78.4 |
| c6bf82a9-874a-37d6-8fad-1cccc5a2622c | -13.0231 | -51.0171 | 2025-10-07 12:50:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 88.2 |
| 49023d1a-dad3-3af9-9b50-804a2b4994d4 | -17.9979 | -45.0011 | 2025-10-07 12:50:00 | GOES-19 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 77.9 |
| 88cca6e3-5c30-3670-b5ef-f6cfec3b8ca1 | -15.3737 | -47.3201 | 2025-10-07 12:50:00 | GOES-19 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 102.8 |
| 76c609d1-3dec-3c80-9563-a37a79efa334 | -14.5057 | -46.9242 | 2025-10-07 12:50:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 89.3 |
| 2c437598-9f4d-3c47-8a2b-be357e0799a2 | -16.2942 | -50.9868 | 2025-10-07 12:50:00 | GOES-19 | ISRAELÂNDIA | GOIÁS | Brasil | 5210307 | 52 | 33 | nan | nan | nan | Cerrado | 64.6 |
| 250003eb-564f-3598-a89f-bd9c286b2a77 | -8.5007 | -46.3342 | 2025-10-07 12:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 78.9 |
| 2221df4f-5629-3ac5-b3b4-c2c09ed64211 | -11.7217 | -45.3738 | 2025-10-07 12:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 91.4 |
| 07a57032-49aa-3964-bdff-c4f891a6861b | -13.2232 | -51.6744 | 2025-10-07 12:50:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 110.6 |
| 6e5971b8-62ac-3d24-8327-c2d4de54ef44 | -14.7389 | -46.0138 | 2025-10-07 12:50:00 | GOES-19 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 110.4 |
| f75cf731-936f-3c23-8f76-e2c05daa4480 | -8.501 | -46.3117 | 2025-10-07 12:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 88.0 |
| 0e4dcf3a-0ff6-3537-b517-1621e73cf053 | -8.2068 | -44.2263 | 2025-10-07 12:50:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 492.3 |
| 729b33ec-a401-31d2-b1f5-e0bbc0cd2222 | -8.872 | -46.7655 | 2025-10-07 12:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 89.2 |
| 128a7046-f13b-3e09-b3a6-996b04eceb7a | -10.1573 | -45.4701 | 2025-10-07 12:50:00 | GOES-19 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 125.1 |
| 1b0c9f41-bcd5-3439-904c-3f1583945b18 | -8.1876 | -44.2514 | 2025-10-07 12:50:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 97.1 |
| f7ca4f7b-88e0-39c2-91bc-6751cd9bfb5d | -14.2759 | -45.8416 | 2025-10-07 12:50:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 75.3 |
| 35d5a2ca-008b-3b5b-9808-4701644a8f69 | -10.1943 | -45.5339 | 2025-10-07 12:50:00 | GOES-19 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 168.6 |
| c756a042-5aae-399d-a9ee-fb7ae7e36508 | -12.891 | -54.7577 | 2025-10-07 12:50:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 228.5 |
| c5ba9083-3ef9-311e-ba5e-a4e0392a2be0 | -11.2433 | -50.2859 | 2025-10-07 12:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 99.9 |
| 6892b424-3ea1-3c00-a2f1-5c9d5a9764f1 | -18.0187 | -44.9725 | 2025-10-07 12:50:00 | GOES-19 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 71.7 |
| 47b4465a-711f-3c8a-83bc-9605a14e4293 | -8.1804 | -43.3445 | 2025-10-07 12:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 121.2 |
| a9622be1-de9c-38dd-a5d9-d186dba9b06e | -14.7384 | -46.037 | 2025-10-07 12:50:00 | GOES-19 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 114.2 |
| 2d70ba09-7765-3e6a-9a8d-2e6765daf18f | -11.8447 | -44.9176 | 2025-10-07 12:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 121.8 |
| 3dee4d48-715e-3ab2-89eb-2ae1e79bb5b6 | -14.2949 | -45.8613 | 2025-10-07 12:50:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 80.7 |
| 7db85116-2982-32a7-9801-1167a77fa4f9 | -10.4245 | -45.3907 | 2025-10-07 12:50:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 261.1 |
| cd93cf72-2567-3a37-82d7-148cb2461198 | -14.758 | -46.0335 | 2025-10-07 12:50:00 | GOES-19 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 115.4 |
| f4f72d7b-b008-3b45-938d-ae9313c7246d | -12.9426 | -46.8109 | 2025-10-07 12:50:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 63.5 |
| 258b579a-2798-3dca-bc09-89213f744c09 | -10.9303 | -47.0882 | 2025-10-07 12:50:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 116.5 |
| 5be6c924-731d-3c3f-ae57-fbf8cb3bdbb8 | -10.4054 | -45.3931 | 2025-10-07 12:50:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 120.1 |
| f21f7b46-d4c4-3734-be9b-416e8fc7652d | -12.9101 | -54.7558 | 2025-10-07 12:50:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 77.3 |
| b594ed5c-2617-3fd4-8fa3-69e805929da1 | -10.1753 | -45.5363 | 2025-10-07 12:50:00 | GOES-19 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 93.2 |
| a108b224-f36d-3ed6-abd6-56e041a3b08b | -12.8913 | -54.7372 | 2025-10-07 12:50:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 364.8 |
| b47b44c8-acda-3167-b065-b3984564e108 | -8.1055 | -44.7891 | 2025-10-07 12:50:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 102.3 |
| 375d5de7-dd49-380a-a51b-c6dd40d1aae9 | -11.6859 | -46.3366 | 2025-10-07 12:50:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 77.4 |
| 9735b60b-1b02-3c28-9d83-747183899f8d | -8.1879 | -44.2283 | 2025-10-07 12:50:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 252.3 |
| 392a97d1-c0ce-37c4-a3e5-ed5184ef1388 | -11.2623 | -50.2838 | 2025-10-07 12:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 88.9 |
| a884fdd0-1914-39f3-b516-7dbf85eae885 | -8.4522 | -47.2288 | 2025-10-07 12:50:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 73.1 |
| 321dd4cb-7eec-337d-9a5c-9e0bd6de79fd | -11.1644 | -54.8804 | 2025-10-07 12:50:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 78.9 |
| 52cd5aab-5447-3dc4-86ff-affa311a6796 | -8.6798 | -47.0738 | 2025-10-07 12:50:00 | GOES-19 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 71.7 |
| 5c6dae23-48bb-3074-bd55-2105f8ccf12b | -8.1882 | -44.2052 | 2025-10-07 12:50:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 219.6 |
| 3c3411b2-81cf-3953-a753-2091dba1107b | -12.9619 | -46.808 | 2025-10-07 12:50:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 102.0 |
| da5fdd8a-8e27-323c-86cb-2c152630d90d | -8.8986 | -47.6483 | 2025-10-07 12:50:00 | GOES-19 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 75.1 |
| cd74d9db-476e-3d80-b138-61489210885e | -14.7585 | -46.0104 | 2025-10-07 12:50:00 | GOES-19 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 95.2 |
| 34e92614-553c-3ec7-94ab-6c5514b30e05 | -14.8645 | -51.4158 | 2025-10-07 12:50:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 87.2 |
| 83ab4c48-1c28-3201-a465-06f3d601b956 | -10.4058 | -45.3702 | 2025-10-07 12:50:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 124.8 |
| e9e520fd-340a-3105-baa9-51414a73794d | -10.8919 | -47.1153 | 2025-10-07 12:50:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 131.5 |
| 45a05bc6-9af1-326d-bb53-40974041e089 | -11.1455 | -54.882 | 2025-10-07 13:00:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 194.5 |
| 4a761ff3-3841-3b31-8449-510710aa233d | -9.6804 | -45.6645 | 2025-10-07 13:00:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 78.4 |
| d7c001b6-fc7e-3c45-9f6e-d8646bd78c5b | -13.2465 | -48.066 | 2025-10-07 13:00:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 55.0 |
| 3a486a04-478d-3f2e-b590-ca98ebebfb3b | -13.2424 | -51.672 | 2025-10-07 13:00:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 85.1 |
| e0fb7b51-25e9-3f5f-8dfb-b5f2c83d26a5 | -11.2433 | -50.2859 | 2025-10-07 13:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 93.4 |
| a7b67f7d-d083-3b5c-bab6-40ae605037cb | -14.3148 | -45.8348 | 2025-10-07 13:00:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 102.5 |
| 4e10d3ec-2702-3427-944a-006dd76f9693 | -8.4821 | -46.3136 | 2025-10-07 13:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 96.9 |
| 095ccef7-9ee5-3162-9f6f-f9c9dc309ed1 | -11.7221 | -45.3508 | 2025-10-07 13:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 85.7 |
| d88b7178-f0eb-383c-9221-5d1934693c6c | -8.4525 | -47.2067 | 2025-10-07 13:00:00 | GOES-19 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 160.0 |
| 69315968-7d36-3d1b-bb04-28ab525f155c | -12.891 | -54.7577 | 2025-10-07 13:00:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 291.0 |
| b1af42ed-272f-35f5-a3a1-6821db1171c4 | -15.5812 | -52.5556 | 2025-10-07 13:00:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 79.1 |
| ad74b370-a55c-30d2-8e1b-92b59098cf9c | -15.5808 | -52.5769 | 2025-10-07 13:00:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 64.1 |
| c0910106-a3ab-370b-b0ec-f70b28f878e2 | -10.428 | -50.3946 | 2025-10-07 13:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 100.7 |
| db8952d7-8743-36c8-b24e-e288abc246b1 | -14.758 | -46.0335 | 2025-10-07 13:00:00 | GOES-19 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 130.9 |
| 0ad231c0-140b-3a80-92ce-049cfaf91f23 | -10.1569 | -45.493 | 2025-10-07 13:00:00 | GOES-19 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 89.4 |
| e7e6aa62-3905-3110-8bed-eb23f38d1dc1 | -8.1804 | -43.3445 | 2025-10-07 13:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 107.7 |
| 3bb61174-247d-3a1f-bc81-a74d5d948c72 | -14.2949 | -45.8613 | 2025-10-07 13:00:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 63.5 |
| 3f2795ec-f50a-35e0-a6b0-63703ad10d1d | -11.6859 | -46.3366 | 2025-10-07 13:00:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 100.7 |
| 3639053f-0bcc-3a1e-a40d-4ff68db5c1d9 | -8.4522 | -47.2288 | 2025-10-07 13:00:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 127.2 |
| 9e75b86f-4fb4-36dc-b7ab-9c6276eb204e | -13.2658 | -48.0632 | 2025-10-07 13:00:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 118.9 |
| e82814a1-7025-3004-ac45-72bd9a4ee4c3 | -14.7775 | -46.03 | 2025-10-07 13:00:00 | GOES-19 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 90.6 |
| 8c25dd4b-f5e8-3313-bf8e-d9d522efabc1 | -14.6327 | -48.3219 | 2025-10-07 13:00:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 83.5 |
| 489bb56b-3e8c-3542-a656-7b8f395f5eb3 | -12.4669 | -45.5155 | 2025-10-07 13:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 140.7 |
| a22ffacd-d852-35db-88d5-72bf3e31c63b | -13.0775 | -47.8457 | 2025-10-07 13:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 76.3 |
| 73a756d2-4158-3cc4-a57f-e0549e41d807 | -12.9101 | -54.7558 | 2025-10-07 13:00:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 84.9 |
| 81bdae4c-8172-324e-baaa-fceb3ff35809 | -9.6098 | -46.6416 | 2025-10-07 13:00:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 90.8 |
| 018b10e4-b327-3cf7-9f9c-efd71de74142 | -14.7384 | -46.037 | 2025-10-07 13:00:00 | GOES-19 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 155.4 |
| a72e3ef2-19f5-38b2-ad68-4a490788e139 | -12.4476 | -45.5185 | 2025-10-07 13:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 150.5 |
| ed525947-05d1-3831-8729-095f65c32b76 | -13.0939 | -47.9992 | 2025-10-07 13:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 82.3 |
| 79114291-ae75-37f3-8ad4-ca43134d5580 | -15.3737 | -47.3201 | 2025-10-07 13:00:00 | GOES-19 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 114.7 |
| 99204207-de93-3a0c-b963-870550667379 | -13.3241 | -48.0324 | 2025-10-07 13:00:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 195.2 |
| e3f6ae98-cecd-3774-80c2-f846948c1ba1 | -11.1644 | -54.8804 | 2025-10-07 13:00:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 154.1 |
| 8a4ba9ec-0e83-3dd2-ac95-8c8b143e00b0 | -8.5395 | -46.2406 | 2025-10-07 13:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 321.9 |
| 09095c90-74c9-3901-88af-8660644827ca | -12.8913 | -54.7372 | 2025-10-07 13:00:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 428.7 |
| 34a3a2bd-5f9a-325f-9219-fb94b1398a8d | -13.3434 | -48.0296 | 2025-10-07 13:00:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 67.7 |
| 94fdfc01-e7bd-3989-8fa7-619462be9a65 | -17.9784 | -44.9817 | 2025-10-07 13:00:00 | GOES-19 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 123.4 |
| 089b0847-110d-38c3-b637-1614f31d52df | -12.9103 | -54.7352 | 2025-10-07 13:00:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 137.3 |
| a15fdbd3-a6f0-3812-b6a3-c0dfcdb187c3 | -8.501 | -46.3117 | 2025-10-07 13:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 95.9 |
| c4fa34b4-2ede-39b5-b776-670eeb15c608 | -12.7637 | -50.4921 | 2025-10-07 13:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 321.9 |
| 1d068b6a-abab-3e62-b65c-879ab0bb4ecf | -13.2232 | -51.6744 | 2025-10-07 13:00:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 147.0 |
| bfa61633-3411-3e5f-8e13-06770616be5d | -14.8645 | -51.4158 | 2025-10-07 13:00:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 110.8 |
| 1e97370c-0063-3bd1-af63-f90776fddaaf | -8.5007 | -46.3342 | 2025-10-07 13:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 78.6 |
| 1cd474c3-28ed-3524-9047-8ca833d097f1 | -11.6855 | -46.3593 | 2025-10-07 13:00:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 292.0 |


[Clique aqui para ver as próximas entradas](README119.md)
