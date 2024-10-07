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

## Dados Diários - Página 63

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e8bfbf2f-bba3-3233-9861-a34573bd6652 | -14.10007 | -45.49413 | 2024-10-07 04:02:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 29.2 |
| 3ae95940-e4ba-3fb2-b34e-34b1f30d0b21 | -14.09979 | -45.5175 | 2024-10-07 04:02:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a091cfb1-8381-3ad0-9f5a-1155b1d01940 | -14.09905 | -45.49107 | 2024-10-07 04:02:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 20ef6dad-ab5a-3f70-baba-d31eb0f377b7 | -14.09891 | -45.51448 | 2024-10-07 04:02:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a7d5db33-968a-3ae9-89ae-b5675a344ace | -14.09829 | -45.49557 | 2024-10-07 04:02:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 20.5 |
| 25a5cf12-3945-3bcd-a797-95769ba03f1e | -14.09813 | -45.51907 | 2024-10-07 04:02:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 2aa24059-b507-31b7-908c-269b2a065aed | -14.09688 | -45.51225 | 2024-10-07 04:02:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6d3999e0-f791-3f70-abfc-0157960dee81 | -14.09637 | -45.49337 | 2024-10-07 04:02:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 29.2 |
| 3403cf2a-2ce1-31b3-aab0-88a37807508f | -14.09535 | -45.49033 | 2024-10-07 04:02:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 8.6 |
| cdf898fd-fc4f-3ad5-8355-e99267864734 | -14.09458 | -45.49482 | 2024-10-07 04:02:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 20.5 |
| 2a9ceffc-2314-3895-b361-ac1c2ab4dbe1 | -14.08576 | -45.47908 | 2024-10-07 04:02:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8980afcd-e11c-3ace-b2db-9d4d95450972 | -14.07989 | -45.46864 | 2024-10-07 04:02:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 41.9 |
| 1a455468-b2fa-38d0-b64a-c52dda447ce9 | -14.07912 | -45.47313 | 2024-10-07 04:02:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 19.1 |
| 7c32fa2b-a0de-3c6c-a3b0-cfa5c6f05759 | -14.07695 | -45.46341 | 2024-10-07 04:02:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 41.9 |
| 1a6527aa-4c14-31de-8917-679f6f1d73b9 | -14.07618 | -45.4679 | 2024-10-07 04:02:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 41.9 |
| 9e963d95-32c0-3957-a5bb-bc42316fcf12 | -14.07541 | -45.47242 | 2024-10-07 04:02:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 19.1 |
| dcd7ab9e-f508-31e7-8e2d-322a7e0f61f1 | -14.07463 | -45.47697 | 2024-10-07 04:02:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 19.1 |
| 8ae278d8-0a76-3137-ae66-f669ca561808 | -14.07248 | -45.46717 | 2024-10-07 04:02:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 24.8 |
| 6f0d8964-4243-383b-a90e-32cf5f62b1e4 | -14.07091 | -45.4763 | 2024-10-07 04:02:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a277d717-9de7-367f-a152-d65f8fb88e23 | -14.06954 | -45.46194 | 2024-10-07 04:02:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 24.8 |
| c60bbe8d-6475-3254-be3c-e4aa862b1708 | -14.06592 | -45.52771 | 2024-10-07 04:02:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d57a964d-2595-3220-9695-003761fa9d8d | -14.06513 | -45.53231 | 2024-10-07 04:02:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3a80767b-db41-3d99-a35d-2be30ee4cf9f | -14.06219 | -45.52705 | 2024-10-07 04:02:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 28961fc2-3048-3702-a341-68e9958a019c | -14.0614 | -45.53163 | 2024-10-07 04:02:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b1dadb10-c182-3461-aa98-59fbc32ac66c | -14.05767 | -45.53092 | 2024-10-07 04:02:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 876349d6-ef30-3e9c-9b15-6ff2ddd16919 | -17.63069 | -46.97878 | 2024-10-07 04:02:00 | NOAA-20 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 259d0894-6915-3a6c-8f43-3cacfdedf69e | -17.6227 | -46.95679 | 2024-10-07 04:02:00 | NOAA-20 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9075afb7-37ba-350c-b9fc-580ab2fac67c | -17.61887 | -46.95601 | 2024-10-07 04:02:00 | NOAA-20 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f22e7cee-2874-3a18-975c-8dfac7de6c60 | -17.61207 | -46.94967 | 2024-10-07 04:02:00 | NOAA-20 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 18.0 |
| 0721a78f-ec51-3aa6-b2db-e53d8ebf8a53 | -17.60825 | -46.94886 | 2024-10-07 04:02:00 | NOAA-20 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 21.1 |
| 35fb9a99-cc64-3fd9-8864-a6c996cd02f1 | -17.24865 | -46.39086 | 2024-10-07 04:02:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 18d5fb95-91bd-3bf5-bf20-f3f7cfbf94be | -16.91807 | -46.95068 | 2024-10-07 04:02:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 2f1c39e1-30d9-30c4-b560-6ce24cc7b105 | -16.91 | -47.1507 | 2024-10-07 04:02:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 9b15c315-a555-3484-a35e-e8787d958348 | -16.90606 | -47.15 | 2024-10-07 04:02:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 621d0c86-6659-370d-9e61-d1e51b1f13af | -16.90511 | -47.15527 | 2024-10-07 04:02:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 4.6 |
| cfceb513-2cb4-3a06-b22c-00973e02ebd3 | -16.90118 | -47.15454 | 2024-10-07 04:02:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 19c15a46-a368-3cad-adf7-c77eb9d28f9f | -16.90023 | -47.15976 | 2024-10-07 04:02:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c2dd7563-3fb7-3735-9597-c90b9c932b50 | -16.89726 | -47.1538 | 2024-10-07 04:02:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 511fbc9a-64cd-3698-96f1-052ce802aff9 | -16.88851 | -47.15725 | 2024-10-07 04:02:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 24915bd2-1848-339c-bd9b-df77435f1ccf | -16.88757 | -47.16239 | 2024-10-07 04:02:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| a8a82093-2c30-3d29-ba69-d501a172f9e7 | -16.88474 | -47.17789 | 2024-10-07 04:02:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 3.6 |
| db7fafdb-357a-3a0c-ae5c-02835bf97c14 | -16.88378 | -47.18317 | 2024-10-07 04:02:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 6.5 |
| da787773-7903-31dd-909f-a0c3facb8a91 | -16.88271 | -47.16671 | 2024-10-07 04:02:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 808d7ac9-d1d1-37d8-906f-3d47860cf224 | -16.8788 | -47.16589 | 2024-10-07 04:02:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 4a57f759-d553-31e8-80a9-5023e743bb94 | -19.19658 | -46.5783 | 2024-10-07 04:02:00 | NOAA-20 | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 013a67a1-8acf-3283-99fd-eeac5280d7d8 | -19.1929 | -46.5776 | 2024-10-07 04:02:00 | NOAA-20 | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| cb61bd9a-78ea-3aa0-9883-bf6530d87ada | -18.88025 | -47.52745 | 2024-10-07 04:02:00 | NOAA-20 | ROMARIA | MINAS GERAIS | Brasil | 3156403 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8e16cffa-9f9d-3474-bb9b-d2a1c660ac87 | -18.59481 | -46.55273 | 2024-10-07 04:02:00 | NOAA-20 | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 02c412b4-2fa1-3a4a-916c-847c48442860 | -18.59332 | -46.55085 | 2024-10-07 04:02:00 | NOAA-20 | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 67db98b2-16ea-3913-8e8e-f501ceeb660f | -18.59306 | -47.31054 | 2024-10-07 04:02:00 | NOAA-20 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 8.5 |
| acc6d114-1040-378b-aacc-5fafad390706 | -18.58919 | -47.30986 | 2024-10-07 04:02:00 | NOAA-20 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 8.5 |
| f8b4ddae-9ee9-3972-82ca-0cbbb617171a | -18.38422 | -46.56646 | 2024-10-07 04:02:00 | NOAA-20 | PRESIDENTE OLEGÁRIO | MINAS GERAIS | Brasil | 3153400 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6bbf79ec-2c00-38a0-a6e2-67facae0e152 | -18.38153 | -46.5681 | 2024-10-07 04:02:00 | NOAA-20 | PRESIDENTE OLEGÁRIO | MINAS GERAIS | Brasil | 3153400 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 66e78f49-84e6-317b-8acd-fa79dbaca980 | -18.37173 | -47.16611 | 2024-10-07 04:02:00 | NOAA-20 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6e00d32a-1615-3f46-b014-c6b7650f587c | -18.32371 | -47.1461 | 2024-10-07 04:02:00 | NOAA-20 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 169450c3-9f4d-3d7b-a286-3155b9d27a94 | -18.3085 | -47.1424 | 2024-10-07 04:02:00 | NOAA-20 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b52690cf-ea64-3513-b567-45cd45db09dc | -18.30556 | -47.13675 | 2024-10-07 04:02:00 | NOAA-20 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 7e8cca01-435d-36b9-b14b-acb3411368c4 | -18.30468 | -47.14157 | 2024-10-07 04:02:00 | NOAA-20 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 4.5 |
| dc1c21e6-ca9e-3168-a24d-70f7e548b636 | -18.30344 | -47.12664 | 2024-10-07 04:02:00 | NOAA-20 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 5e9cf8a6-6c0f-30b6-a772-3f696d011013 | -18.30173 | -47.13597 | 2024-10-07 04:02:00 | NOAA-20 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 4.5 |
| af0bef0f-2bbe-3bae-b034-b665b8fef8e0 | -18.30085 | -47.14079 | 2024-10-07 04:02:00 | NOAA-20 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 4.5 |
| d580be1a-fb31-3c0e-a17f-30e918a22e77 | -18.29994 | -47.1458 | 2024-10-07 04:02:00 | NOAA-20 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 93d6f4a1-f904-3f31-a460-8d7c65df98b7 | -18.29899 | -47.15096 | 2024-10-07 04:02:00 | NOAA-20 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 197f742f-684e-3f3e-9137-4bb4094b69d1 | -18.29789 | -47.13527 | 2024-10-07 04:02:00 | NOAA-20 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| fa0495c0-ae14-381a-b154-99c3c3816ede | -18.29702 | -47.14003 | 2024-10-07 04:02:00 | NOAA-20 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 7aab0b13-a0bb-3208-a97b-120797eaab9e | -18.2961 | -47.14506 | 2024-10-07 04:02:00 | NOAA-20 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 6.4 |
| fefe8761-b023-311b-a19a-baf5a808038e | -18.24566 | -46.40795 | 2024-10-07 04:02:00 | NOAA-20 | PRESIDENTE OLEGÁRIO | MINAS GERAIS | Brasil | 3153400 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| cc083bf7-189c-3709-a02d-a1cf196cd70c | -18.2399 | -46.39739 | 2024-10-07 04:02:00 | NOAA-20 | PRESIDENTE OLEGÁRIO | MINAS GERAIS | Brasil | 3153400 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1a16550e-42c9-362d-822f-0f822e1b9936 | -18.2391 | -46.40194 | 2024-10-07 04:02:00 | NOAA-20 | PRESIDENTE OLEGÁRIO | MINAS GERAIS | Brasil | 3153400 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6295dfe1-3968-38e5-b0d4-e22ef3d26ecc | -14.1197 | -45.53545 | 2024-10-07 04:02:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 56.7 |
| fcdfaed4-0ed3-3628-add7-1549cae92d85 | -13.23665 | -45.58095 | 2024-10-07 04:02:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ffaa5a77-8737-3b79-9607-6f9211891184 | -13.23287 | -45.58026 | 2024-10-07 04:02:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4a7ae3d7-1704-3b40-84cc-b1ce604a8367 | -13.22949 | -45.53313 | 2024-10-07 04:02:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 4a621291-4efd-398d-a1cf-541d0d1726dd | -13.22909 | -45.57956 | 2024-10-07 04:02:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 691b5ad5-0572-394c-9ca4-dce17ccbf9ff | -13.09122 | -46.34274 | 2024-10-07 04:02:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 389854a1-3387-323b-9435-254a1e9f4f0a | -13.09027 | -46.34832 | 2024-10-07 04:02:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a6102341-34c7-3eaa-a77c-a70bfb83383c | -13.08916 | -46.3448 | 2024-10-07 04:02:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| f5811a79-05d6-3e15-be05-2b5d35f9f301 | -14.21412 | -46.46131 | 2024-10-07 04:02:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 102c76ca-f330-3450-9b07-95bddc801adb | -14.21206 | -46.45004 | 2024-10-07 04:02:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 1144a2c6-824e-335c-a0d7-6cac1348951c | -14.21114 | -46.45522 | 2024-10-07 04:02:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 515881a5-488c-3f1e-ae71-2cfcb6ecd4b8 | -14.21019 | -46.46057 | 2024-10-07 04:02:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |
| ae5150f7-2391-3887-a910-c9ff742bcfad | -14.20812 | -46.44938 | 2024-10-07 04:02:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 7579ba99-e9ed-379a-9937-387f311e752c | -14.12049 | -45.53094 | 2024-10-07 04:02:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 17.7 |
| d1e667f2-008e-3ca6-ad87-ea8824598a59 | -14.11891 | -45.53998 | 2024-10-07 04:02:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 56.7 |
| 24d73494-843a-379f-9d3e-19c64f36b1c5 | -14.11832 | -45.5874 | 2024-10-07 04:02:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 13.0 |
| a17d724b-7c88-3113-a187-acf83d9fef98 | -14.11811 | -45.54453 | 2024-10-07 04:02:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ed9372d6-0236-3729-a403-7fb1bf7d5d80 | -14.11757 | -45.52568 | 2024-10-07 04:02:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 19.6 |
| 22e8d5ab-ef4f-35d3-85c1-266249add170 | -14.1175 | -45.59206 | 2024-10-07 04:02:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 887aca93-bafb-3d61-a715-40c057ec6997 | -14.11677 | -45.53022 | 2024-10-07 04:02:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 19.6 |
| ffda9245-535a-322d-942e-bc3b4f8f6793 | -14.11619 | -45.5775 | 2024-10-07 04:02:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 69714fa7-0399-3592-bd02-4efbf85b64b2 | -14.11598 | -45.53474 | 2024-10-07 04:02:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 19.9 |
| 14cbf8aa-3041-36d7-8e5c-b7a44ad86b2c | -14.11544 | -45.5159 | 2024-10-07 04:02:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 759e5232-5f28-3556-b29d-7d682f09dae8 | -14.11519 | -45.53928 | 2024-10-07 04:02:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 19.9 |
| bec2233b-2cd6-3a69-b036-fe37da45d7f9 | -14.11466 | -45.52039 | 2024-10-07 04:02:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 390613c3-f61d-35c0-b1f1-bae2c3216911 | -14.11457 | -45.58677 | 2024-10-07 04:02:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 15.4 |
| d715c7e7-7352-3d76-8613-392750603a6b | -14.11386 | -45.52492 | 2024-10-07 04:02:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 19.6 |
| aad81422-bdab-3f32-87e8-ef2622fb11b2 | -14.11376 | -45.59143 | 2024-10-07 04:02:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 6f409585-fd50-312c-b6bd-e9b6679c3eeb | -14.11306 | -45.52948 | 2024-10-07 04:02:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 19.6 |
| 9ae185aa-6e3c-3f76-b17a-bee70562e651 | -14.11226 | -45.53403 | 2024-10-07 04:02:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 19.9 |
| 8b7b4b08-f580-3b8e-9f11-e7fea25f8540 | -14.11173 | -45.51517 | 2024-10-07 04:02:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 108.9 |


[Clique aqui para ver as próximas entradas](README64.md)
