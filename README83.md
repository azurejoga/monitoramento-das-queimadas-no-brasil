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

## Dados Diários - Página 83

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9eb29c50-3187-3fc6-ab43-7411f9fa942b | -3.28638 | -53.68582 | 2024-10-26 04:44:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7184d7e2-0ffe-3742-86af-c4bb445a0f62 | -3.28343 | -53.68103 | 2024-10-26 04:44:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a8a91344-63c3-38e4-be81-09baeffa81a2 | -3.27979 | -53.68043 | 2024-10-26 04:44:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fc7b19b4-0184-39ad-97aa-ee86bed01454 | -3.2791 | -53.68466 | 2024-10-26 04:44:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5d0b1c64-95a5-3984-be37-8a7b3695f03d | -3.74385 | -53.40956 | 2024-10-26 04:44:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 2d12b06c-f566-3f09-89f8-0a4bf7ce071e | -3.74319 | -53.41362 | 2024-10-26 04:44:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 47294032-cb5f-3f95-90d6-c7b4ff358f52 | -3.74123 | -53.40999 | 2024-10-26 04:44:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 56ced18b-d0e8-3868-9138-cc4e20204dd2 | -3.74059 | -53.41407 | 2024-10-26 04:44:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7e6b60dd-c9ba-3667-9f35-58e389994993 | -3.73546 | -53.73489 | 2024-10-26 04:44:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 38e02f9c-4f60-3f27-b671-f3f30be7dc39 | -3.69123 | -53.4479 | 2024-10-26 04:44:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1a3bd9d0-e45c-3ca1-8e7f-1f12f3536fc9 | -3.68667 | -53.43048 | 2024-10-26 04:44:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 514c7f92-39e3-3fc3-9cd0-e8622222572e | -4.18811 | -53.669 | 2024-10-26 04:44:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fc58aa99-70e5-3947-b3d0-752726b0dfe6 | -4.16115 | -53.69865 | 2024-10-26 04:44:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f976ba0f-341b-3602-8116-87d4a3c0a39d | -3.98953 | -53.80747 | 2024-10-26 04:44:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1f87cfc1-c97f-370a-a161-893567f49605 | -3.98657 | -53.80265 | 2024-10-26 04:44:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| e3d52819-3db9-3fea-9734-dca77576ff10 | -3.98589 | -53.80691 | 2024-10-26 04:44:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7a46bbe2-2f69-3f8b-9496-9fb89a54c36c | -3.93757 | -53.47255 | 2024-10-26 04:44:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 92855700-b85a-39e3-924d-0a2b0109909c | -3.87006 | -53.8284 | 2024-10-26 04:44:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 45c15513-78d2-3c57-970f-5b4db4ac0b7e | -3.9079 | -52.39702 | 2024-10-26 04:44:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| d9f4cc64-7d03-3082-834c-e74f58295cf5 | -3.90508 | -52.39281 | 2024-10-26 04:44:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8eb50c7f-cbc3-373b-9ae5-c84640bc78d3 | -3.84093 | -52.3981 | 2024-10-26 04:44:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 9aa8537e-249b-39f2-a916-cf2ef9092995 | -3.84035 | -52.40176 | 2024-10-26 04:44:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 8ad95f0c-d789-3729-b1e6-a5b26d114bea | -3.83976 | -52.40544 | 2024-10-26 04:44:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 6da81900-1b46-3e20-8ea2-2440fa3b465f | -3.83693 | -52.40125 | 2024-10-26 04:44:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| faa17047-2537-3756-8d54-a6360e49f544 | -3.83634 | -52.40491 | 2024-10-26 04:44:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2364b735-8b7e-38d2-a042-7b67859a2aa5 | -3.8339 | -52.33263 | 2024-10-26 04:44:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 334cd25e-a5f4-335b-be7a-96d3142996a0 | -3.78334 | -52.38567 | 2024-10-26 04:44:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6fbada9c-c7c7-387a-92ae-e65ea2c3d695 | -3.78 | -52.36245 | 2024-10-26 04:44:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d94afe1c-6a57-39c3-a969-4a983fe10803 | -3.77943 | -52.3661 | 2024-10-26 04:44:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7a94003a-f7a5-3c5b-bd27-ad7dfd70d167 | -6.23249 | -53.90953 | 2024-10-26 04:44:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 55a8840a-b11f-3620-bc01-a05e1d79508d | -10.793 | -53.86518 | 2024-10-26 04:44:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1845fd18-b38d-36f4-bbbc-46943ddff66e | -10.7896 | -53.8646 | 2024-10-26 04:44:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ff17b98d-20fc-3dce-9397-8bf36da9dc04 | -10.78619 | -53.86404 | 2024-10-26 04:44:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 17b2b6d7-642c-3576-b3cf-d51f8fb9c160 | -10.78558 | -53.86777 | 2024-10-26 04:44:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 420dd647-02df-35da-adbd-b9b07699233c | -10.7834 | -53.85973 | 2024-10-26 04:44:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 38f3882b-2fe1-3171-bb3d-d0e63d754295 | -10.78279 | -53.86346 | 2024-10-26 04:44:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 67d6ed96-a313-3dc1-9242-7e5d044d7c02 | -10.77781 | -53.85116 | 2024-10-26 04:44:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4c052dca-e56b-318b-a51d-2fa072a7ea43 | -10.7772 | -53.85488 | 2024-10-26 04:44:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c5a4d1ec-0399-375c-b5bd-e4eba8691bc2 | -3.66141 | -53.84549 | 2024-10-26 04:44:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 9adf3e28-0cd2-3787-b2e8-0ab8bee24557 | -3.66074 | -53.84971 | 2024-10-26 04:44:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 38302df7-8162-3bc2-8d51-518e61de6771 | -3.65773 | -53.84504 | 2024-10-26 04:44:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 12.5 |
| acc171b6-a148-34b8-92cf-af4a8e707e6f | -3.65706 | -53.84926 | 2024-10-26 04:44:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 12.5 |
| cab6d3a2-18f8-3414-9cdf-fd5c5b3e2589 | -3.65271 | -54.22427 | 2024-10-26 04:44:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4ab220c9-74cd-3ca5-9ece-e704e42bec33 | -3.64899 | -54.22359 | 2024-10-26 04:44:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fa6588fc-e0ec-3cf9-8051-a9362ce77376 | -3.63429 | -53.96922 | 2024-10-26 04:44:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 04040ae2-08e8-3ff6-b8e6-5b7b9ac280ce | -3.6306 | -53.96868 | 2024-10-26 04:44:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6e24932f-de02-3923-830e-c214b3a33e7e | -3.61212 | -54.03734 | 2024-10-26 04:44:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 59fd04f3-e9d6-34a7-9afe-cd76672466a9 | -3.61141 | -54.04181 | 2024-10-26 04:44:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 77749e30-e65e-3109-aedf-5c7630aedced | -3.5916 | -53.79045 | 2024-10-26 04:44:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 60e2962f-e995-3ade-9ad3-8ad49f5ba3f2 | -3.58558 | -54.66305 | 2024-10-26 04:44:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 543e94b9-ff90-3650-9a6b-3b5f0d86c884 | -3.58175 | -54.66239 | 2024-10-26 04:44:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7d7dc3a6-4bb3-350a-8334-7366b8c003fe | -3.58098 | -54.66713 | 2024-10-26 04:44:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 962e3e85-e884-3926-88fe-b5c723b4f9c4 | -3.58061 | -54.0683 | 2024-10-26 04:44:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6d119daa-5784-399f-97a2-ae4d9f82bcd7 | -3.57869 | -54.6328 | 2024-10-26 04:44:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| f89d776f-0e59-34b0-9d3a-d37835f5adb6 | -3.57486 | -54.63223 | 2024-10-26 04:44:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| a18c2c77-80c0-375c-a174-65aa467b0bee | -3.57409 | -54.63696 | 2024-10-26 04:44:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| f65c1e59-39c5-305b-95bb-3cfe6cd2ed0d | -3.55423 | -53.997 | 2024-10-26 04:44:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ba696204-1608-3063-a98f-4355af86060c | -3.55126 | -53.99199 | 2024-10-26 04:44:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 404ccf11-a251-31d5-bd29-e89666e432aa | -3.15168 | -54.34847 | 2024-10-26 04:44:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1c2372f9-e1bf-397d-a0f8-5e37208ba1af | -3.15145 | -54.35038 | 2024-10-26 04:44:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 646f1542-bc16-36e2-a807-6118e247eefe | -3.15093 | -54.35304 | 2024-10-26 04:44:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 03a1a450-8d9e-3eb1-a0b5-48afe52f7ec9 | -3.13828 | -54.28663 | 2024-10-26 04:44:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a6e1591f-1534-390a-a1ff-2f34da019183 | -3.13754 | -54.29127 | 2024-10-26 04:44:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| da0cd060-9895-3578-9c36-5688faacc33b | -3.13596 | -54.27687 | 2024-10-26 04:44:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7bc5855a-f1ac-3299-8b14-7c9c378d25f4 | -3.13524 | -54.28142 | 2024-10-26 04:44:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7fa9db30-f245-3c01-9e21-6268cbde3a70 | -3.13292 | -54.27171 | 2024-10-26 04:44:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3096df21-39cf-325c-a409-9dfae9dd9b95 | -3.1322 | -54.27624 | 2024-10-26 04:44:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 0cacd7d3-901c-31bc-9e8f-beb7292d0899 | -3.13147 | -54.28079 | 2024-10-26 04:44:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 3587e4cf-f7ec-37e7-9393-005bdab616cb | -3.12916 | -54.27107 | 2024-10-26 04:44:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 378b8e83-688c-3b51-98f7-7c4a25c16235 | -3.12843 | -54.27561 | 2024-10-26 04:44:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 9d2daddb-ff45-39ba-a1c2-c87dcd1e767d | -3.12466 | -54.27499 | 2024-10-26 04:44:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7f93902a-1a5b-39dd-b9de-ba949bab6398 | -3.11006 | -54.99398 | 2024-10-26 04:44:00 | NOAA-20 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 881c38c0-b379-3d8f-be7f-6bb104d8ff2e | -3.10762 | -54.16524 | 2024-10-26 04:44:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fb97ff53-cfed-34cb-a521-3abcc1bd291d | -3.1069 | -54.16968 | 2024-10-26 04:44:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c2a95c99-b7b4-3794-ad2b-099fdb6dec95 | -3.10675 | -54.1469 | 2024-10-26 04:44:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a1f16074-ff1c-373c-94fd-f087d21d0f00 | -3.10603 | -54.15136 | 2024-10-26 04:44:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 115219aa-2dbb-35ac-9b3c-5b0a41758398 | -3.10387 | -54.16465 | 2024-10-26 04:44:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| b3dba1d7-f753-3db9-bcc1-2353e3224497 | -3.10315 | -54.16908 | 2024-10-26 04:44:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| d93fb404-6601-3ac1-9f63-e5bbab29247e | -3.10228 | -54.15077 | 2024-10-26 04:44:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 784fdab3-d93c-3e47-b260-8d51d7204713 | -3.08726 | -54.43563 | 2024-10-26 04:44:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 0f5d9b9f-2ac2-3c64-96e5-a2ad6d8120d4 | -3.04108 | -54.84752 | 2024-10-26 04:44:00 | NOAA-20 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ba389739-0a33-3810-921e-bfb21967e7e2 | -3.5097 | -54.02314 | 2024-10-26 04:44:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a119e06f-afba-39eb-a86d-5947f29e4fd6 | -3.506 | -54.02256 | 2024-10-26 04:44:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3a3f920d-e2df-3fd4-b2f6-73dfb306eda0 | -3.50477 | -54.6861 | 2024-10-26 04:44:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e19c6e3e-36ca-336f-8d4c-070f36e819eb | -3.50129 | -54.44035 | 2024-10-26 04:44:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c13fecdd-7323-3b49-b6ac-5cff8c2ab1e7 | -3.49751 | -54.43971 | 2024-10-26 04:44:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c51ed6a2-18e2-38d0-aa3b-6c92639f8bf6 | -3.49373 | -54.43905 | 2024-10-26 04:44:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 484bc68a-deae-3ed1-ab77-1fb29f92a822 | -3.49296 | -54.4438 | 2024-10-26 04:44:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6c55d0dd-a126-3215-b655-ab3a78a999dc | -3.48995 | -54.43839 | 2024-10-26 04:44:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5727d4c4-548f-30cb-a90f-c2fca60ff849 | -3.48917 | -54.44315 | 2024-10-26 04:44:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2f7d4109-3e22-3f1d-96b0-ec3ff2405b6d | -3.48617 | -54.43776 | 2024-10-26 04:44:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 5d556537-20db-38b0-834f-8cdbe55a40d5 | -3.48614 | -54.46173 | 2024-10-26 04:44:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 62559841-8fff-3c32-88b6-7dd639634444 | -3.48486 | -54.15538 | 2024-10-26 04:44:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 084fa6e7-4f82-305b-9195-3ca8d51f6264 | -3.48462 | -54.4472 | 2024-10-26 04:44:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7c973784-0912-37e1-b9b6-01bf1dc22ecb | -3.48235 | -54.46114 | 2024-10-26 04:44:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d75da61d-7874-3aca-812d-c6fb140d3e6c | -3.4816 | -54.46574 | 2024-10-26 04:44:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9909eae6-b946-3dd0-ada8-753bf7444efb | -3.48134 | -53.98724 | 2024-10-26 04:44:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 350280cc-6ebb-380c-b641-221c65aa0d56 | -3.47764 | -53.98668 | 2024-10-26 04:44:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 6e034c91-a0b4-3a0f-8842-43a62c967fba | -3.46794 | -54.52538 | 2024-10-26 04:44:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| fdf3e206-2113-3b25-a09f-4f350771c8cf | -3.46413 | -54.52481 | 2024-10-26 04:44:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |


[Clique aqui para ver as próximas entradas](README84.md)
