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

## Dados Diários - Página 41

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c3cd4d74-ac80-364a-8211-d9c24464fa21 | -4.54389 | -46.5649 | 2024-10-15 04:23:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b3f6e35a-3d61-3e8e-8d32-6ddf4136a044 | -4.54111 | -46.56086 | 2024-10-15 04:23:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 6deaf879-31f3-3394-b4c9-ee15d9679936 | -4.54055 | -46.56437 | 2024-10-15 04:23:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| ef3f22d7-2709-3e1d-ae01-cc7c34cecf13 | -4.53721 | -46.5854 | 2024-10-15 04:23:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 283c1f53-65b1-3b5c-9a08-4a1158fc9e44 | -4.53443 | -46.58135 | 2024-10-15 04:23:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 9fe551c8-1c19-3777-81f7-e772202689e0 | -4.53387 | -46.58487 | 2024-10-15 04:23:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 99953544-087e-3374-b464-2fe8e541eaad | -4.37932 | -46.72316 | 2024-10-15 04:23:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| dc0b835e-7b83-3add-94e2-bf97465260ee | -4.37326 | -47.28366 | 2024-10-15 04:23:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ebbc8abc-e659-395d-a217-da2ccd0cad6c | -4.36421 | -47.27478 | 2024-10-15 04:23:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| abd9ce11-4a9f-3e58-a445-c2202f2c9e0f | -4.36418 | -46.75334 | 2024-10-15 04:23:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a3f5ed15-2be6-3fe1-bb80-a5499032e5ce | -4.36363 | -47.27845 | 2024-10-15 04:23:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 740eb811-82d3-347f-baaa-195bfa2a07ff | -4.36081 | -47.27425 | 2024-10-15 04:23:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 00f06fd7-307c-36d3-a214-ce9f46ca20cc | -4.36023 | -47.27791 | 2024-10-15 04:23:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a281bd3f-af12-3a05-b3a4-4522f9802081 | -4.35682 | -47.27739 | 2024-10-15 04:23:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 90dd78ac-2b80-3d38-9f69-17e5c5b58d93 | -4.33825 | -46.73442 | 2024-10-15 04:23:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1f02913c-450d-340a-97ef-d9fe014b6e9a | -4.33321 | -46.70108 | 2024-10-15 04:23:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c8696142-411c-35b5-9fdc-7d45cc2a76c2 | -4.32548 | -47.32093 | 2024-10-15 04:23:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 01006122-7930-3e0b-942e-1a39d0aaed1d | -4.32207 | -47.32039 | 2024-10-15 04:23:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d0ff503f-4117-37aa-953c-514b269c6e67 | -4.32156 | -47.3017 | 2024-10-15 04:23:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 69bbb7d0-5abf-3102-a87f-3be4e5535113 | -4.31866 | -47.31985 | 2024-10-15 04:23:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 42d1a9c8-7f76-356e-9df2-0558d38c1431 | -4.31389 | -46.2886 | 2024-10-15 04:23:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5b8077c0-aa9c-3cce-92cd-c54543471ccb | -4.31359 | -47.30791 | 2024-10-15 04:23:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0383a20d-197f-341d-b287-a6ad937ac821 | -4.2707 | -47.00814 | 2024-10-15 04:23:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8731f35a-7384-3b5a-a989-7ec7cb71b1f8 | -4.27013 | -47.01172 | 2024-10-15 04:23:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3d3a6180-b5c5-3ad1-81e3-cc97511ce67a | -4.26732 | -47.00761 | 2024-10-15 04:23:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0a9f83f4-836d-3c12-a082-5b5a0a3c4689 | -5.00576 | -46.49055 | 2024-10-15 04:23:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f1c1400c-8cfa-34ff-b71d-cdcf3e88c52c | -5.00077 | -46.5005 | 2024-10-15 04:23:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 08aa2001-50c0-36a5-ab20-ab6cd9af5158 | -4.98743 | -46.49839 | 2024-10-15 04:23:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 56903d14-b5e2-3eb2-bbb2-e095ec5b00f8 | -4.9841 | -46.49786 | 2024-10-15 04:23:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b557299c-d65d-3988-84e1-49d8afe417ff | -4.89961 | -46.69214 | 2024-10-15 04:23:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1f8dfd13-3177-3ef3-b62c-10fc63ac39da | -4.53777 | -46.58187 | 2024-10-15 04:23:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 11.0 |
| e1e6eab7-0dd9-389e-9a5b-104b89b5eaad | -4.52885 | -46.55177 | 2024-10-15 04:23:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e5950081-be3a-30f6-9f16-0756d11cf330 | -4.52774 | -46.55877 | 2024-10-15 04:23:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 529381bc-6475-3a15-9c9b-1a07c06a8f0f | -4.52495 | -46.55475 | 2024-10-15 04:23:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| ee8a7fbd-fc47-312e-8f2c-92e6668083cc | -4.38155 | -46.73075 | 2024-10-15 04:23:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4f006cf7-f2be-35a1-bc2c-d5aa32ea0073 | -4.33881 | -46.7309 | 2024-10-15 04:23:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 18581576-4478-3fbd-98b7-290cf4b7eb49 | -4.33657 | -46.70162 | 2024-10-15 04:23:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c6df5495-ed4a-3a64-990c-04c7b9a5debd | -4.3349 | -46.73389 | 2024-10-15 04:23:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1bd4b7aa-2ae9-3d61-9b7b-6d641647acff | -4.15619 | -46.25694 | 2024-10-15 04:23:00 | NPP-375D | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d9670a52-79c4-3b30-9dfe-aae5a13b122a | -4.15285 | -46.25642 | 2024-10-15 04:23:00 | NPP-375D | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b90b14b5-0494-3529-ba22-a21205f90a68 | -4.0171 | -46.53597 | 2024-10-15 04:23:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3050b93c-c7ef-3e26-a963-a86c93c83d3b | -3.95128 | -46.44251 | 2024-10-15 04:23:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 13.1 |
| 15e0a982-6b2c-3954-9a1f-77b4fd9c08eb | -3.94849 | -46.43845 | 2024-10-15 04:23:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| af2cbc77-6ea0-3810-9290-e6785963b128 | -3.94515 | -46.43792 | 2024-10-15 04:23:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| bee3d659-93c7-3c65-b535-a27f7a8f55ad | -3.94178 | -46.4159 | 2024-10-15 04:23:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d9982eba-4854-37ac-aac8-451f03183099 | -3.9351 | -46.41487 | 2024-10-15 04:23:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| adc8a2ad-f2c8-37ad-ba1d-a4455b93e831 | -3.93231 | -46.41086 | 2024-10-15 04:23:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 6.1 |
| d54ac218-f687-3bca-9c9e-16babf6222d6 | -3.93175 | -46.41434 | 2024-10-15 04:23:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 26.7 |
| 34b456fd-411a-3880-b406-f96fe1a8e710 | -3.92897 | -46.41033 | 2024-10-15 04:23:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 41b1763d-7474-3d66-9485-95a1b141ff7b | -3.92621 | -46.471 | 2024-10-15 04:23:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 852fa956-9caf-395a-9df8-0ac3be5cc674 | -3.92287 | -46.47047 | 2024-10-15 04:23:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3e90ce1d-b8a0-3bfb-b553-35c1813dba8d | -3.92009 | -46.46637 | 2024-10-15 04:23:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4e7cc06a-ba1d-31e8-9ce9-c44e10b5efc9 | -3.91619 | -46.44773 | 2024-10-15 04:23:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0ec2760c-5769-3c4b-8cc5-69136101b0ff | -3.90279 | -46.42418 | 2024-10-15 04:23:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 056a196f-5b77-34e3-8310-929d947a145d | -3.89947 | -46.44514 | 2024-10-15 04:23:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 039c333c-d63b-3b94-826a-f670be99380f | -3.89891 | -46.44864 | 2024-10-15 04:23:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bcba0662-4112-3142-9b5e-d1170d54796e | -3.87772 | -46.47411 | 2024-10-15 04:23:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a23c670e-081d-3c7c-ab72-e47d51fe8a22 | -3.87716 | -46.47766 | 2024-10-15 04:23:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0cdbec2d-69f0-3b13-8fe7-6d3e3dbc33c8 | -3.87381 | -46.47712 | 2024-10-15 04:23:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 37151bb0-d08e-3aa3-a532-7b686c239a1e | -3.8716 | -46.46951 | 2024-10-15 04:23:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6a27cb42-4f51-35d5-9676-1a0f2cc602f9 | -3.86994 | -46.45843 | 2024-10-15 04:23:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8bc21a9f-fdf9-3e76-bdd6-148cd048d8bf | -3.86882 | -46.46545 | 2024-10-15 04:23:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f80f277f-cfa6-38c0-96fa-92fe7557b934 | -3.86491 | -46.46844 | 2024-10-15 04:23:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ec68f81b-1bde-3105-b606-debc2cd8e1dd | -3.86441 | -46.45766 | 2024-10-15 04:23:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 930d5690-3a2c-303f-8349-2de4a7a26362 | -3.86435 | -46.47197 | 2024-10-15 04:23:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7d9bc1b8-5a08-3055-b179-c4c6d5ad7a5e | -3.86378 | -46.47551 | 2024-10-15 04:23:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5954aee0-c8fc-3639-b8c2-f69f8a43f456 | -3.86219 | -46.47171 | 2024-10-15 04:23:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1897e52a-9598-3b35-9be0-12edbfe137db | -3.85105 | -46.47719 | 2024-10-15 04:23:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| db78a6ac-ae0a-35f2-b1f6-4c0e6524f6a7 | -3.84768 | -46.45507 | 2024-10-15 04:23:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8108c460-1094-3712-83b1-bc07f5fe5b95 | -3.8399 | -46.48264 | 2024-10-15 04:23:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d8fab08a-639b-37d1-90bb-493b1e688dd9 | -3.83766 | -46.47508 | 2024-10-15 04:23:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 80cc3471-a69f-37d9-8b87-4b3d86203d41 | -4.95292 | -47.84979 | 2024-10-15 04:23:00 | NPP-375D | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 343271a9-a9ba-3d2f-bf1a-c96090d6ff25 | -4.93533 | -47.56934 | 2024-10-15 04:23:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7f830908-fd16-3cfb-b669-f5a49f4b96b5 | -4.89612 | -47.63874 | 2024-10-15 04:23:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5b0380d7-7276-3e7c-83e6-4d3ca2021223 | -4.89553 | -47.64245 | 2024-10-15 04:23:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fede5814-4ade-3573-ad7a-6706a9a763f0 | -4.89211 | -47.64186 | 2024-10-15 04:23:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 15.5 |
| c09e8e4e-23bb-3795-a3af-bbc3117705a3 | -4.88929 | -47.63758 | 2024-10-15 04:23:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 15.5 |
| 40c74510-c5e7-34d4-831f-55f2f8340551 | -4.88869 | -47.64128 | 2024-10-15 04:23:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 15.5 |
| cf6df57b-dd8b-3260-a9fc-359eb6deee01 | -4.50369 | -47.60477 | 2024-10-15 04:23:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 39d859f6-352c-30e4-ba35-32ee93786445 | -4.5031 | -47.60846 | 2024-10-15 04:23:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ce77334b-7dad-3bbf-b3c8-64a50ecb2474 | -4.47536 | -47.73788 | 2024-10-15 04:23:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 498873db-29ee-3abd-a6d8-f631763cc7b6 | -4.47252 | -47.73354 | 2024-10-15 04:23:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7540d6e3-082f-3845-b840-192932164457 | -4.47191 | -47.73733 | 2024-10-15 04:23:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 937890a8-93dc-3ea8-8afc-a76898826d63 | -4.38871 | -47.75944 | 2024-10-15 04:23:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| d872b1b5-d43b-3544-b199-08852bc263c0 | -4.38525 | -47.75889 | 2024-10-15 04:23:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| d455bfd3-1b32-331c-99c4-7d93e4de2143 | -4.20322 | -46.90241 | 2024-10-15 04:23:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8493e092-2c29-3941-b9d0-8a4bf8116394 | -4.20266 | -46.90598 | 2024-10-15 04:23:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 49281cff-a3e1-3c41-ae2f-7557d62238e5 | -4.19929 | -46.90542 | 2024-10-15 04:23:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 74ddbb16-4c31-34db-b3cf-c04b71baa04f | -4.15385 | -46.86543 | 2024-10-15 04:23:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 38dd1dfd-bada-36e9-955b-435f44d50dd7 | -4.15161 | -46.85782 | 2024-10-15 04:23:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 19e6e001-08a6-342c-8f52-6b1ef2eea5c8 | -4.15049 | -46.86488 | 2024-10-15 04:23:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 190e1fa9-f53a-3347-a28c-362bcf67ae8c | -4.14917 | -47.17786 | 2024-10-15 04:23:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c695f92c-0c77-3d66-aeb7-c01e69e68ff9 | -4.02823 | -47.21508 | 2024-10-15 04:23:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 85525b3f-7f76-3489-8ae4-54f03084600a | -4.01013 | -47.50589 | 2024-10-15 04:23:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9fc823d2-478e-3577-b6b4-990a85bfc514 | -4.0067 | -47.50534 | 2024-10-15 04:23:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ec61f6fb-ea6c-32bb-ba68-8b61d182c4c4 | -4.00611 | -47.50906 | 2024-10-15 04:23:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 020bdfa1-40ac-3c2f-a725-d938b824b075 | -4.00209 | -47.51225 | 2024-10-15 04:23:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 81997a4b-1322-36fa-93c9-ec8b7b905c79 | -3.97123 | -47.10954 | 2024-10-15 04:23:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ef8f0f5e-e32d-39ff-9cf2-9b951d0e3d49 | -3.95183 | -46.43899 | 2024-10-15 04:23:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 13.1 |
| 41a640d2-b796-3870-818f-c82cd95d3a3d | -3.9457 | -46.43442 | 2024-10-15 04:23:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |


[Clique aqui para ver as próximas entradas](README42.md)
