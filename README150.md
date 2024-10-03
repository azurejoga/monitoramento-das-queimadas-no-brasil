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

## Dados Diários - Página 150

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b81227bd-fd32-34d2-af80-0b938c24448e | -3.11268 | -49.4109 | 2024-10-03 05:14:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e12957ef-976e-33ec-b9c4-df6f98037053 | -3.11223 | -49.414 | 2024-10-03 05:14:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5c102b4a-fb42-3d3b-972a-802a4eb9031e | -2.95871 | -49.36023 | 2024-10-03 05:14:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 848442fa-dc33-38ab-8459-2a6f94b640d9 | -2.95824 | -49.36333 | 2024-10-03 05:14:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5d061284-36a4-3cd5-b941-629bb2863edb | -2.95776 | -49.36652 | 2024-10-03 05:14:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c84978d3-3641-308f-b583-0b1719c96859 | -2.95351 | -49.35946 | 2024-10-03 05:14:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 11165e42-aad5-31b0-8ce8-d7ede8dcfeb9 | -2.95256 | -49.36571 | 2024-10-03 05:14:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 241c902c-9479-3357-8254-e2df54889a35 | -2.79819 | -50.28677 | 2024-10-03 05:14:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 668af3b7-67b6-332b-a0d7-59a2cb9c0a13 | -2.48952 | -49.05325 | 2024-10-03 05:14:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3cc3b21b-59be-31b5-b105-21547796ded0 | -2.48904 | -49.05651 | 2024-10-03 05:14:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 2efa1476-25dd-37b8-8609-99e2d35bcc09 | -4.70198 | -50.87146 | 2024-10-03 05:14:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f0149a5d-02fd-32f9-a3a1-7e062685f3e8 | -4.09146 | -49.98663 | 2024-10-03 05:14:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 16277d0a-17ac-3dd7-abd4-37ba8a2451d2 | -5.52001 | -50.04174 | 2024-10-03 05:14:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1427a963-530e-34eb-94f6-b29a6e4bb6db | -5.51957 | -50.04483 | 2024-10-03 05:14:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7093dd26-e395-3556-98d8-a9e9bc7f5f50 | -5.514 | -50.04695 | 2024-10-03 05:14:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 26ad2202-42cc-3195-abc7-77e40e421e8d | -5.51356 | -50.05005 | 2024-10-03 05:14:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 98fcf521-2460-3073-80f5-266ee9dfc683 | -5.01896 | -50.87019 | 2024-10-03 05:14:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8c6cc0f7-fe33-36f2-abbb-690d903b6dc8 | -2.88475 | -50.72399 | 2024-10-03 05:14:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 309e9d61-c0ed-3bfa-bc0e-13c1bd9628db | -2.89198 | -50.74055 | 2024-10-03 05:14:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4b489d61-0069-3665-b8da-6a2fefc98970 | -2.89124 | -50.74558 | 2024-10-03 05:14:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0dafa331-9756-36d7-9550-968ece1a52f5 | -2.89099 | -50.73839 | 2024-10-03 05:14:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c0951ed8-abe0-32de-83d8-1214ebd73b8f | -2.89095 | -50.71465 | 2024-10-03 05:14:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 7ad0fff8-fabf-3dcf-ae29-212c29141c1d | -2.89021 | -50.74341 | 2024-10-03 05:14:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a4f081e9-a210-340e-99de-90d774bbfcba | -2.89021 | -50.71967 | 2024-10-03 05:14:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 157acfb4-3057-3f48-aaf2-6274afce5fe7 | -2.89015 | -50.71257 | 2024-10-03 05:14:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 05952272-823e-30bb-95ce-d413ea78412b | -2.88947 | -50.72471 | 2024-10-03 05:14:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1038eee3-9102-3642-8e6f-8317ce8f77cb | -2.88937 | -50.71757 | 2024-10-03 05:14:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c9f662c7-da9c-3299-845b-1e22fedfc6d1 | -2.88867 | -50.7534 | 2024-10-03 05:14:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8f428fa0-b2a7-3724-bb99-a516981ebc7c | -2.8886 | -50.72259 | 2024-10-03 05:14:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7e9efdee-8a2b-37e6-8bb3-0530e40e9e0d | -2.88782 | -50.72762 | 2024-10-03 05:14:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 08575d3e-492b-32b8-9e51-a8470a7fab0f | -2.88726 | -50.73983 | 2024-10-03 05:14:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8df0c6b9-0854-326b-b678-679ee35d3119 | -2.88695 | -50.70889 | 2024-10-03 05:14:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| ecd577fb-8657-3f74-a605-e628cbac6107 | -2.88652 | -50.74486 | 2024-10-03 05:14:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d978ee84-76d6-3305-906f-d389cb1a1a02 | -2.88627 | -50.73769 | 2024-10-03 05:14:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d1ac38ab-ddfa-31e6-af9f-dcf8d46b835c | -2.88622 | -50.71394 | 2024-10-03 05:14:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| d24c360d-e77a-3068-b5b9-f80371d5f3d0 | -2.88549 | -50.7427 | 2024-10-03 05:14:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| dfd0ce6f-65af-358d-b954-10afb11ee8ad | -2.88548 | -50.71895 | 2024-10-03 05:14:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 97eacc28-0dea-3be9-ae5a-a93b666818cb | -2.88541 | -50.71187 | 2024-10-03 05:14:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| c4debd02-3ea4-36af-b712-0619a66c45d1 | -2.88472 | -50.7477 | 2024-10-03 05:14:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cc3bde8d-0057-3695-9ed4-b2d96b7f5019 | -2.88464 | -50.71688 | 2024-10-03 05:14:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 560f8178-88ee-3a67-ab33-a4cfbf4d99b3 | -2.88387 | -50.72189 | 2024-10-03 05:14:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c777bbea-df50-3032-aa92-79e656ab71e1 | -2.8831 | -50.72691 | 2024-10-03 05:14:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 431f410a-abe7-3a09-80ee-3b9944d8f578 | -2.88222 | -50.70818 | 2024-10-03 05:14:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 06e68541-67c0-3a30-9e58-dc42f39bf6f7 | -2.88148 | -50.71324 | 2024-10-03 05:14:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 301d56c6-f759-3d4f-b3da-b313dd903bb5 | -2.88107 | -50.74915 | 2024-10-03 05:14:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 9f9ab73a-b133-36f6-b60e-1c285c258352 | -2.88075 | -50.71827 | 2024-10-03 05:14:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 05aa4a45-ad1f-3370-873d-b0e233998958 | -2.88068 | -50.71117 | 2024-10-03 05:14:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| bbe28860-e5d0-3560-bf10-5c8c4340dfcc | -2.87991 | -50.71619 | 2024-10-03 05:14:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| b2296363-4b4d-3a98-a1f4-115d2aca819f | -2.86419 | -50.7241 | 2024-10-03 05:14:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 105a58a5-c731-339f-82dd-53be562c924d | -2.86342 | -50.7291 | 2024-10-03 05:14:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 06f238ba-abee-3826-b231-da903d5c10fd | -2.86022 | -50.71838 | 2024-10-03 05:14:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 23094067-31ce-3c83-a07b-d09071baf0e5 | -2.85946 | -50.7234 | 2024-10-03 05:14:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 31778fb9-b83d-362d-a140-1f6d8ecfe660 | -2.8587 | -50.72839 | 2024-10-03 05:14:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c9163574-8404-37bd-8474-71211be67765 | -2.8555 | -50.71765 | 2024-10-03 05:14:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7e8cb193-51d6-3c7d-901a-c5f31c26a873 | -2.85474 | -50.72267 | 2024-10-03 05:14:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7f7bbf0b-29c4-3886-9895-b6d4d6d442e9 | -2.85398 | -50.72768 | 2024-10-03 05:14:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7bea024b-5cb1-31df-9670-e3bc6470b7f7 | -2.85321 | -50.7327 | 2024-10-03 05:14:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1adf055f-4c66-3b41-a7ea-842721689493 | -2.85077 | -50.71695 | 2024-10-03 05:14:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3e246b4d-e56c-3ef0-96c0-b80dfd9b7a88 | -2.85001 | -50.72198 | 2024-10-03 05:14:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7df83584-48fa-367e-9fdf-b657cfc28f25 | -2.84925 | -50.72697 | 2024-10-03 05:14:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 02c7c293-514a-3c73-9c69-bacc26b14bda | -3.32534 | -50.7868 | 2024-10-03 05:14:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 82dc3cfd-9524-32d7-a956-1c79f422cda3 | -3.3247 | -50.78478 | 2024-10-03 05:14:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| cc8eeeb4-f61a-3a25-b01e-a02c7eaf093c | -3.3246 | -50.79186 | 2024-10-03 05:14:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| a8b8c6dd-9e94-3438-a111-ff0e21d718bc | -3.32393 | -50.78981 | 2024-10-03 05:14:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 7d00e3f9-e337-30ac-a64e-5672edd21c77 | -3.32134 | -50.78104 | 2024-10-03 05:14:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f7fe0905-677e-357a-9e7d-7708b6d1bd00 | -3.32061 | -50.78606 | 2024-10-03 05:14:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 198fd445-9e39-3f4e-8f8c-bced95d73617 | -3.31997 | -50.78406 | 2024-10-03 05:14:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| c6a0a133-0bab-3d80-9fc3-09ebd34709a8 | -3.31586 | -50.78541 | 2024-10-03 05:14:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 66632a96-2417-33dc-9b44-05f908e1f8b5 | -3.31444 | -50.78846 | 2024-10-03 05:14:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 976e1621-5a00-3531-b41e-5e74b9ad1d9c | -3.22615 | -50.79622 | 2024-10-03 05:14:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 24c04e77-c9b3-3703-bfa5-c5f068e3b2be | -3.22143 | -50.79546 | 2024-10-03 05:14:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 37efdc1a-aeb8-3b77-8ae6-a8ade09ece24 | -2.90939 | -50.75341 | 2024-10-03 05:14:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 21a6797b-1f86-3c5f-87c6-61048a107c4e | -2.90541 | -50.74772 | 2024-10-03 05:14:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| a27119c1-8be2-31a4-abd2-d6fb068c4071 | -2.90467 | -50.75269 | 2024-10-03 05:14:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 44fbe99a-197a-3cc1-af61-0ac3ffda471a | -2.90143 | -50.74199 | 2024-10-03 05:14:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 804c2819-3161-31fd-bdba-bcf42e580725 | -2.90069 | -50.74701 | 2024-10-03 05:14:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bf840c5f-2d5b-3950-82f4-664693b2c171 | -2.90043 | -50.7398 | 2024-10-03 05:14:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4e209b3e-0efb-3bb7-bfbd-b477b8af127a | -2.90042 | -50.71607 | 2024-10-03 05:14:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f2d6d235-6cb6-3455-a481-b8ffee5a463f | -2.89995 | -50.75201 | 2024-10-03 05:14:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 787fddaa-a8c3-32ad-8840-69fe00433e8b | -2.89967 | -50.72112 | 2024-10-03 05:14:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9d365326-bca7-3407-914b-19d85e8462f2 | -2.89965 | -50.74483 | 2024-10-03 05:14:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f16eeac7-a932-3616-851d-6a055c153156 | -2.89893 | -50.72616 | 2024-10-03 05:14:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4d899748-c091-3ea8-b5ba-9bef5a35980e | -2.89888 | -50.74983 | 2024-10-03 05:14:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0e4dd682-9060-31ff-bca5-3557689c7613 | -2.89883 | -50.71899 | 2024-10-03 05:14:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 05d17deb-626c-30c6-bb71-837a97e5a915 | -2.8981 | -50.75482 | 2024-10-03 05:14:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 33758151-0505-305b-83ab-75dba2eadcde | -2.89805 | -50.72403 | 2024-10-03 05:14:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 9e18635f-6077-3e7e-b5e4-0d77624f5f85 | -2.89671 | -50.74126 | 2024-10-03 05:14:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0f14b2d0-2313-3630-a51e-a4c9fd2cbf2d | -2.89596 | -50.74631 | 2024-10-03 05:14:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 16d4a9d2-386f-3ec0-abb1-367979ea49d6 | -2.89568 | -50.71536 | 2024-10-03 05:14:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 7b982ff1-50fc-3081-a3f5-74047433212c | -2.89522 | -50.75132 | 2024-10-03 05:14:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 14c8ec88-b75e-3a66-ad4c-53d9dbb35c3f | -2.89494 | -50.72039 | 2024-10-03 05:14:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f66800f2-faeb-3412-8d8d-8a526f351bc3 | -2.89493 | -50.74413 | 2024-10-03 05:14:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 059c64c2-cfdb-3efa-9c4a-b06b686655b2 | -2.8942 | -50.72543 | 2024-10-03 05:14:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b1a43f58-ca13-3a6b-bdf3-0749dcb6c0ee | -2.89416 | -50.74913 | 2024-10-03 05:14:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 07478c81-6879-331e-960a-1d97afa30816 | -2.8941 | -50.71828 | 2024-10-03 05:14:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 1394794e-5d16-3dbe-b302-0ee36337c7ee | -2.89338 | -50.75413 | 2024-10-03 05:14:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 951b1855-25f7-3d26-af74-ae418b8396b4 | -2.89332 | -50.7233 | 2024-10-03 05:14:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cc29a13f-5c9c-3afa-9b4d-cd1767cac0c0 | -3.87862 | -52.0972 | 2024-10-03 05:14:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6c5d8aea-01b6-3baf-bf82-2ddcb74ead58 | -3.8775 | -52.098 | 2024-10-03 05:14:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 769a9b83-d352-3b86-8f66-4cc3db8e8c7f | -3.86366 | -52.25969 | 2024-10-03 05:14:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |


[Clique aqui para ver as próximas entradas](README151.md)
