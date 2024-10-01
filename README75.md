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

## Dados Diários - Página 75

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b6ab97c7-7fb4-3ee4-90f9-de34f8e418e4 | -15.20142 | -46.22355 | 2024-10-01 04:14:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| da0f1e2d-75bd-3cf5-ae38-ec48d9b8320b | -15.19807 | -46.223 | 2024-10-01 04:14:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4de5c722-8db3-3239-8cd0-8d15daaf755d | -15.19748 | -46.22662 | 2024-10-01 04:14:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7d60103a-5ca7-3265-8171-b1cba3b316ca | -15.19413 | -46.22607 | 2024-10-01 04:14:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d865dd2e-8b60-3478-aa36-c98e774db1f8 | -15.19295 | -46.23331 | 2024-10-01 04:14:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c42bd8e4-11de-3f1b-bb17-5551ad8f38c1 | -15.189 | -46.2364 | 2024-10-01 04:14:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 146d6755-b7cd-3aa2-8ceb-7b409dfc99d6 | -15.18565 | -46.23585 | 2024-10-01 04:14:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6202e319-bdc5-384b-b69a-5ae421e0f901 | -15.18506 | -46.23948 | 2024-10-01 04:14:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 762a078d-5e27-3fb6-b790-781ac75b0132 | -15.18447 | -46.2431 | 2024-10-01 04:14:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 69589600-d2a7-314e-89a7-faea4fe6b6dc | -15.18053 | -46.24615 | 2024-10-01 04:14:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 0a222837-376b-3f49-bcdc-a368810d0d1c | -15.17993 | -46.24981 | 2024-10-01 04:14:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 6d673847-4934-3366-8e06-90e9360b402f | -18.09013 | -46.13707 | 2024-10-01 04:14:00 | NOAA-20 | PRESIDENTE OLEGÁRIO | MINAS GERAIS | Brasil | 3153400 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 110a6c73-06c0-3b43-84fb-7a0ed5eb4c20 | -18.08954 | -46.1407 | 2024-10-01 04:14:00 | NOAA-20 | PRESIDENTE OLEGÁRIO | MINAS GERAIS | Brasil | 3153400 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5206e088-245f-3584-a84f-7bae8c42cee7 | -17.97866 | -46.79176 | 2024-10-01 04:14:00 | NOAA-20 | LAGAMAR | MINAS GERAIS | Brasil | 3137106 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cb988359-993b-3d4f-8427-791d884d9e18 | -17.59432 | -46.95697 | 2024-10-01 04:14:00 | NOAA-20 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5bf1108e-4fed-38c5-abc2-c4d0c283e2fa | -17.59097 | -46.95636 | 2024-10-01 04:14:00 | NOAA-20 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0e934d36-5155-3e9f-b84f-c4a348cc802d | -17.59035 | -46.96011 | 2024-10-01 04:14:00 | NOAA-20 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b3b6c2f9-df9a-3f05-8e1a-234f479e8b7d | -17.58761 | -46.95574 | 2024-10-01 04:14:00 | NOAA-20 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8d441c78-c45a-3b61-94b6-504360b7e7ce | -17.58699 | -46.95951 | 2024-10-01 04:14:00 | NOAA-20 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a4383e05-08c5-302b-88b9-6dc0ed716d4d | -17.582 | -46.77915 | 2024-10-01 04:14:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 181c13e1-3133-3b3c-a0d7-e65712626114 | -17.58139 | -46.78285 | 2024-10-01 04:14:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 56e10cac-1861-3fde-a145-3aadc5cf24d2 | -17.47758 | -47.00611 | 2024-10-01 04:14:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 2bd67038-b2c4-39c1-a1ff-897943ccc69d | -10.90689 | -46.34582 | 2024-10-01 04:14:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9e0c2ea0-aba0-39e3-b933-538417c3f244 | -10.90625 | -46.34969 | 2024-10-01 04:14:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8c3091c1-0274-30f0-869a-c3cceaf0378f | -10.90406 | -46.34139 | 2024-10-01 04:14:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1e986424-628f-3a6a-85db-3aa73db14d2a | -10.90059 | -46.34081 | 2024-10-01 04:14:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7ce7157e-76a0-34bd-9c71-f616c1403598 | -10.87503 | -46.34451 | 2024-10-01 04:14:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e1f7d2ce-fcf4-368d-8e57-c3e056f352c4 | -10.84384 | -46.37195 | 2024-10-01 04:14:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2c70a347-3252-3ad9-b9c8-e00bc9db5879 | -10.8432 | -46.37585 | 2024-10-01 04:14:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9bff6428-0dcc-366b-8354-2831b9ee0221 | -10.77711 | -46.53798 | 2024-10-01 04:14:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a9795573-1ee8-32d4-940d-5bc9056e18d5 | -10.77648 | -46.54182 | 2024-10-01 04:14:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 473a7385-74f4-3902-a011-50d62f5376e4 | -10.77362 | -46.53734 | 2024-10-01 04:14:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0c3d07ff-5236-36ba-83ba-7fa564d63583 | -10.7042 | -46.16976 | 2024-10-01 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 68a4d605-27fc-32e6-81d6-a38e89c8b3f3 | -10.70076 | -46.16917 | 2024-10-01 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| bf86c0d5-e4cf-337c-b058-8b1238a2bf6d | -10.69731 | -46.16857 | 2024-10-01 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 7695126e-ae8a-336e-bc92-63a5e247a16f | -10.69387 | -46.16798 | 2024-10-01 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7007de2b-4f06-3b5f-b435-26534900c03e | -10.69105 | -46.16357 | 2024-10-01 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 7d5553b2-231c-343e-a8f1-d9fec2d7fbf7 | -10.68824 | -46.15917 | 2024-10-01 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9dfdc220-964f-38c6-bc14-29dc2b3310d3 | -10.68761 | -46.16297 | 2024-10-01 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| dfb75ff5-82a2-3826-a183-fcba043484ba | -10.68579 | -46.15955 | 2024-10-01 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 49bb0227-4eac-3918-8569-be3ee9c6dd50 | -10.68479 | -46.15859 | 2024-10-01 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a4d58771-7625-36bb-af82-dbdfbddf63a1 | -10.68235 | -46.15897 | 2024-10-01 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| ae586a97-7f26-31fe-a99f-ae0413b6b790 | -10.68075 | -46.14701 | 2024-10-01 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| be43ca80-3c52-35a1-ba2f-7fe8b3272a1e | -10.68013 | -46.15079 | 2024-10-01 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 89c3bd82-bf92-3e4b-ad8d-27be6c75ac7c | -10.67951 | -46.15459 | 2024-10-01 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b929080e-cd26-384a-8223-34f3ee89f0b4 | -10.6789 | -46.15839 | 2024-10-01 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 14ff375f-b9a0-3523-a5aa-6d8291dbf864 | -10.67597 | -46.11102 | 2024-10-01 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 0cbe2bf1-2fa1-382e-9ebb-aca06c95420f | -10.67535 | -46.11482 | 2024-10-01 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d63cdec8-39bc-33ee-84a9-dea0feb8ea2f | -10.67473 | -46.11863 | 2024-10-01 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4f95c71a-ef5d-3af6-862e-bd9bc84c40e8 | -15.28284 | -47.51327 | 2024-10-01 04:14:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 98f09135-9a19-37ba-afe6-eea32afdbfe2 | -11.00681 | -46.48637 | 2024-10-01 04:14:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 3dbc0e34-f954-354a-999d-6ed30064258e | -11.00399 | -46.48177 | 2024-10-01 04:14:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 23.5 |
| a9c49d67-390d-3c58-8277-6031a6c5a841 | -11.00331 | -46.48591 | 2024-10-01 04:14:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 23.5 |
| f5db654a-1a7d-3089-a290-38ecc1f3b4f3 | -11.00264 | -46.48994 | 2024-10-01 04:14:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 7d7d1276-18ac-31fe-8d4e-706dba048e9e | -11.00119 | -46.47709 | 2024-10-01 04:14:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| b80d06af-acd7-30f3-b659-0d4899b6019f | -11.00051 | -46.48122 | 2024-10-01 04:14:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 23.5 |
| 2ef66f27-fd5f-3b01-8210-c52797d125a3 | -10.99983 | -46.48533 | 2024-10-01 04:14:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 23.5 |
| 07e05807-e0b0-3cff-b60d-c70d9ea7202c | -10.99916 | -46.48936 | 2024-10-01 04:14:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| db06d6e3-4555-349e-bdc7-da058dabbffa | -10.99851 | -46.4933 | 2024-10-01 04:14:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| e7f91df7-6ccb-3b8e-a1c6-5394e778659d | -10.99785 | -46.49724 | 2024-10-01 04:14:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 8.3 |
| edb9301f-c0a0-3b85-90f1-3bac5884f0d8 | -10.9977 | -46.47653 | 2024-10-01 04:14:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 03457b35-6fd6-3042-b0fa-940fd11b5cbb | -10.99702 | -46.48066 | 2024-10-01 04:14:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 7fe67f7e-530b-3f89-8093-5fec5d1d74c3 | -10.99525 | -46.51295 | 2024-10-01 04:14:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 5ee4dda8-4c09-39d4-9d6f-159ccf618f87 | -10.9946 | -46.51685 | 2024-10-01 04:14:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 23f787c2-9b8b-39fb-93bf-ea3edc7a0de9 | -10.99437 | -46.49665 | 2024-10-01 04:14:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| dcc9952c-17a2-3803-a684-c07abdd7bfbb | -10.99396 | -46.52075 | 2024-10-01 04:14:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 860f095d-e873-36be-8bcd-9269d4fa4f66 | -10.99338 | -46.45948 | 2024-10-01 04:14:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 464a30ec-22bf-313b-9c5e-f63407bd994a | -10.99331 | -46.52466 | 2024-10-01 04:14:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 11.1 |
| da19f1bd-e2a2-3392-8f1f-e11c3d8ab354 | -10.99266 | -46.52858 | 2024-10-01 04:14:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 23.3 |
| 5e3d09b1-14d2-3897-a1ff-57093a14d0d4 | -10.99241 | -46.50844 | 2024-10-01 04:14:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f7ad9da6-ac87-39fb-8bb5-6ac663d15cd1 | -10.99201 | -46.53252 | 2024-10-01 04:14:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 23.3 |
| 02ebf4b0-bc46-3f1f-8ce4-6bc99bfc400f | -10.99176 | -46.51236 | 2024-10-01 04:14:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 565600d6-9fef-3537-a46a-fc43066a46ce | -10.99135 | -46.53646 | 2024-10-01 04:14:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 36.9 |
| 5b2e4533-f4da-3e5c-9061-9930ae7475da | -10.99054 | -46.45499 | 2024-10-01 04:14:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d8337305-f60b-34e6-9a25-bdc4972a7408 | -16.07049 | -50.37389 | 2024-10-01 04:14:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| df7fd9e7-c278-33e7-8e39-1d9ceece6ba1 | -10.99047 | -46.52016 | 2024-10-01 04:14:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 754f68c9-40e8-3413-8f8b-fa2913d7daa7 | -10.98982 | -46.52407 | 2024-10-01 04:14:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 887db207-3c11-30f2-9a8b-d0610687ca89 | -10.98917 | -46.528 | 2024-10-01 04:14:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 36.5 |
| db8df085-6fa9-3303-b23b-6ce68edf1e5a | -10.98851 | -46.53193 | 2024-10-01 04:14:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 36.5 |
| 34991575-4d57-3580-9a97-4076b46064dc | -10.98786 | -46.53589 | 2024-10-01 04:14:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 16.5 |
| c8e72dc0-83ee-3642-8c16-2cc329f87a80 | -10.98772 | -46.45047 | 2024-10-01 04:14:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 95cded5d-870d-3159-8d33-3c40237c441c | -10.98273 | -46.43752 | 2024-10-01 04:14:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 65053aef-401a-39ab-9030-b116f01943e2 | -10.98207 | -46.44145 | 2024-10-01 04:14:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d74300b2-b5fa-34d0-87e1-7ed1560b899c | -10.96497 | -46.47958 | 2024-10-01 04:14:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d69a62f7-9b31-34a9-be2a-4d3c2b24dcae | -10.96148 | -46.479 | 2024-10-01 04:14:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 43d7d797-91cf-3d4b-b953-532ba8527be4 | -10.95906 | -46.5149 | 2024-10-01 04:14:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 60d31300-871d-3e2a-ba8c-b92e07dcf83c | -10.95822 | -46.49851 | 2024-10-01 04:14:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3a424c8e-0a06-3218-92e4-e1f1818c47bd | -11.33708 | -46.26913 | 2024-10-01 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a1f9f0e3-ffa2-3a15-8a5e-aa474dc58c19 | -12.19297 | -47.26898 | 2024-10-01 04:14:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6328461a-dd9a-3573-8a29-c23b46f67741 | -11.87561 | -47.32473 | 2024-10-01 04:14:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c5ef8552-6c68-3741-9ef5-19feff60e4a7 | -11.86468 | -47.12704 | 2024-10-01 04:14:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e3e161f6-91b6-3b7e-9ef7-80806d18343f | -11.86399 | -47.13114 | 2024-10-01 04:14:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4712bc23-e261-3b18-ba84-06539f0a887e | -11.80777 | -47.59629 | 2024-10-01 04:14:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0202ed41-4ce3-3292-97dd-33b691d2c741 | -11.80703 | -47.60067 | 2024-10-01 04:14:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| cd109f44-9bba-3eb3-bb54-0be8f39d2b47 | -11.8034 | -47.60003 | 2024-10-01 04:14:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| cb2e3e38-2f8e-3b8f-a43a-9c755050dc00 | -11.76998 | -47.59847 | 2024-10-01 04:14:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 74514e83-3298-38dd-91d1-de74e2ef0856 | -11.76923 | -47.60284 | 2024-10-01 04:14:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 935d7c13-e8f4-38fd-a591-73acd5148228 | -11.7656 | -47.60218 | 2024-10-01 04:14:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0e1b7038-f351-3112-a242-79317855ba45 | -11.76485 | -47.60653 | 2024-10-01 04:14:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7adcb0e9-48ba-39ac-bf84-b75624f68fee | -11.44613 | -46.96241 | 2024-10-01 04:14:00 | NOAA-20 | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |


[Clique aqui para ver as próximas entradas](README76.md)
