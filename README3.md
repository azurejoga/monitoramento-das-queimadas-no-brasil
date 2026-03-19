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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 47a1a41d-4416-3848-ac24-79bff41ecdd6 | -14.78243 | -43.95329 | 2026-03-19 04:06:00 | NOAA-20 | MANGA | MINAS GERAIS | Brasil | 3139300 | 31 | 33 | nan | nan | nan | Caatinga | 4.0 |
| d5ed7c68-edda-30eb-b019-4619d7b26ae9 | -14.7756 | -43.95209 | 2026-03-19 04:06:00 | NOAA-20 | MANGA | MINAS GERAIS | Brasil | 3139300 | 31 | 33 | nan | nan | nan | Caatinga | 3.2 |
| ad5ce048-7b9c-33fe-a6b9-c09294ec792a | -15.52851 | -40.83752 | 2026-03-19 04:06:00 | NOAA-20 | ENCRUZILHADA | BAHIA | Brasil | 2910404 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 0ed92644-19e8-39eb-a1c7-7f3e8215b1cc | -16.40909 | -39.75368 | 2026-03-19 04:06:00 | NOAA-20 | EUNÁPOLIS | BAHIA | Brasil | 2910727 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 7a6a47f4-2aab-341e-a456-a15d4f639dd9 | -14.77902 | -43.95269 | 2026-03-19 04:06:00 | NOAA-20 | MANGA | MINAS GERAIS | Brasil | 3139300 | 31 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 0efb50ac-c095-3237-9a07-99865363fad2 | -15.84097 | -39.18395 | 2026-03-19 04:06:00 | NOAA-20 | BELMONTE | BAHIA | Brasil | 2903409 | 29 | 33 | nan | nan | nan | Mata Atlântica | 8.2 |
| c3d030bd-4eaf-3f91-867e-2623e2780a42 | -19.77737 | -49.75194 | 2026-03-19 04:08:00 | NOAA-20 | SÃO FRANCISCO DE SALES | MINAS GERAIS | Brasil | 3161304 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9129112f-ecd9-30db-8da7-c4dcdd7faf77 | -19.78168 | -49.75296 | 2026-03-19 04:08:00 | NOAA-20 | SÃO FRANCISCO DE SALES | MINAS GERAIS | Brasil | 3161304 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d23a0481-b918-31c6-adb2-5a25d4f64604 | 1.98955 | -60.88604 | 2026-03-19 04:49:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 08f6df3b-f473-32c0-a93b-52b32763906a | 3.38163 | -60.19656 | 2026-03-19 04:49:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7e3926f3-487e-3946-9308-f1435e1bfc39 | 2.95157 | -60.71511 | 2026-03-19 04:49:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 4.2 |
| a633d627-551c-3fcf-846c-057244ad50e0 | 1.64512 | -60.29481 | 2026-03-19 04:49:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 15477b70-c4bf-3379-8c0f-ba3e18953fc8 | 2.24949 | -60.28839 | 2026-03-19 04:49:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 3.1 |
| b2592a19-a455-3dcb-bd2c-6f4da3259246 | 2.25005 | -60.29211 | 2026-03-19 04:49:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 76a7704c-bade-3d5f-ba27-9a78d170dce6 | 2.94643 | -60.71991 | 2026-03-19 04:49:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 156a26ac-4225-365f-b128-c054c21c0773 | 3.41733 | -60.16893 | 2026-03-19 04:49:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 4.1 |
| fad6d549-a7e4-3d03-8a86-1d10e91da7fc | 3.38109 | -60.19284 | 2026-03-19 04:49:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 5d987b3e-5e86-378a-8593-1d6f5ebb3e3a | 1.64457 | -60.29132 | 2026-03-19 04:49:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2e6dc8b4-26ab-306b-8fe6-5a7c9dd30a1a | 2.95097 | -60.71115 | 2026-03-19 04:49:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 4.2 |
| c7a9ebd4-10f4-32c7-b4c2-f7e3c0ac4f5b | 3.21112 | -60.14874 | 2026-03-19 04:49:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 3.4 |
| cc92b3df-dcfe-3401-b89f-ac6d1de855fe | 1.64082 | -60.29507 | 2026-03-19 04:49:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7453d537-fb56-3e7a-99fb-ab1730b95676 | 1.96388 | -60.56479 | 2026-03-19 04:49:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 4.1 |
| f324c723-bd2e-3ce2-8df3-02daf770ed89 | 3.41623 | -60.16151 | 2026-03-19 04:49:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 70e5d7ba-9712-3cc0-a1a4-f400148a3e48 | 1.99015 | -60.88997 | 2026-03-19 04:49:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e62ba92c-7ae0-35a2-93d2-0e5dd0674215 | 3.21665 | -60.1479 | 2026-03-19 04:49:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f3930701-c20d-3304-8d09-43de4103c274 | 3.41678 | -60.16521 | 2026-03-19 04:49:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 8c304ed3-798c-3ab7-8bb4-2c8247f9a9be | 3.42235 | -60.16445 | 2026-03-19 04:49:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 75b92d78-5e19-35d5-9e68-4f720635846a | 3.41066 | -60.16227 | 2026-03-19 04:49:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 8efab07e-96e8-375d-8723-11942ac9a539 | 1.64627 | -60.29422 | 2026-03-19 04:49:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 71129210-797f-3c0a-ac53-751495a0ac1b | -0.87854 | -64.14479 | 2026-03-19 04:51:00 | NOAA-21 | BARCELOS | AMAZONAS | Brasil | 1300409 | 13 | 33 | nan | nan | nan | Amazônia | 0.0 |
| af81a47d-2862-37bb-90b4-bb24a2bacf1b | -12.91658 | -43.01712 | 2026-03-19 04:53:00 | NOAA-21 | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 85018d0b-6fad-3fe2-b174-e2706a014f7a | -14.78119 | -43.9591 | 2026-03-19 04:53:00 | NOAA-21 | MANGA | MINAS GERAIS | Brasil | 3139300 | 31 | 33 | nan | nan | nan | Caatinga | 8.9 |
| 75d49dd7-6efc-3a3e-bcdd-5d7e6b80edad | -14.77587 | -43.95417 | 2026-03-19 04:53:00 | NOAA-21 | MANGA | MINAS GERAIS | Brasil | 3139300 | 31 | 33 | nan | nan | nan | Caatinga | 5.6 |
| 0215e3c4-d5b4-3f95-94b5-61bb94d7225b | -11.7985 | -47.09448 | 2026-03-19 04:53:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 1e69f5ff-1154-341d-84dd-5cad81300fb5 | -11.80301 | -47.0951 | 2026-03-19 04:53:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b14b3800-5c69-3cc0-9882-c61140b636f9 | -9.48388 | -46.10775 | 2026-03-19 04:53:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1561f337-0777-30c2-9463-1414a40da28f | -14.78213 | -43.95063 | 2026-03-19 04:53:00 | NOAA-21 | MANGA | MINAS GERAIS | Brasil | 3139300 | 31 | 33 | nan | nan | nan | Caatinga | 6.8 |
| 52769d78-6678-3f0a-bd75-20d3f37ecf75 | -14.78261 | -43.94633 | 2026-03-19 04:53:00 | NOAA-21 | MANGA | MINAS GERAIS | Brasil | 3139300 | 31 | 33 | nan | nan | nan | Caatinga | 6.8 |
| 77657d93-c828-3a35-b86f-2c7e225e0b54 | -12.9161 | -43.02145 | 2026-03-19 04:53:00 | NOAA-21 | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| cde6d0c3-0003-3ea6-aafd-203106c6f9ea | -11.80241 | -47.09971 | 2026-03-19 04:53:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| aa8c4fe5-d912-332e-83af-b143cbeb4d59 | -14.78166 | -43.9549 | 2026-03-19 04:53:00 | NOAA-21 | MANGA | MINAS GERAIS | Brasil | 3139300 | 31 | 33 | nan | nan | nan | Caatinga | 8.9 |
| 4d7f6762-79f1-368f-8ed5-ddba2d5c01ff | -14.7754 | -43.95835 | 2026-03-19 04:53:00 | NOAA-21 | MANGA | MINAS GERAIS | Brasil | 3139300 | 31 | 33 | nan | nan | nan | Caatinga | 5.6 |
| c8107e93-c57f-3da8-80d2-7e9180b977d0 | -19.77819 | -49.74894 | 2026-03-19 04:55:00 | NOAA-21 | SÃO FRANCISCO DE SALES | MINAS GERAIS | Brasil | 3161304 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5f3c6da3-8c9e-389b-9edf-65229340ed52 | -20.94211 | -48.70745 | 2026-03-19 04:55:00 | NOAA-21 | MONTE AZUL PAULISTA | SÃO PAULO | Brasil | 3531506 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 6f2dc15f-29fc-3c54-ae69-c5c2ff92cecb | -19.78242 | -49.74948 | 2026-03-19 04:55:00 | NOAA-21 | SÃO FRANCISCO DE SALES | MINAS GERAIS | Brasil | 3161304 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3dcf4019-6e82-3e34-9465-8caaf0a0c94c | -27.30293 | -51.35647 | 2026-03-19 04:57:00 | NOAA-21 | ERVAL VELHO | SANTA CATARINA | Brasil | 4205209 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 891c90a8-e8f8-3ffe-84c3-9eea9cca3306 | 2.95173 | -60.71257 | 2026-03-19 05:21:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 2e49de2f-d70a-34e7-ad79-fb5996ca409d | 2.24985 | -60.29051 | 2026-03-19 05:21:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 556f28e6-9274-32f0-8fe1-f87a0a813666 | 2.94795 | -60.71315 | 2026-03-19 05:21:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c43a740c-8db3-30f8-8046-3271625faccf | 3.41807 | -60.15906 | 2026-03-19 05:21:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 011d02b6-b2d0-3d53-8335-4adbc2d8a3c7 | 3.31198 | -60.57415 | 2026-03-19 05:21:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 16e1ef09-d720-36db-821c-d931842c1ad5 | 3.21564 | -60.15092 | 2026-03-19 05:21:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6e9cc8e0-be42-3be7-ba00-386c35e2cc8d | 3.37958 | -60.1945 | 2026-03-19 05:21:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.9 |
| e4587ea6-9951-37aa-b737-7dd3f35e5b0c | 3.38148 | -60.19128 | 2026-03-19 05:21:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2dd54d7b-a444-3dbf-8614-7f48ccce5fbf | 2.82939 | -60.03749 | 2026-03-19 05:21:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| bf1c25d8-8e62-3887-a76d-13bb7d73ef89 | 3.38214 | -60.19563 | 2026-03-19 05:21:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fe243843-f80c-3949-9d77-ebcc41421864 | 3.41505 | -60.16395 | 2026-03-19 05:21:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 8f8043dc-9f93-314f-ba4b-40bd3a6094b0 | 3.42678 | -60.1666 | 2026-03-19 05:21:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 5e5dc27c-18d5-3b5d-99ad-fb5db9369f3e | 4.45162 | -60.80043 | 2026-03-19 05:21:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 3dd090fb-24fa-3c4e-a56d-070f96b42bcd | 3.41874 | -60.16339 | 2026-03-19 05:21:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 48c746f8-5e40-33a7-a2cb-6253e392fc07 | 3.41572 | -60.16829 | 2026-03-19 05:21:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 51192acb-d329-344a-938f-b4d9235a265d | 2.32336 | -60.49553 | 2026-03-19 05:21:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9b473927-792c-37b8-b5f4-63a1418b530b | 3.31127 | -60.56961 | 2026-03-19 05:21:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7e1517d6-b83b-36c7-87e6-f4523dcd97af | 3.38452 | -60.18638 | 2026-03-19 05:21:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1ddcff93-5126-313a-823e-b0c016e829d9 | 2.94865 | -60.71772 | 2026-03-19 05:21:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 6ff5a1d5-b319-390f-83df-8d59409ab7b6 | 3.21431 | -60.14237 | 2026-03-19 05:21:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e2445d0c-4000-362d-996e-50e7899025f7 | 3.2113 | -60.14723 | 2026-03-19 05:21:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e7a2904b-95ea-39ff-b5af-e739acf90804 | 3.21497 | -60.14664 | 2026-03-19 05:21:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4d1fbe77-d3f1-384c-bf64-0c20b05e6df4 | 3.38259 | -60.18961 | 2026-03-19 05:21:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b305460b-8f91-32d8-b1fd-818cc58119d3 | 2.95551 | -60.71199 | 2026-03-19 05:21:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 4.0 |
| ad42eae7-c37b-31af-a98d-c4b55d6fcf6f | 3.37845 | -60.19619 | 2026-03-19 05:21:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6ef5665b-cfbe-33e9-a8bc-8ff1fe5bc723 | 3.4194 | -60.16772 | 2026-03-19 05:21:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 3.3 |
| f3bb8a63-e5cb-3d1e-8ca3-f1b5aa66bab8 | 2.24619 | -60.29104 | 2026-03-19 05:21:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 2d6bfefe-ac9d-3bb8-bfc4-806151575104 | 3.41136 | -60.16451 | 2026-03-19 05:21:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 848cd90f-7db3-3325-bab7-083615418100 | 2.24917 | -60.28613 | 2026-03-19 05:21:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 3.3 |
| cc2aa378-ade1-341d-9429-a9c1d742fe58 | 1.17422 | -59.14653 | 2026-03-19 05:23:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e34278d9-869f-3ffb-8237-65a6a112e893 | 1.12761 | -59.4494 | 2026-03-19 05:23:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9bac2e4e-e9e3-3f90-b239-0d36ea73e5c2 | 2.06676 | -60.67536 | 2026-03-19 05:23:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c7bad059-0cb7-3741-a71c-fd2d913bc247 | -15.84187 | -39.17911 | 2026-03-19 05:23:00 | AQUA_M-M | BELMONTE | BAHIA | Brasil | 2903409 | 29 | 33 | nan | nan | nan | Mata Atlântica | 17.1 |
| 0bc1f3f5-57e2-376c-95d9-fea72b3796da | 1.33475 | -60.06152 | 2026-03-19 05:23:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1fb68e6c-cdc1-3191-8db5-a04c817b6d53 | 1.20623 | -60.62552 | 2026-03-19 05:23:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 50075187-cefa-354d-bd4f-6c485e157db6 | 1.33538 | -60.06557 | 2026-03-19 05:23:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3324fe18-4fbf-3299-bbdc-7cb840bd126d | 1.1748 | -59.15026 | 2026-03-19 05:23:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 14fa2acd-a695-3b60-a4d4-3a9d5d87d332 | 1.96085 | -60.56447 | 2026-03-19 05:23:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6bf6718d-62e1-35f7-a7e7-0038b6ba13c8 | 1.51006 | -59.91566 | 2026-03-19 05:23:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0c5ed6e1-e75a-36f5-b170-b5123bdf9a39 | 1.51361 | -59.91505 | 2026-03-19 05:23:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2e41b134-2837-310f-8ab4-e03be7a6fb62 | 1.98587 | -61.4007 | 2026-03-19 05:23:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 32de6139-547c-3d05-8c08-1d08a333e0b6 | 1.96455 | -60.5639 | 2026-03-19 05:23:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 89ae2eb6-c4dd-371d-bf10-f807b6fb3cd4 | 1.14649 | -60.91052 | 2026-03-19 05:23:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d36c809b-1398-3aba-b065-cae823a56c4b | 1.07813 | -60.68229 | 2026-03-19 05:23:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 979b2341-9aea-37e0-bd16-119cfc157c09 | 1.9878 | -60.88834 | 2026-03-19 05:23:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 2cf4db32-adb9-36b3-ba90-09c85008a8b0 | 1.98198 | -61.40132 | 2026-03-19 05:23:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d73130bc-8d0d-3fef-8225-02d5462390ef | 1.5599 | -60.52298 | 2026-03-19 05:23:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d8662e17-4189-3f40-8dca-26812acc826d | -18.26292 | -54.03865 | 2026-03-19 05:25:00 | NPP-375D | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4246a828-2bff-343e-9c9d-ea11849c09ce | 3.42747 | -60.16513 | 2026-03-19 05:42:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 759d9f35-1448-3753-b60e-911590c02c98 | 1.98255 | -61.39827 | 2026-03-19 05:42:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 59c2fcfd-6b16-3711-8710-cf0ad9fa336f | 3.20867 | -60.13482 | 2026-03-19 05:42:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ffe6d5f8-2cd9-3f72-b605-8edf079f5a85 | 1.64469 | -60.29364 | 2026-03-19 05:42:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6d257fec-f169-3fbf-afd3-bc6366f19562 | 3.41802 | -60.16537 | 2026-03-19 05:42:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 4.1 |
| e32f2681-ad58-3a2a-917a-24bedf9e8374 | 3.41607 | -60.16277 | 2026-03-19 05:42:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 4.4 |


[Clique aqui para ver as próximas entradas](README4.md)
