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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| cc724eca-20c1-3813-b752-02a681460c01 | 2.69887 | -60.39186 | 2026-03-11 05:40:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 663ba80a-7f3a-34de-a7e4-ee21fdbcb25c | 2.70856 | -60.36131 | 2026-03-11 05:40:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 68eff864-f434-385e-a80e-30700a248194 | 2.70177 | -60.38724 | 2026-03-11 05:40:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4f74c0c2-8e7b-39e9-86be-382b2ccef15a | 2.69111 | -60.38895 | 2026-03-11 05:40:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 85866151-52d7-37ea-ad6b-716fc5fd9d7f | 2.25977 | -60.27735 | 2026-03-11 05:40:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 83a0ecf9-ef45-3c19-928c-ac246b740e3c | 2.69563 | -60.37165 | 2026-03-11 05:40:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 1bca7eba-6a66-36f3-8d4a-93ddba5c6ffd | 2.68301 | -60.36122 | 2026-03-11 05:40:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4150ba0b-fa79-3021-ae3c-8c2721b0bb7c | 2.69724 | -60.35894 | 2026-03-11 05:40:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 18.2 |
| cbb26f3c-e29f-3758-86c0-a290a733e851 | 2.69142 | -60.36816 | 2026-03-11 05:40:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 69.1 |
| 0bcd4b23-5921-3db1-b439-e2e284572f57 | 3.23839 | -59.89898 | 2026-03-11 05:40:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a642cd76-c357-378e-a60e-b966b347cc7b | 2.70306 | -60.39532 | 2026-03-11 05:40:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6a502779-0ea2-383b-bb08-e5c214ac77c2 | 2.70726 | -60.39878 | 2026-03-11 05:40:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ca82d0f7-590a-3ea5-a64f-870d51084a76 | 3.12559 | -60.42698 | 2026-03-11 05:40:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 49533625-d07f-31f4-95a2-3d4334bdd4fa | 2.71341 | -60.36885 | 2026-03-11 05:40:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a8c2e37c-20f0-3af6-8b9c-3b825a66778a | 2.69303 | -60.35546 | 2026-03-11 05:40:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3d317e6a-aab0-3f51-bf41-90b74b8cf48c | 2.70597 | -60.39071 | 2026-03-11 05:40:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c61fe781-d709-31e0-8b4d-697271ec3e28 | 2.70952 | -60.39015 | 2026-03-11 05:40:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 33fa97c5-23fb-3d5e-b890-80dfc7bfd10f | 2.69207 | -60.37219 | 2026-03-11 05:40:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.9 |
| a6507ddb-8923-30c1-8153-6fb66e7bcb55 | 2.69077 | -60.36411 | 2026-03-11 05:40:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 69.1 |
| 73ade922-b135-3e5f-9522-d953e529ae11 | 2.69433 | -60.36354 | 2026-03-11 05:40:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 69.1 |
| 2281e248-9f73-3724-8f65-0dcd0e3b31be | 2.24148 | -60.30104 | 2026-03-11 05:40:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cdc6a566-3251-3614-be5e-6b9835a0b2e7 | 2.69693 | -60.37975 | 2026-03-11 05:40:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 3.3 |
| d3ecd074-042f-372c-8874-51d6f077c800 | 2.26072 | -60.26016 | 2026-03-11 05:40:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 686e64ba-2992-33a9-be18-0f534f090310 | 2.25618 | -60.27788 | 2026-03-11 05:40:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 3a1e807c-712d-3096-b5d1-681e973fd3dd | 2.70501 | -60.36187 | 2026-03-11 05:40:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 3.2 |
| f0244f29-504a-3a92-9e27-d8850a6949e7 | 2.70921 | -60.36536 | 2026-03-11 05:40:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 6d322e1b-ca6a-3f9d-afd3-14fdc4629394 | 2.68786 | -60.36872 | 2026-03-11 05:40:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.6 |
| de98cb32-aa71-3d82-852a-cd0416be8f40 | 2.71277 | -60.3648 | 2026-03-11 05:40:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ef8a3fe8-e916-37b8-90e0-42c32fee220b | 2.70015 | -60.35434 | 2026-03-11 05:40:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 18.2 |
| 04940c2a-babb-30f7-9f39-e2c2c92c1cfc | 4.37104 | -60.89489 | 2026-03-11 05:40:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 0.2 |
| bb5f7239-18b3-337f-a9ff-2354b8f58fbb | 2.70145 | -60.36243 | 2026-03-11 05:40:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 109.6 |
| 7c2604b5-3a1e-3f45-b879-a614bed38585 | 2.69659 | -60.35489 | 2026-03-11 05:40:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 18.2 |
| ee9fa2c9-a25c-36bd-bbe0-056893da73d4 | 2.68626 | -60.38141 | 2026-03-11 05:40:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 79acc37a-0f2e-3a41-861f-d9db0c53ed18 | 3.22096 | -59.9061 | 2026-03-11 05:40:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0727af54-657c-37a8-83ab-e22609861897 | 1.72869 | -60.70276 | 2026-03-11 05:42:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6d62dd57-9c0e-3a2a-9dec-ea33ed6ad89a | 1.00886 | -60.38895 | 2026-03-11 05:42:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.2 |
| 412924bd-0839-3546-b551-1edc01b42a9f | -3.77142 | -55.83068 | 2026-03-11 05:42:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f2966616-67bb-3e7a-a75a-e90cef4f5fd9 | 1.64704 | -60.29734 | 2026-03-11 05:42:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3ad641c1-f40a-3e0f-ad01-48ba589193ad | -1.63981 | -54.49217 | 2026-03-11 05:42:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2b6e37dc-e176-3cbd-9ee8-80f11b36865c | -3.30745 | -56.28763 | 2026-03-11 05:42:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| dc480eff-a519-3bf4-a084-f896ceee6d9c | 1.62368 | -60.26668 | 2026-03-11 05:42:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 29f6239d-8a57-3f51-bea6-271703782d7c | -11.80497 | -59.19853 | 2026-03-11 05:44:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 9ae55f44-3d43-3ea8-ae0b-e573e6eae762 | -8.23882 | -62.35704 | 2026-03-11 05:44:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 50233d6c-8c0a-3f52-a155-5caa042c5b72 | -8.98959 | -72.47722 | 2026-03-11 05:44:00 | NOAA-21 | MARECHAL THAUMATURGO | ACRE | Brasil | 1200351 | 12 | 33 | nan | nan | nan | Amazônia | 0.3 |
| d61517a1-54dc-3402-a182-4af1fd009829 | -7.35227 | -65.8875 | 2026-03-11 05:44:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| e244a3bf-c687-3d10-96c5-73593dba0400 | -5.84854 | -71.66351 | 2026-03-11 05:44:00 | NOAA-21 | ATALAIA DO NORTE | AMAZONAS | Brasil | 1300201 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5c0c14c7-94c2-3291-a0c6-45cef3c8ff28 | -11.31466 | -54.86616 | 2026-03-11 05:44:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 887c0312-af58-3e55-959d-94e2d8a94d54 | -7.64858 | -54.91346 | 2026-03-11 05:44:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| f66e8438-df90-36c3-8936-c17e10b1ba4f | -5.43928 | -66.27898 | 2026-03-11 05:44:00 | NOAA-21 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| fe8c53cd-484f-3038-8dbb-1c2397e82ebf | -9.35617 | -54.12146 | 2026-03-11 05:44:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 4da267dc-c951-3797-b0a6-f147aa3b813c | -12.26765 | -55.94215 | 2026-03-11 05:44:00 | NOAA-21 | SORRISO | MATO GROSSO | Brasil | 5107925 | 51 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 6c0308af-ed30-3933-9044-f59d8e3a09d5 | -7.20549 | -63.97108 | 2026-03-11 05:44:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 8db6c56e-8a18-3f14-b4fa-c2dcaa21631b | -9.60617 | -61.65332 | 2026-03-11 05:44:00 | NOAA-21 | VALE DO ANARI | RONDÔNIA | Brasil | 1101757 | 11 | 33 | nan | nan | nan | Amazônia | 0.4 |
| e54ce4b7-791c-3f68-b092-017050c296e2 | 3.23711 | -59.90228 | 2026-03-11 06:10:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d8a7a60f-c42f-3bcc-8afd-7ddcf1842905 | 2.70426 | -60.36037 | 2026-03-11 06:10:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 78c425d3-3f39-36c2-a062-c10e60d4571c | 2.70313 | -60.35356 | 2026-03-11 06:10:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4648f476-6516-3ba2-8f2e-a1ed0e1e852a | 2.69719 | -60.35105 | 2026-03-11 06:10:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e0a14e56-afa8-3a0f-b439-e1d0b6c8e46a | 2.69831 | -60.35783 | 2026-03-11 06:10:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 84b19343-c011-3446-a98e-2e7609010032 | 2.70482 | -60.36378 | 2026-03-11 06:10:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 574fdfe0-e0fd-3613-be3a-031ff3c3bea8 | 2.69663 | -60.34766 | 2026-03-11 06:10:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a6607dd9-6ded-3393-8649-e23fb73c3704 | 2.7102 | -60.3629 | 2026-03-11 06:10:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 96e84b3c-7224-35d6-88ae-3e9b0ae1ca82 | 2.70226 | -60.38165 | 2026-03-11 06:10:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3a06cb88-b08b-3544-8f33-da5def583e83 | 2.7 | -60.36805 | 2026-03-11 06:10:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d95805b1-e11b-35c3-8450-95ccabe912ec | 2.69944 | -60.36464 | 2026-03-11 06:10:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 8f57ce74-79be-352b-be30-fbe5dc1a208c | 2.70369 | -60.35697 | 2026-03-11 06:10:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c45bc0b1-d698-3bcc-94ac-1b0e1fab640c | 3.24199 | -59.89775 | 2026-03-11 06:10:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 89812d38-52ef-372b-bef5-6ade617398b1 | 2.69293 | -60.35872 | 2026-03-11 06:10:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e8227a11-fbc0-39a0-ac2d-fbc8bef360c9 | 2.98752 | -60.06445 | 2026-03-11 06:10:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| fbe98510-c643-3d7d-8fa1-820226151e7a | 3.22978 | -59.89243 | 2026-03-11 06:10:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9afac0a8-25f4-39dc-9087-2726395fe4f8 | 2.70908 | -60.35609 | 2026-03-11 06:10:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0e3da1f2-af9d-301f-9c22-69adb9b9c8c8 | 2.69126 | -60.34864 | 2026-03-11 06:10:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c0aa5263-4796-3717-bd08-d9c60df109d1 | 3.23039 | -59.89601 | 2026-03-11 06:10:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7a94896f-9717-3551-b438-b908a6e1adfc | 2.69887 | -60.36124 | 2026-03-11 06:10:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 568b94c7-94d9-395c-bcd3-39f8e58b6fd5 | 3.22612 | -59.90413 | 2026-03-11 06:10:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 24b01930-70a4-398e-8cda-40461d87fae8 | 2.70057 | -60.37145 | 2026-03-11 06:10:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.5 |
| eb3c6b4b-dbb6-38dc-a378-b36bbbd70b43 | 2.69462 | -60.36893 | 2026-03-11 06:10:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 10000cc9-6fbb-3eb7-b1eb-5854404d4b13 | 2.70795 | -60.34926 | 2026-03-11 06:10:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a44306c7-6928-3f33-9527-366e59aedbe7 | 2.69519 | -60.37234 | 2026-03-11 06:10:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d60b800b-ed26-3813-bc87-a1c623ad4cf6 | 2.69775 | -60.35443 | 2026-03-11 06:10:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e69c8a85-1a1b-3f51-b652-27c215873970 | 2.69349 | -60.36211 | 2026-03-11 06:10:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 808a070e-b47a-35a0-8a72-66607f46fcd7 | 2.7017 | -60.37827 | 2026-03-11 06:10:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0bd6ca02-964c-3e4a-ab31-9a07b191d334 | 2.70964 | -60.35949 | 2026-03-11 06:10:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6cfdfc54-a8ae-3c93-9d0e-ff75e8aa2f08 | 3.22001 | -59.9015 | 2026-03-11 06:10:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5bc7d04b-dbf2-35de-a6b5-583f498407a8 | 2.69181 | -60.35198 | 2026-03-11 06:10:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 95c7e4b6-f288-3a17-becf-a2894dfe0998 | 2.70851 | -60.35267 | 2026-03-11 06:10:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 619879dd-9fda-379b-a52e-a117794d73ad | 2.70538 | -60.36717 | 2026-03-11 06:10:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c7ccc9a3-4cb4-32b2-8a52-922ee7fef3bb | 3.22062 | -59.90507 | 2026-03-11 06:10:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8b28d815-7303-318e-8355-ba92d9282d3e | 2.69406 | -60.36551 | 2026-03-11 06:10:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2a3b2379-4037-33df-a95f-49e19a9bd00f | 3.2255 | -59.90055 | 2026-03-11 06:10:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 782091c4-d209-31aa-b38d-aad12e8dbc08 | 2.70651 | -60.37399 | 2026-03-11 06:10:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7a67d259-6c55-3fe6-b91d-fe52568c852e | 2.70594 | -60.37057 | 2026-03-11 06:10:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6c7ca1ee-d915-3b45-ad6f-ca08dbe28823 | 2.69237 | -60.35535 | 2026-03-11 06:10:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| bc7370e9-1eae-36d8-b584-957c6dfee34c | 2.70113 | -60.37486 | 2026-03-11 06:10:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 795db91a-e860-35ba-a1e3-c17cf1a0c4bd | 2.70763 | -60.38078 | 2026-03-11 06:10:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 10aac083-29b9-3bb7-aa7e-69ac3b2f3f56 | 2.99297 | -60.0635 | 2026-03-11 06:10:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e05b18fd-d6f5-3154-9629-019993d93fe0 | 3.23161 | -59.90321 | 2026-03-11 06:10:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 7f2f7985-65b2-3b46-8690-d9a564f9728a | 3.22489 | -59.89696 | 2026-03-11 06:10:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 28f2f091-c867-31af-92a6-b7cd2ddca457 | 2.69576 | -60.37576 | 2026-03-11 06:10:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5436d89f-6941-3e7a-a364-dbd6290a72d7 | 3.23528 | -59.8915 | 2026-03-11 06:10:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0e1a532c-fe8b-3c25-a813-6f5575446709 | 2.70257 | -60.35014 | 2026-03-11 06:10:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |


[Clique aqui para ver as próximas entradas](README6.md)
