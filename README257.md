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

## Dados Diários - Página 257

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 256782dd-1dcc-3ceb-b117-e0bead007a9e | -17.03424 | -42.36357 | 2026-10-08 16:16:00 | NPP-375 | FRANCISCO BADARÓ | MINAS GERAIS | Brasil | 3126505 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8c0585f3-fd26-3264-bd68-5ba358112433 | -14.42199 | -41.50586 | 2026-10-08 16:16:00 | NPP-375 | ARACATU | BAHIA | Brasil | 2902005 | 29 | 33 | nan | nan | nan | Caatinga | 5.8 |
| 77cedb50-c796-3d71-b4de-7385be34d4c3 | -17.00264 | -42.37969 | 2026-10-08 16:16:00 | NPP-375 | FRANCISCO BADARÓ | MINAS GERAIS | Brasil | 3126505 | 31 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 48641327-4d32-3eff-bac5-26d9c45fa670 | -18.29494 | -42.88436 | 2026-10-08 16:16:00 | NPP-375 | RIO VERMELHO | MINAS GERAIS | Brasil | 3156007 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.7 |
| ebae45c5-7e57-3ab0-ba7c-b35949448918 | -16.31495 | -44.56479 | 2026-10-08 16:16:00 | NPP-375 | BRASÍLIA DE MINAS | MINAS GERAIS | Brasil | 3108602 | 31 | 33 | nan | nan | nan | Cerrado | 45.1 |
| 4d0c37ae-4c48-335d-a649-a4591a6e1b46 | -16.7641 | -40.99442 | 2026-10-08 16:16:00 | NPP-375 | JOAÍMA | MINAS GERAIS | Brasil | 3136009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 33.3 |
| e0fd482b-1483-3320-8d15-1343bb268a35 | -20.08041 | -42.7083 | 2026-10-08 16:16:00 | NPP-375 | RIO CASCA | MINAS GERAIS | Brasil | 3154903 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| aa297018-10da-3ac3-911d-20eb95261520 | -17.57924 | -42.27422 | 2026-10-08 16:16:00 | NPP-375 | SETUBINHA | MINAS GERAIS | Brasil | 3165552 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.5 |
| 95c443d0-daf3-3e4c-a485-804596da9424 | -15.11391 | -43.63077 | 2026-10-08 16:16:00 | NPP-375 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 55.0 |
| 82dfd5dd-8bb4-30c4-815c-01f6ed467dc3 | -16.24363 | -41.73495 | 2026-10-08 16:16:00 | NPP-375 | COMERCINHO | MINAS GERAIS | Brasil | 3117009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 13.4 |
| cb67c9f1-4f56-3ce1-bc32-efe278b64795 | -15.70263 | -40.59161 | 2026-10-08 16:16:00 | NPP-375 | MACARANI | BAHIA | Brasil | 2919702 | 29 | 33 | nan | nan | nan | Mata Atlântica | 7.4 |
| 87759cef-7ec6-321e-9115-c32ed5b9c282 | -17.36509 | -45.44992 | 2026-10-08 16:16:00 | NPP-375 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 578668f1-c4e0-3881-90ac-d3adadaaf8db | -18.4497 | -51.02951 | 2026-10-08 16:16:00 | NPP-375 | CACHOEIRA ALTA | GOIÁS | Brasil | 5204102 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 4ae50b98-0182-3138-b777-5a1caa300743 | -15.47595 | -41.00495 | 2026-10-08 16:16:00 | NPP-375 | VITÓRIA DA CONQUISTA | BAHIA | Brasil | 2933307 | 29 | 33 | nan | nan | nan | Mata Atlântica | 22.1 |
| 0baa16ac-165a-3fd1-b5a7-0c9f62b02dc7 | -16.2476 | -41.73473 | 2026-10-08 16:16:00 | NPP-375 | COMERCINHO | MINAS GERAIS | Brasil | 3117009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 13.4 |
| fb5f26b9-6fa7-3706-876a-0fc8dbf841ee | -14.35555 | -41.49432 | 2026-10-08 16:16:00 | NPP-375 | ARACATU | BAHIA | Brasil | 2902005 | 29 | 33 | nan | nan | nan | Caatinga | 7.3 |
| 654cf5fb-1082-370b-848c-d5d17676e21c | -14.35176 | -41.49481 | 2026-10-08 16:16:00 | NPP-375 | ARACATU | BAHIA | Brasil | 2902005 | 29 | 33 | nan | nan | nan | Caatinga | 88.6 |
| 22fbed14-b01a-3193-85b8-499703eb6e24 | -14.55768 | -41.34653 | 2026-10-08 16:16:00 | NPP-375 | CARAÍBAS | BAHIA | Brasil | 2906899 | 29 | 33 | nan | nan | nan | Caatinga | 6.1 |
| 3ab81158-bd69-3751-8404-c21d0fb1eabf | -15.68354 | -50.57566 | 2026-10-08 16:16:00 | NPP-375 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 6a6d3aaf-864a-3aca-8d2b-6a654f092a0a | -15.95539 | -41.08959 | 2026-10-08 16:16:00 | NPP-375 | PEDRA AZUL | MINAS GERAIS | Brasil | 3148707 | 31 | 33 | nan | nan | nan | Mata Atlântica | 17.8 |
| 663e5522-e240-3436-b023-69686b267044 | -16.76013 | -40.9969 | 2026-10-08 16:16:00 | NPP-375 | JOAÍMA | MINAS GERAIS | Brasil | 3136009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 21.9 |
| df69e2d6-e85f-39f8-a0e8-92cae49de16c | -14.47173 | -41.24982 | 2026-10-08 16:16:00 | NPP-375 | ARACATU | BAHIA | Brasil | 2902005 | 29 | 33 | nan | nan | nan | Caatinga | 14.9 |
| 1d7fe9a8-9015-33d6-8a1a-f16ac4617c5d | -17.18606 | -44.43899 | 2026-10-08 16:16:00 | NPP-375 | JEQUITAÍ | MINAS GERAIS | Brasil | 3135605 | 31 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 531ce6f5-252e-3a2f-8249-d63c79054d11 | -14.68242 | -43.13111 | 2026-10-08 16:16:00 | NPP-375 | ESPINOSA | MINAS GERAIS | Brasil | 3124302 | 31 | 33 | nan | nan | nan | Caatinga | 38.5 |
| b9e91d75-09df-3779-ac04-2797b67be4eb | -13.9134 | -39.82549 | 2026-10-08 16:16:00 | NPP-375 | JEQUIÉ | BAHIA | Brasil | 2918001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 282c1ff4-a653-3658-8f34-f8f7e85e0e21 | -14.53286 | -41.67155 | 2026-10-08 16:16:00 | NPP-375 | PRESIDENTE JÂNIO QUADROS | BAHIA | Brasil | 2925709 | 29 | 33 | nan | nan | nan | Caatinga | 23.7 |
| 8e1157c2-daf7-3456-9f90-517df33297b9 | -14.69941 | -41.01108 | 2026-10-08 16:16:00 | NPP-375 | ANAGÉ | BAHIA | Brasil | 2901205 | 29 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 6fab7bcd-bbf7-3207-821c-15477447ee80 | -16.63327 | -45.50918 | 2026-10-08 16:16:00 | NPP-375 | SANTA FÉ DE MINAS | MINAS GERAIS | Brasil | 3157609 | 31 | 33 | nan | nan | nan | Cerrado | 6.7 |
| f8ec1875-2cf0-379d-aaba-42fa14ec2300 | -14.98663 | -42.66866 | 2026-10-08 16:16:00 | NPP-375 | ESPINOSA | MINAS GERAIS | Brasil | 3124302 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.0 |
| a8655128-7fb3-31b1-81e8-d40cd3636e4b | -19.36045 | -40.35452 | 2026-10-08 16:16:00 | NPP-375 | LINHARES | ESPÍRITO SANTO | Brasil | 3203205 | 32 | 33 | nan | nan | nan | Mata Atlântica | 5.3 |
| b78e4142-0f76-383e-b734-2630756d9160 | -14.90571 | -41.11014 | 2026-10-08 16:16:00 | NPP-375 | VITÓRIA DA CONQUISTA | BAHIA | Brasil | 2933307 | 29 | 33 | nan | nan | nan | Mata Atlântica | 6.8 |
| 3099452e-6e76-37fc-ab35-53ff2f17f682 | -15.95224 | -41.09479 | 2026-10-08 16:16:00 | NPP-375 | PEDRA AZUL | MINAS GERAIS | Brasil | 3148707 | 31 | 33 | nan | nan | nan | Mata Atlântica | 17.8 |
| 57ce7048-8e73-307a-8593-779d50a80953 | -16.12784 | -43.75292 | 2026-10-08 16:16:00 | NPP-375 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 36.4 |
| ac9cc0c8-dbf1-3780-962d-6df8f498cb78 | -19.07986 | -40.08793 | 2026-10-08 16:16:00 | NPP-375 | SOORETAMA | ESPÍRITO SANTO | Brasil | 3205010 | 32 | 33 | nan | nan | nan | Mata Atlântica | 4.7 |
| 35f657ed-267c-3a0c-84ab-194ee86ae683 | -17.88328 | -42.19124 | 2026-10-08 16:16:00 | NPP-375 | MALACACHETA | MINAS GERAIS | Brasil | 3139201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 794fccbb-43df-3fbb-af88-050600974151 | -14.13756 | -40.79303 | 2026-10-08 16:16:00 | NPP-375 | MIRANTE | BAHIA | Brasil | 2921450 | 29 | 33 | nan | nan | nan | Caatinga | 25.9 |
| 95d4014d-8788-3267-9a7f-da8e65f1c476 | -15.56903 | -44.52662 | 2026-10-08 16:16:00 | NPP-375 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 13.5 |
| 06006dd4-bbaf-39fb-ab9b-d74ab328edda | -17.36474 | -45.44678 | 2026-10-08 16:16:00 | NPP-375 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 1d9f508a-e3f8-3811-92f4-a3815b226eac | -14.88402 | -39.52618 | 2026-10-08 16:16:00 | NPP-375 | IBICARAÍ | BAHIA | Brasil | 2912103 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| 69ae9bd4-661b-3817-91ec-86ae124a5c2e | -16.19446 | -44.56614 | 2026-10-08 16:16:00 | NPP-375 | LUISLÂNDIA | MINAS GERAIS | Brasil | 3138682 | 31 | 33 | nan | nan | nan | Cerrado | 8.7 |
| d8b46413-490a-3102-856a-8310c026fdb8 | -15.93238 | -38.95072 | 2026-10-08 16:16:00 | NPP-375 | BELMONTE | BAHIA | Brasil | 2903409 | 29 | 33 | nan | nan | nan | Mata Atlântica | 7.0 |
| 99673586-aecb-3785-91dd-0f8d0e400589 | -16.47345 | -41.39873 | 2026-10-08 16:16:00 | NPP-375 | JEQUITINHONHA | MINAS GERAIS | Brasil | 3135803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| a90a48eb-c18e-313c-89d8-7e5bd223d5ad | -15.88338 | -40.78024 | 2026-10-08 16:16:00 | NPP-375 | ALMENARA | MINAS GERAIS | Brasil | 3101706 | 31 | 33 | nan | nan | nan | Mata Atlântica | 80.8 |
| 1f5e951d-fd74-3fe3-b7b3-a46eacadd0ac | -18.98423 | -44.46319 | 2026-10-08 16:16:00 | NPP-375 | CURVELO | MINAS GERAIS | Brasil | 3120904 | 31 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 62380e00-42af-316b-b654-8287f7d89f61 | -14.68199 | -43.13085 | 2026-10-08 16:16:00 | NPP-375 | ESPINOSA | MINAS GERAIS | Brasil | 3124302 | 31 | 33 | nan | nan | nan | Caatinga | 44.7 |
| 2b6740b1-cba0-36ca-b158-99005de65e00 | -15.56434 | -44.52713 | 2026-10-08 16:16:00 | NPP-375 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 7638749f-c5b0-344c-9b17-88117ff2b4fc | -17.88178 | -42.1914 | 2026-10-08 16:16:00 | NPP-375 | MALACACHETA | MINAS GERAIS | Brasil | 3139201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 3bf00b40-5ecd-34dc-b66e-52fb83fa0c92 | -14.75368 | -47.13874 | 2026-10-08 16:16:00 | NPP-375 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| ab8da755-bdfe-33fb-91f8-2b9d0a0fcd43 | -15.68917 | -40.46802 | 2026-10-08 16:16:00 | NPP-375 | MACARANI | BAHIA | Brasil | 2919702 | 29 | 33 | nan | nan | nan | Mata Atlântica | 36.5 |
| 3f093d16-e837-3f9a-a027-11ab9ed14be9 | -15.95601 | -41.09423 | 2026-10-08 16:16:00 | NPP-375 | PEDRA AZUL | MINAS GERAIS | Brasil | 3148707 | 31 | 33 | nan | nan | nan | Mata Atlântica | 17.8 |
| b4d34041-f742-3f07-9a3e-e18ad90008d2 | -18.92056 | -41.02056 | 2026-10-08 16:16:00 | NPP-375 | MANTENÓPOLIS | ESPÍRITO SANTO | Brasil | 3203304 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 111bbd4c-1c53-3276-ad27-ab5fd95fa0e0 | -15.6898 | -40.47253 | 2026-10-08 16:16:00 | NPP-375 | MACARANI | BAHIA | Brasil | 2919702 | 29 | 33 | nan | nan | nan | Mata Atlântica | 9.4 |
| 385f51c4-47fc-343c-bf22-ebee6f1fbcdd | -15.54813 | -42.3548 | 2026-10-08 16:16:00 | NPP-375 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 4.1 |
| b16c614f-d7a3-3a6f-acf0-655672be1a3a | -20.88305 | -43.29928 | 2026-10-08 16:16:00 | NPP-375 | CIPOTÂNEA | MINAS GERAIS | Brasil | 3116308 | 31 | 33 | nan | nan | nan | Mata Atlântica | 12.2 |
| 7b696b91-8e06-30f0-8279-ebd5a132ddd9 | -15.39234 | -44.34151 | 2026-10-08 16:16:00 | NPP-375 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 35.2 |
| 2b80cf17-01ad-36ee-911b-2b93dfa10e30 | -14.56426 | -44.07148 | 2026-10-08 16:16:00 | NPP-375 | MANGA | MINAS GERAIS | Brasil | 3139300 | 31 | 33 | nan | nan | nan | Caatinga | 27.2 |
| 6428511d-8b20-3bc4-a8a2-8e8404eb4689 | -14.66844 | -40.49734 | 2026-10-08 16:16:00 | NPP-375 | PLANALTO | BAHIA | Brasil | 2925006 | 29 | 33 | nan | nan | nan | Mata Atlântica | 5.2 |
| 60cc530b-374e-31c7-ae50-a40b760e27ff | -14.99067 | -42.66769 | 2026-10-08 16:16:00 | NPP-375 | ESPINOSA | MINAS GERAIS | Brasil | 3124302 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.0 |
| 78d0e529-ad3c-3159-8f21-325a2d460ad7 | -16.7595 | -40.99208 | 2026-10-08 16:16:00 | NPP-375 | JOAÍMA | MINAS GERAIS | Brasil | 3136009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 21.9 |
| fdf83ad4-4495-3b10-8853-b90a83db8272 | -17.20649 | -39.27988 | 2026-10-08 16:16:00 | NPP-375 | PRADO | BAHIA | Brasil | 2925501 | 29 | 33 | nan | nan | nan | Mata Atlântica | 4.5 |
| c7889c91-caef-30d6-bd27-467fac80645a | -15.93516 | -38.96976 | 2026-10-08 16:16:00 | NPP-375 | BELMONTE | BAHIA | Brasil | 2903409 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| 9f80f039-bc2c-358d-8164-b43952fedc13 | -16.48402 | -41.80983 | 2026-10-08 16:16:00 | NPP-375 | ITINGA | MINAS GERAIS | Brasil | 3134004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 11.3 |
| fc6010a7-7b75-3048-b16f-032c52a79e13 | -18.14371 | -41.6298 | 2026-10-08 16:16:00 | NPP-375 | FREI GASPAR | MINAS GERAIS | Brasil | 3126802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.8 |
| f9c4d920-1b3b-3b71-be82-5cde5de92e90 | -15.47772 | -42.07141 | 2026-10-08 16:16:00 | NPP-375 | INDAIABIRA | MINAS GERAIS | Brasil | 3130655 | 31 | 33 | nan | nan | nan | Mata Atlântica | 22.6 |
| 78c2f457-ee3d-3b3d-8cf2-392bac7cd8b3 | -16.69035 | -42.51945 | 2026-10-08 16:16:00 | NPP-375 | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 6.1 |
| dbe940c3-596b-345e-bb0d-8d6dc5fcfd3d | -14.97006 | -48.19805 | 2026-10-08 16:16:00 | NPP-375 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 13.2 |
| a4cd3786-0351-3b51-826b-adea872f32cf | -17.61216 | -42.08571 | 2026-10-08 16:16:00 | NPP-375 | SETUBINHA | MINAS GERAIS | Brasil | 3165552 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 25e42e70-c955-35c7-bfe7-6387fe530285 | -20.94971 | -44.7743 | 2026-10-08 16:16:00 | NPP-375 | BOM SUCESSO | MINAS GERAIS | Brasil | 3108008 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.8 |
| 61292a74-4947-301b-bbc0-e45f8eaf2b0c | -15.31298 | -41.02457 | 2026-10-08 16:16:00 | NPP-375 | VITÓRIA DA CONQUISTA | BAHIA | Brasil | 2933307 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| ff04e05b-2d7c-3ebf-9a71-a42a6d74b3b6 | -16.15649 | -43.63565 | 2026-10-08 16:16:00 | NPP-375 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 13.4 |
| cb681ea6-c494-341e-b0c8-ed8f395b52ab | -14.52363 | -40.65969 | 2026-10-08 16:16:00 | NPP-375 | ANAGÉ | BAHIA | Brasil | 2901205 | 29 | 33 | nan | nan | nan | Caatinga | 4.5 |
| d942f8b6-c2df-3e14-a211-3dcdceef7693 | -15.31584 | -40.64389 | 2026-10-08 16:16:00 | NPP-375 | RIBEIRÃO DO LARGO | BAHIA | Brasil | 2926657 | 29 | 33 | nan | nan | nan | Mata Atlântica | 5.5 |
| b9363c37-fc11-304c-8cdc-e68472b126b1 | -16.907 | -40.88878 | 2026-10-08 16:16:00 | NPP-375 | FRONTEIRA DOS VALES | MINAS GERAIS | Brasil | 3127057 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.7 |
| f2da8e89-4cd5-3e83-a92e-f84941e04577 | -15.31705 | -40.64708 | 2026-10-08 16:16:00 | NPP-375 | RIBEIRÃO DO LARGO | BAHIA | Brasil | 2926657 | 29 | 33 | nan | nan | nan | Mata Atlântica | 7.6 |
| bc882014-8d5c-3e1d-942e-d4bdde00a9cc | -14.46556 | -40.72095 | 2026-10-08 16:16:00 | NPP-375 | ANAGÉ | BAHIA | Brasil | 2901205 | 29 | 33 | nan | nan | nan | Caatinga | 12.2 |
| 3020ae02-f331-3c6d-8183-cc724941f8d2 | -15.96555 | -41.43012 | 2026-10-08 16:16:00 | NPP-375 | CACHOEIRA DE PAJEÚ | MINAS GERAIS | Brasil | 3102704 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| fa851bbc-a7b7-34b5-bd39-8b9c295ec78d | -14.46983 | -40.72484 | 2026-10-08 16:16:00 | NPP-375 | ANAGÉ | BAHIA | Brasil | 2901205 | 29 | 33 | nan | nan | nan | Caatinga | 69.2 |
| 31739d8e-e5d5-35f0-bcaa-364824398077 | -15.73796 | -47.35809 | 2026-10-08 16:16:00 | NPP-375 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 3.9 |
| ae45b16c-0c02-38c2-804b-bacf07dbe492 | -15.72232 | -38.99032 | 2026-10-08 16:16:00 | NPP-375 | CANAVIEIRAS | BAHIA | Brasil | 2906303 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 95de89e4-b690-3ba3-bf77-a3a68eb5d4da | -14.73298 | -41.79636 | 2026-10-08 16:16:00 | NPP-375 | PRESIDENTE JÂNIO QUADROS | BAHIA | Brasil | 2925709 | 29 | 33 | nan | nan | nan | Caatinga | 14.2 |
| 9383bb63-4e9d-3240-8c8a-5aee551c0a02 | -15.33923 | -42.77534 | 2026-10-08 16:16:00 | NPP-375 | MONTE AZUL | MINAS GERAIS | Brasil | 3142908 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 562af4b8-4917-3dba-8a5a-a5a6f068c443 | -19.06436 | -48.64553 | 2026-10-08 16:16:00 | NPP-375 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 5d220392-c5a8-33a1-90f4-29cf231ea512 | -18.26671 | -42.1819 | 2026-10-08 16:16:00 | NPP-375 | SÃO JOSÉ DA SAFIRA | MINAS GERAIS | Brasil | 3163003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 25.4 |
| c6d89d9c-4ee3-33d3-9c9f-561557df1ded | -14.41064 | -41.28463 | 2026-10-08 16:16:00 | NPP-375 | ARACATU | BAHIA | Brasil | 2902005 | 29 | 33 | nan | nan | nan | Caatinga | 41.8 |
| 6d6ea89f-6792-3de1-9e87-8c60655b8f0b | -17.95603 | -42.77314 | 2026-10-08 16:16:00 | NPP-375 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f16bb22b-6a02-35e1-bb4a-693c2945fdb6 | -19.65119 | -40.22904 | 2026-10-08 16:16:00 | NPP-375 | ARACRUZ | ESPÍRITO SANTO | Brasil | 3200607 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 8e9f503e-44c0-3144-bcf6-2ae9a8e825ab | -17.46864 | -42.7143 | 2026-10-08 16:16:00 | NPP-375 | VEREDINHA | MINAS GERAIS | Brasil | 3171071 | 31 | 33 | nan | nan | nan | Cerrado | 14.1 |
| b1d8d65d-4324-3bea-a903-8a1bb23ff241 | -16.45821 | -41.25682 | 2026-10-08 16:16:00 | NPP-375 | JEQUITINHONHA | MINAS GERAIS | Brasil | 3135803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.9 |
| e80f840d-4cac-399f-b5b3-5de90ad7f448 | -15.68685 | -40.77745 | 2026-10-08 16:16:00 | NPP-375 | ENCRUZILHADA | BAHIA | Brasil | 2910404 | 29 | 33 | nan | nan | nan | Mata Atlântica | 5.8 |
| 0d9388f6-f9d6-339e-a075-edac449063c9 | -15.55966 | -44.52765 | 2026-10-08 16:16:00 | NPP-375 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 7.8 |
| dffbe252-3fc6-3a86-b5d9-6d0ec1f2e894 | -15.85785 | -40.80139 | 2026-10-08 16:16:00 | NPP-375 | ALMENARA | MINAS GERAIS | Brasil | 3101706 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| 75f0b110-eeb2-3d13-83a9-f760dcec4074 | -14.46983 | -40.72574 | 2026-10-08 16:16:00 | NPP-375 | ANAGÉ | BAHIA | Brasil | 2901205 | 29 | 33 | nan | nan | nan | Caatinga | 62.1 |
| ad771707-29b9-385a-9cae-62d941ca47f2 | -19.25211 | -47.21437 | 2026-10-08 16:16:00 | NPP-375 | PERDIZES | MINAS GERAIS | Brasil | 3149804 | 31 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 56097459-22a9-332e-b72a-7de1e98136d2 | -15.3134 | -40.64767 | 2026-10-08 16:16:00 | NPP-375 | RIBEIRÃO DO LARGO | BAHIA | Brasil | 2926657 | 29 | 33 | nan | nan | nan | Mata Atlântica | 7.6 |
| 1b054673-54e4-3ea0-9157-ce2bc8878180 | -17.69737 | -39.17084 | 2026-10-08 16:16:00 | NPP-375 | CARAVELAS | BAHIA | Brasil | 2906907 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 42318dbb-4d08-3473-9fda-33a554086c5f | -19.07028 | -48.63986 | 2026-10-08 16:16:00 | NPP-375 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 8293daaa-a9e6-30f0-a6a7-c68e879fcbfb | -19.6042 | -40.10572 | 2026-10-08 16:16:00 | NPP-375 | ARACRUZ | ESPÍRITO SANTO | Brasil | 3200607 | 32 | 33 | nan | nan | nan | Mata Atlântica | 11.6 |
| 60dea1e8-8da5-3fa4-99c5-ad74c0a57ac9 | -16.12648 | -43.74211 | 2026-10-08 16:16:00 | NPP-375 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 27.8 |
| 98650c01-d21c-36b9-9086-fd91f07565ec | -14.86277 | -40.88078 | 2026-10-08 16:16:00 | NPP-375 | VITÓRIA DA CONQUISTA | BAHIA | Brasil | 2933307 | 29 | 33 | nan | nan | nan | Mata Atlântica | 7.3 |
| c9520117-e381-31ec-96b3-6a48a4ee25e3 | -17.96083 | -42.77653 | 2026-10-08 16:16:00 | NPP-375 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 12.8 |


[Clique aqui para ver as próximas entradas](README258.md)
