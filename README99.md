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

## Dados Diários - Página 99

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c4d793ab-0f5d-3e12-81f7-ce0b7138dc5d | -16.73005 | -55.55006 | 2024-09-27 04:42:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.9 |
| e681d0e7-a8b3-358e-b948-ded5c791f52b | -16.72794 | -55.54029 | 2024-09-27 04:42:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| b576c17f-8b20-3124-af3e-ddba98249167 | -16.72715 | -55.54483 | 2024-09-27 04:42:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 08700ff2-bec2-3979-b011-e1296a9a1092 | -13.13042 | -56.42186 | 2024-09-27 04:42:00 | NOAA-21 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c73ce977-5dca-3764-b382-0c9f80de1665 | -13.12632 | -56.42115 | 2024-09-27 04:42:00 | NOAA-21 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 165f7a36-181d-3d6f-9805-24400db1cca1 | -12.80263 | -56.19267 | 2024-09-27 04:42:00 | NOAA-21 | LUCAS DO RIO VERDE | MATO GROSSO | Brasil | 5105259 | 51 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 150539f6-0cbf-39bc-8796-cd97d44be36c | -12.80199 | -56.19636 | 2024-09-27 04:42:00 | NOAA-21 | LUCAS DO RIO VERDE | MATO GROSSO | Brasil | 5105259 | 51 | 33 | nan | nan | nan | Cerrado | 6.4 |
| f00c1773-5fb8-3059-b88c-64e162f20b46 | -12.79857 | -56.19193 | 2024-09-27 04:42:00 | NOAA-21 | LUCAS DO RIO VERDE | MATO GROSSO | Brasil | 5105259 | 51 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 42f9c451-4fbe-392d-b936-d15ee7fd43ac | -13.96102 | -56.16303 | 2024-09-27 04:42:00 | NOAA-21 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 22baffc7-843e-3975-9990-a664c5ede066 | -13.94836 | -56.14207 | 2024-09-27 04:42:00 | NOAA-21 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 010b8e32-5a42-3192-8b50-0ed1638693ff | -13.94439 | -56.14134 | 2024-09-27 04:42:00 | NOAA-21 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0df5e024-ee96-33cf-8caa-eaeb38b50899 | -13.82119 | -56.38149 | 2024-09-27 04:42:00 | NOAA-21 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 219b4830-65e0-395f-958e-35ddde29b7e0 | -16.48893 | -57.37752 | 2024-09-27 04:42:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| ecacc3bc-3ef6-346c-8c17-95ebe79a0154 | -16.87503 | -57.7205 | 2024-09-27 04:42:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 8348346d-5bd3-3b4b-8783-ce1163099eaf | -16.87012 | -57.72366 | 2024-09-27 04:42:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| fd4949f6-b210-318f-83d9-92470ff00777 | -16.85955 | -57.73398 | 2024-09-27 04:42:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 03f39db6-fd47-36af-8b1a-df7b3cf7be66 | -16.85537 | -57.73314 | 2024-09-27 04:42:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| b600f12a-7a16-3c30-8893-6e38cd7c139f | -16.84135 | -57.73864 | 2024-09-27 04:42:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.7 |
| 072fd234-99fe-3660-8ca0-8f89bdb66373 | -16.83717 | -57.7378 | 2024-09-27 04:42:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.7 |
| 9aa75763-7db5-3afc-8537-414c58af1ea7 | -14.04884 | -57.9213 | 2024-09-27 04:42:00 | NOAA-21 | CAMPO NOVO DO PARECIS | MATO GROSSO | Brasil | 5102637 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 740f5eb6-8111-37c2-87e9-d8a67cce92ef | -14.04249 | -57.90619 | 2024-09-27 04:42:00 | NOAA-21 | CAMPO NOVO DO PARECIS | MATO GROSSO | Brasil | 5102637 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 0e29d9aa-245e-3d55-94f5-806a3e5baa91 | -14.04165 | -57.91065 | 2024-09-27 04:42:00 | NOAA-21 | CAMPO NOVO DO PARECIS | MATO GROSSO | Brasil | 5102637 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 568c77b9-43b6-37af-b6f8-af5f36efdefa | -14.03979 | -57.90317 | 2024-09-27 04:42:00 | NOAA-21 | CAMPO NOVO DO PARECIS | MATO GROSSO | Brasil | 5102637 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 78bf3207-23aa-30c0-9357-625e4c61f921 | -14.03898 | -57.90764 | 2024-09-27 04:42:00 | NOAA-21 | CAMPO NOVO DO PARECIS | MATO GROSSO | Brasil | 5102637 | 51 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 24f56b65-a5f8-3820-b056-8100d8566589 | -14.03805 | -57.90535 | 2024-09-27 04:42:00 | NOAA-21 | CAMPO NOVO DO PARECIS | MATO GROSSO | Brasil | 5102637 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| b1d0733b-8991-3a16-ab8c-ea6bbf883fba | -14.0372 | -57.90981 | 2024-09-27 04:42:00 | NOAA-21 | CAMPO NOVO DO PARECIS | MATO GROSSO | Brasil | 5102637 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| aaa5e195-0802-37d4-a078-8ad700c6cccb | -14.03536 | -57.90232 | 2024-09-27 04:42:00 | NOAA-21 | CAMPO NOVO DO PARECIS | MATO GROSSO | Brasil | 5102637 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4d0b38c5-72d2-39f4-9209-2356401ed556 | -14.03455 | -57.90677 | 2024-09-27 04:42:00 | NOAA-21 | CAMPO NOVO DO PARECIS | MATO GROSSO | Brasil | 5102637 | 51 | 33 | nan | nan | nan | Cerrado | 5.1 |
| b40a0f1b-2ba4-3a3c-a1e1-b6798d0bacb3 | -14.03445 | -57.90006 | 2024-09-27 04:42:00 | NOAA-21 | CAMPO NOVO DO PARECIS | MATO GROSSO | Brasil | 5102637 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 65eded85-55f8-302c-93f4-b610c6b7a51b | -14.03361 | -57.9045 | 2024-09-27 04:42:00 | NOAA-21 | CAMPO NOVO DO PARECIS | MATO GROSSO | Brasil | 5102637 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| f2fb817d-04d6-3fc6-aa66-d02ffbfc99bf | -15.31565 | -58.16657 | 2024-09-27 04:42:00 | NOAA-21 | RIO BRANCO | MATO GROSSO | Brasil | 5107206 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 251a0a64-d6b1-3326-ae95-75577a6fefe6 | -12.01068 | -61.22366 | 2024-09-27 04:42:00 | NOAA-21 | PARECIS | RONDÔNIA | Brasil | 1101450 | 11 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 0d8aa635-8bf8-3e34-861e-d34d106556f8 | -17.42242 | -39.35088 | 2024-09-27 04:42:00 | NOAA-21 | ALCOBAÇA | BAHIA | Brasil | 2900801 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| e6b54d1f-447d-370a-ac31-98a9739ac4c0 | -17.42188 | -39.35641 | 2024-09-27 04:42:00 | NOAA-21 | ALCOBAÇA | BAHIA | Brasil | 2900801 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 0eb207d0-9cbe-3330-b906-3793af6a4f9a | -18.17444 | -39.82264 | 2024-09-27 04:42:00 | NOAA-21 | MUCURI | BAHIA | Brasil | 2922003 | 29 | 33 | nan | nan | nan | Mata Atlântica | 10.9 |
| 8721891c-4305-3b63-8d7b-6d4ec57e2f13 | -18.16808 | -39.82186 | 2024-09-27 04:42:00 | NOAA-21 | MUCURI | BAHIA | Brasil | 2922003 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 0e6f6157-fff0-3be7-9c63-0d0012af5a57 | -17.06284 | -41.14902 | 2024-09-27 04:42:00 | NOAA-21 | ÁGUAS FORMOSAS | MINAS GERAIS | Brasil | 3100906 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| 8e7b5ca9-67f7-3f67-84f5-cf9433f70b47 | -17.06332 | -41.14436 | 2024-09-27 04:42:00 | NOAA-21 | ÁGUAS FORMOSAS | MINAS GERAIS | Brasil | 3100906 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| 10235b7d-e156-3f96-8130-7b612e4ed357 | -18.9905 | -41.04306 | 2024-09-27 04:42:00 | NOAA-21 | CUPARAQUE | MINAS GERAIS | Brasil | 3120839 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| ef8eaab7-2fb4-398e-bb0d-4b666d86824e | -19.15234 | -41.37652 | 2024-09-27 04:42:00 | NOAA-21 | CONSELHEIRO PENA | MINAS GERAIS | Brasil | 3118403 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| d638df43-e1bd-337a-b54f-b6c8612b9527 | -18.99635 | -41.04498 | 2024-09-27 04:42:00 | NOAA-21 | CUPARAQUE | MINAS GERAIS | Brasil | 3120839 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 7fbac7ce-35d4-3d9d-888c-d553b134a397 | -19.15192 | -41.38095 | 2024-09-27 04:42:00 | NOAA-21 | CONSELHEIRO PENA | MINAS GERAIS | Brasil | 3118403 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 9cd7716d-6812-3c51-84c3-5b61e2b1e8fc | -19.15736 | -41.38597 | 2024-09-27 04:42:00 | NOAA-21 | CONSELHEIRO PENA | MINAS GERAIS | Brasil | 3118403 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.5 |
| a3a8e0ab-31ec-3e06-9e7b-0ab6bd580a3e | -19.14647 | -41.37603 | 2024-09-27 04:42:00 | NOAA-21 | CONSELHEIRO PENA | MINAS GERAIS | Brasil | 3118403 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 1dc89885-93ed-3c19-9b6c-405542876fdc | -18.5856 | -41.33995 | 2024-09-27 04:42:00 | NOAA-21 | MENDES PIMENTEL | MINAS GERAIS | Brasil | 3141504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 28a70901-1a15-3df5-a7e3-0d66922ea6dd | -18.57933 | -41.34388 | 2024-09-27 04:42:00 | NOAA-21 | MENDES PIMENTEL | MINAS GERAIS | Brasil | 3141504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 3b56829e-30d4-37fa-a742-916b54a23601 | -20.5963 | -41.23158 | 2024-09-27 04:42:00 | NOAA-21 | CASTELO | ESPÍRITO SANTO | Brasil | 3201407 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| db737c9d-31d1-3a5a-8131-2ca41baefbac | -20.59576 | -41.23803 | 2024-09-27 04:42:00 | NOAA-21 | CASTELO | ESPÍRITO SANTO | Brasil | 3201407 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 0d81f8fe-b55d-33a6-af5e-b4bd2f795c16 | -20.59379 | -41.23345 | 2024-09-27 04:42:00 | NOAA-21 | CASTELO | ESPÍRITO SANTO | Brasil | 3201407 | 32 | 33 | nan | nan | nan | Mata Atlântica | 4.5 |
| 74d250e7-928c-3476-b9f7-48facd37785f | -20.64623 | -41.07561 | 2024-09-27 04:42:00 | NOAA-21 | CACHOEIRO DE ITAPEMIRIM | ESPÍRITO SANTO | Brasil | 3201209 | 32 | 33 | nan | nan | nan | Mata Atlântica | 4.8 |
| d33e403d-d9ab-34f2-a6ea-8a16deaf0d6b | -20.64473 | -41.07782 | 2024-09-27 04:42:00 | NOAA-21 | CACHOEIRO DE ITAPEMIRIM | ESPÍRITO SANTO | Brasil | 3201209 | 32 | 33 | nan | nan | nan | Mata Atlântica | 5.3 |
| 1727874c-804e-3f55-9989-58203ed40931 | -20.6229 | -41.20428 | 2024-09-27 04:42:00 | NOAA-21 | CASTELO | ESPÍRITO SANTO | Brasil | 3201407 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 6c9bac88-64b8-39bf-b765-fae092d93245 | -20.51906 | -41.96748 | 2024-09-27 04:42:00 | NOAA-21 | CAPARAÓ | MINAS GERAIS | Brasil | 3112109 | 31 | 33 | nan | nan | nan | Mata Atlântica | 23.6 |
| ba81b099-3f45-3678-91ac-53e6d376cd61 | -20.51868 | -41.97142 | 2024-09-27 04:42:00 | NOAA-21 | CAPARAÓ | MINAS GERAIS | Brasil | 3112109 | 31 | 33 | nan | nan | nan | Mata Atlântica | 37.2 |
| cb8ac5b0-3b10-374a-a579-4e0edbb07ad8 | -20.51293 | -41.97104 | 2024-09-27 04:42:00 | NOAA-21 | CAPARAÓ | MINAS GERAIS | Brasil | 3112109 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| a4a6407b-c7d7-3d11-928f-968ce3228f5c | -20.51217 | -41.97902 | 2024-09-27 04:42:00 | NOAA-21 | CAPARAÓ | MINAS GERAIS | Brasil | 3112109 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| a151af5e-c706-3a71-8884-0a6da892f874 | -20.64658 | -41.07155 | 2024-09-27 04:42:00 | NOAA-21 | CACHOEIRO DE ITAPEMIRIM | ESPÍRITO SANTO | Brasil | 3201209 | 32 | 33 | nan | nan | nan | Mata Atlântica | 4.8 |
| 8cdcee46-4e6d-34c8-b568-35c8622bd720 | -20.59326 | -41.23926 | 2024-09-27 04:42:00 | NOAA-21 | CASTELO | ESPÍRITO SANTO | Brasil | 3201407 | 32 | 33 | nan | nan | nan | Mata Atlântica | 4.5 |
| af421761-67d2-395e-93bb-c3f4b6a07871 | -20.51366 | -41.96343 | 2024-09-27 04:42:00 | NOAA-21 | CAPARAÓ | MINAS GERAIS | Brasil | 3112109 | 31 | 33 | nan | nan | nan | Mata Atlântica | 15.8 |
| 69bb7203-36e6-3a24-bd6b-53b580c2435d | -20.51255 | -41.97501 | 2024-09-27 04:42:00 | NOAA-21 | CAPARAÓ | MINAS GERAIS | Brasil | 3112109 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| b1aa51d4-91f9-33de-bbb2-a7c75084a260 | -20.40933 | -41.88484 | 2024-09-27 04:42:00 | NOAA-21 | ALTO JEQUITIBÁ | MINAS GERAIS | Brasil | 3153509 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 79dcc111-9767-313f-a006-07d673f146a6 | -20.65248 | -41.07398 | 2024-09-27 04:42:00 | NOAA-21 | CACHOEIRO DE ITAPEMIRIM | ESPÍRITO SANTO | Brasil | 3201209 | 32 | 33 | nan | nan | nan | Mata Atlântica | 4.8 |
| 7fbb9c99-2da4-373f-8a7c-bf62177da7fa | -20.64513 | -41.07349 | 2024-09-27 04:42:00 | NOAA-21 | CACHOEIRO DE ITAPEMIRIM | ESPÍRITO SANTO | Brasil | 3201209 | 32 | 33 | nan | nan | nan | Mata Atlântica | 5.3 |
| 66018e35-bc17-30b6-9ae2-7c9b82e03667 | -20.54721 | -40.93185 | 2024-09-27 04:42:00 | NOAA-21 | ALFREDO CHAVES | ESPÍRITO SANTO | Brasil | 3200300 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| c1896f2a-825c-3fe5-b91b-38c758a9e90e | -20.51944 | -41.96357 | 2024-09-27 04:42:00 | NOAA-21 | CAPARAÓ | MINAS GERAIS | Brasil | 3112109 | 31 | 33 | nan | nan | nan | Mata Atlântica | 23.6 |
| e001f340-7c9e-31d3-ad77-88729b8019ae | -20.51329 | -41.96727 | 2024-09-27 04:42:00 | NOAA-21 | CAPARAÓ | MINAS GERAIS | Brasil | 3112109 | 31 | 33 | nan | nan | nan | Mata Atlântica | 15.8 |
| 9e6a28b5-5510-351f-8307-256173ead295 | -20.40963 | -41.88169 | 2024-09-27 04:42:00 | NOAA-21 | ALTO JEQUITIBÁ | MINAS GERAIS | Brasil | 3153509 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| e613bf2f-94c8-3982-8b38-676509920bf2 | -17.99931 | -42.30611 | 2024-09-27 04:42:00 | NOAA-21 | ÁGUA BOA | MINAS GERAIS | Brasil | 3100609 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 0dfec5e8-b57f-39a4-b922-fc365d3d73d4 | -17.99421 | -42.30215 | 2024-09-27 04:42:00 | NOAA-21 | ÁGUA BOA | MINAS GERAIS | Brasil | 3100609 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 4eaf4b35-071e-3162-adc7-77c9631e7113 | -16.87368 | -42.14838 | 2024-09-27 04:42:00 | NOAA-21 | ARAÇUAÍ | MINAS GERAIS | Brasil | 3103405 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 2320148b-e5e5-3997-a229-4b10af8dd42f | -19.38679 | -42.57254 | 2024-09-27 04:42:00 | NOAA-21 | SANTANA DO PARAÍSO | MINAS GERAIS | Brasil | 3158953 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| 5be77460-c1a6-3de7-8df6-cd2a180bba9d | -19.38569 | -42.5834 | 2024-09-27 04:42:00 | NOAA-21 | SANTANA DO PARAÍSO | MINAS GERAIS | Brasil | 3158953 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.9 |
| 3b6f6f89-65a4-3a42-b776-8811d0a05bcd | -19.38516 | -42.5886 | 2024-09-27 04:42:00 | NOAA-21 | SANTANA DO PARAÍSO | MINAS GERAIS | Brasil | 3158953 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 6bdccadf-d6c6-38ac-9a20-618d28f79245 | -19.36924 | -42.58287 | 2024-09-27 04:42:00 | NOAA-21 | SANTANA DO PARAÍSO | MINAS GERAIS | Brasil | 3158953 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.4 |
| 65c15ed9-7e7b-3516-9064-baba24db2d1f | -18.69817 | -42.09081 | 2024-09-27 04:42:00 | NOAA-21 | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 87c9c0c2-daec-3827-8286-a27ba0da5beb | -18.50049 | -42.22076 | 2024-09-27 04:42:00 | NOAA-21 | NACIP RAYDAN | MINAS GERAIS | Brasil | 3144201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| b95365a2-78d3-3abc-ac35-e724dadfde11 | -18.50045 | -42.2171 | 2024-09-27 04:42:00 | NOAA-21 | NACIP RAYDAN | MINAS GERAIS | Brasil | 3144201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| b8dabfbb-b69b-3efd-897b-8c7e75f4dc87 | -18.49449 | -42.22078 | 2024-09-27 04:42:00 | NOAA-21 | NACIP RAYDAN | MINAS GERAIS | Brasil | 3144201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| b972c861-88bd-3be1-aecb-e68f5ec4aa2a | -18.49065 | -42.20435 | 2024-09-27 04:42:00 | NOAA-21 | NACIP RAYDAN | MINAS GERAIS | Brasil | 3144201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| f6bf1ee1-4136-3396-84f2-97f4b1f0f2e1 | -18.48515 | -42.20352 | 2024-09-27 04:42:00 | NOAA-21 | NACIP RAYDAN | MINAS GERAIS | Brasil | 3144201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.2 |
| 5dd3e76d-1ee0-3ef4-8812-e51d01f59fc1 | -18.70449 | -42.08414 | 2024-09-27 04:42:00 | NOAA-21 | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 5fa9641d-f4a3-33b0-9a8a-8001d3a5d289 | -18.70406 | -42.08837 | 2024-09-27 04:42:00 | NOAA-21 | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 9b0676dc-2394-3d05-a5bb-92adc88731dc | -19.38725 | -42.56804 | 2024-09-27 04:42:00 | NOAA-21 | SANTANA DO PARAÍSO | MINAS GERAIS | Brasil | 3158953 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| a666de8d-dce4-34a3-af16-532c1f13a772 | -19.37008 | -42.57449 | 2024-09-27 04:42:00 | NOAA-21 | SANTANA DO PARAÍSO | MINAS GERAIS | Brasil | 3158953 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| cfbd4b05-2a56-3c75-b10b-79b3515d5dcd | -19.22593 | -42.34094 | 2024-09-27 04:42:00 | NOAA-21 | NAQUE | MINAS GERAIS | Brasil | 3144359 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 801d1f08-fa1e-3f03-b58e-51a6759ac646 | -19.39214 | -42.57412 | 2024-09-27 04:42:00 | NOAA-21 | SANTANA DO PARAÍSO | MINAS GERAIS | Brasil | 3158953 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| 6c19c588-7847-350e-b353-3b11a6cedf9c | -19.38472 | -42.59286 | 2024-09-27 04:42:00 | NOAA-21 | SANTANA DO PARAÍSO | MINAS GERAIS | Brasil | 3158953 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 36d22a31-60e6-3652-b269-7cf315550173 | -19.37669 | -42.56354 | 2024-09-27 04:42:00 | NOAA-21 | SANTANA DO PARAÍSO | MINAS GERAIS | Brasil | 3158953 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 60c5107d-ce51-3605-9952-7070f8616559 | -19.37616 | -42.56882 | 2024-09-27 04:42:00 | NOAA-21 | SANTANA DO PARAÍSO | MINAS GERAIS | Brasil | 3158953 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| cf12cb21-843c-3ec0-8ceb-7fe0f130d327 | -19.22586 | -42.34118 | 2024-09-27 04:42:00 | NOAA-21 | NAQUE | MINAS GERAIS | Brasil | 3144359 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 7532a85d-6f51-31a2-8079-f6150ac9f7d0 | -19.39796 | -42.57114 | 2024-09-27 04:42:00 | NOAA-21 | IPATINGA | MINAS GERAIS | Brasil | 3131307 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 9b20c641-6096-39f2-af94-47992ce68188 | -19.39751 | -42.57547 | 2024-09-27 04:42:00 | NOAA-21 | SANTANA DO PARAÍSO | MINAS GERAIS | Brasil | 3158953 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 9813ac05-9fd0-3a8f-b33e-5c5fb7512288 | -19.39259 | -42.56973 | 2024-09-27 04:42:00 | NOAA-21 | SANTANA DO PARAÍSO | MINAS GERAIS | Brasil | 3158953 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| 02f727bc-d4d9-3829-b36e-bfbe6760b591 | -19.38626 | -42.57772 | 2024-09-27 04:42:00 | NOAA-21 | SANTANA DO PARAÍSO | MINAS GERAIS | Brasil | 3158953 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.9 |
| 9266bc0d-bcaa-3370-93b2-ff95071a5f80 | -19.3822 | -42.56356 | 2024-09-27 04:42:00 | NOAA-21 | SANTANA DO PARAÍSO | MINAS GERAIS | Brasil | 3158953 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| d387a410-ed3a-323a-9e2f-33902fc0f78e | -19.37957 | -42.58948 | 2024-09-27 04:42:00 | NOAA-21 | SANTANA DO PARAÍSO | MINAS GERAIS | Brasil | 3158953 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 7fcce43e-e886-3991-a764-ab70f97746f9 | -20.15623 | -43.51112 | 2024-09-27 04:42:00 | NOAA-21 | MARIANA | MINAS GERAIS | Brasil | 3140001 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| 704e9bf8-5e15-33bb-a660-d61977b37ebf | -19.37918 | -42.59336 | 2024-09-27 04:42:00 | NOAA-21 | SANTANA DO PARAÍSO | MINAS GERAIS | Brasil | 3158953 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 9dda8d60-2c98-36e5-8faa-f2e2ee216443 | -19.37459 | -42.58437 | 2024-09-27 04:42:00 | NOAA-21 | SANTANA DO PARAÍSO | MINAS GERAIS | Brasil | 3158953 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.4 |
| c02b232e-efdb-3f41-8f04-c8d122c63171 | -19.37058 | -42.56963 | 2024-09-27 04:42:00 | NOAA-21 | SANTANA DO PARAÍSO | MINAS GERAIS | Brasil | 3158953 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |


[Clique aqui para ver as próximas entradas](README100.md)
