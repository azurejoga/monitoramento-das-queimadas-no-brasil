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

## Dados Diários - Página 73

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c6cdd771-4b03-3b79-8ba4-c13d2b3cdcfe | -17.84999 | -41.42476 | 2024-10-03 03:38:00 | NOAA-20 | TEÓFILO OTONI | MINAS GERAIS | Brasil | 3168606 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| dca8f789-6f18-3ea9-acff-1a75adcb94b7 | -17.84929 | -41.42856 | 2024-10-03 03:38:00 | NOAA-20 | TEÓFILO OTONI | MINAS GERAIS | Brasil | 3168606 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| fefed76b-9997-37fe-b015-32f5070cebe1 | -17.83666 | -50.8121 | 2024-10-03 03:38:00 | NOAA-20 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ce02bc8d-cd11-33d7-b1ec-2abdc152db16 | -17.83487 | -50.81945 | 2024-10-03 03:38:00 | NOAA-20 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 25f14a07-061e-3783-bc44-3f78db135374 | -17.79968 | -42.90557 | 2024-10-03 03:38:00 | NOAA-20 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| cb8c821e-3221-3a3c-ac48-09869e7e8ee4 | -17.78095 | -42.8125 | 2024-10-03 03:38:00 | NOAA-20 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c9401528-ba9d-3ea8-9fe2-bd8c288745b6 | -17.77744 | -42.80701 | 2024-10-03 03:38:00 | NOAA-20 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 134b0b3e-3bf0-3248-889d-86fa925032f2 | -17.61353 | -41.97449 | 2024-10-03 03:38:00 | NOAA-20 | LADAINHA | MINAS GERAIS | Brasil | 3137007 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| a23a72f5-b1d5-3a0a-80db-c0e89d5dd8a9 | -17.61278 | -41.97848 | 2024-10-03 03:38:00 | NOAA-20 | NOVO CRUZEIRO | MINAS GERAIS | Brasil | 3145307 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 08bdfb7c-04cf-3121-853a-e10ca6a75898 | -17.59939 | -46.96154 | 2024-10-03 03:38:00 | NOAA-20 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 325c0547-5dc9-3211-a088-fd42bc32294b | -17.59851 | -46.96564 | 2024-10-03 03:38:00 | NOAA-20 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0e02dfac-819f-3118-8c86-69f07a330ca6 | -17.59758 | -46.96997 | 2024-10-03 03:38:00 | NOAA-20 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0eb4896f-5d27-3740-9b7f-ebc45846d048 | -17.5927 | -43.19822 | 2024-10-03 03:38:00 | NOAA-20 | CARBONITA | MINAS GERAIS | Brasil | 3113503 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 461da9c9-4cde-38c7-9c0e-d3a00f307831 | -17.41074 | -46.31731 | 2024-10-03 03:38:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 10ae18a5-e059-3a0a-b4d6-4370bd540ce4 | -17.40993 | -46.32113 | 2024-10-03 03:38:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f01ae357-51e2-3cbd-9dc6-2770101b9f76 | -17.32692 | -42.50336 | 2024-10-03 03:38:00 | NOAA-20 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 13.6 |
| 4bb47e72-8909-36a1-9c27-1b180b2872eb | -17.3261 | -42.5077 | 2024-10-03 03:38:00 | NOAA-20 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 13.6 |
| 24aa2752-77a3-31c3-9771-a58d56e16125 | -17.32214 | -41.83016 | 2024-10-03 03:38:00 | NOAA-20 | NOVO CRUZEIRO | MINAS GERAIS | Brasil | 3145307 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 9472af89-2101-3fc6-89a1-d69d43376015 | -17.261 | -43.59377 | 2024-10-03 03:38:00 | NOAA-20 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 23c142b0-8b33-34d0-ab70-2cca73c4895b | -17.25816 | -43.59565 | 2024-10-03 03:38:00 | NOAA-20 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 5f9a6d38-8cc7-3cce-92fa-3e284068dcfe | -17.25418 | -43.18488 | 2024-10-03 03:38:00 | NOAA-20 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 41cbf932-f972-3548-a435-2e093095191c | -17.24169 | -40.75312 | 2024-10-03 03:38:00 | NOAA-20 | UMBURATIBA | MINAS GERAIS | Brasil | 3170305 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 3f36075c-a44d-3abc-bc77-d6cd99a52ee9 | -17.24134 | -40.75484 | 2024-10-03 03:38:00 | NOAA-20 | UMBURATIBA | MINAS GERAIS | Brasil | 3170305 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| abc02af9-cdc0-3a2d-8402-678ea65aa84d | -17.23687 | -40.75755 | 2024-10-03 03:38:00 | NOAA-20 | UMBURATIBA | MINAS GERAIS | Brasil | 3170305 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 6f9176e7-f969-3957-8e58-25131802fdfc | -17.20167 | -41.39523 | 2024-10-03 03:38:00 | NOAA-20 | CARAÍ | MINAS GERAIS | Brasil | 3113008 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 99fb6a41-51cb-3970-970f-f8570f47fe67 | -17.11567 | -47.13439 | 2024-10-03 03:38:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 6.7 |
| d321608a-cfda-35d1-995a-a999747ac0fa | -17.11466 | -47.13908 | 2024-10-03 03:38:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 89fd69ed-fd51-3269-94fa-f6539f9c5e07 | -17.11003 | -47.1322 | 2024-10-03 03:38:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 571191a7-3093-3f52-892f-7a5ebd624486 | -17.10897 | -47.13711 | 2024-10-03 03:38:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 6a607569-df52-387b-b8e8-644c587696d8 | -16.90608 | -45.32114 | 2024-10-03 03:38:00 | NOAA-20 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c7912fff-83d7-3645-a052-694c3fb77539 | -16.90292 | -45.30969 | 2024-10-03 03:38:00 | NOAA-20 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d5b6ed2e-12b1-344d-9c0a-7b52ef5e6ad2 | -16.64631 | -44.36359 | 2024-10-03 03:38:00 | NOAA-20 | CORAÇÃO DE JESUS | MINAS GERAIS | Brasil | 3118809 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 06735e59-3eb4-3134-a115-e53db1fcd826 | -16.64514 | -44.36951 | 2024-10-03 03:38:00 | NOAA-20 | CORAÇÃO DE JESUS | MINAS GERAIS | Brasil | 3118809 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7c672809-b783-33b4-9a9b-70c668c65dc9 | -16.33734 | -50.10776 | 2024-10-03 03:38:00 | NOAA-20 | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 19.0 |
| 319062aa-e050-3945-9906-df01a30ac0bc | -16.33574 | -50.11487 | 2024-10-03 03:38:00 | NOAA-20 | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 24.8 |
| 709db8c9-0b6f-3d2a-84f1-39bb79d159fb | -16.33415 | -50.12189 | 2024-10-03 03:38:00 | NOAA-20 | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 24.8 |
| 5d76ad61-be83-34c8-aa7c-61f1683f4d93 | -16.33386 | -50.11168 | 2024-10-03 03:38:00 | NOAA-20 | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 21.0 |
| 9e87e1c4-e6f1-311c-b723-05cbe942e887 | -16.33225 | -50.11863 | 2024-10-03 03:38:00 | NOAA-20 | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 31.2 |
| 7d1c9141-7bc0-3135-a7fd-d43c957c95bd | -16.11251 | -50.43718 | 2024-10-03 03:38:00 | NOAA-20 | BURITI DE GOIÁS | GOIÁS | Brasil | 5203939 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 8754bfe5-8b44-399d-91d1-fed7f09bac7c | -16.11037 | -50.43695 | 2024-10-03 03:38:00 | NOAA-20 | BURITI DE GOIÁS | GOIÁS | Brasil | 5203939 | 52 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 2c6f352f-c993-3bf8-b804-dfe911c5610b | -16.10854 | -50.44497 | 2024-10-03 03:38:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 99f7a8b3-16f9-3d1a-ba69-ca18c22ce735 | -16.10566 | -50.45758 | 2024-10-03 03:38:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 92c297cc-2240-3b1e-bdde-0608931be29f | -16.10426 | -50.44021 | 2024-10-03 03:38:00 | NOAA-20 | BURITI DE GOIÁS | GOIÁS | Brasil | 5203939 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 880dcd61-cc30-35c5-863e-e55e7e534af9 | -16.10287 | -50.27412 | 2024-10-03 03:38:00 | NOAA-20 | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 6ee2a07b-d084-3283-bd87-7451d0122323 | -16.10183 | -50.44136 | 2024-10-03 03:38:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 9538994f-3da1-3d7f-8120-7e2e6c06b393 | -16.10126 | -50.2811 | 2024-10-03 03:38:00 | NOAA-20 | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d5116887-b7b1-3293-a860-205b9da23295 | -16.10095 | -50.45427 | 2024-10-03 03:38:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 86bf1bb2-5fe7-3f45-8465-91fe22ed69dd | -16.09855 | -50.45572 | 2024-10-03 03:38:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 16c9a5bf-5e53-37f1-a865-41ca047eb7a7 | -16.09685 | -50.43968 | 2024-10-03 03:38:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 5.7 |
| eb52ead5-76af-3995-924e-53ed4ece749d | -16.09662 | -50.26884 | 2024-10-03 03:38:00 | NOAA-20 | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 6672617b-7d43-317f-87ae-812b58db4355 | -16.09385 | -50.44339 | 2024-10-03 03:38:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 08649b24-aa5c-3e6d-b3f5-5c79000d7104 | -16.09348 | -50.45393 | 2024-10-03 03:38:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| fc27059f-2892-3493-9238-b36598b062df | -16.08735 | -50.27665 | 2024-10-03 03:38:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| b0b2d4c5-1cc9-3d22-abca-32103a3003fe | -16.08579 | -50.2834 | 2024-10-03 03:38:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 3bba24ef-8713-30fd-9d04-edc6f5811ada | -15.9214 | -48.17041 | 2024-10-03 03:38:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 2.8 |
| ea161493-3586-3983-98f4-be0cf1330481 | -15.89316 | -50.15226 | 2024-10-03 03:38:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| c28aa148-17d1-35ff-9309-d38b5ff9331b | -15.8912 | -50.16074 | 2024-10-03 03:38:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 96d8348e-7c9a-338d-b38e-eae93862b104 | -15.88976 | -50.15105 | 2024-10-03 03:38:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 9ed46594-465e-3b7a-bf8c-dd9ef802b172 | -15.88795 | -50.15911 | 2024-10-03 03:38:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 6ddcd83c-5f9a-3483-82e4-63a93e5b6c4f | -15.73759 | -48.39178 | 2024-10-03 03:38:00 | NOAA-20 | COCALZINHO DE GOIÁS | GOIÁS | Brasil | 5205513 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| c6aedceb-9fb3-3ce9-8b5a-8cf7b5131755 | -15.73738 | -48.39249 | 2024-10-03 03:38:00 | NOAA-20 | COCALZINHO DE GOIÁS | GOIÁS | Brasil | 5205513 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 089d954c-67ca-3a0f-b123-290bfd8b8f9f | -15.73226 | -48.38523 | 2024-10-03 03:38:00 | NOAA-20 | COCALZINHO DE GOIÁS | GOIÁS | Brasil | 5205513 | 52 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 2edc3737-7f9e-3aa8-8bf7-0df3cc8f9301 | -15.73208 | -48.38595 | 2024-10-03 03:38:00 | NOAA-20 | COCALZINHO DE GOIÁS | GOIÁS | Brasil | 5205513 | 52 | 33 | nan | nan | nan | Cerrado | 15.3 |
| 3391f86d-05a2-3cbe-abf4-bc7346a25da7 | -15.73108 | -48.39072 | 2024-10-03 03:38:00 | NOAA-20 | COCALZINHO DE GOIÁS | GOIÁS | Brasil | 5205513 | 52 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 806c6066-e3b2-33ef-8e3a-2dc8088e1891 | -15.73086 | -48.39144 | 2024-10-03 03:38:00 | NOAA-20 | COCALZINHO DE GOIÁS | GOIÁS | Brasil | 5205513 | 52 | 33 | nan | nan | nan | Cerrado | 34.6 |
| 47a1e0af-a8fa-3dda-befb-eb351ab05f60 | -15.72989 | -48.39622 | 2024-10-03 03:38:00 | NOAA-20 | COCALZINHO DE GOIÁS | GOIÁS | Brasil | 5205513 | 52 | 33 | nan | nan | nan | Cerrado | 12.8 |
| 367c9f9c-8fb4-3de1-8a83-84595fac4309 | -15.72564 | -48.38468 | 2024-10-03 03:38:00 | NOAA-20 | COCALZINHO DE GOIÁS | GOIÁS | Brasil | 5205513 | 52 | 33 | nan | nan | nan | Cerrado | 11.5 |
| e6e3a60f-ff79-32a8-87e0-9fc4e739bfb8 | -15.72545 | -48.38542 | 2024-10-03 03:38:00 | NOAA-20 | COCALZINHO DE GOIÁS | GOIÁS | Brasil | 5205513 | 52 | 33 | nan | nan | nan | Cerrado | 15.3 |
| 6dc7a493-3644-320e-93b3-1e3efc486691 | -15.72445 | -48.3902 | 2024-10-03 03:38:00 | NOAA-20 | COCALZINHO DE GOIÁS | GOIÁS | Brasil | 5205513 | 52 | 33 | nan | nan | nan | Cerrado | 11.5 |
| b856c90b-dbcd-321e-8f78-fe228f0f33a9 | -15.71878 | -48.38506 | 2024-10-03 03:38:00 | NOAA-20 | COCALZINHO DE GOIÁS | GOIÁS | Brasil | 5205513 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| b93a80a3-71af-3713-835a-abdf38ec540a | -15.71755 | -48.39057 | 2024-10-03 03:38:00 | NOAA-20 | COCALZINHO DE GOIÁS | GOIÁS | Brasil | 5205513 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 60723170-ae24-3da1-94bb-1c2e9208e387 | -22.94728 | -45.14522 | 2024-10-03 03:38:00 | NOAA-20 | GUARATINGUETÁ | SÃO PAULO | Brasil | 3518404 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 03fc96eb-4148-31ef-9202-9713ae56d561 | -22.77085 | -44.66671 | 2024-10-03 03:38:00 | NOAA-20 | AREIAS | SÃO PAULO | Brasil | 3503505 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 6af2a4f8-dd50-3702-8c91-856e369abc0e | -22.76962 | -44.67277 | 2024-10-03 03:38:00 | NOAA-20 | AREIAS | SÃO PAULO | Brasil | 3503505 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| eb13644e-6cfe-38a9-95b2-ec1c29adf833 | -22.76635 | -44.66579 | 2024-10-03 03:38:00 | NOAA-20 | AREIAS | SÃO PAULO | Brasil | 3503505 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| be853b6c-b528-34d9-b7cb-8fca3f54bb21 | -22.7385 | -44.8945 | 2024-10-03 03:38:00 | NOAA-20 | SILVEIRAS | SÃO PAULO | Brasil | 3552007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 05c40ab0-28ac-3d46-a944-aea21a2ec7aa | -22.73381 | -44.89412 | 2024-10-03 03:38:00 | NOAA-20 | SILVEIRAS | SÃO PAULO | Brasil | 3552007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 9ac0be5c-ef35-3384-b7a0-5d39771a6746 | -22.72818 | -44.80587 | 2024-10-03 03:38:00 | NOAA-20 | SILVEIRAS | SÃO PAULO | Brasil | 3552007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| c51315c0-f7ea-3ac8-a114-0f1f50bc80f0 | -22.6212 | -44.65649 | 2024-10-03 03:38:00 | NOAA-20 | SÃO JOSÉ DO BARREIRO | SÃO PAULO | Brasil | 3549607 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| a0152852-ee66-3e6f-a7fa-f10acac8da81 | -22.62024 | -44.66116 | 2024-10-03 03:38:00 | NOAA-20 | SÃO JOSÉ DO BARREIRO | SÃO PAULO | Brasil | 3549607 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| dcda810f-6a44-3cee-9947-43e773e7ac94 | -22.53081 | -44.84126 | 2024-10-03 03:38:00 | NOAA-20 | QUELUZ | SÃO PAULO | Brasil | 3541901 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| e21ad624-4dbd-33d9-9119-430bc7ad965c | -22.52526 | -44.84509 | 2024-10-03 03:38:00 | NOAA-20 | QUELUZ | SÃO PAULO | Brasil | 3541901 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 125eabaf-db53-3201-89ee-7f388078da0c | -16.34072 | -50.11387 | 2024-10-03 03:38:00 | NOAA-20 | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 21.0 |
| 84103a7b-5fa5-3d23-9942-1e5f9dba869b | -3.3854 | -42.2866 | 2024-10-03 03:45:25 | GOES-16 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 63.7 |
| 5e973804-d399-3af2-8f64-a3ce84d45f25 | -3.4039 | -42.3094 | 2024-10-03 03:45:25 | GOES-16 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Caatinga | 74.3 |
| d50c55de-26e2-3415-ba0c-d4fca33dccdb | -3.404 | -42.2858 | 2024-10-03 03:45:25 | GOES-16 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 602.2 |
| b45ca0f9-9205-313e-864a-59dd83adeebb | -3.4042 | -42.2621 | 2024-10-03 03:45:25 | GOES-16 | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Cerrado | 260.3 |
| 98195173-0ba2-39fa-b67b-a747495892d9 | -3.4227 | -42.2849 | 2024-10-03 03:45:25 | GOES-16 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 98.2 |
| ff5112d3-c3ef-3388-8964-cbc4f6802d15 | -3.4229 | -42.2612 | 2024-10-03 03:45:25 | GOES-16 | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Cerrado | 50.1 |
| fce3fd56-815c-3529-9faa-51e144107922 | -4.0949 | -48.4894 | 2024-10-03 03:45:29 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 94.4 |
| 8db2236f-502c-34dc-9c4f-187cb0a97df2 | -4.095 | -48.4679 | 2024-10-03 03:45:29 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 55.5 |
| ea778984-7af6-3d5b-91d6-6826ad47f51a | -4.1134 | -48.4886 | 2024-10-03 03:45:29 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 56.0 |
| c43c51f7-4f17-35a9-a72d-93a47782b6d7 | -4.4657 | -42.8877 | 2024-10-03 03:45:31 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 50.7 |
| cc471732-ccea-3804-828d-dae6d418d939 | -4.4844 | -42.8866 | 2024-10-03 03:45:31 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 167.5 |
| f9ded96f-90d7-3e9c-ba58-f961ea98827d | -4.4845 | -42.8631 | 2024-10-03 03:45:31 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 83.0 |
| c8770a63-9055-30b8-9c74-5f76431ffa9b | -4.5031 | -42.8854 | 2024-10-03 03:45:31 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 82.3 |
| 25b39e52-28f4-37a9-b7b2-2f809a233147 | -4.5033 | -42.862 | 2024-10-03 03:45:31 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 46.8 |
| 8816505d-3c50-3b8e-a844-fd888ca8e3c8 | -4.5373 | -43.3273 | 2024-10-03 03:45:31 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 78.4 |
| e797057f-e0f6-38b1-831f-556e51d36e9c | -4.5375 | -43.304 | 2024-10-03 03:45:31 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 96.4 |
| d16306ae-279a-30ec-bd8e-429e7c61fce8 | -6.6529 | -45.3324 | 2024-10-03 03:45:43 | GOES-16 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 62.9 |


[Clique aqui para ver as próximas entradas](README74.md)
