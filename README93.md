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

## Dados Diários - Página 93

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7e8ae913-4eb5-3415-833c-d8947262743f | -9.15902 | -63.17719 | 2024-10-30 05:10:00 | NOAA-20 | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a411143a-5e40-35f9-8e9d-a806b765d961 | -9.15498 | -63.17646 | 2024-10-30 05:10:00 | NOAA-20 | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 579a90e7-2603-3663-b343-dd100b65917f | -8.93603 | -63.72127 | 2024-10-30 05:10:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e8867219-a03c-3124-b06e-5f9fdf2c48b0 | -8.93535 | -63.7252 | 2024-10-30 05:10:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3e361bc5-5e16-3e39-9b85-6e1697d220b3 | -8.87661 | -63.7646 | 2024-10-30 05:10:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 10366d1f-8ab0-3e98-9fb0-1c0968d8f21d | -8.71329 | -63.31896 | 2024-10-30 05:10:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5b16bde3-8b04-3bf1-a547-fd749f356846 | -8.59503 | -63.86158 | 2024-10-30 05:10:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b6c40e92-d184-3b83-b55a-0836df8cd6c7 | -8.54233 | -63.45999 | 2024-10-30 05:10:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e1dc6e55-8529-3860-a5f8-83bdca235d3f | -8.23661 | -63.94889 | 2024-10-30 05:10:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9804cb34-9cd1-363b-aef3-5a2e0064ae48 | -7.88616 | -63.71919 | 2024-10-30 05:10:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 61d25ed4-a6bd-3ddb-a2dd-17e621a51146 | -9.7259 | -63.23167 | 2024-10-30 05:10:00 | NOAA-20 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6ae1d1fc-33b9-3618-a5d0-03d8dafbde51 | -9.72289 | -63.23143 | 2024-10-30 05:10:00 | NOAA-20 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 87440dc9-ea03-3e07-ae86-b02c54b7f840 | -9.55913 | -63.13673 | 2024-10-30 05:10:00 | NOAA-20 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f73f6761-142d-31ac-baa8-35d7fbbdb5b0 | -9.55853 | -63.14022 | 2024-10-30 05:10:00 | NOAA-20 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5eb04582-dabc-31ee-b28b-2a823567d652 | -9.55512 | -63.13602 | 2024-10-30 05:10:00 | NOAA-20 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| edfcf16c-98e2-381e-bdc0-d30ad1d30848 | -9.55452 | -63.13952 | 2024-10-30 05:10:00 | NOAA-20 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 74f11db0-40d3-36da-a2c7-6380441c4996 | -9.31837 | -64.25202 | 2024-10-30 05:10:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5fed8faa-93cc-3461-8027-7a00c4b5dc36 | -12.02671 | -64.04488 | 2024-10-30 05:10:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6012d2ff-b85a-3196-8000-6c2c4ae08852 | -9.3786 | -64.4544 | 2024-10-30 05:10:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| f332396c-cc29-315a-afee-9930f987ea8e | -9.37787 | -64.45866 | 2024-10-30 05:10:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| ab1b14b5-4079-3707-8c9d-81cbc8446298 | -9.00953 | -64.36671 | 2024-10-30 05:10:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 11430614-5aca-3bf4-a22b-df8a34ad07c7 | -8.8602 | -64.23704 | 2024-10-30 05:10:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| dbabd455-b0e8-3288-8001-e7a28f987a53 | -8.85946 | -64.24129 | 2024-10-30 05:10:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 26eb603e-bea4-3229-a835-681d54f7b400 | -8.85873 | -64.24554 | 2024-10-30 05:10:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 73c47a70-8461-3c27-a734-6b9c7503b173 | -8.82889 | -64.26198 | 2024-10-30 05:10:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 11614955-c1f8-3ac9-9f15-49eb775c1de1 | -9.96087 | -64.93938 | 2024-10-30 05:10:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1ecb6f84-86e0-3eb2-b365-41b805d8ed43 | -9.65045 | -65.74371 | 2024-10-30 05:10:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 22260162-93db-34ea-8660-75dae0d20b67 | -9.64569 | -65.74283 | 2024-10-30 05:10:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e712bd04-8460-38a0-835a-f87cd58bef3e | -9.51449 | -65.59947 | 2024-10-30 05:10:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f080f287-5e5d-324b-9d72-e57df37590e1 | -9.51352 | -65.59809 | 2024-10-30 05:10:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4b5786d9-ffbd-3463-a361-3df41f48ea6b | -9.50523 | -64.42706 | 2024-10-30 05:10:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9db1dbe2-4d17-3b26-bf08-58dcab806a12 | -9.50087 | -64.42625 | 2024-10-30 05:10:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9cf5b756-b0e5-3201-9221-e67930042cd9 | -9.49353 | -64.44267 | 2024-10-30 05:10:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 74b1886e-e989-3360-bb70-88c1e4599cca | -9.48992 | -64.43752 | 2024-10-30 05:10:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f81b4c48-a1ab-3055-a6b3-2ebacaf54e88 | -9.48917 | -64.44183 | 2024-10-30 05:10:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 295fbcf8-a192-38a6-99aa-d661bd3073c6 | -10.68892 | -65.00081 | 2024-10-30 05:10:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d3c502cf-c29d-3d97-8136-3e7a6822615e | -10.68447 | -65.00002 | 2024-10-30 05:10:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d7f5ce9f-0660-3497-afa8-75899113811b | -8.75307 | -44.71731 | 2024-10-30 05:10:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7588d463-df86-3569-bfb7-2fd0bbb20dee | -8.74618 | -44.71645 | 2024-10-30 05:10:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6a21a328-6d96-3fe1-af44-bd105cc1757d | -9.53794 | -66.65057 | 2024-10-30 05:10:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 705ef0e3-2f3a-3543-b33d-c3b46856eecf | -10.71289 | -44.92606 | 2024-10-30 05:10:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 13.6 |
| 97577383-024a-3d45-b4ba-0d668a3f8b00 | -10.71213 | -44.93253 | 2024-10-30 05:10:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 63013a4a-8a4c-3c75-96fe-afeab1cdaa9d | -10.71187 | -44.92577 | 2024-10-30 05:10:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 8.0 |
| c1c0825d-9982-3f72-a569-063fbbd8a3a9 | -10.71115 | -44.93228 | 2024-10-30 05:10:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 1d6c2b93-bd4f-3b7f-b286-f5873cbbe8a8 | -7.88482 | -46.9005 | 2024-10-30 05:10:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| fa1811d4-b612-33ed-ad2e-a495fc531fac | -7.88425 | -46.90488 | 2024-10-30 05:10:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| a0c1a3b8-4789-3f88-824e-f1128051add3 | -7.87178 | -46.90753 | 2024-10-30 05:10:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 9556d571-35d7-3e1c-9b23-bc175773267e | -7.87119 | -46.91204 | 2024-10-30 05:10:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 66eb20f7-42b5-3823-9f1b-0b951413f206 | -7.86945 | -46.89913 | 2024-10-30 05:10:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ff20517a-090d-3312-b355-13135fdfef0b | -7.86884 | -46.90354 | 2024-10-30 05:10:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f9c8f303-edf0-3132-919e-adcb1c2f8723 | -7.86823 | -46.90799 | 2024-10-30 05:10:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e5104d62-235d-388b-a2b4-6b7c380e082a | -7.86698 | -46.89775 | 2024-10-30 05:10:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| dc19ee21-4315-395c-8bdf-66671c24e7dd | -7.86641 | -46.90216 | 2024-10-30 05:10:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ebf3cca3-64e5-351d-b219-46e335291c0b | -7.86584 | -46.90658 | 2024-10-30 05:10:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 89d00c96-ef72-344d-a06b-c12d140056ef | -7.86349 | -46.89829 | 2024-10-30 05:10:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d1fb3fa8-b26b-38f2-bbcb-7f45fdeda847 | -7.8629 | -46.90267 | 2024-10-30 05:10:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0bd12dba-df29-3aa5-b04e-f5392b4428a3 | -7.86047 | -46.90128 | 2024-10-30 05:10:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c853986a-efe4-37fd-b5d6-d69540db0fbb | -9.57826 | -46.64561 | 2024-10-30 05:10:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 3f4a0f03-52d2-3a78-bacc-fb98c813ca5d | -11.78072 | -47.07325 | 2024-10-30 05:10:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 42010458-c127-3c5e-bfcb-43552cf13d5f | -11.78015 | -47.07818 | 2024-10-30 05:10:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 43c42326-a1f5-3ab4-a4e2-82c737d0b0fe | -11.77505 | -47.07833 | 2024-10-30 05:10:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2479b2ed-ba00-3cc7-9b94-6fdf543735e3 | -11.77394 | -47.07751 | 2024-10-30 05:10:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 6f3f8dd6-404d-3bf3-949d-1e3fd692e368 | -11.77385 | -47.08812 | 2024-10-30 05:10:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d1fa9df1-b7fc-3791-b8f3-58a8a90eaaeb | -11.77338 | -47.08246 | 2024-10-30 05:10:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 39a8f120-17d0-3cac-9b13-054a57e4bc93 | -11.77282 | -47.08733 | 2024-10-30 05:10:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 19390850-b066-3646-8225-4ec91f4810a9 | -11.76885 | -47.07763 | 2024-10-30 05:10:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7f52269b-fed4-307a-959e-21065afea705 | -11.76825 | -47.08255 | 2024-10-30 05:10:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 70bc91c2-f977-3df4-9daf-705d45cab7d5 | -11.76718 | -47.08169 | 2024-10-30 05:10:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 28f3e474-7078-3c3f-b153-ce3dfc308b6b | -9.47226 | -47.83442 | 2024-10-30 05:10:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 555ea64d-2c5f-3f5b-a0dd-4f94a2a7eda0 | -10.09245 | -48.47009 | 2024-10-30 05:10:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7c0e877d-cf0a-3875-be12-61c3b4cf220d | -10.09188 | -48.4693 | 2024-10-30 05:10:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cdf76a2c-3534-390c-be36-4234aa0a383a | -11.82168 | -48.76204 | 2024-10-30 05:10:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a5a1aa50-ca8a-304e-a23e-92df41e20c87 | -11.6549 | -48.79811 | 2024-10-30 05:10:00 | NOAA-20 | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 20b6ff4d-9141-3147-957f-4688717de3a1 | -11.6546 | -48.79829 | 2024-10-30 05:10:00 | NOAA-20 | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 7fffd107-b6c5-3450-b452-69c6d9133b48 | -11.65442 | -48.8019 | 2024-10-30 05:10:00 | NOAA-20 | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 26b53717-2d05-3b81-9056-a7d033c56d56 | -11.65415 | -48.80209 | 2024-10-30 05:10:00 | NOAA-20 | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 2d94a660-fb9d-3b7f-a0f9-616c41e59ba1 | -11.65394 | -48.80566 | 2024-10-30 05:10:00 | NOAA-20 | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 7a352ce8-8edc-308d-b9f1-f3391ad5f468 | -11.6537 | -48.80585 | 2024-10-30 05:10:00 | NOAA-20 | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 6694d472-8162-3bd8-bf59-84379e2ac065 | -11.64937 | -48.79729 | 2024-10-30 05:10:00 | NOAA-20 | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 35452d45-252f-30a9-839b-6fc2e5ba4cf8 | -11.64908 | -48.79745 | 2024-10-30 05:10:00 | NOAA-20 | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 29b187f4-e6f5-3f83-80ac-4fae4cc043c1 | -11.6489 | -48.80102 | 2024-10-30 05:10:00 | NOAA-20 | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 962cd80f-47a0-386d-8231-dc768c32a3f2 | -11.64863 | -48.80119 | 2024-10-30 05:10:00 | NOAA-20 | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 7ca0b1f3-9922-3571-9ed2-c0f31a783e64 | -11.64843 | -48.80476 | 2024-10-30 05:10:00 | NOAA-20 | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| d259cab8-43da-3755-bfb5-a4f347ac3135 | -9.0491 | -50.00725 | 2024-10-30 05:10:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 8fbdbf35-8a67-3d37-b2b2-6f3752c0bbc3 | -9.04832 | -50.0128 | 2024-10-30 05:10:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 90659ace-34f3-3c08-a623-47767311ff90 | -9.04577 | -50.00812 | 2024-10-30 05:10:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 46962b0d-c4a2-34cc-bd06-640f26f50e28 | -8.8463 | -49.85749 | 2024-10-30 05:10:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 3e135e44-7a1c-3d2c-8644-074dc3f9b496 | -8.84557 | -49.86308 | 2024-10-30 05:10:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 103ed590-e738-322a-8653-0e74d7790d5a | -8.8455 | -49.85614 | 2024-10-30 05:10:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 15.1 |
| c88385e3-ac7c-3e26-93d4-78ca19ed76b9 | -8.84472 | -49.86171 | 2024-10-30 05:10:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 15.1 |
| 53689f0d-0bb3-33e2-903b-e7ec40355833 | -8.84135 | -49.85674 | 2024-10-30 05:10:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| f15169f5-29a2-3545-9935-1bbbb2af0e28 | -8.84061 | -49.86234 | 2024-10-30 05:10:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 69fb2457-60c9-3860-aa54-6533d9bc8a7a | -8.83977 | -49.86098 | 2024-10-30 05:10:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6824db43-4625-37c1-beef-924e65f24d24 | -8.55061 | -49.70248 | 2024-10-30 05:10:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7ba5f547-bee4-3d69-a686-dda5a4b7da0e | -8.55009 | -49.70211 | 2024-10-30 05:10:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2a93ed81-388a-3300-8fad-c398c0f4f632 | -8.54599 | -49.69901 | 2024-10-30 05:10:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| c2435526-eca6-379f-b96f-12d28273a0e3 | -8.54561 | -49.70186 | 2024-10-30 05:10:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4f9834ae-9064-3110-b654-547a3c1d5fc2 | -8.54509 | -49.70152 | 2024-10-30 05:10:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2b0c6d83-e9a1-3d78-b349-8c8a637f1ad0 | -10.34257 | -49.65166 | 2024-10-30 05:10:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| ce68c6b5-6548-3145-b69a-f1eab63d8efa | -10.34216 | -49.65476 | 2024-10-30 05:10:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |


[Clique aqui para ver as próximas entradas](README94.md)
