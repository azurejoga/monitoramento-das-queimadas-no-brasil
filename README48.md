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

## Dados Diários - Página 48

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 22adf02c-c96b-3ef8-8740-4d0ea113f223 | -16.71226 | -49.3544 | 2025-08-27 04:27:00 | NOAA-20 | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 0.2 |
| 0c3b5e7e-2379-38f1-bca1-bbabec63b7ea | -12.95379 | -44.58023 | 2025-08-27 04:27:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 7cff3ce4-963c-3dca-92c6-1a75663f3e0c | -13.05843 | -46.29924 | 2025-08-27 04:27:00 | NOAA-20 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 016e90ee-53e5-3bab-8f47-5b083ba4577a | -19.17666 | -44.51526 | 2025-08-27 04:27:00 | NOAA-20 | PARAOPEBA | MINAS GERAIS | Brasil | 3147402 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e4a675db-701a-30e3-8309-a58b206181c1 | -13.06976 | -46.31585 | 2025-08-27 04:27:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 974e6074-28c6-3a1d-beef-4475ce101641 | -15.79319 | -41.47104 | 2025-08-27 04:27:00 | NOAA-20 | ÁGUAS VERMELHAS | MINAS GERAIS | Brasil | 3101003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| e0683a49-804c-39f0-9003-0354b7abb8ca | -15.61594 | -52.72668 | 2025-08-27 04:27:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 55839d4b-adfb-3fd3-a900-4ac791cd7b7c | -13.39972 | -46.88232 | 2025-08-27 04:27:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 47c92e43-c0a3-336a-aae4-e57f99b6c093 | -16.70522 | -50.41517 | 2025-08-27 04:27:00 | NOAA-20 | AURILÂNDIA | GOIÁS | Brasil | 5202601 | 52 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 56540d73-d5d2-32b8-aac0-ef2e5daef100 | -16.73957 | -48.53882 | 2025-08-27 04:27:00 | NOAA-20 | VIANÓPOLIS | GOIÁS | Brasil | 5222005 | 52 | 33 | nan | nan | nan | Cerrado | 6.1 |
| c2c5452f-96c5-356a-b92d-9a78a608f01e | -13.63513 | -46.87492 | 2025-08-27 04:27:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 42dfd03b-58f1-3b59-bb8b-9b160078dfe7 | -12.87982 | -48.10105 | 2025-08-27 04:27:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 1ad2dbe3-63ba-378d-bd3a-0b78d7c488e1 | -16.92299 | -49.43896 | 2025-08-27 04:27:00 | NOAA-20 | ARAGOIÂNIA | GOIÁS | Brasil | 5201801 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 32d7a0d4-c1c4-3157-8acb-3d10644aafa4 | -16.38038 | -48.81382 | 2025-08-27 04:27:00 | NOAA-20 | ANÁPOLIS | GOIÁS | Brasil | 5201108 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| c428c679-201f-3ff8-9cf0-03b6d999c731 | -13.50175 | -46.87962 | 2025-08-27 04:27:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2550080d-11e0-3f0b-b85f-1111a9dfd62b | -17.97234 | -48.04988 | 2025-08-27 04:27:00 | NOAA-20 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6985960a-4797-3c39-a0ea-9c983c2b58af | -13.47618 | -47.00119 | 2025-08-27 04:27:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8c993095-797a-32ba-9e0d-4063e00123c8 | -12.70413 | -48.18088 | 2025-08-27 04:27:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 28afd8ab-d651-3417-865b-bdfb3602b1e9 | -12.77831 | -48.12062 | 2025-08-27 04:27:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f3a1a64a-e832-3c51-bf81-6c5b11f8d84b | -13.07031 | -46.31221 | 2025-08-27 04:27:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f874bf6c-3152-3547-856a-1c19a5088aa1 | -12.73895 | -48.17582 | 2025-08-27 04:27:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 92313a32-c670-3ea6-a4b0-3fbf95804045 | -14.84297 | -49.2076 | 2025-08-27 04:27:00 | NOAA-20 | HIDROLINA | GOIÁS | Brasil | 5209804 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4cf1a008-816d-3f43-a549-6bf579046739 | -14.76961 | -59.71194 | 2025-08-27 04:27:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 37e9ce76-32cb-3c48-a8a3-aaac3411a56c | -13.39638 | -46.88178 | 2025-08-27 04:27:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 83a2a4e9-506c-3281-be78-d022375f0ad5 | -18.19773 | -45.56227 | 2025-08-27 04:27:00 | NOAA-20 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 92333cb5-eea2-39e6-9e12-6ae173411821 | -12.73951 | -48.17228 | 2025-08-27 04:27:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ee2ce972-423d-3b88-9752-74a4dc8971dc | -15.44867 | -59.10451 | 2025-08-27 04:27:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| eeba841b-7e5d-3eed-9509-85b27e491b48 | -13.67128 | -46.89905 | 2025-08-27 04:27:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bb19482b-0061-3120-8e13-d8827f0adf66 | -10.02476 | -59.35878 | 2025-08-27 04:27:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 16328bcf-d340-322f-96de-33e4dbd929b5 | -14.30422 | -53.0617 | 2025-08-27 04:27:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c55a40f4-d3c0-3702-a4be-788862ffb9b5 | -12.76159 | -48.18318 | 2025-08-27 04:27:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2efa8fb9-045a-31e4-a32e-9f1dacde28df | -13.07192 | -46.30841 | 2025-08-27 04:27:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c58209fe-33c9-3ca5-aba9-853d9cb0e32c | -13.44442 | -46.98529 | 2025-08-27 04:27:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9fc6f4b9-5adb-3900-8d60-a31c02fccb72 | -13.22267 | -44.55144 | 2025-08-27 04:27:00 | NOAA-20 | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 72c4b5c7-f761-38c4-8bc0-78f48614ba26 | -13.61261 | -48.19241 | 2025-08-27 04:27:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c2ef347f-46f1-391a-8cc4-981b9a7f3781 | -18.13993 | -44.45144 | 2025-08-27 04:27:00 | NOAA-20 | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 759150f9-e092-32f0-aada-89c84f12ce6d | -18.05928 | -45.1637 | 2025-08-27 04:27:00 | NOAA-20 | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bd2515e3-3136-3887-9521-1112c4d49f7e | -13.40584 | -46.88707 | 2025-08-27 04:27:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 73057b46-4ee0-3684-9f1d-75864cb05a57 | -14.27125 | -48.02104 | 2025-08-27 04:27:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 25f1eb95-492f-3494-adad-32c88d641c3b | -19.90981 | -41.58347 | 2025-08-27 04:27:00 | NOAA-20 | MUTUM | MINAS GERAIS | Brasil | 3144003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 63b6cdbf-8aa4-304d-8bac-ef76538ef9f0 | -15.62007 | -52.72 | 2025-08-27 04:27:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 21c51e19-296f-3c83-8d3d-f8fe99709602 | -12.76771 | -48.16601 | 2025-08-27 04:27:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 5e1fa5ee-ae59-35db-ae86-669f043697b6 | -18.37286 | -49.27037 | 2025-08-27 04:27:00 | NOAA-20 | ITUMBIARA | GOIÁS | Brasil | 5211503 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 3306d4cb-2c27-3a37-99d3-93d5e2f8328f | -12.76496 | -48.16191 | 2025-08-27 04:27:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 7910ba9a-ccbe-39da-bf55-e40039eae7fb | -15.10486 | -48.54892 | 2025-08-27 04:27:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0d4d05a6-f1c5-3b45-bd52-0426d4937d3a | -12.24484 | -45.05782 | 2025-08-27 04:27:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| eb895240-8da4-38a7-9af5-605d0fe01431 | -13.45443 | -46.98693 | 2025-08-27 04:27:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 881b361d-60f9-31e0-ae0c-d75e7c133569 | -16.77978 | -47.55639 | 2025-08-27 04:27:00 | NOAA-20 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 493a2bd9-3462-36de-8bc7-3bee64302ea8 | -15.09711 | -48.55493 | 2025-08-27 04:27:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 8814faa9-9854-3b1b-af01-d58af2a1b4ee | -13.60609 | -48.14778 | 2025-08-27 04:27:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 176e3a88-b19d-3d00-a1bd-a28497e217d7 | -19.52901 | -42.58579 | 2025-08-27 04:27:00 | NOAA-20 | CORONEL FABRICIANO | MINAS GERAIS | Brasil | 3119401 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 1c7adfa4-ad57-3dc9-b775-157e7432e6a0 | -12.78111 | -48.10296 | 2025-08-27 04:27:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| af236d5f-63ae-3e63-a3e4-4d48e2d95aa3 | -13.42555 | -46.99684 | 2025-08-27 04:27:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 490a267d-4d8c-37a2-8616-422e11e0cb0c | -12.75934 | -48.19736 | 2025-08-27 04:27:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 2f083baa-e99c-3a0b-bcd5-bd13952bd23d | -13.06856 | -46.30094 | 2025-08-27 04:27:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 517d679b-d4a8-3421-a92b-54f26e6e2240 | -12.70975 | -48.14563 | 2025-08-27 04:27:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6683b999-2b60-3a6b-8f0c-58a7a63f9d5c | -13.8421 | -46.69413 | 2025-08-27 04:27:00 | NOAA-20 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a53a2681-374f-3583-b79b-83df74c6363f | -15.61919 | -52.72488 | 2025-08-27 04:27:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 08e1eeab-032a-3612-9349-471ff0ec2718 | -13.49391 | -46.8637 | 2025-08-27 04:27:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5dceddd1-506a-3664-80b6-376143e7001c | -14.48473 | -52.05707 | 2025-08-27 04:27:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f81bf599-2f1f-3ec8-8b23-1d677bf36301 | -19.46224 | -44.18631 | 2025-08-27 04:27:00 | NOAA-20 | SETE LAGOAS | MINAS GERAIS | Brasil | 3167202 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9161cffa-edcf-34ca-80ce-28269b0d582e | -15.63938 | -52.74383 | 2025-08-27 04:27:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c5680dbe-ea3f-3df8-941e-b7b329ac5d8d | -12.79586 | -48.11616 | 2025-08-27 04:27:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 8641c3f6-f8e5-3c5c-ab04-1abff3eb80ec | -15.65167 | -52.74098 | 2025-08-27 04:27:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ba92d80a-8fbd-3a37-860f-2b83434a65f6 | -15.0386 | -48.68785 | 2025-08-27 04:27:00 | NOAA-20 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c0af8efe-b853-3dc3-acb0-8f99728f8730 | -14.32279 | -53.26556 | 2025-08-27 04:27:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 2fa73257-ed5f-3c4f-a25a-df0abf267f24 | -15.61539 | -52.72421 | 2025-08-27 04:27:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d584a85d-06b2-3935-b519-148f1ce35a3b | -17.77528 | -44.48463 | 2025-08-27 04:27:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| bd612b2c-82bc-347c-98be-d25535f40068 | -12.73839 | -48.17937 | 2025-08-27 04:27:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 98a92a09-0656-318d-b281-6217ac88aad5 | -13.61368 | -48.20713 | 2025-08-27 04:27:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 74ed081d-7e8c-3ac0-85c0-b34a65f9b080 | -12.9568 | -44.58498 | 2025-08-27 04:27:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6eb42997-35ec-3323-beb0-3bca21f96e2f | -14.90745 | -49.60799 | 2025-08-27 04:27:00 | NOAA-20 | ITAPACI | GOIÁS | Brasil | 5210901 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 5754886a-5bb9-3353-9a68-73401b255294 | -16.37098 | -43.03574 | 2025-08-27 04:27:00 | NOAA-20 | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 69e9f665-e83f-3c54-8302-167c77bb8ed2 | -13.07085 | -46.30865 | 2025-08-27 04:27:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 72e65411-6b77-3a9e-80a2-e714bf9ff457 | -12.7778 | -48.10242 | 2025-08-27 04:27:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7325780a-410f-3fd6-a738-a8e9609a4450 | -13.42253 | -46.85969 | 2025-08-27 04:27:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 14.0 |
| 4526d9ca-c233-3ed5-86dc-1af044ce4672 | -14.1295 | -45.4011 | 2025-08-27 04:27:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 25a0b4fd-1e06-3b70-905b-38b85bac7c63 | -12.39804 | -46.50645 | 2025-08-27 04:27:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| adb7969a-8afe-39b5-98b2-d433ee9093fb | -13.06751 | -46.33054 | 2025-08-27 04:27:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 916449b1-627e-3079-adce-5b7e65f50c5f | -18.93428 | -46.96304 | 2025-08-27 04:27:00 | NOAA-20 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9e6f838d-6de2-3619-b9c4-8db723b01e7e | -12.74333 | -48.19107 | 2025-08-27 04:27:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cf74952b-c9ef-33f0-abc8-cf4229f1403c | -17.55074 | -46.61372 | 2025-08-27 04:27:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1d5b1acb-594f-32b6-ae2e-424011e30b8e | -12.0051 | -50.6241 | 2025-08-27 04:27:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7ab1329f-cb29-32d7-b016-793b5ad28ef5 | -13.5051 | -46.88014 | 2025-08-27 04:27:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e896b8c8-dc50-3aa0-a9bf-96184cb80121 | -18.19469 | -45.55719 | 2025-08-27 04:27:00 | NOAA-20 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7a6b1003-3945-342e-ac91-eed4d193a1da | -15.08669 | -48.53483 | 2025-08-27 04:27:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9ca6fe22-7f09-36d2-aaeb-d6cc027e24bb | -13.42504 | -47.02246 | 2025-08-27 04:27:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 220c8a25-7468-32ef-8b2a-9fcc827a2ea0 | -13.16726 | -45.29257 | 2025-08-27 04:27:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e41653e9-9792-3ad1-af27-c0f76d782873 | -16.83928 | -43.85139 | 2025-08-27 04:27:00 | NOAA-20 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 24dbdc6a-418e-370b-8209-9556e58565e7 | -13.06695 | -46.33421 | 2025-08-27 04:27:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 0aa246aa-f60a-38bd-b166-90cccec3568b | -10.59622 | -54.89262 | 2025-08-27 04:27:00 | NOAA-20 | TERRA NOVA DO NORTE | MATO GROSSO | Brasil | 5108055 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 984bebf4-fb02-3df1-a30d-bb6853befb6b | -17.97512 | -48.05408 | 2025-08-27 04:27:00 | NOAA-20 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 82f1eed5-737d-3f8f-b0b3-cfcb4631c405 | -13.64792 | -45.70504 | 2025-08-27 04:27:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| be8d30d7-ce73-3aaa-bbee-e0533ad93b2e | -16.70925 | -50.41195 | 2025-08-27 04:27:00 | NOAA-20 | AURILÂNDIA | GOIÁS | Brasil | 5202601 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bce285f3-2efb-3d48-bd0c-9fe48fdefe35 | -17.75617 | -50.49349 | 2025-08-27 04:27:00 | NOAA-20 | SANTA HELENA DE GOIÁS | GOIÁS | Brasil | 5219308 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 0eb5ad69-d811-3142-8ef0-9c48283ecfb5 | -13.44386 | -46.98893 | 2025-08-27 04:27:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 331d25c8-4577-3677-84e9-ee1d547ee2c9 | -13.62529 | -48.19812 | 2025-08-27 04:27:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c3f143ce-c127-3ece-a2bd-08dae2b9662f | -17.97569 | -48.05043 | 2025-08-27 04:27:00 | NOAA-20 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 44f0c725-202f-3ea1-a109-a73a7252e461 | -16.73683 | -48.53466 | 2025-08-27 04:27:00 | NOAA-20 | VIANÓPOLIS | GOIÁS | Brasil | 5222005 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| e95d7b57-56b5-3063-b072-b1ccd1bff89a | -12.76434 | -48.18729 | 2025-08-27 04:27:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |


[Clique aqui para ver as próximas entradas](README49.md)
