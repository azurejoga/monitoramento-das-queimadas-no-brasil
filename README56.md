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

## Dados Diários - Página 56

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f98e431b-d937-34e6-a93f-09dc497e4910 | -3.08446 | -51.07532 | 2024-12-02 04:48:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e3889eb1-767a-323a-a847-a6369880c239 | -1.94941 | -53.34728 | 2024-12-02 04:48:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 34564019-96ca-38f1-b43c-92019af3a627 | -3.11047 | -54.18584 | 2024-12-02 04:48:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9cecf6ae-808d-3d6f-be4f-ee38bdcbb66a | -4.18688 | -50.66985 | 2024-12-02 04:48:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b2dbfbfa-8314-373e-8327-15757f7a4bdb | -2.8032 | -54.04477 | 2024-12-02 04:48:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6264cde8-5cfb-3754-8a2c-a28c07678767 | -3.18858 | -54.33269 | 2024-12-02 04:48:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 9527a946-5d4b-3713-ab62-cc78ebdcf95e | -2.90842 | -54.11215 | 2024-12-02 04:48:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0981a76e-3193-3c73-a63a-b85fdac0a1ee | -3.09843 | -54.01531 | 2024-12-02 04:48:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7f2bd099-258d-31b1-8155-01868e876951 | -3.27939 | -50.60738 | 2024-12-02 04:48:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8a746e0f-1b53-3869-bb25-556cf0ba5d59 | -4.59629 | -50.83162 | 2024-12-02 04:48:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 515151e2-2a66-32db-b12c-ecf6a9cf7a3c | -2.97929 | -53.88111 | 2024-12-02 04:48:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 07e6ed46-44bc-3784-80ba-1c38d325338d | -1.08967 | -53.64003 | 2024-12-02 04:48:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3052caa2-624d-3e28-8ad0-01bcef36b2b0 | -3.21509 | -54.23325 | 2024-12-02 04:48:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 9f5c7c84-8ff3-36aa-b3e5-fb5a342213d7 | -2.2698 | -53.60427 | 2024-12-02 04:48:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 65cdc26f-de89-3bfb-8caf-9de22eeedd73 | -3.37351 | -49.86267 | 2024-12-02 04:48:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 83cad4f2-8316-359c-ba46-c2a54a2ad97c | -1.44743 | -54.54162 | 2024-12-02 04:48:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6d444536-d3e4-3fd1-9f0f-0489baba2f44 | -3.27752 | -48.78438 | 2024-12-02 04:48:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f6894229-defb-3430-9245-d7375787f9e4 | -2.89989 | -54.16613 | 2024-12-02 04:48:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 69d749a7-c1be-33f4-8b7e-28e1004421af | -4.67821 | -46.37137 | 2024-12-02 04:48:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 507d911c-2b63-3a4f-a2dc-76acd762f8af | -2.64375 | -54.09545 | 2024-12-02 04:48:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2ca21258-8a87-35ef-a477-3bc9499aa218 | -3.64956 | -49.88869 | 2024-12-02 04:48:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 516cbafe-9632-3913-8cb7-f6fdafcb801e | -3.18797 | -54.33655 | 2024-12-02 04:48:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| e0ab6c6d-3571-3bca-9638-2a4eae483013 | -2.02987 | -52.07804 | 2024-12-02 04:48:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 185e6824-6b54-3775-bf80-c287413ac262 | -1.0114 | -51.72764 | 2024-12-02 04:48:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 815bbf7e-ddef-35de-8a73-35171f2edece | -2.41637 | -48.87944 | 2024-12-02 04:48:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 30244a04-e49e-39c1-8663-6e0c2816763c | -2.98255 | -53.90485 | 2024-12-02 04:48:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 9f1e366a-6d65-3413-bf3c-669858aa7bce | -1.49435 | -51.94125 | 2024-12-02 04:48:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e66819f1-fbb6-3862-a878-908cfa156564 | -3.28679 | -53.66912 | 2024-12-02 04:48:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b6a3a654-dca8-37a6-bc20-00863c8f7a75 | -2.4829 | -46.57259 | 2024-12-02 04:48:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ff15de5b-5f08-37ee-98b2-021ffcab769f | -3.25115 | -53.62952 | 2024-12-02 04:48:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8b984f9a-964a-37bd-9a66-0599c20727fc | -3.10838 | -53.99742 | 2024-12-02 04:48:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 15d2a83d-4575-3a98-8a42-52870dacf01d | -3.27161 | -48.7751 | 2024-12-02 04:48:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9f59e718-38e4-36e2-a21f-e897e266ead9 | -2.45337 | -54.01595 | 2024-12-02 04:48:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0940b75d-95d7-319e-a2d6-4a05faa835f0 | -1.99624 | -52.09757 | 2024-12-02 04:48:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a8c4dc79-6faa-3e94-a171-dc2fe890e62b | -1.82701 | -47.28658 | 2024-12-02 04:48:00 | NOAA-20 | IRITUIA | PARÁ | Brasil | 1503507 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 97e775c3-daa4-3b14-8f24-c1da6e59984e | 1.14385 | -55.9726 | 2024-12-02 04:48:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e7bb4f00-3795-3acb-9db5-683c22cfa723 | -1.59923 | -51.2747 | 2024-12-02 04:48:00 | NOAA-20 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f7b2c25d-b980-3348-9c93-c9383e581056 | -1.5829 | -52.28532 | 2024-12-02 04:48:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4f6cbd2d-3b17-314d-8275-dbe9b8e55c22 | -2.87152 | -54.00827 | 2024-12-02 04:48:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 98fac24c-889d-3d59-b2e0-d32f92c4b90e | -3.79308 | -51.2571 | 2024-12-02 04:48:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| da005ddf-d60d-3cff-b154-ac3fa1c75a47 | -3.74916 | -52.27044 | 2024-12-02 04:48:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| eab9d698-f25a-3900-9125-3cb305b389af | -2.82033 | -54.19353 | 2024-12-02 04:48:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 30054d3d-ca87-32af-9494-e80df347a959 | -3.96243 | -54.65906 | 2024-12-02 04:48:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 680acc28-16a4-34cb-87b3-c33805dff451 | -2.79456 | -48.68306 | 2024-12-02 04:48:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 89ba4e26-1d8f-383e-b903-44a653c8070c | -4.52675 | -45.74261 | 2024-12-02 04:48:00 | NOAA-20 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 894882d4-6549-301a-bf56-9999b2d9d896 | -1.45122 | -55.1904 | 2024-12-02 04:48:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 2dcad31d-016e-3168-a0bd-3827cfb3f422 | -4.07219 | -49.07079 | 2024-12-02 04:48:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6255b7bd-906d-38d1-b71b-a4169aa8be43 | -1.95819 | -46.44278 | 2024-12-02 04:48:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| daccc551-eeaa-3e71-af7a-23653d1872af | -3.3922 | -50.30309 | 2024-12-02 04:48:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 43cf35c4-5fef-3f35-a13b-f68e5f73f2e9 | -2.33552 | -50.67439 | 2024-12-02 04:48:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 83c2fa7b-ba38-3709-ae15-196cc26106f6 | -2.36226 | -53.68327 | 2024-12-02 04:48:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e4d0c378-251e-3e42-a1e0-e3ffa0ec6e3a | -1.88481 | -53.29203 | 2024-12-02 04:48:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1b8fa043-3ca4-3ed8-8855-97ba46f4b1d5 | -2.86019 | -48.55653 | 2024-12-02 04:48:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0d4315a1-1cc1-38f7-9fa7-7106820a6e51 | -3.10802 | -53.27275 | 2024-12-02 04:48:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 7814b083-4798-3d45-ac7c-6adc155422d2 | -4.64257 | -46.90127 | 2024-12-02 04:48:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7aa88890-e09a-38b7-a2c6-c0109ba77296 | -2.9659 | -53.89841 | 2024-12-02 04:48:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 29a81c8f-fa63-3da8-a301-ce85dd931009 | -1.34947 | -55.17146 | 2024-12-02 04:48:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 406f7af6-a1f3-3e69-9356-bf852f2670cc | -1.17986 | -52.12622 | 2024-12-02 04:48:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e55855f7-22ab-3ddf-9552-91786b73ab6c | -2.20117 | -48.33777 | 2024-12-02 04:48:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 991155ca-6245-3d00-bfad-9f8d8280b894 | -1.61528 | -52.29428 | 2024-12-02 04:48:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 74c327cb-ce84-390b-8910-ae15efb24291 | -1.57367 | -51.20039 | 2024-12-02 04:48:00 | NOAA-20 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 173a72af-ba4e-3a8c-9dec-e3ebda315b45 | -3.49493 | -53.83794 | 2024-12-02 04:48:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| dda93319-939a-31f2-b2f0-cf4a7d4cff10 | -1.00755 | -51.73057 | 2024-12-02 04:48:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c6042209-2a43-3107-a4e7-50428bddf823 | -2.74678 | -51.75351 | 2024-12-02 04:48:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 25dfa465-7b56-3392-8799-6d5110462bd3 | -2.55321 | -53.40985 | 2024-12-02 04:48:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 38968b18-61d0-30ed-bdd5-b5b2127044e6 | -3.81951 | -52.08438 | 2024-12-02 04:48:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a324bebc-1a5d-33e0-904c-7fedf3df1671 | -2.48311 | -46.57654 | 2024-12-02 04:48:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1e30b4a8-7a67-30d0-ba8e-0cc9bee1ac38 | -3.53995 | -51.02874 | 2024-12-02 04:48:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ffefdbff-b595-35c7-94b2-efa634947646 | -1.09887 | -53.36009 | 2024-12-02 04:48:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5aa98d53-1138-33b1-8927-ee0d4fcef0bd | -0.98102 | -51.70529 | 2024-12-02 04:48:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6545c943-d42f-3464-8844-72701bda72f5 | -2.97203 | -53.29234 | 2024-12-02 04:48:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 630ac53b-23e6-31dd-a844-35e0aaf468f1 | -3.03527 | -54.04128 | 2024-12-02 04:48:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2e081af0-a21f-39d5-a342-2d5a9a034b83 | -3.16457 | -49.02393 | 2024-12-02 04:48:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bdd7c607-3395-33d4-b6ed-8de08a9e10cc | -2.84743 | -54.04752 | 2024-12-02 04:48:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ca56a8f0-0a38-308e-a47a-b307793530b9 | -4.20209 | -50.23541 | 2024-12-02 04:48:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 56cca52e-8bad-39ac-8ba6-bf2c63e43749 | -2.20413 | -48.34251 | 2024-12-02 04:48:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6e47c634-ac20-3386-babb-1f8f90c554bf | -2.3002 | -57.08292 | 2024-12-02 04:48:00 | NOAA-20 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ddee66b3-6150-33ff-adc7-46a8ca3f1e0e | -3.10744 | -54.04783 | 2024-12-02 04:48:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| df43d037-eb77-3237-895f-6022536525e2 | -3.11591 | -53.99469 | 2024-12-02 04:48:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| a5efc880-4c85-3320-b845-c0cf11a76ddf | -2.00111 | -51.18262 | 2024-12-02 04:48:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3b75dada-7c45-30f0-a4d9-d22d4d0cd6bd | -1.14107 | -53.67516 | 2024-12-02 04:48:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 07bd9d1a-ffe7-3a1d-bd4d-f3cf9ec9c22f | -3.80385 | -49.73106 | 2024-12-02 04:48:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 586e53a8-fc03-3b89-a3b4-ddbc740c81cd | -3.69984 | -47.11996 | 2024-12-02 04:48:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| aa9412af-ece6-3f4c-a1b3-cdf5be3fb837 | -1.80713 | -48.77126 | 2024-12-02 04:48:00 | NOAA-20 | ABAETETUBA | PARÁ | Brasil | 1500107 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a98b5ba3-813e-3633-b76a-7d7911cd8fbd | -3.74639 | -52.26648 | 2024-12-02 04:48:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5b57b387-60eb-3a4e-a8cd-d34cd8516548 | -2.55777 | -53.40309 | 2024-12-02 04:48:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| c3814d90-0143-388f-ad22-11b515b9a458 | -2.45995 | -53.62215 | 2024-12-02 04:48:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 35a1b55d-611f-3c94-81d0-670f97fed3fc | -1.63323 | -53.86399 | 2024-12-02 04:48:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 34f72b21-a480-3ecb-bc48-3cc0629ea2a3 | -1.50334 | -51.19257 | 2024-12-02 04:48:00 | NOAA-20 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 812e11aa-7d38-3384-a35e-cec88ea6573f | -2.56568 | -53.99261 | 2024-12-02 04:48:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c1a3e377-0be8-3711-b488-91e1f57098a5 | -2.63403 | -54.20108 | 2024-12-02 04:48:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1469c0b5-8c18-3368-ae04-c500e9178211 | -3.42631 | -49.99529 | 2024-12-02 04:48:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| dfb2e3c6-f0c3-3527-9adf-df382a8286a7 | -1.39008 | -51.58978 | 2024-12-02 04:48:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2d95b42f-df3b-3d6a-bb87-34dda63b2bdf | -3.05555 | -51.7139 | 2024-12-02 04:48:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fdfd2e44-ca3c-3dd2-86a4-e0bb9d1e1dbb | -2.9024 | -51.36967 | 2024-12-02 04:48:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e484f5be-0259-3d42-b429-c3dfeba82be9 | -1.67311 | -52.10052 | 2024-12-02 04:48:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b715e32a-0d03-37a8-ba04-6cab8a918410 | -4.45027 | -47.62042 | 2024-12-02 04:48:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| cbd24c78-c317-3b57-8e91-c8c503efeb87 | -3.09812 | -54.12875 | 2024-12-02 04:48:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0c4446fe-f052-3a6c-8e48-52b4df1e5645 | -2.1121 | -50.36268 | 2024-12-02 04:48:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 741618b5-655d-30f3-8dc8-1a84728925a6 | -2.45291 | -48.16327 | 2024-12-02 04:48:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |


[Clique aqui para ver as próximas entradas](README57.md)
