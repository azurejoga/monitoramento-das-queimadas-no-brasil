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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 774d6401-bcbd-3b28-9e2e-d4d6cdcd1b70 | -11.78192 | -43.66112 | 2026-05-10 03:38:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d85033dd-b994-3393-8d93-97b7b008b1c3 | -12.84827 | -43.75891 | 2026-05-10 03:38:00 | NOAA-21 | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 821c5501-3211-3915-8d46-32201ca801e5 | -11.75836 | -43.64394 | 2026-05-10 03:38:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6ae9a5e6-a6c0-3a50-ab21-0cba75d5a988 | -14.14767 | -45.42047 | 2026-05-10 03:38:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c498f024-86d8-3264-8d78-765f42da83c0 | -11.52904 | -43.32891 | 2026-05-10 03:38:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 63c568e7-f92b-30e5-9d5a-ab0fd84e363d | -13.05013 | -43.86684 | 2026-05-10 03:38:00 | NOAA-21 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e77acbbc-4040-300f-8e31-446e28823f11 | -12.86858 | -43.79183 | 2026-05-10 03:38:00 | NOAA-21 | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 18c8b2b8-20fd-30f4-a08f-ddbfebd8d862 | -12.27691 | -44.63061 | 2026-05-10 03:38:00 | NOAA-21 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| dd01a117-9ef3-32fd-9414-89cad633c871 | -12.865 | -43.79548 | 2026-05-10 03:38:00 | NOAA-21 | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 06f8db4b-8b5f-3e71-8de9-be5d4967cf74 | -8.72947 | -47.97988 | 2026-05-10 03:38:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 49de9cfa-e46f-3621-9a6c-bfa109693306 | -8.7332 | -47.98104 | 2026-05-10 03:38:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 4a3c72a8-2423-38f6-ad53-dc4c918ed41c | -10.59959 | -44.99282 | 2026-05-10 03:38:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| da382eec-69de-3555-9fba-d6d4aee833f8 | -11.77673 | -43.66024 | 2026-05-10 03:38:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0618316e-d878-3f55-9044-3830f329880f | -8.72805 | -47.98727 | 2026-05-10 03:38:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| baed1368-85d6-3f70-8216-36892bf83077 | -12.86561 | -43.79236 | 2026-05-10 03:38:00 | NOAA-21 | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7446f301-858d-37f1-95c8-f859ae818680 | -11.77791 | -43.65395 | 2026-05-10 03:38:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8f119f32-f6d5-35b4-810d-208816be9786 | -15.48166 | -41.64748 | 2026-05-10 03:40:00 | NOAA-21 | NINHEIRA | MINAS GERAIS | Brasil | 3144656 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 650c5cac-0556-3481-a25e-1eaa8b6ca65e | -20.21739 | -46.82535 | 2026-05-10 03:40:00 | NOAA-21 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| cd48aaeb-adfd-3e9e-9937-64bc633ddbef | -15.47742 | -41.64663 | 2026-05-10 03:40:00 | NOAA-21 | NINHEIRA | MINAS GERAIS | Brasil | 3144656 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| b73c85fe-5195-3178-86e6-627d7756977b | -16.86302 | -44.20465 | 2026-05-10 03:40:00 | NOAA-21 | CLARO DOS POÇÕES | MINAS GERAIS | Brasil | 3116506 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f47f93a2-ab34-3b73-9f2c-a0b822be3370 | -17.38036 | -42.61818 | 2026-05-10 03:40:00 | NOAA-21 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 24904d50-6fc1-3c2b-ab2e-d8efcc076757 | -15.35168 | -44.24452 | 2026-05-10 03:40:00 | NOAA-21 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 2fd989f7-8f94-35ad-ac42-a3efb29c01e9 | -21.12037 | -48.63504 | 2026-05-10 03:40:00 | NOAA-21 | PIRANGI | SÃO PAULO | Brasil | 3539004 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| a81a172f-f22f-38ec-a31b-985f140d1f13 | -18.07712 | -46.36598 | 2026-05-10 03:40:00 | NOAA-21 | PRESIDENTE OLEGÁRIO | MINAS GERAIS | Brasil | 3153400 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 610f69cd-3864-39be-8072-8a578453fd96 | -17.68584 | -40.37534 | 2026-05-10 03:40:00 | NOAA-21 | NANUQUE | MINAS GERAIS | Brasil | 3144300 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| b5cc7440-0b83-363b-86e7-400b0dcd1257 | -18.08326 | -46.36398 | 2026-05-10 03:40:00 | NOAA-21 | PRESIDENTE OLEGÁRIO | MINAS GERAIS | Brasil | 3153400 | 31 | 33 | nan | nan | nan | Cerrado | 6.4 |
| e2322f71-6809-3778-943e-0c0957d136b7 | -19.18307 | -40.67968 | 2026-05-10 03:40:00 | NOAA-21 | PANCAS | ESPÍRITO SANTO | Brasil | 3204005 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 2387cd2d-2ae8-3821-b01d-b81e98d89ba3 | -15.35109 | -44.24752 | 2026-05-10 03:40:00 | NOAA-21 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 4461c197-908a-372d-8a7f-86a9ac3c8ca6 | -19.74093 | -40.91563 | 2026-05-10 03:40:00 | NOAA-21 | ITAGUAÇU | ESPÍRITO SANTO | Brasil | 3202702 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.2 |
| 61d52a5a-56d5-3cb9-8a17-4fef10f8b03b | -21.11787 | -48.63135 | 2026-05-10 03:40:00 | NOAA-21 | PIRANGI | SÃO PAULO | Brasil | 3539004 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| d86ae665-496c-3ca2-9bfa-3d82cd6badcc | -18.08251 | -46.36753 | 2026-05-10 03:40:00 | NOAA-21 | PRESIDENTE OLEGÁRIO | MINAS GERAIS | Brasil | 3153400 | 31 | 33 | nan | nan | nan | Cerrado | 5.1 |
| cf71f8b2-96e5-3598-ad3f-9f2b9ac08cd2 | -15.35611 | -44.2486 | 2026-05-10 03:40:00 | NOAA-21 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Caatinga | 0.5 |
| dc0ff9b6-95f9-3aab-9934-84e3aea0b18d | -20.21912 | -46.81746 | 2026-05-10 03:40:00 | NOAA-21 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| bf3c31cc-78ef-31b2-8bab-366d28e38d35 | -19.54841 | -42.12685 | 2026-05-10 03:40:00 | NOAA-21 | INHAPIM | MINAS GERAIS | Brasil | 3130903 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| e5655b01-eb06-3da6-894d-dba5089872d7 | -19.73638 | -40.91913 | 2026-05-10 03:40:00 | NOAA-21 | ITAGUAÇU | ESPÍRITO SANTO | Brasil | 3202702 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| b40c548b-40b7-385e-bba7-43877d25983b | -21.11688 | -48.63576 | 2026-05-10 03:40:00 | NOAA-21 | PIRANGI | SÃO PAULO | Brasil | 3539004 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 4fcdd96e-555b-3625-8db3-8fded24c5deb | -20.21371 | -46.81633 | 2026-05-10 03:40:00 | NOAA-21 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1d3a946d-2eb6-33b7-b4fe-b434fcd727c0 | -20.21827 | -46.82133 | 2026-05-10 03:40:00 | NOAA-21 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| c624a7ae-042b-3326-bb56-319d06d2e620 | -30.08492 | -50.79614 | 2026-05-10 03:45:00 | NOAA-21 | VIAMÃO | RIO GRANDE DO SUL | Brasil | 4323002 | 43 | 33 | nan | nan | nan | Pampa | 1.9 |
| c6bd95b3-0559-32de-83f0-efbfe068f862 | -9.41724 | -50.69337 | 2026-05-10 04:10:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 9db8726c-d9da-3684-828b-a30d53a0b8a0 | -6.99045 | -42.87097 | 2026-05-10 04:10:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 5.4 |
| 18a93f68-df1c-37ab-9553-34cea8c38c94 | -6.99399 | -42.87156 | 2026-05-10 04:10:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 8760929c-0392-3669-bd92-414a9a675df8 | -6.9792 | -42.8732 | 2026-05-10 04:10:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 433d90fc-87f3-3d7b-9a6b-0960e3a928f4 | -8.488 | -46.3703 | 2026-05-10 04:10:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0b1861be-863e-3dfe-b060-48f9d6effd07 | -8.72729 | -47.98742 | 2026-05-10 04:10:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| e7289d7d-7161-3bc5-962f-5d6e63f5b7e2 | -8.48924 | -46.36761 | 2026-05-10 04:10:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2adff84b-3139-3711-ace4-fffa7f46494a | -6.97631 | -42.86864 | 2026-05-10 04:10:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 0a6cafc6-4b05-3d50-b1ef-5cbe47191be2 | -6.97566 | -42.8726 | 2026-05-10 04:10:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| bdbb588b-99b7-3379-b3f4-c9082e6737f7 | -6.97984 | -42.86924 | 2026-05-10 04:10:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 03ee201c-ebba-38f1-bcee-0ca113469d89 | -8.49431 | -46.35931 | 2026-05-10 04:10:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3952dcc2-8f4e-3c4a-8d16-0204cb9a6625 | -6.9911 | -42.86701 | 2026-05-10 04:10:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 9.9 |
| cc66a688-d034-32c6-a993-07579291fdc8 | -8.72956 | -47.97882 | 2026-05-10 04:10:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| e219d222-31f9-3f50-8d4b-11309c0f240d | -9.41446 | -50.68751 | 2026-05-10 04:10:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 4f74d357-cf7f-302e-8a4e-cff5e8f4b7ff | -6.98338 | -42.86981 | 2026-05-10 04:10:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| b30394a3-83d7-381c-adb1-cd00530c9941 | -9.41796 | -50.68963 | 2026-05-10 04:10:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d7fb590b-d0c9-35b5-a781-d40e0ff76cb1 | -8.48857 | -46.37156 | 2026-05-10 04:10:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 52302c3d-08ff-338f-a93b-9c0a780f31ca | -6.99463 | -42.8676 | 2026-05-10 04:10:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| a2902b9c-2fd2-3131-9f29-5ee1fc25b2c8 | -11.52572 | -43.32996 | 2026-05-10 04:10:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8d6d3cca-33fa-347f-b9ff-af548e954ca1 | -8.72908 | -47.97718 | 2026-05-10 04:10:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 186da7ee-e629-30df-9829-b2a8aae778ee | -8.49292 | -46.36718 | 2026-05-10 04:10:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 09d2bee9-96e7-3900-a0dc-5b59bf2ead87 | -9.41236 | -50.69884 | 2026-05-10 04:10:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 8a032bdd-6190-37ad-a8a2-8420dc648429 | -8.72819 | -47.98228 | 2026-05-10 04:10:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 3c7a236b-a118-34b4-9ca0-0090263dc614 | -8.57432 | -41.41847 | 2026-05-10 04:10:00 | NPP-375D | QUEIMADA NOVA | PIAUÍ | Brasil | 2208650 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| bff6959d-4629-399d-8cbd-256b0ae8e63b | -8.72862 | -47.98393 | 2026-05-10 04:10:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| e38e8fb1-4a4f-3934-928e-1a3e5efd54f4 | -8.48869 | -46.36637 | 2026-05-10 04:10:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9215c3d4-bab4-320c-bbc5-5e5cd68d42a2 | -5.29215 | -44.68168 | 2026-05-10 04:10:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9cbfb716-deaf-3572-a244-ba7df4e17071 | -9.41307 | -50.69505 | 2026-05-10 04:10:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 7ad79e54-b784-3ef0-90ff-e0e61e4cbabf | -6.98981 | -42.87492 | 2026-05-10 04:10:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 5.4 |
| ffbd4b5a-94e5-3623-9637-aea46d877b6b | -5.29613 | -44.68241 | 2026-05-10 04:10:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3d3fba0a-33de-30f2-958f-e42ed9ba8508 | -9.41377 | -50.69127 | 2026-05-10 04:10:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 4f6ef885-822c-3dac-9189-42a07369ae13 | -15.34923 | -44.24413 | 2026-05-10 04:12:00 | NPP-375D | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 02fb5551-cba7-340f-b464-b723a3c4160f | -14.90062 | -45.18494 | 2026-05-10 04:12:00 | NPP-375D | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4f63e8ae-6f16-3f4f-9047-58db3ff8e213 | -14.11934 | -46.93677 | 2026-05-10 04:12:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4d56eae4-7c82-3b33-8db9-bde6e48a3ab0 | -13.19324 | -52.70524 | 2026-05-10 04:12:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3819f6e0-507f-34d5-8d03-17f622dcfffd | -14.30231 | -49.2498 | 2026-05-10 04:12:00 | NPP-375D | NOVA IGUAÇU DE GOIÁS | GOIÁS | Brasil | 5214879 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b9093506-c500-3a7d-a1c7-9c5ad9ab2179 | -17.38269 | -42.61753 | 2026-05-10 04:12:00 | NPP-375D | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bab64e1e-28b2-3110-8427-d88ab59b47dd | -14.23069 | -43.65305 | 2026-05-10 04:12:00 | NPP-375D | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b233f9d3-baec-3821-8d0f-49fc78412b9f | -15.35404 | -44.24893 | 2026-05-10 04:12:00 | NPP-375D | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 8d5b768b-8b28-3641-b175-418ff6654c54 | -15.35059 | -44.2483 | 2026-05-10 04:12:00 | NPP-375D | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Caatinga | 1.5 |
| d0eb6ef7-0bb5-3242-905b-f219bcda123e | -14.86253 | -41.61582 | 2026-05-10 04:12:00 | NPP-375D | PRESIDENTE JÂNIO QUADROS | BAHIA | Brasil | 2925709 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 9991232e-3c23-3a99-a2e9-855a7dd69577 | -15.4792 | -41.64626 | 2026-05-10 04:12:00 | NPP-375D | NINHEIRA | MINAS GERAIS | Brasil | 3144656 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| e16aa648-39cd-35ff-abbe-3ddee4405d99 | -17.68683 | -40.37314 | 2026-05-10 04:12:00 | NPP-375D | NANUQUE | MINAS GERAIS | Brasil | 3144300 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 4620861c-6e54-392f-a97b-e9a1c8d38f5d | -17.37936 | -42.61696 | 2026-05-10 04:12:00 | NPP-375D | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d4ffdf16-c1f8-33bf-a960-0119c8575c44 | -14.14727 | -45.41615 | 2026-05-10 04:12:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f22dc201-24f1-36c7-b323-689ef5b088f2 | -17.53954 | -43.5333 | 2026-05-10 04:12:00 | NPP-375D | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| fa3a1a34-4389-3f19-87b1-135be5367131 | -14.15018 | -45.42125 | 2026-05-10 04:12:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4fe1acde-feb2-3b24-a81c-777b7b80b129 | -16.36602 | -47.12088 | 2026-05-10 04:12:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5f548917-eebf-3951-b24d-2301671ae8e8 | -15.35124 | -44.24443 | 2026-05-10 04:12:00 | NPP-375D | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Caatinga | 1.5 |
| b8b8e035-dd05-3184-9fc5-0ff2909742c0 | -14.14651 | -45.42056 | 2026-05-10 04:12:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 51218384-7921-37da-af39-5bb8ced50ca8 | -13.19232 | -52.70977 | 2026-05-10 04:12:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d4e5bb2f-5451-3aa3-aa8f-ab18891f1a11 | -14.11979 | -46.93629 | 2026-05-10 04:12:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 71699457-cd30-3f69-81aa-7e1c90f98c96 | -16.86221 | -44.20504 | 2026-05-10 04:12:00 | NPP-375D | SÃO JOÃO DA LAGOA | MINAS GERAIS | Brasil | 3162252 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 93c49422-8803-3e67-8062-b9d0c5538ec4 | -16.36601 | -47.1175 | 2026-05-10 04:12:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| dd2e90e9-955c-36da-bacf-5ed9e8fe7020 | -13.18643 | -52.70842 | 2026-05-10 04:12:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 212eb60a-a3c8-3632-809d-6eaa12a7aabc | -14.1531 | -45.42635 | 2026-05-10 04:12:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| befa6a9e-496a-3481-bab8-389c900ec10b | -17.68789 | -40.37223 | 2026-05-10 04:12:00 | NPP-375D | NANUQUE | MINAS GERAIS | Brasil | 3144300 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 5b30db22-e192-3cb4-8ce1-f941a632ed63 | -12.86811 | -43.79313 | 2026-05-10 04:12:00 | NPP-375D | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 79ae67bc-4610-31af-838d-8d59c0abc40c | -12.27406 | -44.63311 | 2026-05-10 04:12:00 | NPP-375D | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5de216a7-99ae-3337-a491-5603e2b8e404 | -12.76199 | -46.97624 | 2026-05-10 04:12:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 17100af2-f8e1-38d8-bef8-f360b010f9c2 | -13.04808 | -43.86312 | 2026-05-10 04:12:00 | NPP-375D | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |


[Clique aqui para ver as próximas entradas](README3.md)
