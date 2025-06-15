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
| 2881f747-7c7f-3523-a146-7bc3aeb45f74 | -7.2025 | -43.1171 | 2025-06-15 01:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 85.7 |
| c33af082-99f7-3f95-8684-7c2f8c242d4e | -7.2028 | -43.0936 | 2025-06-15 01:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 78.8 |
| 133514fc-eb8e-3212-83d1-8aca6c477a86 | -13.9062 | -54.6084 | 2025-06-15 01:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 404.2 |
| d1634b8c-2ba0-32e0-97bf-2c324adf395f | -10.9924 | -55.078 | 2025-06-15 01:00:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 51.3 |
| abb10652-df92-38c9-bb03-b6538dd49413 | -11.885 | -54.6926 | 2025-06-15 01:00:00 | GOES-19 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 54.9 |
| 085c7797-946a-3346-a729-e9dcad62f790 | -9.4158 | -48.4504 | 2025-06-15 01:00:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 104.2 |
| e52b984d-cdd5-316b-9766-500ca61bc3bf | -7.2214 | -43.1153 | 2025-06-15 01:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 61.7 |
| 6d025eed-ad99-36d3-b3b0-af7b3e679889 | -11.0113 | -55.0764 | 2025-06-15 01:00:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 97.2 |
| 0d4625a6-5c11-3c25-8f47-a32355f0510e | -13.9254 | -54.6063 | 2025-06-15 01:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 587.5 |
| 0b072595-d14b-39f2-8a43-4c989dd0d358 | -13.9251 | -54.627 | 2025-06-15 01:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 266.1 |
| 41561fa2-be71-3218-b6a1-2c2f8ebbea27 | -13.9257 | -54.5856 | 2025-06-15 01:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 96.2 |
| 7e781207-d14f-3c49-ba11-1c3c2a4610e6 | -10.2827 | -60.5432 | 2025-06-15 01:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 59.4 |
| 0bded863-e283-3d5e-af46-b214e6ac0308 | -7.2025 | -43.1171 | 2025-06-15 01:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 90.1 |
| d82c1ec6-29c4-3b07-a68c-3271f97faa32 | -10.9207 | -54.7592 | 2025-06-15 01:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 83.7 |
| c2f4710b-0c29-38c7-bdc6-0dfadf3894b1 | -14.8442 | -48.4218 | 2025-06-15 01:10:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 59.3 |
| 679cea95-33f4-3026-b591-328563f584a9 | -7.2028 | -43.0936 | 2025-06-15 01:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 61.4 |
| 50a1e4b7-2b19-3e2d-a901-02bcd04dc901 | -10.3014 | -60.5421 | 2025-06-15 01:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 54.4 |
| 205b1b4f-f4ad-3c4a-9c2a-a5cdaaca6730 | -11.0113 | -55.0764 | 2025-06-15 01:10:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 115.5 |
| 4b85dc74-1c0b-3f72-b65c-07fbc179fb57 | -9.4158 | -48.4504 | 2025-06-15 01:10:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 93.0 |
| 038c0d71-a000-3f62-a1b8-f2d56b8f74d4 | -10.9207 | -54.7592 | 2025-06-15 01:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 82.9 |
| faa00b92-862f-3ead-901f-77420c3aca5a | -11.0113 | -55.0764 | 2025-06-15 01:20:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 94.6 |
| 3fd2839b-938b-369e-bdeb-d9773d9230c2 | -10.9355 | -56.8322 | 2025-06-15 01:20:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 44.3 |
| 2243bc45-2daa-3963-b1b1-73c4de9145d0 | -9.4158 | -48.4504 | 2025-06-15 01:20:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 72.7 |
| f2bac514-27dc-3ab6-91ea-a1f7efcbf7fb | -7.2028 | -43.0936 | 2025-06-15 01:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 64.5 |
| f19f5909-8c2a-31d9-ba1c-afae424b8596 | -7.2025 | -43.1171 | 2025-06-15 01:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 80.3 |
| 1d08a996-918e-388a-bdd3-e7ddea48aa3a | -9.4158 | -48.4504 | 2025-06-15 01:30:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 82.1 |
| d94beb00-a161-351c-983c-3369b512cd9d | -10.9207 | -54.7592 | 2025-06-15 01:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 64.6 |
| f72ce147-991c-3b20-b648-a83861d2995b | -11.1826 | -44.481 | 2025-06-15 01:30:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 59.5 |
| 9a3f71df-9e66-3f45-b487-b57626245b50 | -7.2025 | -43.1171 | 2025-06-15 01:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 71.3 |
| ff71ea88-07ec-36a2-9391-dae59047819e | -12.696 | -52.3917 | 2025-06-15 01:30:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 49.8 |
| 8489ce3d-9c4b-3d60-8977-5cfa1ea2452a | -14.8442 | -48.4218 | 2025-06-15 01:30:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 65.9 |
| 25af699d-6c7d-3cd8-acb6-31856b890220 | -11.0113 | -55.0764 | 2025-06-15 01:30:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 92.6 |
| 6433553a-29f9-3b14-97fc-e609a20b8442 | -9.4158 | -48.4504 | 2025-06-15 01:40:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 69.2 |
| 21599ffa-7e42-3530-bdd6-fef5b1949b89 | -10.9207 | -54.7592 | 2025-06-15 01:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 72.5 |
| df993d1d-0f7e-35db-9a16-9e288db1b660 | -10.9355 | -56.8322 | 2025-06-15 01:40:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 48.8 |
| 28c5b8c5-3362-346e-880d-20b2e8b7dd17 | -11.0113 | -55.0764 | 2025-06-15 01:40:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 104.8 |
| a95be1a0-3ef2-36bd-9588-e8efe4d57308 | -7.2025 | -43.1171 | 2025-06-15 01:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 69.4 |
| 77514d70-1994-3469-ae4f-bef72c3550c0 | -11.1826 | -44.481 | 2025-06-15 01:40:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 63.0 |
| 96910b94-0922-3cf9-a27c-a7c8beae7ae5 | -11.2018 | -44.4783 | 2025-06-15 01:40:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 58.5 |
| f8dd6961-033c-3605-8e96-f54c11c6a3ee | -9.4158 | -48.4504 | 2025-06-15 01:50:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 65.7 |
| 20d43a3b-e2a9-3b0e-a458-fcb57787aa00 | -10.9207 | -54.7592 | 2025-06-15 01:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 63.6 |
| 07559fa9-cff8-3968-a98e-a509ed8ae5e9 | -7.2025 | -43.1171 | 2025-06-15 01:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 58.6 |
| e05ebc19-75c3-3097-b457-b334add25713 | -10.9355 | -56.8322 | 2025-06-15 01:50:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 46.6 |
| e17b3fa5-800e-31e8-8170-c36d2d0d141d | -11.1826 | -44.481 | 2025-06-15 01:50:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 63.7 |
| 3b907ba3-92ff-3ebf-a239-feec19b98c38 | -10.9167 | -56.8336 | 2025-06-15 01:50:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 38.1 |
| 5692f36b-56a6-3013-ae90-2e69cb8df1c9 | -11.0113 | -55.0764 | 2025-06-15 01:50:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 83.8 |
| 95912fd0-dcef-3c91-b82e-c1d471cf8ea8 | -12.696 | -52.3917 | 2025-06-15 01:50:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 50.8 |
| f71e6c19-b076-3bab-8f37-8e8fe6abe765 | -11.2018 | -44.4783 | 2025-06-15 01:50:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 55.6 |
| 283f34b0-291a-3aa9-949d-949def963392 | -11.1826 | -44.481 | 2025-06-15 02:00:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 62.9 |
| bdd957c7-c407-3f4f-8e03-07f3c7e23e64 | -13.9251 | -54.627 | 2025-06-15 02:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 105.7 |
| b81defa2-8c21-3f1b-9ca9-923ae72af3a1 | -10.9207 | -54.7592 | 2025-06-15 02:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 58.9 |
| a3a6414f-f60c-3632-9eed-90f53908eed0 | -13.9254 | -54.6063 | 2025-06-15 02:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 202.8 |
| e0788212-fd85-37f8-b391-fb94cc536c30 | -11.2018 | -44.4783 | 2025-06-15 02:00:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 52.7 |
| 96a54a47-bb86-3bdf-9be7-f07b97c63904 | -13.9257 | -54.5856 | 2025-06-15 02:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 37.6 |
| a4d0dad9-ed6e-39ce-a452-6d4db3f0c83b | -13.9062 | -54.6084 | 2025-06-15 02:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 187.4 |
| 99a7a3cb-a453-35bd-a699-2913162e0816 | -13.9065 | -54.5878 | 2025-06-15 02:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 43.9 |
| e4bbd7c4-99b8-3572-94d3-45dcc2033806 | -13.9059 | -54.6291 | 2025-06-15 02:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 71.7 |
| f18f9fb1-dc69-39c4-ba5b-f76bc88073bd | -11.0113 | -55.0764 | 2025-06-15 02:00:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 87.4 |
| ebac69c1-e788-3baf-9e4d-35bb8dfddf19 | -9.4158 | -48.4504 | 2025-06-15 02:00:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 60.7 |
| 6731ab15-df56-3b5f-9f86-7ac660725606 | -11.0113 | -55.0764 | 2025-06-15 02:10:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 89.4 |
| b8f4b873-c689-3c75-a875-e586a4357782 | -9.4158 | -48.4504 | 2025-06-15 02:10:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 59.1 |
| 2df02ee9-7adf-386e-836f-a6141f391952 | -10.9207 | -54.7592 | 2025-06-15 02:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 63.9 |
| b8f7d1cd-82f6-3b84-a5fc-633cff07a366 | -11.2018 | -44.4783 | 2025-06-15 02:10:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 55.8 |
| ba476e4c-d577-38b3-818c-5db1ccc5b4ae | -11.1826 | -44.481 | 2025-06-15 02:10:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 58.7 |
| b165f666-7251-3a3f-be71-e83478eed77a | -11.1826 | -44.481 | 2025-06-15 02:20:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 55.0 |
| 3db2e818-b96c-3062-85cc-f29a70e52a80 | -13.9059 | -54.6291 | 2025-06-15 02:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 81.7 |
| 1dc4268a-90da-3889-a831-96b74156a02f | -11.0113 | -55.0764 | 2025-06-15 02:20:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 79.2 |
| 918c6422-0ebf-3b36-82ed-e287ff33f7fc | -10.9207 | -54.7592 | 2025-06-15 02:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 56.8 |
| 8418f53a-c620-3e5f-83d2-1e46b5e49fe9 | -10.9355 | -56.8322 | 2025-06-15 02:20:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 54.4 |
| acfd9603-ea00-341c-b38f-3ede8a1503e8 | -13.9062 | -54.6084 | 2025-06-15 02:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 165.2 |
| e5e82958-725b-3921-a73d-ce724ccd6474 | -9.4158 | -48.4504 | 2025-06-15 02:20:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 64.8 |
| 6235d0a9-bc25-3534-99e0-d42ad01ebaba | -13.9254 | -54.6063 | 2025-06-15 02:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 165.2 |
| 609a8ec3-28b1-318c-bbb2-166cdf8bab3d | -13.9251 | -54.627 | 2025-06-15 02:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 101.6 |
| 7f7222f8-2fa7-3f87-b569-28af2b4415b4 | -11.1826 | -44.481 | 2025-06-15 02:30:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 54.6 |
| 3a98b307-ba1a-31d0-b7cf-c5d1cc5dd677 | -10.9355 | -56.8322 | 2025-06-15 02:30:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 63.3 |
| 7ff3a520-2a0f-3b07-ba65-9249186f7116 | -13.9059 | -54.6291 | 2025-06-15 02:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 93.1 |
| c3d1da30-dcc1-3594-a8b4-43f3b25ae650 | -13.9254 | -54.6063 | 2025-06-15 02:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 217.2 |
| 77387484-eb4a-370e-acb8-e07e408400c9 | -13.9065 | -54.5878 | 2025-06-15 02:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 32.8 |
| bd42f3ed-e4e6-3511-84e5-db10bf1a49a4 | -10.9207 | -54.7592 | 2025-06-15 02:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 59.2 |
| df8c24e1-c174-3231-bdbd-e570be729abd | -13.9062 | -54.6084 | 2025-06-15 02:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 224.9 |
| dcf5d4a1-978c-31be-a44f-2124bc6ba54a | -13.9251 | -54.627 | 2025-06-15 02:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 120.9 |
| 8ee4a8c6-4bb9-32f7-aa75-387c24059651 | -9.4158 | -48.4504 | 2025-06-15 02:30:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 56.0 |
| fd6078d9-86cf-398e-952d-a1f2079146d6 | -11.0113 | -55.0764 | 2025-06-15 02:30:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 72.5 |
| 17c7e6f7-94ba-3b2a-88d6-0f9023121322 | -23.444 | -47.6894 | 2025-06-15 02:30:00 | GOES-19 | CAPELA DO ALTO | SÃO PAULO | Brasil | 3510302 | 35 | 33 | nan | nan | nan | Mata Atlântica | 67.0 |
| 62ed44fc-7368-3a85-acb9-97fab01e0a0a | -10.9207 | -54.7592 | 2025-06-15 02:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 56.7 |
| 28a9ef7a-8a10-349a-8aa1-e26a2dc4c4b0 | -13.9254 | -54.6063 | 2025-06-15 02:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 174.5 |
| 9aca153c-e1b1-3b28-a995-0009eeceb594 | -11.0113 | -55.0764 | 2025-06-15 02:40:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 79.5 |
| 2c30c250-552d-30ce-afba-338eb62b415b | -13.9251 | -54.627 | 2025-06-15 02:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 92.9 |
| 7a1b03fc-d52f-31b8-97ff-6c0173e0534d | -13.9059 | -54.6291 | 2025-06-15 02:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 49.7 |
| a1d26eeb-a70a-346f-84c7-709181bf2979 | -13.9062 | -54.6084 | 2025-06-15 02:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 137.2 |
| 0630e9ab-c2f9-3fac-9230-391d752fd848 | -13.9254 | -54.6063 | 2025-06-15 02:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 164.1 |
| 8c46293a-a5cd-3f2d-b206-edaca165ddcb | -10.9207 | -54.7592 | 2025-06-15 02:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 51.9 |
| 7d0d2054-9c5d-38b0-bb51-8c95eae833d5 | -11.0113 | -55.0764 | 2025-06-15 02:50:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 67.4 |
| 419b13e3-be24-30d1-8584-9e614fb14b2a | -13.9059 | -54.6291 | 2025-06-15 02:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 74.6 |
| 24700361-2158-3929-8fda-ea90628d5069 | -10.9355 | -56.8322 | 2025-06-15 02:50:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 47.1 |
| 8725a2b2-036e-3095-b818-16b4f8c979ec | -13.9251 | -54.627 | 2025-06-15 02:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 98.1 |
| 31845e4a-46a5-3cad-a54f-4590a0650f55 | -9.4158 | -48.4504 | 2025-06-15 02:50:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 49.6 |
| f991c6f6-1dc0-369c-a3fb-d25021a9a764 | -13.9062 | -54.6084 | 2025-06-15 02:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 173.2 |
| 655a0296-267e-3ac0-9815-0a95708632e2 | -13.9251 | -54.627 | 2025-06-15 03:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 112.9 |
| 1a16a615-6c85-36e1-94ba-64209a11ad1c | -13.9254 | -54.6063 | 2025-06-15 03:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 184.6 |


[Clique aqui para ver as próximas entradas](README4.md)
