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

## Dados Diários - Página 95

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 43fac3a0-6777-32b9-99c1-33b4384b1d1f | -8.1685 | -52.79979 | 2024-09-27 04:40:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| fb108b20-db9a-387e-a041-c97fec43b88e | -8.16771 | -52.79922 | 2024-09-27 04:40:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2328af5f-4cb1-3aaa-8158-95972d67029c | -8.13865 | -52.87078 | 2024-09-27 04:40:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 62840fbd-43ef-394a-9a5d-921e744cb8fa | -8.13507 | -52.87019 | 2024-09-27 04:40:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8bc2d6f3-5298-3990-9489-78729e69651e | -8.13281 | -52.86149 | 2024-09-27 04:40:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| dd18e728-101a-3676-9b24-8bb0aefeb41e | -8.13214 | -52.86557 | 2024-09-27 04:40:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e7ea0adf-88a5-3b9c-b904-4424ffa5d62a | -8.13148 | -52.86968 | 2024-09-27 04:40:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0d7ef86f-868a-3477-8148-00a297bbb70a | -8.05741 | -52.80667 | 2024-09-27 04:40:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6d164954-318f-3be1-bc28-50e72aae96c5 | -8.05482 | -52.80733 | 2024-09-27 04:40:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| c3891e79-5745-3a0e-9063-fd51551f496b | -8.05416 | -52.81139 | 2024-09-27 04:40:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d0162638-fc17-3a95-a142-e0d51db31d17 | -8.05381 | -52.8062 | 2024-09-27 04:40:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b0e929fc-8b4a-3a41-9a68-dcaedef9b0bf | -8.05314 | -52.81024 | 2024-09-27 04:40:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 00d70543-0043-3c85-b4ca-93bb4e4ef509 | -8.05124 | -52.80679 | 2024-09-27 04:40:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| acf6f2eb-9ec1-351f-9d17-64ff9ba62380 | -7.99627 | -52.80635 | 2024-09-27 04:40:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f5759c24-a1f8-3e21-aa3e-95311a71fbc7 | -8.4756 | -53.22409 | 2024-09-27 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 480a71f3-ef72-3110-8c9c-045161554cb1 | -8.46905 | -53.21862 | 2024-09-27 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 4c2f52c7-d07e-3175-b291-19fc17d5416a | -8.46765 | -53.22707 | 2024-09-27 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 7c24f4c4-2422-3520-928d-a842ed1dc3a8 | -8.37421 | -52.4731 | 2024-09-27 04:40:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 505a2e2e-af31-38b5-abd4-d576ea63eb2e | -8.3707 | -52.47252 | 2024-09-27 04:40:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| de816b03-5230-399d-9dbe-eb523674f527 | -8.36718 | -52.47206 | 2024-09-27 04:40:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| da927790-3fbc-3174-a9e5-bc9eba256cc9 | -9.11919 | -53.30688 | 2024-09-27 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8b750765-b0ea-360a-923c-2e7666a345c5 | -9.11557 | -53.30624 | 2024-09-27 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| c53282f7-7515-365b-b5ae-b3ed73e73401 | -9.10976 | -53.29651 | 2024-09-27 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 3ee5a611-963a-383b-ab6e-1ea4cb545cd1 | -9.10905 | -53.30077 | 2024-09-27 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 19ed7722-c8b5-3e2e-a346-687d3a54de6d | -8.95298 | -52.81853 | 2024-09-27 04:40:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1ca1e629-0473-36b2-87e5-eea6dd97dbaa | -8.94522 | -52.82145 | 2024-09-27 04:40:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2c9affee-b14e-33db-a1c6-9683da3fbf24 | -8.9417 | -52.82078 | 2024-09-27 04:40:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d2b57b26-d8ed-348d-b41e-829575db5864 | -8.93817 | -52.82013 | 2024-09-27 04:40:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f5d4ada8-2882-3266-aeca-92f889fa689c | -8.93681 | -52.82828 | 2024-09-27 04:40:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5ebe565c-2c8b-31e3-93a1-9528624acb5f | -8.91772 | -52.76821 | 2024-09-27 04:40:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 67c30c7a-3ecf-3052-a786-55362b8a0e6e | -8.91708 | -52.77215 | 2024-09-27 04:40:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8de2a0c4-cfa0-30ba-a80b-a19eb65eb8d5 | -8.91483 | -52.76366 | 2024-09-27 04:40:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 60004251-a76a-3205-b22c-902a3f1a505a | -8.9129 | -52.77554 | 2024-09-27 04:40:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d916e389-ce34-3cda-ad31-e39475bd4691 | -8.9113 | -52.76308 | 2024-09-27 04:40:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 84b27d56-c5a5-3dab-9326-a8b72d279e23 | -8.91 | -52.77103 | 2024-09-27 04:40:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5a434d99-01b6-35a9-848b-d0ad28914466 | -8.90935 | -52.77502 | 2024-09-27 04:40:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f44b8b24-5d63-3a8e-b2b4-31e42c0c7d83 | -8.89493 | -53.03493 | 2024-09-27 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b4c997b2-dc3a-3774-bda9-27e8469dff66 | -8.89321 | -53.03132 | 2024-09-27 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| ae149773-29c9-3463-a14d-09d69ff6575c | -8.89098 | -53.02238 | 2024-09-27 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 9d8613fc-0842-31f2-ac42-02495742d9d6 | -8.88741 | -53.02176 | 2024-09-27 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 45d830fd-40c2-3df3-980c-d7a6aa64a89c | -8.88674 | -53.02588 | 2024-09-27 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| c618b118-67b8-3eb7-b957-78fdc077e076 | -8.66978 | -53.18781 | 2024-09-27 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 439e9030-8698-3580-9912-197880f3b6c7 | -8.66757 | -53.17884 | 2024-09-27 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ee2203bf-4f13-39b0-8e2f-d6bddf3a57a5 | -8.66687 | -53.18301 | 2024-09-27 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a5e745d9-ffd3-3259-869c-714d75dd7a57 | -8.66543 | -53.19161 | 2024-09-27 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 58ce1b55-0c1f-3a49-bb1c-fa1e5f656431 | -8.66154 | -53.07145 | 2024-09-27 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8d43919a-dba9-3b1d-8923-43cff4b30525 | -8.65967 | -53.18165 | 2024-09-27 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| c62a77c0-1863-374d-a221-1426e88c61f4 | -8.65747 | -53.19473 | 2024-09-27 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 6fceefd0-68d1-3bd5-94a6-117a4ab2af3a | -8.65676 | -53.17688 | 2024-09-27 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| a0ae45c2-04be-327a-853a-d786938b037a | -8.65607 | -53.18099 | 2024-09-27 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 42760a16-f27c-3915-941d-283e6adaffc4 | -8.64963 | -53.19025 | 2024-09-27 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| bf7a8989-30bb-3968-a1b6-392d85578fe4 | -8.60686 | -51.75798 | 2024-09-27 04:40:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ad606a5c-2211-3312-a369-c6020d408aef | -9.34609 | -52.52716 | 2024-09-27 04:40:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 870d61ee-f8ff-38c6-a735-e5afd2e9daaf | -9.34068 | -52.5383 | 2024-09-27 04:40:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 561879bf-b0ca-385e-a618-cc7f52178b83 | -9.04834 | -52.96672 | 2024-09-27 04:40:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e06945e7-1bcc-36c9-ac8e-efe99112154a | -8.94943 | -52.81798 | 2024-09-27 04:40:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8b628ce7-a28f-3f8d-83ff-43a5835095e6 | -8.94034 | -52.82894 | 2024-09-27 04:40:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ce496617-609c-3fb8-be19-edaac0bf1de1 | -8.93749 | -52.82418 | 2024-09-27 04:40:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1f20d704-3b3d-3a76-9e1d-800af5670d6b | -8.92061 | -52.77273 | 2024-09-27 04:40:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 72f6a904-427c-3d51-892e-ae7cfda33dc1 | -8.91644 | -52.77608 | 2024-09-27 04:40:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| bfe7e3e2-d001-31dc-9db0-c6af71d25716 | -8.90777 | -52.76252 | 2024-09-27 04:40:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 76894c2f-eec3-3d2e-82f1-9c5c1da0486a | -8.90711 | -52.76651 | 2024-09-27 04:40:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f78fbba6-d010-3dd3-a825-9ce55a352f3c | -8.90646 | -52.77051 | 2024-09-27 04:40:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| eabd59a7-5fce-3ceb-8082-d234498c5b1c | -8.89564 | -53.03072 | 2024-09-27 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| d70ca1d5-436a-378a-a36a-c8a16c0b97c2 | -8.89523 | -53.01885 | 2024-09-27 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 92e7df20-599b-3c73-aa64-5c3c45172251 | -8.89417 | -53.0176 | 2024-09-27 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 07b70103-2dcd-3246-9341-a8dab4ad414c | -8.89208 | -53.03004 | 2024-09-27 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| ba4d5f33-cf01-3ecc-b60d-d0511a47abd8 | -8.89166 | -53.01823 | 2024-09-27 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| f04e944c-7881-3a2a-84b0-adfd0b219f57 | -8.89136 | -53.03428 | 2024-09-27 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 08272573-6565-34ab-bdca-e799d416a1f1 | -8.89059 | -53.01702 | 2024-09-27 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 5908e9a1-ae58-36fe-b4c7-b3e26e361a2e | -8.88989 | -53.02117 | 2024-09-27 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 044658aa-3cb0-3cc3-9887-be9a4cc7ee08 | -8.88964 | -53.03065 | 2024-09-27 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| e9bf2b6e-d0cd-38d1-aa84-0d3902a59d95 | -8.88852 | -53.02937 | 2024-09-27 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 4b5404c4-2423-30e8-81b0-1680ec79a0f4 | -8.88607 | -53.03004 | 2024-09-27 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 4ad68643-1ab0-317a-8d5a-8cd47748418e | -8.67266 | -53.1928 | 2024-09-27 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5c9cf8ff-e665-33a8-bed7-3e608ba15e10 | -8.67048 | -53.18365 | 2024-09-27 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2d2492e2-3036-38a6-8ac4-4fc20a57ef33 | -8.66904 | -53.1922 | 2024-09-27 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 2e384971-10cc-30c2-862d-d846a273d156 | -8.66398 | -53.17812 | 2024-09-27 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| cb8ed7f6-616e-3adb-a882-5d1965d990b2 | -8.66037 | -53.17747 | 2024-09-27 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 29a5162d-edc9-3fa0-906d-88675129b43e | -8.65607 | -53.10513 | 2024-09-27 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f7551442-b946-3358-acbe-626d415c3ecc | -8.65535 | -53.18526 | 2024-09-27 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 29a60d35-45dd-37e6-9189-3ce6f38a0ddf | -8.65246 | -53.18039 | 2024-09-27 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 316477c3-464b-38a8-8a95-a580506e451d | -8.65173 | -53.1847 | 2024-09-27 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 6e1ae362-9471-3c80-996d-cd012e021cfe | -8.651 | -53.18906 | 2024-09-27 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| eee5ef6a-2250-3a90-9a5c-2d0d3aca4c12 | -8.65035 | -53.18586 | 2024-09-27 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 2c665544-73a1-34b9-970c-186f4a115de5 | -8.65025 | -53.19348 | 2024-09-27 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 58808b14-73d3-3a8b-98aa-65013ad94e71 | -8.63615 | -53.13648 | 2024-09-27 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 116e52d0-87e7-3222-b686-93ec62a69317 | -8.62756 | -53.14363 | 2024-09-27 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 6805c8fa-4e8b-3148-a75f-dffd76625c3a | -8.46472 | -53.22224 | 2024-09-27 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 4886cba6-47dc-3676-81df-b6b29e613592 | -8.46401 | -53.2265 | 2024-09-27 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| da0035b8-76ea-3bda-8713-2a830cfb4d92 | -10.4371 | -53.67457 | 2024-09-27 04:40:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| cd877835-6393-3152-a705-eb9abfc43b62 | -10.43638 | -53.67883 | 2024-09-27 04:40:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 9a4cd42c-df35-38b3-b8ec-1182334f023a | -10.43566 | -53.68309 | 2024-09-27 04:40:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 89d6a03c-b0ca-31d7-93b4-3e116ea9adc5 | -10.43421 | -53.69165 | 2024-09-27 04:40:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 137c8b76-e585-3d5f-87fc-df9c4277ae29 | -9.81381 | -53.51498 | 2024-09-27 04:40:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e118c800-558d-3bf3-ab2b-a3c4e78c02e5 | -9.80153 | -53.54351 | 2024-09-27 04:40:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4102cf05-fc8e-345d-95db-29bb53465ce8 | -9.77581 | -53.53634 | 2024-09-27 04:40:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| df8ea77a-7edc-3dbf-8fb0-dd96e6d612f0 | -9.76642 | -53.54801 | 2024-09-27 04:40:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0baaebba-edd1-3028-86a6-01591f9ca274 | -9.69298 | -53.49624 | 2024-09-27 04:40:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 165b2012-dd08-3be8-bb3e-d13c49658cfb | -9.69226 | -53.50048 | 2024-09-27 04:40:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |


[Clique aqui para ver as próximas entradas](README96.md)
