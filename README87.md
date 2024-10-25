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

## Dados Diários - Página 87

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6ee9e0dc-c547-3b5a-ad52-a2869be7bf12 | -5.30644 | -50.5672 | 2024-10-25 05:01:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 987a9433-48ba-3af2-8f51-7e73ae5cafbe | -5.30242 | -50.56661 | 2024-10-25 05:01:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2e359935-b385-3455-8542-5f493ef97d2b | -5.2967 | -50.98549 | 2024-10-25 05:01:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 39874414-2508-327e-ae64-be9465e2e2bc | -2.20792 | -50.83699 | 2024-10-25 05:01:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 2e22df3a-bc27-3582-96fa-4c112348984e | -5.23158 | -50.88416 | 2024-10-25 05:01:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 40feca41-b6ba-356f-b838-1b5285d270fa | -5.22746 | -50.88632 | 2024-10-25 05:01:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5f1f85a3-b38e-3ad4-8781-12e9794ccf49 | -5.17959 | -50.07423 | 2024-10-25 05:01:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0663d82e-b7fe-3a05-98c5-8195296002ee | -7.813 | -50.22885 | 2024-10-25 05:01:00 | NOAA-20 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fb208070-00b0-3828-8e4b-fd85400c5949 | -7.81213 | -50.2275 | 2024-10-25 05:01:00 | NOAA-20 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e3cdde19-6252-3c91-961c-6f3de29b0ca2 | -6.89646 | -50.32468 | 2024-10-25 05:01:00 | NOAA-20 | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fd5ecfd7-9bf4-3abb-aaaf-2bf1bf34a5fa | -6.8959 | -50.32851 | 2024-10-25 05:01:00 | NOAA-20 | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 50f75a33-0bed-3c5a-b141-7e65aa9b8283 | -6.80681 | -50.87897 | 2024-10-25 05:01:00 | NOAA-20 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 145cf67f-c8a5-3fef-ac5d-e38b4d81161a | -6.80335 | -50.87459 | 2024-10-25 05:01:00 | NOAA-20 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 0b0621ef-4f06-3b5a-b482-3357d96d2e54 | -6.80282 | -50.87814 | 2024-10-25 05:01:00 | NOAA-20 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8984feae-1497-33c6-b820-746ba0472ab8 | -6.68375 | -49.97488 | 2024-10-25 05:01:00 | NOAA-20 | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 7cf5dfc2-ef16-3e31-8e8a-a20683793a5a | -6.68318 | -49.97892 | 2024-10-25 05:01:00 | NOAA-20 | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 12.7 |
| 05a86322-b47a-3ba3-bb10-1f1434363d0f | -6.67893 | -49.97815 | 2024-10-25 05:01:00 | NOAA-20 | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| aa8c13fc-8ddb-3eba-a2ac-06e6dae2c34e | -6.53318 | -51.13158 | 2024-10-25 05:01:00 | NOAA-20 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 665e4656-badf-32b6-a287-2f01e1bda7c7 | -8.1765 | -50.15331 | 2024-10-25 05:01:00 | NOAA-20 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 63ddb217-e030-32b5-924f-f2e043dd123b | -1.77446 | -50.73456 | 2024-10-25 05:01:00 | NOAA-20 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b53158db-d302-3edc-a966-3e468af1ecbc | -1.67175 | -50.4485 | 2024-10-25 05:01:00 | NOAA-20 | BREVES | PARÁ | Brasil | 1501808 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f891f619-f300-3a6e-8fc9-d480c7eb7672 | -1.52418 | -50.62508 | 2024-10-25 05:01:00 | NOAA-20 | BREVES | PARÁ | Brasil | 1501808 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f8524a3d-5d9e-333d-b717-763a4b821078 | -1.52038 | -50.6245 | 2024-10-25 05:01:00 | NOAA-20 | BREVES | PARÁ | Brasil | 1501808 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 2d4a1c1f-3d42-3b2c-b8d1-dae195eb9e4d | -2.23986 | -50.45782 | 2024-10-25 05:01:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0437194a-bc16-361e-a284-8dbc6148c0ff | -2.23315 | -50.67631 | 2024-10-25 05:01:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 210436dc-62db-3f50-9810-a4f6a544f07b | -2.23241 | -50.68102 | 2024-10-25 05:01:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b9412377-a06a-3f3b-bfbb-23c43f8b4684 | -2.23178 | -50.67886 | 2024-10-25 05:01:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 9bd3a1d8-f9d1-3916-87d2-fdc6ffb2b3a4 | -2.20824 | -50.83422 | 2024-10-25 05:01:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 5eb73d1b-d261-318e-9d24-60d2b61fd367 | -2.14457 | -50.66763 | 2024-10-25 05:01:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fdb3f117-1011-35e8-9854-14b205438871 | -2.13118 | -50.83183 | 2024-10-25 05:01:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0d82cb9b-57bf-34ce-8cb3-a9a0f89c99ef | -2.11147 | -50.88504 | 2024-10-25 05:01:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d0d9a60c-e533-337f-882e-55ea0c0f2deb | -3.60237 | -51.46003 | 2024-10-25 05:01:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 39b61e26-e912-3e71-a440-5894f560fded | -3.51629 | -51.06445 | 2024-10-25 05:01:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 4b8ac946-9528-36f3-8d50-ce4945e2afdb | -3.51559 | -51.06908 | 2024-10-25 05:01:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 1759c72a-a994-3cfe-9be5-f6e6ee7f1606 | -3.51505 | -51.02135 | 2024-10-25 05:01:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 7b6c63a4-b767-345a-8b17-d11b95d432f9 | -3.5125 | -51.06386 | 2024-10-25 05:01:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 1d1dcee1-af23-3c0a-8481-1e4a33267a30 | -3.51179 | -51.06851 | 2024-10-25 05:01:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 2cb08b09-e1a3-3394-b1d7-3a602dc0c110 | -3.45175 | -51.58703 | 2024-10-25 05:01:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8baf3fee-b224-30a8-93e1-4bd9ea8e614d | -3.34818 | -51.65208 | 2024-10-25 05:01:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 99843847-75a9-3f53-97b7-fef370bb9671 | -3.263 | -50.7734 | 2024-10-25 05:01:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 3739678d-049e-3d04-9293-80f1277d83d0 | -3.26226 | -50.77817 | 2024-10-25 05:01:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 11d939ff-f2f8-3d9a-9012-1a056a627878 | -3.08293 | -51.26378 | 2024-10-25 05:01:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 6b8daca0-074a-345d-8e58-f23c2636496e | -3.0792 | -51.26322 | 2024-10-25 05:01:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| bb7e8798-379c-36e9-8760-5e63af50ec9e | -2.99882 | -52.00904 | 2024-10-25 05:01:00 | NOAA-20 | VITÓRIA DO XINGU | PARÁ | Brasil | 1508357 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 153664b1-d82a-3c3a-9534-5d008c3511b5 | -2.99658 | -52.00994 | 2024-10-25 05:01:00 | NOAA-20 | VITÓRIA DO XINGU | PARÁ | Brasil | 1508357 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1efce7dc-0958-3e94-90d5-19d3069e95ec | -2.87735 | -51.31319 | 2024-10-25 05:01:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d21b238c-9016-3553-b2a5-a0b4eb7c4c08 | -2.87364 | -51.31262 | 2024-10-25 05:01:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 852a6079-a85e-372d-a236-3857faf927e5 | -2.86275 | -51.59785 | 2024-10-25 05:01:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1f4d1c82-254f-3f42-bfda-ba2c02a4d31d | -2.85909 | -51.59729 | 2024-10-25 05:01:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b6e163cb-94f5-3ef0-a839-0fa00dde04f9 | -2.85845 | -51.60154 | 2024-10-25 05:01:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d52c6b41-df35-3409-953e-a4b86bdd123a | -2.85107 | -51.28657 | 2024-10-25 05:01:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5d4b19cf-78f3-324f-bdd2-4ede003f7e60 | -2.83434 | -51.80912 | 2024-10-25 05:01:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 14.3 |
| 3a302eb7-5eeb-34a0-a362-17e2bc569a3d | -2.8337 | -51.81329 | 2024-10-25 05:01:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 14.3 |
| 09951e76-a9a8-3965-8a53-b6f83f63f3f9 | -2.83073 | -51.80856 | 2024-10-25 05:01:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 1793c99e-bff3-3abd-a0b2-d5659a1b598e | -2.83009 | -51.81273 | 2024-10-25 05:01:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| f55d5e3b-4672-3435-8489-3c17af75ef54 | -2.82648 | -51.81218 | 2024-10-25 05:01:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| e0df4c7a-d058-3540-9f0c-a0f0b701dc46 | -2.81495 | -51.34873 | 2024-10-25 05:01:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f3eb03a4-d12d-34ba-a2e7-e7f14343e60b | -2.81428 | -51.35312 | 2024-10-25 05:01:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 179cf2d6-129d-37a5-aff8-994ea1d0a4df | -2.81058 | -51.35255 | 2024-10-25 05:01:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a0e51aef-c548-3a78-83bd-c143ea8f7883 | -2.80991 | -51.35694 | 2024-10-25 05:01:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 53dee901-66d4-3c05-b49e-8c66374c15f2 | -2.79916 | -51.59836 | 2024-10-25 05:01:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a73ea66c-2efc-3970-a063-a472993d96ab | -2.79748 | -51.364 | 2024-10-25 05:01:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b5ad32cd-d9ac-3fce-91ba-1da5ec370945 | -2.79378 | -51.36343 | 2024-10-25 05:01:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7496af26-839a-342f-9512-cc013f15d087 | -2.79312 | -51.36781 | 2024-10-25 05:01:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| eceac8cd-8a66-3f6e-8a34-12edcf543364 | -2.79008 | -51.36287 | 2024-10-25 05:01:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f1bf0e39-56d2-3552-a200-9e1d0fe7b28a | -2.73862 | -51.62827 | 2024-10-25 05:01:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4a2cac46-c4b1-3f5b-84fe-551b77ef0be9 | -2.73785 | -51.62996 | 2024-10-25 05:01:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3c87739c-6793-3c3c-a41b-5c75361fe131 | -2.40916 | -50.48252 | 2024-10-25 05:01:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| be2207b7-373a-348f-9211-72eec6dec31e | -2.29639 | -50.84103 | 2024-10-25 05:01:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 99c3959e-bb37-307e-838e-66e3b5ee4c2e | -2.2926 | -50.84045 | 2024-10-25 05:01:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5439ea3d-a536-3a8e-9733-cb10c50acc7d | -2.28905 | -51.14228 | 2024-10-25 05:01:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 333fe04d-f030-32a5-8b4a-763ef94709ef | -2.28863 | -50.43313 | 2024-10-25 05:01:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0672b882-d824-371f-bb9b-526d1d2f96f8 | -2.28601 | -51.13727 | 2024-10-25 05:01:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1b0b548e-232b-30ca-9a41-8a0b33fab15e | -2.28475 | -50.43253 | 2024-10-25 05:01:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 652ab116-5cd6-3f38-bf75-dae5008a2e0f | -2.27479 | -50.44592 | 2024-10-25 05:01:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 0bd40057-6c15-3027-86a3-3d8b8fd3cccc | -2.27406 | -50.45077 | 2024-10-25 05:01:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| c33455ae-4e8d-3064-a6f0-514437a81f4a | -2.27313 | -50.44802 | 2024-10-25 05:01:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| ebe0df76-5c80-3686-a0b8-2e306712c165 | -2.22657 | -50.9427 | 2024-10-25 05:01:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 58bd4ff9-3839-302e-8ec9-a61c5255472a | -3.34518 | -51.64721 | 2024-10-25 05:01:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bc539915-5ae5-35d3-b9d2-dec712453399 | -3.34451 | -51.65152 | 2024-10-25 05:01:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c38eb21e-cd77-3aa8-86c7-7acf4ed77f6d | -3.30856 | -51.64143 | 2024-10-25 05:01:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3153c446-86da-37a4-8adb-f3c7d61168c3 | -3.30467 | -51.05638 | 2024-10-25 05:01:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5d0b0678-387c-309c-99fd-b193b799bd03 | -3.26685 | -50.77397 | 2024-10-25 05:01:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 70a60bc2-7e12-3bfa-b1de-fe670128060f | -3.2147 | -51.01149 | 2024-10-25 05:01:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 920fcd92-db5c-31a5-9ee5-2d921394fae1 | -3.20247 | -51.33915 | 2024-10-25 05:01:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 22f864e3-2d19-30ac-8bd7-68726f30ed21 | -3.20178 | -51.34357 | 2024-10-25 05:01:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b60bebf9-5a4a-37a9-8ea8-2d2b11b225f6 | -3.19908 | -51.03746 | 2024-10-25 05:01:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ea628435-3fc5-36ff-a1d0-6553c878414d | -3.19439 | -51.2188 | 2024-10-25 05:01:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 57d384da-0ef8-346a-80a9-01536a2fc6f1 | -3.16777 | -51.24241 | 2024-10-25 05:01:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4197fb57-acde-30a8-ab5d-40bc72bab276 | -2.70154 | -51.71921 | 2024-10-25 05:01:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d884ef14-f1d8-359d-a692-7414c676f31a | -2.60662 | -51.77434 | 2024-10-25 05:01:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 62e23ccd-9d5d-3b25-bf2c-0bde40c34f0a | -2.60449 | -51.77266 | 2024-10-25 05:01:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e4b5b482-085f-307b-b388-9db10aac4490 | -2.60301 | -51.7738 | 2024-10-25 05:01:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 171ce011-af5c-39bc-8d6d-689fc671c069 | -2.60236 | -51.77793 | 2024-10-25 05:01:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e7118d50-3bcf-32ee-ab8d-575d3ef794fd | -2.60025 | -51.77626 | 2024-10-25 05:01:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 93662ad8-5f2b-37fd-a3a2-9ef4a242dbee | -2.58557 | -51.92147 | 2024-10-25 05:01:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 445c4d43-f0c6-36b9-8b64-acbe74e4d3dc | -2.58329 | -51.92233 | 2024-10-25 05:01:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2feafd4c-992b-3ec8-99d3-7a3fc8f08636 | -2.58311 | -51.9377 | 2024-10-25 05:01:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 444bc445-da4c-381c-8d93-4c3ddbc7ffd9 | -2.582 | -51.92091 | 2024-10-25 05:01:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2c215cef-5993-3e07-a068-b1c085fc18b4 | -2.58138 | -51.92497 | 2024-10-25 05:01:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |


[Clique aqui para ver as próximas entradas](README88.md)
