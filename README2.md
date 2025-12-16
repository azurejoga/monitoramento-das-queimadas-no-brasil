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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4730830b-7fa7-3aa7-8c91-7cd284b9a9f0 | -3.29809 | -43.46928 | 2025-12-16 00:13:00 | TERRA_M-M | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 18.3 |
| 56da2ab8-7871-3000-a9fe-caadb9ac32e4 | -2.08915 | -46.15852 | 2025-12-16 00:13:00 | TERRA_M-M | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 5.7 |
| fbbbfa58-9552-3b97-b09f-d4c71a4b80be | -1.61107 | -45.9049 | 2025-12-16 00:13:00 | TERRA_M-M | AMAPÁ DO MARANHÃO | MARANHÃO | Brasil | 2100550 | 21 | 33 | nan | nan | nan | Amazônia | 9.2 |
| a44eb6ee-a023-3b08-b8ba-36a7e1bd8a78 | -2.29667 | -45.53159 | 2025-12-16 00:13:00 | TERRA_M-M | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 0ca879de-e359-33f6-98f7-2d1be3e2af0c | -1.60984 | -45.89601 | 2025-12-16 00:13:00 | TERRA_M-M | AMAPÁ DO MARANHÃO | MARANHÃO | Brasil | 2100550 | 21 | 33 | nan | nan | nan | Amazônia | 12.3 |
| 13a262a5-1dc7-34c7-8763-2778239e9074 | -3.56568 | -47.17958 | 2025-12-16 00:13:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 17.5 |
| ca8decc5-14e2-3c60-b306-e882289f8c8d | -4.108 | -45.7041 | 2025-12-16 00:13:00 | TERRA_M-M | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 13.8 |
| e2492982-c86a-3441-8a8c-a4b7639d1953 | -2.6117 | -45.4075 | 2025-12-16 00:13:00 | TERRA_M-M | PRESIDENTE SARNEY | MARANHÃO | Brasil | 2109270 | 21 | 33 | nan | nan | nan | Amazônia | 5.8 |
| bb7f900b-39be-3fe2-b7c9-6f6515a49fa7 | -2.56897 | -45.56616 | 2025-12-16 00:13:00 | TERRA_M-M | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 80fc5a0a-aded-30ce-bc63-e26853209ffc | -1.66855 | -52.06071 | 2025-12-16 00:13:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 24.3 |
| 69b0b82f-41df-3078-98bc-135064e1c4e8 | -1.34321 | -46.56861 | 2025-12-16 00:13:00 | TERRA_M-M | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 561268f3-eef6-32f2-bb18-bdaa59436907 | -1.80867 | -46.00058 | 2025-12-16 00:13:00 | TERRA_M-M | JUNCO DO MARANHÃO | MARANHÃO | Brasil | 2105658 | 21 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 6165b894-fabe-321c-8620-473cc1017a6e | -3.02604 | -45.34296 | 2025-12-16 00:13:00 | TERRA_M-M | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 13.1 |
| 19c6b871-6c3e-394f-a29e-59b4429764e1 | -2.97807 | -47.93105 | 2025-12-16 00:13:00 | TERRA_M-M | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 21.2 |
| 4dc1f685-c4d9-31bb-bf10-60d08beb5520 | -2.57022 | -45.57512 | 2025-12-16 00:13:00 | TERRA_M-M | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 13.8 |
| a7449b94-495a-32b6-b0fa-ee71eaf9f427 | -2.30309 | -45.51231 | 2025-12-16 00:13:00 | TERRA_M-M | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 9.9 |
| ce617f87-6c63-3c6b-b5b7-fe86760c2cbc | -2.40159 | -46.88965 | 2025-12-16 00:13:00 | TERRA_M-M | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| f4bf3fa5-8337-3b6c-a2d9-caed0e4690f3 | -1.342 | -46.55985 | 2025-12-16 00:13:00 | TERRA_M-M | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | 10.6 |
| ed5e8ab7-332d-30da-8061-fdd104271fe2 | -2.09037 | -46.16732 | 2025-12-16 00:13:00 | TERRA_M-M | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 57.4 |
| 8717ee5e-d62e-3939-b98a-f732df9cf150 | -4.08622 | -43.69366 | 2025-12-16 00:13:00 | TERRA_M-M | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 15817ff7-bb55-3a4e-a3d5-b81e1df40638 | -4.63718 | -47.94276 | 2025-12-16 00:13:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 25.6 |
| 0ac4104c-82e5-3476-a50e-088443e0adf3 | -4.10678 | -45.69527 | 2025-12-16 00:13:00 | TERRA_M-M | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 17.8 |
| a4ddead9-4a5f-3fd1-bce1-d3895e5f1773 | -4.40388 | -42.32892 | 2025-12-16 00:13:00 | TERRA_M-M | CABECEIRAS DO PIAUÍ | PIAUÍ | Brasil | 2202059 | 22 | 33 | nan | nan | nan | Caatinga | 28.5 |
| bc6f09fe-2bf0-30b0-962c-c58dfbf3f442 | -1.67056 | -45.79944 | 2025-12-16 00:13:00 | TERRA_M-M | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 48.6 |
| 2164f240-7dfe-3d76-8bc5-257f65d4c0ca | -4.07528 | -43.68477 | 2025-12-16 00:13:00 | TERRA_M-M | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 258a9a87-e5f9-3966-914c-c572ec30924e | -1.33269 | -45.82562 | 2025-12-16 00:13:00 | TERRA_M-M | LUÍS DOMINGUES | MARANHÃO | Brasil | 2106201 | 21 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 53278b6a-8c63-311a-99c9-5e1f18bcb71d | -3.30387 | -48.82901 | 2025-12-16 00:13:00 | TERRA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 8b6efa62-0986-338b-ac9d-03578fd1e1f9 | -3.02956 | -47.09336 | 2025-12-16 00:13:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 063dd25e-f5e4-344b-8a1a-7bb41fd309d9 | -3.41018 | -44.98859 | 2025-12-16 00:13:00 | TERRA_M-M | CAJARI | MARANHÃO | Brasil | 2102507 | 21 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 0cafc92b-451a-3bff-b6bf-2184b5969e7a | -3.07684 | -51.97937 | 2025-12-16 00:13:00 | TERRA_M-M | VITÓRIA DO XINGU | PARÁ | Brasil | 1508357 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 4a3cff9d-2c63-3a69-9950-9f735ffefc86 | -4.40567 | -42.34122 | 2025-12-16 00:13:00 | TERRA_M-M | CABECEIRAS DO PIAUÍ | PIAUÍ | Brasil | 2202059 | 22 | 33 | nan | nan | nan | Caatinga | 30.0 |
| f24db16c-dc5f-3b4d-a946-075b2bcb0447 | -1.28613 | -46.41573 | 2025-12-16 00:13:00 | TERRA_M-M | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 4e03fb7e-0275-339f-975b-ebfc1f4a1c08 | -2.58304 | -45.53675 | 2025-12-16 00:13:00 | TERRA_M-M | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 12db5434-3d44-343d-9e1d-b65a6d02bfed | -2.57787 | -45.56491 | 2025-12-16 00:13:00 | TERRA_M-M | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 119cbe42-abaf-3ad6-ba87-1f2a51bd76fd | -2.93144 | -52.26266 | 2025-12-16 00:13:00 | TERRA_M-M | VITÓRIA DO XINGU | PARÁ | Brasil | 1508357 | 15 | 33 | nan | nan | nan | Amazônia | 14.6 |
| fa6c0061-40f8-367b-9040-769fb488db46 | -2.24827 | -45.78146 | 2025-12-16 00:13:00 | TERRA_M-M | PRESIDENTE MÉDICI | MARANHÃO | Brasil | 2109239 | 21 | 33 | nan | nan | nan | Amazônia | 4.6 |
| e206af9b-f5f5-3f7b-bb49-f6ab1b7fa94a | -4.6569 | -47.81161 | 2025-12-16 00:13:00 | TERRA_M-M | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 4a0eb203-1606-3466-a469-249fbcca5d0f | -2.58429 | -45.54572 | 2025-12-16 00:13:00 | TERRA_M-M | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 10.5 |
| e433cd08-f23e-3c17-ae81-77fcfdd3faab | -3.72765 | -44.49037 | 2025-12-16 00:13:00 | TERRA_M-M | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 6e522341-a543-318a-ae49-1169c939f377 | -3.80189 | -49.03342 | 2025-12-16 00:13:00 | TERRA_M-M | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 13.4 |
| 8367fbe3-6553-3afd-8f23-2f1d0170c260 | -3.77435 | -47.95578 | 2025-12-16 00:13:00 | TERRA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 7456cc55-ba10-3bb3-96c2-62f507b44e7d | -2.55803 | -45.35647 | 2025-12-16 00:13:00 | TERRA_M-M | PRESIDENTE SARNEY | MARANHÃO | Brasil | 2109270 | 21 | 33 | nan | nan | nan | Amazônia | 19.7 |
| d22aad39-e2e7-3ff9-a47f-0339c9563e90 | -2.47525 | -47.01723 | 2025-12-16 00:13:00 | TERRA_M-M | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 7013346a-2f12-3a2b-8ebb-28f0bd8a9d6a | -1.97915 | -46.22502 | 2025-12-16 00:13:00 | TERRA_M-M | JUNCO DO MARANHÃO | MARANHÃO | Brasil | 2105658 | 21 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 3cf792e1-964e-3ae0-9c01-7f7b7041c1bc | -2.03118 | -45.80613 | 2025-12-16 00:13:00 | TERRA_M-M | GOVERNADOR NUNES FREIRE | MARANHÃO | Brasil | 2104677 | 21 | 33 | nan | nan | nan | Amazônia | 241.9 |
| 68eae81e-be01-383f-93de-f3ea229c171d | -2.03242 | -45.81502 | 2025-12-16 00:13:00 | TERRA_M-M | GOVERNADOR NUNES FREIRE | MARANHÃO | Brasil | 2104677 | 21 | 33 | nan | nan | nan | Amazônia | 85.2 |
| 4f9a4936-1a66-3b84-98fe-a335ecf79284 | -1.6567 | -52.06237 | 2025-12-16 00:13:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 13.5 |
| 4e66779d-1d96-399a-bb00-fd9a348a3e19 | -2.55929 | -45.36553 | 2025-12-16 00:13:00 | TERRA_M-M | PRESIDENTE SARNEY | MARANHÃO | Brasil | 2109270 | 21 | 33 | nan | nan | nan | Amazônia | 9.9 |
| ccb0d4af-6b49-3f9a-aaeb-0cd675051b65 | -4.15597 | -43.73996 | 2025-12-16 00:13:00 | TERRA_M-M | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 97fb9e47-9143-36c1-8215-9bab40e639dc | -1.66521 | -52.07247 | 2025-12-16 00:13:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 24.4 |
| 0da9d1c4-24eb-3535-b918-f144c73ead21 | -4.86546 | -45.70413 | 2025-12-16 00:13:00 | TERRA_M-M | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 7b6b379c-9404-36b7-9fa0-19b78d7e1f87 | -1.26172 | -47.18219 | 2025-12-16 00:13:00 | TERRA_M-M | CAPANEMA | PARÁ | Brasil | 1502202 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 3f2bdfbd-a4c2-34ae-b9ed-1e9bc47c1858 | -0.98928 | -47.21144 | 2025-12-16 00:13:00 | TERRA_M-M | PRIMAVERA | PARÁ | Brasil | 1506104 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 194d32f6-9dca-332c-8c28-773b05f638da | -3.2521 | -43.28605 | 2025-12-16 00:13:00 | TERRA_M-M | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 14.7 |
| dc7f6dcf-816d-31ba-a249-8d29dbcb8f1b | -2.08155 | -46.16856 | 2025-12-16 00:13:00 | TERRA_M-M | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 6.5 |
| e809ee85-05df-373d-bab2-532e77acd0be | -1.66299 | -52.05576 | 2025-12-16 00:13:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 27.5 |
| 3531c4da-5f12-3a8b-b97b-e0d6b50cab60 | -3.02931 | -49.05654 | 2025-12-16 00:13:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 19.4 |
| d5d01b56-1afd-3f27-b86f-4a082730bdf8 | -4.07673 | -43.69507 | 2025-12-16 00:13:00 | TERRA_M-M | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 26.1 |
| cfebfffd-03b8-3b80-a6bc-9574ba44239a | -3.64906 | -44.26595 | 2025-12-16 00:13:00 | TERRA_M-M | CANTANHEDE | MARANHÃO | Brasil | 2102705 | 21 | 33 | nan | nan | nan | Cerrado | 14.1 |
| d1d5846b-f99f-30e6-a08a-950f1593b940 | -1.83959 | -47.42655 | 2025-12-16 00:13:00 | TERRA_M-M | IRITUIA | PARÁ | Brasil | 1503507 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 5c67493a-028d-3e60-969a-2cd3a1e95951 | -1.6718 | -45.80837 | 2025-12-16 00:13:00 | TERRA_M-M | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 26.5 |
| 92eceeeb-8f68-3bff-a303-ea791fe51d74 | -1.84589 | -46.3991 | 2025-12-16 00:13:00 | TERRA_M-M | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 0d06a42c-7fc5-3bf1-9e32-afdd515b57d6 | -2.97679 | -47.92165 | 2025-12-16 00:13:00 | TERRA_M-M | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 12.6 |
| 3791133b-2032-3e3f-8bc8-3dd95adace60 | -1.54278 | -46.4838 | 2025-12-16 00:13:00 | TERRA_M-M | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 17.5 |
| 79311906-6618-328c-a7a4-cfbded5ec702 | -3.35711 | -46.86017 | 2025-12-16 00:13:00 | TERRA_M-M | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 213d173a-1048-330f-ac0f-7767816cff97 | -4.11926 | -45.70558 | 2025-12-16 00:13:00 | TERRA_M-M | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 4abdb539-6a96-3dd7-b231-67d78c8608b7 | -1.32681 | -46.57984 | 2025-12-16 00:13:00 | TERRA_M-M | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| ed3e4513-e006-32ae-9130-0656d15f6f1e | -1.92486 | -46.49786 | 2025-12-16 00:13:00 | TERRA_M-M | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 11.7 |
| 797233dd-fad1-3684-bc57-30a266f427cd | -4.11803 | -45.69676 | 2025-12-16 00:13:00 | TERRA_M-M | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 75.6 |
| d85c9171-c094-3a41-b60b-48714e9883bc | -3.56444 | -47.17058 | 2025-12-16 00:13:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 14.2 |
| 6f904656-a256-3c1f-8f00-7468a7a30ce0 | -3.42993 | -41.65266 | 2025-12-16 00:13:00 | TERRA_M-M | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 85.8 |
| 06e7f6b5-4487-3805-b4d6-ec2efe79dfa3 | -2.6194 | -45.66839 | 2025-12-16 00:13:00 | TERRA_M-M | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 19.1 |
| 2038100b-45de-328d-98aa-a33077e5764c | -2.57912 | -45.57387 | 2025-12-16 00:13:00 | TERRA_M-M | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 61efd0c4-b97c-349b-b2a0-448728aa5429 | -3.39837 | -49.2132 | 2025-12-16 00:13:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 15.2 |
| 972e1e94-872e-39ea-8be8-50da820ae107 | -1.84467 | -46.39034 | 2025-12-16 00:13:00 | TERRA_M-M | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| af19314f-5c20-32a0-9d6c-9a33d0b71c67 | -2.76465 | -45.90694 | 2025-12-16 00:13:00 | TERRA_M-M | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 4.2 |
| f67b7b32-7cfe-30f5-83d4-d034b2e2b8ef | -2.0301 | -45.8236 | 2025-12-16 00:20:00 | GOES-19 | GOVERNADOR NUNES FREIRE | MARANHÃO | Brasil | 2104677 | 21 | 33 | nan | nan | nan | Amazônia | 65.6 |
| e76eb2a8-9004-3e76-a4de-e1dffdad212d | -1.6777 | -45.8091 | 2025-12-16 00:20:00 | GOES-19 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 45.8 |
| 509513c3-ffab-3f04-b72b-28c9cc5de5c5 | -3.6356 | -44.2529 | 2025-12-16 00:20:00 | GOES-19 | CANTANHEDE | MARANHÃO | Brasil | 2102705 | 21 | 33 | nan | nan | nan | Cerrado | 42.1 |
| 87ff1d3c-66bc-380f-bfb3-06bd4d81b296 | -2.0301 | -45.8013 | 2025-12-16 00:20:00 | GOES-19 | GOVERNADOR NUNES FREIRE | MARANHÃO | Brasil | 2104677 | 21 | 33 | nan | nan | nan | Amazônia | 121.3 |
| a26192dd-b7a6-39f7-8256-07f975d7736e | -16.0616 | -58.9778 | 2025-12-16 00:20:00 | GOES-19 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Pantanal | 57.6 |
| 04d6f2fb-b3ad-36d3-a0df-e8ec4c95899a | -2.0487 | -45.8008 | 2025-12-16 00:20:00 | GOES-19 | GOVERNADOR NUNES FREIRE | MARANHÃO | Brasil | 2104677 | 21 | 33 | nan | nan | nan | Amazônia | 57.3 |
| ef7003fb-1e67-3233-b315-1c7aba339da8 | -4.6564 | -42.4048 | 2025-12-16 00:20:00 | GOES-19 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 72.9 |
| 1ce194c6-ddaa-34cb-871f-4851879b344c | -3.6542 | -44.252 | 2025-12-16 00:20:00 | GOES-19 | CANTANHEDE | MARANHÃO | Brasil | 2102705 | 21 | 33 | nan | nan | nan | Cerrado | 44.8 |
| b912ded2-d9dc-3fbe-ba96-42029ea20158 | -1.6637 | -52.065 | 2025-12-16 00:20:00 | GOES-19 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 42.3 |
| a0baedfa-dd91-3060-b32c-250352b4b1a2 | -4.1112 | -45.7018 | 2025-12-16 00:20:00 | GOES-19 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 54.9 |
| 97748d2d-0576-39ba-ad45-dc9d2ba04f43 | -12.3074 | -57.3608 | 2025-12-16 00:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 61.1 |
| 94aa078c-3e93-3882-8b69-c8597cc0d9f6 | -4.2608 | -45.5821 | 2025-12-16 00:30:00 | GOES-19 | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 89.4 |
| 8bc7183f-76e5-3b7f-8447-81aff502cdf8 | -12.3074 | -57.3608 | 2025-12-16 00:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 81.2 |
| 4fb0f318-a858-3759-8c93-597587979a33 | -8.0696 | -43.1452 | 2025-12-16 00:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 148.4 |
| cc360fdb-2bf1-3b5e-b84d-94554aab7c07 | -2.0487 | -45.8008 | 2025-12-16 00:30:00 | GOES-19 | GOVERNADOR NUNES FREIRE | MARANHÃO | Brasil | 2104677 | 21 | 33 | nan | nan | nan | Amazônia | 55.1 |
| a4bdf079-327a-369c-8730-f8576eb83cd6 | -1.6777 | -45.8091 | 2025-12-16 00:30:00 | GOES-19 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 38.7 |
| 7113499a-098f-32d8-8fad-f1a4cabbb12a | -12.3072 | -57.3808 | 2025-12-16 00:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 54.5 |
| ed81a720-9aab-39e4-b2a6-a113ae5e3677 | -2.0301 | -45.8013 | 2025-12-16 00:30:00 | GOES-19 | GOVERNADOR NUNES FREIRE | MARANHÃO | Brasil | 2104677 | 21 | 33 | nan | nan | nan | Amazônia | 116.6 |
| b7ea19dc-870d-3d62-9eed-9aae57cd7c46 | -8.07 | -43.1216 | 2025-12-16 00:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 70.7 |
| 15cbe3d1-2a12-3b13-a9c1-a804f1032169 | -2.0301 | -45.8236 | 2025-12-16 00:30:00 | GOES-19 | GOVERNADOR NUNES FREIRE | MARANHÃO | Brasil | 2104677 | 21 | 33 | nan | nan | nan | Amazônia | 69.7 |
| 9574dd92-a7a8-3ea7-8bb1-b645c4dd1715 | -4.261 | -45.5597 | 2025-12-16 00:30:00 | GOES-19 | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 48.3 |
| e4996c08-6620-3cd5-aeb4-7648fad436d0 | -1.6605 | -52.059898 | 2025-12-16 00:34:00 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 93d5b9fa-ad12-3dd6-9d53-1d84fb7f5bf1 | -1.2205 | -53.737499 | 2025-12-16 00:34:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e745d8cb-3313-3184-91dc-f3a68e14f1ab | -2.0275 | -45.843498 | 2025-12-16 00:34:00 | METOP-B | GOVERNADOR NUNES FREIRE | MARANHÃO | Brasil | 2104677 | 21 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README3.md)
