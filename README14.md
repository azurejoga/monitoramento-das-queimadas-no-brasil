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

## Dados Diários - Página 14

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 408cc7a5-0b72-3dae-9425-239f3957ddeb | -7.66884 | -43.65969 | 2025-05-15 12:19:00 | TERRA_M-T | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 45d0cba6-8a64-33bf-a721-552573e3957f | -8.14023 | -47.09079 | 2025-05-15 12:19:00 | TERRA_M-T | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 60040b2e-14e0-300e-8800-28836a2fb6a8 | -6.55503 | -44.49488 | 2025-05-15 12:19:00 | TERRA_M-T | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 54bf6777-82e3-3f53-95b7-61f4c079fbc9 | -6.18109 | -48.06591 | 2025-05-15 12:19:00 | TERRA_M-T | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 18.0 |
| 29777a36-7760-301b-86d9-094929cc4807 | -6.66505 | -43.19843 | 2025-05-15 12:19:00 | TERRA_M-T | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 10.2 |
| d051c704-c057-3bf7-a054-2aa60fa163c2 | -7.73481 | -46.33924 | 2025-05-15 12:19:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 820a2cdf-660f-31ce-becf-55eebc67660b | -7.71915 | -44.53362 | 2025-05-15 12:19:00 | TERRA_M-T | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 5.5 |
| a899fb9c-891f-30c1-b2d1-d024124d6828 | -6.17097 | -48.06445 | 2025-05-15 12:19:00 | TERRA_M-T | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 59.3 |
| 64968c05-9f94-3b2e-884a-1f51be0696a6 | -10.81023 | -49.92794 | 2025-05-15 12:19:00 | TERRA_M-T | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 34.7 |
| d5f67ed5-9e7e-379d-802e-31be9738d34b | -7.06208 | -45.8915 | 2025-05-15 12:19:00 | TERRA_M-T | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 12c17de3-cc8c-3a12-8d1e-4a472a7e4a76 | -6.66638 | -43.18896 | 2025-05-15 12:19:00 | TERRA_M-T | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 25.7 |
| 3ac6caf4-ea99-3bed-995a-a356c0006923 | -7.74547 | -46.32835 | 2025-05-15 12:19:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| f703b915-d08f-35c3-9162-563d658196d0 | -8.13093 | -47.08941 | 2025-05-15 12:19:00 | TERRA_M-T | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 47.3 |
| 3e720f51-95bb-37b4-9d3a-2231257c44ca | -5.8924 | -45.05194 | 2025-05-15 12:19:00 | TERRA_M-T | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 24.4 |
| c6ff1dd7-3b2d-3875-ad4d-33a38b8ce686 | -7.32171 | -43.31303 | 2025-05-15 12:19:00 | TERRA_M-T | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 84.4 |
| 836ea707-f4e8-398a-92b6-d27236bd1ab3 | -11.06752 | -46.12757 | 2025-05-15 12:19:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 8.6 |
| c6d9049f-b36d-38fe-bd12-51798f030922 | -5.77703 | -43.48417 | 2025-05-15 12:19:00 | TERRA_M-T | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| b830b027-4f84-37dc-a937-2bfe2080af49 | -6.64805 | -41.99686 | 2025-05-15 12:19:00 | TERRA_M-T | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 13.5 |
| 586ee56f-c45b-30b9-a1c9-15f1993ed1f8 | -6.91035 | -43.74335 | 2025-05-15 12:19:00 | TERRA_M-T | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 52e88fca-7329-3d89-9e5f-ec0a23d80657 | -7.33218 | -43.30484 | 2025-05-15 12:19:00 | TERRA_M-T | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 2c8ccdd0-55d1-388a-85d2-d045e37dc41c | -9.99443 | -47.83972 | 2025-05-15 12:19:00 | TERRA_M-T | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 14.4 |
| d99ef6a8-4ded-32b9-8aa4-13a8804262c6 | -5.78588 | -43.6151 | 2025-05-15 12:19:00 | TERRA_M-T | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 23.3 |
| b0849ba6-999c-3e82-b574-9d43bf952e6f | -6.16067 | -44.28197 | 2025-05-15 12:19:00 | TERRA_M-T | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 21.3 |
| 7472a058-6de8-3b74-b749-3e1d11e79e4f | -11.07898 | -46.11092 | 2025-05-15 12:19:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 75f603c7-41cf-33a8-967e-320804e8b555 | -9.65821 | -47.55564 | 2025-05-15 12:19:00 | TERRA_M-T | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 8.7 |
| cbe5c59f-7f4c-38bf-8759-9acf0bff7631 | -6.72038 | -47.6007 | 2025-05-15 12:19:00 | TERRA_M-T | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 0f64e24d-de04-383b-8fb7-a5b993321e96 | -7.55473 | -45.87016 | 2025-05-15 12:19:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 33.2 |
| b786f471-c366-3b0c-84be-d1bbd92829e3 | -10.50616 | -46.18291 | 2025-05-15 12:19:00 | TERRA_M-T | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 19.2 |
| e0975281-6a80-319d-afe3-8fa284b96504 | -7.56022 | -43.38392 | 2025-05-15 12:19:00 | TERRA_M-T | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Cerrado | 10.7 |
| c9bd2382-e201-38e6-b770-4fe8740d8a72 | -11.06882 | -46.11859 | 2025-05-15 12:19:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 341.8 |
| 0e0434dc-caca-3b87-a4c6-722eaa88f126 | -10.51635 | -46.17521 | 2025-05-15 12:19:00 | TERRA_M-T | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| cde504ca-a9a0-364e-a6f6-5454076cae07 | -7.07621 | -44.39065 | 2025-05-15 12:19:00 | TERRA_M-T | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| f794b3f2-70eb-3298-a3d7-6eb5a49bbe46 | -11.0792 | -46.1017 | 2025-05-15 12:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 131.5 |
| 2ad9555c-6b91-3c93-bfde-649aea8dd76c | -11.0789 | -46.1245 | 2025-05-15 12:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 178.2 |
| 206ef187-d99b-3ba9-a22d-8d3606378f1a | -9.6825 | -49.6995 | 2025-05-15 12:20:00 | GOES-19 | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 79.0 |
| abc434a6-940a-3b53-a198-eb5b2de7eee0 | -11.0598 | -46.127 | 2025-05-15 12:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 81.1 |
| d8885411-b9fe-3d54-b9f3-802734fab3dc | -12.3519 | -49.9617 | 2025-05-15 12:20:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 91.4 |
| 5f70e42c-7425-3ccc-a169-dda262b9816f | -18.13784 | -51.12787 | 2025-05-15 12:21:00 | TERRA_M-T | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 7.9 |
| fcdbae60-ac21-3a7f-b34a-90d4f1218473 | -11.50017 | -47.81189 | 2025-05-15 12:21:00 | TERRA_M-T | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 4cc657d6-4c34-3d64-bf93-24292c086723 | -11.61789 | -48.02174 | 2025-05-15 12:21:00 | TERRA_M-T | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 55.5 |
| 9914e161-a611-38cc-a604-90419b01c2e1 | -13.07006 | -47.80659 | 2025-05-15 12:21:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 4566d558-f7c5-3404-ac54-2762aa63a949 | -11.78264 | -47.35003 | 2025-05-15 12:21:00 | TERRA_M-T | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 06d0a681-4e95-342a-af1f-5d0754e06130 | -15.76968 | -47.14896 | 2025-05-15 12:21:00 | TERRA_M-T | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 7ab51c09-2b55-34d4-9c29-a153afbb1cdc | -13.62885 | -47.71234 | 2025-05-15 12:21:00 | TERRA_M-T | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |
| df72831a-cf7e-3154-ba8b-fc8ff34addbf | -11.16012 | -48.67522 | 2025-05-15 12:21:00 | TERRA_M-T | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 17.3 |
| 598be857-6b4e-3fd3-9e57-86f9600b5abc | -17.7998 | -44.35549 | 2025-05-15 12:21:00 | TERRA_M-T | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 23.9 |
| fe155669-4249-3391-a96c-a451c97cb7e4 | -18.4961 | -47.6058 | 2025-05-15 12:21:00 | TERRA_M-T | MONTE CARMELO | MINAS GERAIS | Brasil | 3143104 | 31 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 3ef10c61-ba75-3f79-b059-0933161e6c62 | -11.16991 | -48.67673 | 2025-05-15 12:21:00 | TERRA_M-T | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 7.5 |
| aec1306f-2059-3db3-ad36-7eefa84ec47d | -11.5657 | -47.44163 | 2025-05-15 12:21:00 | TERRA_M-T | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 1b245f46-e17d-35ad-8f62-331823572728 | -12.37733 | -47.32226 | 2025-05-15 12:21:00 | TERRA_M-T | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 79d71fd9-9aec-31e6-b7db-a6cc4c7588c2 | -18.50631 | -47.5979 | 2025-05-15 12:21:00 | TERRA_M-T | MONTE CARMELO | MINAS GERAIS | Brasil | 3143104 | 31 | 33 | nan | nan | nan | Cerrado | 7.8 |
| b8c16f05-c196-381f-8910-bed9ff40b697 | -15.48505 | -43.16314 | 2025-05-15 12:21:00 | TERRA_M-T | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 34.3 |
| 7863918c-cdad-38dc-b536-58295259e857 | -11.81586 | -45.53825 | 2025-05-15 12:21:00 | TERRA_M-T | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 4d191600-f3ef-3206-8b40-e5dee8fef92c | -17.79837 | -44.36664 | 2025-05-15 12:21:00 | TERRA_M-T | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 16.5 |
| de247b8a-54f0-33fc-a2bc-dfdc9efcd9fb | -11.5593 | -47.60884 | 2025-05-15 12:21:00 | TERRA_M-T | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 34053761-24df-310c-8f71-454d4b085078 | -15.36284 | -43.71152 | 2025-05-15 12:21:00 | TERRA_M-T | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 8.4 |
| c355853c-f720-3b33-879d-b2cae79b5029 | -15.26773 | -51.45889 | 2025-05-15 12:21:00 | TERRA_M-T | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 18.8 |
| 227a862a-c08e-3d1d-8893-6be2acca325a | -12.3529 | -49.95771 | 2025-05-15 12:21:00 | TERRA_M-T | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 123.5 |
| 20f653a0-f8b0-3527-9451-77db9a4ffda6 | -11.61942 | -48.01162 | 2025-05-15 12:21:00 | TERRA_M-T | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 53.6 |
| 83a0f79c-2079-377f-8d26-225c128161fc | -11.62094 | -48.00146 | 2025-05-15 12:21:00 | TERRA_M-T | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 0638ae54-484d-311c-bebb-d0c11ac81009 | -12.35079 | -49.97068 | 2025-05-15 12:21:00 | TERRA_M-T | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 66fac335-91c0-325a-b619-ead9c83bbe27 | -17.47951 | -45.46859 | 2025-05-15 12:21:00 | TERRA_M-T | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 6.1 |
| e78b4fbc-f1a4-3ace-ae54-5fc42f56dbc1 | -13.03865 | -53.72916 | 2025-05-15 12:21:00 | TERRA_M-T | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 24.4 |
| b95648a5-0c46-3ec1-8fcd-e263162e0ad2 | -14.86944 | -45.11488 | 2025-05-15 12:21:00 | TERRA_M-T | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 8234bf33-fe3a-3387-a58e-07e2d4148165 | -18.49745 | -47.59651 | 2025-05-15 12:21:00 | TERRA_M-T | MONTE CARMELO | MINAS GERAIS | Brasil | 3143104 | 31 | 33 | nan | nan | nan | Cerrado | 22.5 |
| 2ffb03c8-bc85-3c2f-8162-9086a59406bd | -15.76834 | -47.15816 | 2025-05-15 12:21:00 | TERRA_M-T | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 1794bfb9-ba73-3c19-b9cf-6c89039f03cb | -17.50025 | -45.99141 | 2025-05-15 12:21:00 | TERRA_M-T | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 33.5 |
| b16d2baf-0aa6-389f-af1e-0d5f0def1249 | -14.2036 | -45.46635 | 2025-05-15 12:21:00 | TERRA_M-T | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 9.1 |
| d605d534-15ac-3245-95f5-1afcad78a377 | -12.02783 | -49.70369 | 2025-05-15 12:21:00 | TERRA_M-T | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 6c863fe7-2044-327c-b748-3a7c44ac705a | -11.79255 | -44.26977 | 2025-05-15 12:21:00 | TERRA_M-T | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 3e64f796-f8db-3da6-84ef-5d7d559d6aa6 | -11.56714 | -47.43206 | 2025-05-15 12:21:00 | TERRA_M-T | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 7.7 |
| c5a4d59c-7b41-3796-ba3a-52b33863b71a | -13.04267 | -53.70527 | 2025-05-15 12:21:00 | TERRA_M-T | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 27.8 |
| dc4f3262-fd0b-3917-9e8a-c72e51c957ba | -17.50156 | -45.98188 | 2025-05-15 12:21:00 | TERRA_M-T | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 21.2 |
| 2af62f80-e6cf-34df-854f-cf7cb84c1bc7 | -11.55782 | -47.61868 | 2025-05-15 12:21:00 | TERRA_M-T | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 7.8 |
| d26e883e-46f8-3942-91d6-8e143d5d05ec | -13.57524 | -52.87587 | 2025-05-15 12:21:00 | TERRA_M-T | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 16.5 |
| c9f35b28-f89f-3fdc-8b60-58524a252062 | -13.06864 | -47.81597 | 2025-05-15 12:21:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 65bdf21d-4d33-3f2d-8e68-6274ac196b44 | -11.50169 | -47.80193 | 2025-05-15 12:21:00 | TERRA_M-T | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 462dd599-8b45-3bbf-a3f4-4b162be06a5e | -17.44444 | -44.89939 | 2025-05-15 12:21:00 | TERRA_M-T | PIRAPORA | MINAS GERAIS | Brasil | 3151206 | 31 | 33 | nan | nan | nan | Cerrado | 8.3 |
| da652331-41e6-3184-9eba-fbf77f84ab40 | -12.34585 | -49.96323 | 2025-05-15 12:21:00 | TERRA_M-T | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 121.2 |
| 717c7529-5a0c-3770-aae1-c18228e33246 | -15.48351 | -43.17531 | 2025-05-15 12:21:00 | TERRA_M-T | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 13.4 |
| 321b6c9f-2208-3dfc-b249-937213317140 | -15.03098 | -43.83974 | 2025-05-15 12:21:00 | TERRA_M-T | MATIAS CARDOSO | MINAS GERAIS | Brasil | 3140852 | 31 | 33 | nan | nan | nan | Caatinga | 6.8 |
| 3d113d14-2e88-3066-b998-2cb4c3ac70c9 | -12.34789 | -49.95017 | 2025-05-15 12:21:00 | TERRA_M-T | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 87.3 |
| 1877d175-edcb-33e9-82b1-570a9c32ae57 | -23.60355 | -48.29535 | 2025-05-15 12:23:00 | TERRA_M-T | ITAPETININGA | SÃO PAULO | Brasil | 3522307 | 35 | 33 | nan | nan | nan | Cerrado | 8.1 |
| d3d61f5c-313f-368a-814a-971560337c6b | -19.86838 | -47.36014 | 2025-05-15 12:23:00 | TERRA_M-T | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 7c95c3c4-8dfb-30f4-b489-23adf117df21 | -20.35564 | -49.30412 | 2025-05-15 12:23:00 | TERRA_M-T | NOVA GRANADA | SÃO PAULO | Brasil | 3533007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.9 |
| bb398b8e-a1e0-3f1d-9c99-e2a909a0b43c | -20.95024 | -45.76917 | 2025-05-15 12:23:00 | TERRA_M-T | ILICÍNEA | MINAS GERAIS | Brasil | 3130507 | 31 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 61693f77-9eaa-3e65-86a2-4fc60d89a38e | -24.36365 | -49.9525 | 2025-05-15 12:23:00 | TERRA_M-T | PIRAÍ DO SUL | PARANÁ | Brasil | 4119400 | 41 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 47de5146-073c-35e9-b83a-8c15d1c7541f | -19.86971 | -47.35077 | 2025-05-15 12:23:00 | TERRA_M-T | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 0aa8edae-dfc2-3bdb-a874-f0dde437c76b | -27.2517 | -52.54785 | 2025-05-15 12:25:00 | TERRA_M-T | ERVAL GRANDE | RIO GRANDE DO SUL | Brasil | 4307203 | 43 | 33 | nan | nan | nan | Mata Atlântica | 5.8 |
| 4aff4fee-f895-3260-ba20-24f5248ef202 | -27.24966 | -52.56017 | 2025-05-15 12:25:00 | TERRA_M-T | ERVAL GRANDE | RIO GRANDE DO SUL | Brasil | 4307203 | 43 | 33 | nan | nan | nan | Mata Atlântica | 6.4 |
| c850c507-9fe8-3244-84cf-6c9d0040ec53 | -11.0789 | -46.1245 | 2025-05-15 12:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 128.9 |
| 462aac05-655b-3268-a3f2-dd154a37c6b3 | -12.3519 | -49.9617 | 2025-05-15 12:30:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 119.0 |
| 082b2432-8d0a-376f-8eeb-07a8cf79ae48 | -11.0792 | -46.1017 | 2025-05-15 12:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 130.4 |
| d39f5057-68b7-394e-be8b-7de478910e8f | -12.3519 | -49.9617 | 2025-05-15 12:40:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 167.3 |
| 588dec00-cdfd-334e-be4b-23fc3c137cab | -11.0792 | -46.1017 | 2025-05-15 12:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 93.0 |
| f519de2f-3544-37b8-b6ca-26b7774b7109 | -11.0789 | -46.1245 | 2025-05-15 12:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 89.9 |
| 14e4e1f8-2df8-3272-a363-3d5470db252d | -12.3522 | -49.94 | 2025-05-15 12:50:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 87.6 |
| 37be88e8-f8f6-3e4f-9846-a41129bca8e9 | -11.0789 | -46.1245 | 2025-05-15 12:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 82.5 |
| 78e67e59-c086-34e6-9797-9d9538b65fcd | -12.3519 | -49.9617 | 2025-05-15 12:50:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 195.6 |
| 97a3c893-d466-3fca-8807-22996d9c832a | -9.6825 | -49.6995 | 2025-05-15 13:00:00 | GOES-19 | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 73.4 |


[Clique aqui para ver as próximas entradas](README15.md)
