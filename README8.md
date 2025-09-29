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

## Dados Diários - Página 8

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| acd42c04-6b82-35b2-8e5a-c4daca8036d0 | -11.8291 | -51.7937 | 2025-09-29 03:20:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 182.4 |
| 68dc7fd5-b60e-3f15-82b1-5f64c6415994 | -4.4013 | -44.0755 | 2025-09-29 03:20:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 50.9 |
| 4e0ff736-284c-34a1-925d-142bbad6f482 | -12.282 | -44.1039 | 2025-09-29 03:20:00 | GOES-19 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 88.5 |
| 3e63b947-aded-34f9-8fba-4328b16e65ee | -8.2851 | -45.4999 | 2025-09-29 03:20:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 67.2 |
| c76a522f-b984-3354-b3bd-8ca9601f13ef | -17.0938 | -48.5699 | 2025-09-29 03:20:00 | GOES-19 | VIANÓPOLIS | GOIÁS | Brasil | 5222005 | 52 | 33 | nan | nan | nan | Cerrado | 77.4 |
| 2e1ce88f-581b-3b51-86a9-03ac893822cd | -3.1012 | -47.0301 | 2025-09-29 03:20:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 49.4 |
| 8dde4a30-28d4-352f-9132-09086e5f245f | -4.4011 | -44.0985 | 2025-09-29 03:20:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 46.4 |
| 10a804de-e7e7-3eee-b9a5-f1f330c35293 | -19.94451 | -43.66947 | 2025-09-29 03:21:00 | NOAA-21 | CAETÉ | MINAS GERAIS | Brasil | 3110004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| fc280622-0243-3e71-b647-fcd6a30b7303 | -19.69865 | -45.91625 | 2025-09-29 03:21:00 | NOAA-21 | LUZ | MINAS GERAIS | Brasil | 3138807 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 08c62d2b-9235-39f0-b7d2-1687ac2727e1 | -21.55539 | -41.25003 | 2025-09-29 03:21:00 | NOAA-21 | SÃO FRANCISCO DE ITABAPOANA | RIO DE JANEIRO | Brasil | 3304755 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| cfff3b89-f7ce-35a4-b14c-5fbd31c2ec57 | -19.6999 | -45.91104 | 2025-09-29 03:21:00 | NOAA-21 | LUZ | MINAS GERAIS | Brasil | 3138807 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| d9b34a90-3b8e-34ab-bcb7-612b9a0c6c06 | -19.94348 | -43.67402 | 2025-09-29 03:21:00 | NOAA-21 | CAETÉ | MINAS GERAIS | Brasil | 3110004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| cc0f19b2-b536-35ca-9b94-badcf3f6a790 | -21.5541 | -41.25605 | 2025-09-29 03:21:00 | NOAA-21 | SÃO FRANCISCO DE ITABAPOANA | RIO DE JANEIRO | Brasil | 3304755 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| dc0d2c9d-ec07-35d1-a94d-c79162f214ab | -21.13768 | -45.10588 | 2025-09-29 03:21:00 | NOAA-21 | PERDÕES | MINAS GERAIS | Brasil | 3149903 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| f16d7e8e-bb62-37dc-888c-837b9e27728c | -21.13647 | -45.11093 | 2025-09-29 03:21:00 | NOAA-21 | PERDÕES | MINAS GERAIS | Brasil | 3149903 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 2f453d07-967b-3e3b-9d24-6e7a08c4c462 | -20.0491 | -41.3251 | 2025-09-29 03:30:00 | GOES-19 | MUTUM | MINAS GERAIS | Brasil | 3144003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 204.8 |
| dd1db010-6dbc-3127-8c59-e74d44cf142c | -9.4007 | -54.6984 | 2025-09-29 03:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 48.2 |
| fbaeaf12-feb1-3092-bc37-8f8e9ef2fb25 | -12.282 | -44.1039 | 2025-09-29 03:30:00 | GOES-19 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 59.0 |
| b3fecf65-65ad-3a28-a152-6baa159611cc | -11.8482 | -51.7916 | 2025-09-29 03:30:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 49.5 |
| f77c0315-60bd-3c09-a793-d5cb449050c7 | -23.7612 | -51.7773 | 2025-09-29 03:30:00 | GOES-19 | BOM SUCESSO | PARANÁ | Brasil | 4103206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 70.3 |
| a0db8ed0-c557-32fc-904f-091db5200d12 | -3.1013 | -47.0082 | 2025-09-29 03:30:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 112.2 |
| a350747c-bd69-33af-82f3-31dbb4a870e8 | -11.8101 | -51.7957 | 2025-09-29 03:30:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 49.8 |
| 444c4be1-292e-3dac-843e-cac1aada11c9 | -7.2214 | -44.783 | 2025-09-29 03:30:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 130.8 |
| 802bcb2b-79bb-32ef-a559-34299cb48878 | -2.5772 | -48.4146 | 2025-09-29 03:30:00 | GOES-19 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 53.4 |
| 5f7c6821-2475-39b5-b479-050be620d21b | -6.0684 | -43.7771 | 2025-09-29 03:30:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 64.5 |
| 6cdee332-be7b-3e43-a50b-a1b855bafa3d | -15.2888 | -49.5256 | 2025-09-29 03:30:00 | GOES-19 | RIALMA | GOIÁS | Brasil | 5218607 | 52 | 33 | nan | nan | nan | Cerrado | 118.5 |
| 2fa8c9bd-511c-303c-953c-a76488d2bc81 | -11.8294 | -51.7725 | 2025-09-29 03:30:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 53.1 |
| 6316468e-4921-3ae7-9110-fe301d782d00 | -20.0698 | -41.3189 | 2025-09-29 03:30:00 | GOES-19 | BREJETUBA | ESPÍRITO SANTO | Brasil | 3201159 | 32 | 33 | nan | nan | nan | Mata Atlântica | 270.0 |
| 8db1000e-557d-3257-9940-581d785a11d7 | -7.2402 | -44.7812 | 2025-09-29 03:30:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 97.8 |
| 802f7224-ac96-39ec-ab66-73608eb8a0cc | -11.8291 | -51.7937 | 2025-09-29 03:30:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 128.5 |
| f11623ae-f519-3b90-b661-58229f7de353 | -3.1012 | -47.0301 | 2025-09-29 03:30:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 47.9 |
| 94487b11-c28e-3a2b-bf56-75ec9831429e | -12.5892 | -41.2845 | 2025-09-29 03:30:00 | GOES-19 | ANDARAÍ | BAHIA | Brasil | 2901304 | 29 | 33 | nan | nan | nan | Caatinga | 53.5 |
| 90acc1d5-af46-3a16-9ed1-1dd0a29123b6 | -20.0689 | -41.3449 | 2025-09-29 03:30:00 | GOES-19 | MUTUM | MINAS GERAIS | Brasil | 3144003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 154.9 |
| 5ad3a292-c2a0-39bf-8ff9-0de1414c223c | -20.0482 | -41.351 | 2025-09-29 03:30:00 | GOES-19 | MUTUM | MINAS GERAIS | Brasil | 3144003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 122.5 |
| 5b4e72e8-95ef-375a-bf35-cd38d1571a2d | -8.2851 | -45.4999 | 2025-09-29 03:30:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 73.8 |
| 317c94b6-5229-3c6b-84ec-2abfb0525f8c | -23.7401 | -51.7821 | 2025-09-29 03:30:00 | GOES-19 | BOM SUCESSO | PARANÁ | Brasil | 4103206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 72.4 |
| dedcd65c-545b-3782-8d12-14aff2de91b2 | -0.1012 | -51.2738 | 2025-09-29 03:30:00 | GOES-19 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 47.5 |
| fdb144ad-3df3-31ef-90ff-a325a3fc1443 | -15.2893 | -49.5035 | 2025-09-29 03:30:00 | GOES-19 | SANTA ISABEL | GOIÁS | Brasil | 5219357 | 52 | 33 | nan | nan | nan | Cerrado | 216.6 |
| aa4cc847-67df-3ab8-b909-4f078de556ac | -11.925 | -48.0273 | 2025-09-29 03:30:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 78.8 |
| 50148d12-e680-3a30-83de-cad876c07dd2 | -11.925 | -48.0273 | 2025-09-29 03:40:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 63.7 |
| 803b180a-d872-3c0d-a7c8-84002f68cb9d | -3.1013 | -47.0082 | 2025-09-29 03:40:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 84.9 |
| 75d79715-c176-3848-b6a4-5328c33ed0ec | -20.0689 | -41.3449 | 2025-09-29 03:40:00 | GOES-19 | MUTUM | MINAS GERAIS | Brasil | 3144003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 80.5 |
| b275763b-4a91-3665-b708-569ba9a6cb0a | -3.1012 | -47.0301 | 2025-09-29 03:40:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 68.4 |
| 3d3de6c4-ebcd-3a54-8c36-0e7f52cdfa79 | -15.2888 | -49.5256 | 2025-09-29 03:40:00 | GOES-19 | RIALMA | GOIÁS | Brasil | 5218607 | 52 | 33 | nan | nan | nan | Cerrado | 65.7 |
| adb74211-0081-37b7-9d41-a04f4919f86c | -17.0938 | -48.5699 | 2025-09-29 03:40:00 | GOES-19 | VIANÓPOLIS | GOIÁS | Brasil | 5222005 | 52 | 33 | nan | nan | nan | Cerrado | 65.9 |
| cfd5b197-50b6-3db8-83ee-0abe6db7c9e3 | -20.0698 | -41.3189 | 2025-09-29 03:40:00 | GOES-19 | BREJETUBA | ESPÍRITO SANTO | Brasil | 3201159 | 32 | 33 | nan | nan | nan | Mata Atlântica | 130.3 |
| 60b13780-f969-32b3-81b7-0994edeba662 | -20.0491 | -41.3251 | 2025-09-29 03:40:00 | GOES-19 | MUTUM | MINAS GERAIS | Brasil | 3144003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 133.8 |
| 570532de-1b51-33e9-98d7-978fe7354492 | -15.2893 | -49.5035 | 2025-09-29 03:40:00 | GOES-19 | SANTA ISABEL | GOIÁS | Brasil | 5219357 | 52 | 33 | nan | nan | nan | Cerrado | 125.1 |
| ebf147a1-535a-32b4-b9f7-b4fc34cba8b2 | -2.5772 | -48.4146 | 2025-09-29 03:40:00 | GOES-19 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 74.3 |
| f7b00e3b-17f7-3483-a927-a442a1b34adb | -20.0482 | -41.351 | 2025-09-29 03:40:00 | GOES-19 | MUTUM | MINAS GERAIS | Brasil | 3144003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 79.4 |
| 6dabebbf-3f1d-3992-a4d1-f8d1bbd39f67 | -8.2851 | -45.4999 | 2025-09-29 03:40:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 174.2 |
| a01bcbfb-0768-3395-a82a-91f9f96e3f9b | -7.2211 | -44.8058 | 2025-09-29 03:40:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 71.5 |
| 7080289a-7efc-3d39-954b-b822b5188877 | -4.4011 | -44.0985 | 2025-09-29 03:40:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 52.8 |
| 2cfc25b5-43c0-342e-9255-cdfe2c1127dd | -15.2655 | -48.7544 | 2025-09-29 03:40:00 | GOES-19 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 61.1 |
| 1963a7e4-2e17-3b9c-8074-5ddb1f29a072 | -7.2214 | -44.783 | 2025-09-29 03:40:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 142.3 |
| e1aabe24-998b-304c-8a1d-460678826d74 | -8.2662 | -45.5018 | 2025-09-29 03:40:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 117.4 |
| 93f4609c-0adf-3c72-abcb-a31d36026329 | -6.22558 | -38.24442 | 2025-09-29 03:45:00 | NPP-375D | RAFAEL FERNANDES | RIO GRANDE DO NORTE | Brasil | 2410504 | 24 | 33 | nan | nan | nan | Caatinga | 1.2 |
| d7dfa2e6-a65f-34ae-807b-84046c4442cb | -5.4834 | -42.87833 | 2025-09-29 03:45:00 | NPP-375D | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 7.1 |
| d82bde04-72c9-3975-93fa-8c02722129c6 | -4.9376 | -45.59327 | 2025-09-29 03:45:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 8a749f3b-0130-3c7a-814f-717f98f42612 | -3.1002 | -47.0139 | 2025-09-29 03:45:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 16.4 |
| 30ef851d-52f4-397c-9afe-066ddd2e5c17 | -4.70727 | -41.97651 | 2025-09-29 03:45:00 | NPP-375D | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| dc965142-2484-310b-a564-06e7c77a3085 | -5.74403 | -42.81929 | 2025-09-29 03:45:00 | NPP-375D | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 5.4 |
| 59d8db06-7336-3e62-bb6b-c787162a33c1 | -4.7158 | -41.98304 | 2025-09-29 03:45:00 | NPP-375D | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 5.5 |
| 2e70d6ca-2e3b-382f-bb8e-1589785c733a | -5.39356 | -42.29259 | 2025-09-29 03:45:00 | NPP-375D | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 8fb9317d-52b3-399e-8334-d1e818bbbb6b | -4.71498 | -41.98796 | 2025-09-29 03:45:00 | NPP-375D | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 5.5 |
| 46f4d079-66c3-37aa-b36b-15c6d2449d6e | -5.68721 | -42.63879 | 2025-09-29 03:45:00 | NPP-375D | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 5.8 |
| f1557205-5883-3dd5-9921-778b4196a0bd | -5.38156 | -42.30595 | 2025-09-29 03:45:00 | NPP-375D | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 9463352e-0fa2-3613-b268-b9da8aa4a2e2 | -5.70661 | -42.63271 | 2025-09-29 03:45:00 | NPP-375D | MIGUEL LEÃO | PIAUÍ | Brasil | 2206308 | 22 | 33 | nan | nan | nan | Caatinga | 4.5 |
| 2fde9d33-3086-3d83-a201-7b7998ab0404 | -3.83636 | -40.33142 | 2025-09-29 03:45:00 | NPP-375D | FORQUILHA | CEARÁ | Brasil | 2304350 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 5d8c1dd7-5d16-3027-9765-4f044dae63d6 | -4.31519 | -48.08157 | 2025-09-29 03:45:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 206f3231-ff37-3e1e-8b2b-75b15733bdb5 | -4.29243 | -48.2747 | 2025-09-29 03:45:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| e40a3c80-ab32-3816-8d78-4e71ca27607c | -4.14486 | -40.007 | 2025-09-29 03:45:00 | NPP-375D | SANTA QUITÉRIA | CEARÁ | Brasil | 2312205 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| aaa3f129-5cbd-3936-bc35-f14c518d36e7 | -5.18992 | -43.76686 | 2025-09-29 03:45:00 | NPP-375D | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 44298da9-dcf9-3b7e-b6d8-fdb3df79b4d9 | -4.70563 | -41.98633 | 2025-09-29 03:45:00 | NPP-375D | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 19.5 |
| f0c3617a-b51a-3434-b52c-776ec558c88f | -4.97371 | -44.5069 | 2025-09-29 03:45:00 | NPP-375D | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 7f82c25c-b5ca-3132-9ddd-1faa6ff017c4 | -3.09823 | -47.02542 | 2025-09-29 03:45:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 23.0 |
| 7af5ba51-ecdb-3a83-a358-560257011e86 | -4.25341 | -46.95056 | 2025-09-29 03:45:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6d127735-9943-3da0-96eb-6b97be90d333 | -4.93829 | -45.58936 | 2025-09-29 03:45:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 049dfff3-ed56-3976-8764-52b3069b01a8 | -5.24663 | -45.35551 | 2025-09-29 03:45:00 | NPP-375D | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f99b22c5-bbb0-37ff-96c3-14e63157047f | -5.19585 | -43.76197 | 2025-09-29 03:45:00 | NPP-375D | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| d6a70919-bad3-36b2-9473-36d526edec24 | -5.71526 | -42.86988 | 2025-09-29 03:45:00 | NPP-375D | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 9.4 |
| fad7cceb-ad60-3f24-9d98-da581da047f0 | -4.40428 | -44.08002 | 2025-09-29 03:45:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 8d1f0010-c7e5-3b5f-8a9f-290ab43fd403 | -5.73984 | -42.66958 | 2025-09-29 03:45:00 | NPP-375D | AGRICOLÂNDIA | PIAUÍ | Brasil | 2200103 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| b4bd1a2d-57a5-351e-b5e2-25bade9e943e | -5.17273 | -41.26115 | 2025-09-29 03:45:00 | NPP-375D | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| a93b74ea-5eef-3164-8dfc-cdd8882b785d | -5.14742 | -37.7168 | 2025-09-29 03:45:00 | NPP-375D | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 160135ac-9832-37e6-ba6c-dbad6bf25fc4 | -5.74892 | -42.81998 | 2025-09-29 03:45:00 | NPP-375D | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 5.4 |
| 59b86b8d-4b6a-315f-bdda-c2042fddaa42 | -5.47267 | -42.88189 | 2025-09-29 03:45:00 | NPP-375D | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 7.7 |
| 72fa600c-15cb-32c2-bb95-39d6e4902061 | -4.7103 | -41.98715 | 2025-09-29 03:45:00 | NPP-375D | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 5.5 |
| 4e99f6b1-6809-32c7-992d-b84022de1b3b | -4.24596 | -46.95467 | 2025-09-29 03:45:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 6650684b-9a3d-3b0c-b3da-5656345d04df | -3.09353 | -47.01286 | 2025-09-29 03:45:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 5d78299f-1935-36b7-b3cb-6b53800ed1f7 | -5.3927 | -42.29762 | 2025-09-29 03:45:00 | NPP-375D | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 4aa3ed01-6742-3635-bd98-8e4c03fa8e6f | -3.10685 | -47.01506 | 2025-09-29 03:45:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 16.4 |
| 5968b35e-1e79-39e3-add9-600e68e97e27 | -3.83212 | -40.33072 | 2025-09-29 03:45:00 | NPP-375D | FORQUILHA | CEARÁ | Brasil | 2304350 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| fc20c1a8-6023-3c97-b7a5-a5fa7a4c329b | -4.71416 | -41.99287 | 2025-09-29 03:45:00 | NPP-375D | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 4.9 |
| 691388b8-c56b-37aa-af08-a42822b84f19 | -5.24451 | -45.36156 | 2025-09-29 03:45:00 | NPP-375D | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 9e00526c-0863-3755-97a5-b2d96a3bba37 | -5.72107 | -42.86533 | 2025-09-29 03:45:00 | NPP-375D | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 5.2 |
| 7e3b8223-41a2-3806-a76e-6985660a6ac7 | -5.14369 | -42.7628 | 2025-09-29 03:45:00 | NPP-375D | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| f49b079d-93ba-3ac0-8cc8-7f09bb511729 | -5.2985 | -41.23148 | 2025-09-29 03:45:00 | NPP-375D | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 8ee205b9-40a9-3641-9302-2b150073997f | -6.21565 | -38.23513 | 2025-09-29 03:45:00 | NPP-375D | RAFAEL FERNANDES | RIO GRANDE DO NORTE | Brasil | 2410504 | 24 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 8d20763f-1a79-3d92-81c2-85875fbaeebe | -4.75854 | -38.47864 | 2025-09-29 03:45:00 | NPP-375D | MORADA NOVA | CEARÁ | Brasil | 2308708 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |


[Clique aqui para ver as próximas entradas](README9.md)
