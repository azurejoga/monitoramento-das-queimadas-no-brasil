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

## Dados Diários - Página 27

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 86039ac1-e01f-3859-b042-d8ad0ebb7cc5 | -4.99982 | -46.03182 | 2024-11-02 03:49:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 82057f90-2c4c-3031-b3ca-9356ec46a5b5 | -4.22075 | -47.39233 | 2024-11-02 03:49:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| dbbddb94-0b2f-3413-bad7-25ff6462c2a4 | -4.5215 | -46.48629 | 2024-11-02 03:49:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d6c4c5d3-7d73-3bbc-ab06-94b55090c462 | -4.52078 | -46.49049 | 2024-11-02 03:49:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| e1a05c98-6aed-395e-844b-deb0aa048b04 | -4.30664 | -46.90128 | 2024-11-02 03:49:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9af94dfd-7026-32c2-b43f-1d56bdfd8469 | -4.3059 | -46.90549 | 2024-11-02 03:49:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 39d20512-570e-3b34-9779-7ea2a66f217d | -4.26225 | -46.85571 | 2024-11-02 03:49:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| db870699-c23e-340a-8893-c23038628260 | -4.2615 | -46.86015 | 2024-11-02 03:49:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 12cb4d5b-e9b5-3132-80a4-85eec1c964c9 | -4.25996 | -46.38506 | 2024-11-02 03:49:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f4799203-bfec-301e-8a59-60b64af676bf | -4.25981 | -46.38306 | 2024-11-02 03:49:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8b3164c4-cd47-3b83-b647-a0af16d82192 | -4.25928 | -46.3889 | 2024-11-02 03:49:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 29f56a70-e64a-3c9f-8c05-4d6e70c8407a | -4.25917 | -46.38686 | 2024-11-02 03:49:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1ae62e14-f64d-39ef-afba-7a756e4938fa | -4.25851 | -46.39077 | 2024-11-02 03:49:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 15b203e5-5737-3c9f-8b87-3d2c9bdf0c8e | -4.25639 | -46.85439 | 2024-11-02 03:49:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 71ca0c95-dd5f-3bce-984d-a55d35342c38 | -4.25562 | -46.85888 | 2024-11-02 03:49:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e248afeb-c769-33dc-b25c-049921583eef | -4.2542 | -46.3842 | 2024-11-02 03:49:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fccaa695-5a38-3a27-9f29-aadbeeca501c | -4.25406 | -46.38217 | 2024-11-02 03:49:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 13fc7ce7-a9e6-370c-90b5-58fb89c3659d | -4.25352 | -46.38805 | 2024-11-02 03:49:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 00d07b3a-87f1-3f3a-ae64-95884fcdffb5 | -4.25341 | -46.38604 | 2024-11-02 03:49:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 80c6db97-b0d6-3b16-ba50-c241b5910ced | -4.20261 | -46.71033 | 2024-11-02 03:49:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bad289ff-ceca-30c6-801e-31afae1ff5e8 | -4.19969 | -46.69272 | 2024-11-02 03:49:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a272f12c-0772-3422-b2d9-255b640a5da6 | -4.19897 | -46.69675 | 2024-11-02 03:49:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1c7ef8a7-d339-312a-a2bf-9cb35166b886 | -4.19755 | -46.70481 | 2024-11-02 03:49:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f36f5715-1c80-36ec-b960-d24235045451 | -4.7981 | -47.13334 | 2024-11-02 03:49:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a56a66cf-44b2-33c7-9211-707883a655a7 | -4.79465 | -47.12952 | 2024-11-02 03:49:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e0ae5134-400e-3a39-bcd0-66236aacb16d | -4.79389 | -47.13381 | 2024-11-02 03:49:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 86ee5b1b-f9d2-3fab-a48c-e50547bf60bf | -4.7922 | -47.13189 | 2024-11-02 03:49:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7a358248-c961-3e7b-b9a9-4a99b78e9522 | -4.77805 | -46.41035 | 2024-11-02 03:49:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 84825165-cc6d-3bd1-ac0d-1524afe22a17 | -4.77737 | -46.41434 | 2024-11-02 03:49:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c257cd08-2212-3770-9d9e-1c9581801e01 | -4.77296 | -46.40578 | 2024-11-02 03:49:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9e487a72-dd96-3495-b6b3-d432720f5ec1 | -4.7034 | -46.43411 | 2024-11-02 03:49:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0ecdc5c5-529f-3904-9c4f-9b576958a5e1 | -4.70269 | -46.43815 | 2024-11-02 03:49:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| d7beccfe-0927-3a4b-a36c-4cb0b38570ff | -4.70263 | -46.43386 | 2024-11-02 03:49:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9c41cfd4-dbae-3d03-9dbc-3e9c87453180 | -4.70195 | -46.43791 | 2024-11-02 03:49:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 0fdac8bc-bafe-39ef-aae4-dcfd70e4791f | -4.69767 | -46.43321 | 2024-11-02 03:49:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 53fd444a-69fb-35ee-a0ec-513de7694c25 | -4.69695 | -46.4373 | 2024-11-02 03:49:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 06aaa39f-2934-3828-a28f-0c188479bd19 | -4.6969 | -46.43293 | 2024-11-02 03:49:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5cc51fa1-5e0c-3fc7-a02d-6b0abd0cc1c3 | -4.69621 | -46.43703 | 2024-11-02 03:49:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 6b6b8850-2526-37bf-a8e3-17df1735e105 | -4.6758 | -46.38413 | 2024-11-02 03:49:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 61574769-9efd-3b30-98ae-4e6b3a447eae | -4.67514 | -46.38798 | 2024-11-02 03:49:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1f52dc77-ba74-3c68-9dcb-3ceab986dc35 | -4.663 | -46.3221 | 2024-11-02 03:49:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| aeff65e5-be91-35dd-979f-a30d5ceac456 | -4.65802 | -46.31708 | 2024-11-02 03:49:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 65ac93f1-9174-36dc-9007-6c226f283638 | -4.65731 | -46.32115 | 2024-11-02 03:49:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9721bd28-b082-3428-a7eb-50b0be6f66d9 | -4.65649 | -46.60193 | 2024-11-02 03:49:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 9b9464ce-bc90-34d5-a128-c49eddd99728 | -4.65603 | -46.60188 | 2024-11-02 03:49:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 6d99f534-5c42-3810-8db3-c770ba3d1dbc | -5.53744 | -46.79875 | 2024-11-02 03:49:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| c931a272-0ec2-3c94-a59b-f80722bb9056 | -5.53673 | -46.80279 | 2024-11-02 03:49:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| d008e2c9-37b3-3d67-9f95-467435ce0e6f | -5.43388 | -46.50121 | 2024-11-02 03:49:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 49047264-74c8-38ed-bc03-c8a9df033404 | -5.43325 | -46.50485 | 2024-11-02 03:49:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d694283f-e973-37ee-a494-b10e536776e6 | -5.35764 | -47.35426 | 2024-11-02 03:49:00 | NPP-375D | JOÃO LISBOA | MARANHÃO | Brasil | 2105500 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1b274ee8-cab5-390e-89e6-ba42e4a6bee8 | -5.35166 | -47.35309 | 2024-11-02 03:49:00 | NPP-375D | JOÃO LISBOA | MARANHÃO | Brasil | 2105500 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6b5e2eeb-8e75-3354-ad88-851ac14e71e8 | -5.2922 | -47.37419 | 2024-11-02 03:49:00 | NPP-375D | JOÃO LISBOA | MARANHÃO | Brasil | 2105500 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 1b40e6c2-e3a9-3178-8683-3504bd395082 | -5.29139 | -47.37872 | 2024-11-02 03:49:00 | NPP-375D | JOÃO LISBOA | MARANHÃO | Brasil | 2105500 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 737cfb0d-6fe5-3bd9-8533-d888bd167e2d | -5.2902 | -47.37578 | 2024-11-02 03:49:00 | NPP-375D | JOÃO LISBOA | MARANHÃO | Brasil | 2105500 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 7742b1ca-916e-398d-8e55-2810936cc5c3 | -11.82356 | -48.76055 | 2024-11-02 03:49:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7a917716-2f3c-3f46-9848-94ab573da4ea | -11.82271 | -48.76485 | 2024-11-02 03:49:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 55e64742-ad9d-33e4-8957-5e7a1b0b60b3 | -11.81683 | -48.76371 | 2024-11-02 03:49:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 1162578f-3bc8-33b2-9584-059b66c43678 | -11.81597 | -48.76805 | 2024-11-02 03:49:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| ebe2b166-8d48-3e53-a231-3ccbfb9ba758 | -11.66233 | -48.79901 | 2024-11-02 03:49:00 | NPP-375D | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ce1cd0f4-96f8-3296-8fa8-ceff657f18d3 | -11.66152 | -48.80321 | 2024-11-02 03:49:00 | NPP-375D | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8ebade21-5e2c-393b-b648-15f13dd71e94 | -11.6593 | -48.80085 | 2024-11-02 03:49:00 | NPP-375D | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| ad7d69d9-705e-3349-8a34-1ee82d14aa3f | -11.65845 | -48.80508 | 2024-11-02 03:49:00 | NPP-375D | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 368208c5-e401-31ce-8ea8-0c33f9557e90 | -11.65562 | -48.802 | 2024-11-02 03:49:00 | NPP-375D | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ec80aaa6-067c-3d83-8286-240d67321936 | -4.35924 | -48.60498 | 2024-11-02 03:49:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| b5f9aa43-8cf0-387c-ab47-fe4180a83ffa | -4.35825 | -48.61063 | 2024-11-02 03:49:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 6fa908fc-fafc-37b4-8408-287b47c41746 | -4.35729 | -48.61606 | 2024-11-02 03:49:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 3fcb49c2-3082-3a6e-918a-577e7997dc3c | -4.35265 | -48.60395 | 2024-11-02 03:49:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 26487c55-9cb9-3fc1-aace-b2439763bf1f | -4.3517 | -48.60931 | 2024-11-02 03:49:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| e973b2c0-9d50-36fb-8eec-1d94735d6429 | -4.35164 | -48.15723 | 2024-11-02 03:49:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| b7bb2cdb-4e41-3ed6-9925-029fe5445265 | -4.35074 | -48.61474 | 2024-11-02 03:49:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| f3283c96-b1ff-3c6b-9734-a76620268a08 | -4.33777 | -48.58665 | 2024-11-02 03:49:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 01d32c04-bff5-3a5a-b56f-f9e3be684e9f | -4.33687 | -48.5919 | 2024-11-02 03:49:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 091af891-cda6-383e-8e31-57b17933a9fa | -4.33498 | -48.58884 | 2024-11-02 03:49:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| c6adabfa-be5f-347b-ac16-ac0ce84b35da | -4.33122 | -48.58536 | 2024-11-02 03:49:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 912b1d50-1c18-3d11-b5ab-babaa3348022 | -4.33029 | -48.59076 | 2024-11-02 03:49:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 08499409-e63a-371d-8849-0cb337270ea2 | -4.32842 | -48.58763 | 2024-11-02 03:49:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 2e7c4adf-7818-3a31-8862-77c736897e5e | -4.32729 | -48.648 | 2024-11-02 03:49:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ce93f282-180e-391e-8806-378053f9fde7 | -4.326 | -48.63932 | 2024-11-02 03:49:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c28f1ba2-db34-3468-b0e1-26e5b32fa5a2 | -4.32504 | -48.64473 | 2024-11-02 03:49:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5fabe4e8-118c-3952-9f44-61047a487d44 | -4.3216 | -48.64149 | 2024-11-02 03:49:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 946550fa-19ae-3cc0-9d35-9227578522c3 | -4.32065 | -48.64708 | 2024-11-02 03:49:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 789d2007-8bda-3f98-bc5a-b14308d41caa | -4.31839 | -48.64386 | 2024-11-02 03:49:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0a47a923-2b76-34a8-8ce1-76007f03843f | -4.30381 | -48.62646 | 2024-11-02 03:49:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1fe91176-1262-34db-98c4-e0400482839b | -4.30168 | -48.62329 | 2024-11-02 03:49:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 50db97ff-1f1a-3049-84d8-668e562f3159 | -4.30066 | -48.62897 | 2024-11-02 03:49:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 692bfa66-49cc-32e4-be71-c3f9069a69e6 | -4.29818 | -48.61972 | 2024-11-02 03:49:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c3325aab-039b-37b0-92ca-c6d62e5bbc26 | -4.29719 | -48.62543 | 2024-11-02 03:49:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c16c7ae7-f0b5-3501-93e6-478b466eb892 | -4.29508 | -48.6222 | 2024-11-02 03:49:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b4466ab8-a6da-3620-8210-8f979f56bbdc | -3.95116 | -48.36085 | 2024-11-02 03:49:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 0ee5543e-87d8-3c8e-8392-4f74e3519026 | -3.94978 | -48.36065 | 2024-11-02 03:49:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 983d519d-8f45-35a7-a78b-9ddccd40d07e | -3.94557 | -48.35419 | 2024-11-02 03:49:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 7840c8aa-4584-3801-b8d3-0281e24fb664 | -3.9452 | -48.34853 | 2024-11-02 03:49:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8f5e57f5-cec9-395b-9d7c-d08ad7c75be3 | -3.94461 | -48.35989 | 2024-11-02 03:49:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 7a096a1e-1d03-3846-9b19-12be64a17d30 | -3.94424 | -48.35398 | 2024-11-02 03:49:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 6e8c1bf6-a8cf-321f-a5c4-9ac45e35c3ba | -3.94324 | -48.35964 | 2024-11-02 03:49:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| c2d3997e-e721-3e60-a84c-788197f6bee6 | -3.94001 | -48.34742 | 2024-11-02 03:49:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 7b6e0fec-a4be-3a54-9df8-f8d1a155ac76 | -3.93908 | -48.35288 | 2024-11-02 03:49:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 709891bf-45fd-3db0-a762-00e6614cca87 | -3.93871 | -48.34722 | 2024-11-02 03:49:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 2e55d0c6-c19d-33ba-b08b-7d35d153782d | -3.9381 | -48.35864 | 2024-11-02 03:49:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| f9af5a07-f0fb-30c7-9f48-20797f6e7653 | -3.93775 | -48.35268 | 2024-11-02 03:49:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |


[Clique aqui para ver as próximas entradas](README28.md)
