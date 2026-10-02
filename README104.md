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

## Dados Diários - Página 104

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 67e266c8-7391-3868-9a6e-b93ec9db7c32 | -1.227 | -49.01123 | 2026-10-02 15:56:00 | NOAA-21 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 481243a4-27ad-33aa-8ffa-5bc54b46d7a4 | -1.25976 | -49.30189 | 2026-10-02 15:56:00 | NOAA-21 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 16.1 |
| 276dda2d-da4b-375a-aa70-bacd5e2f4dab | -0.24582 | -48.48934 | 2026-10-02 15:56:00 | NOAA-21 | SOURE | PARÁ | Brasil | 1507904 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| e13312f6-0e6e-38a5-9337-047b9cecd3a3 | -3.2364 | -40.02895 | 2026-10-02 15:56:00 | NOAA-21 | MORRINHOS | CEARÁ | Brasil | 2308906 | 23 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 1ea8743f-d8d6-3139-8594-f0e62db65ee5 | -1.72697 | -47.40956 | 2026-10-02 15:56:00 | NOAA-21 | IRITUIA | PARÁ | Brasil | 1503507 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| f9a7899a-231f-33e0-afb9-cbb1d5b4b41e | -6.62104 | -44.72121 | 2026-10-02 15:56:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 33bc8f8a-1c68-32df-abf5-98ecf4eb02a4 | -3.0857 | -49.25647 | 2026-10-02 15:56:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| bdb95613-d5a4-3785-bfc3-b04fc1fc841d | -5.49572 | -40.9602 | 2026-10-02 15:56:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 11.7 |
| bb2e5185-821c-33ed-bf83-6c7f101b96fc | -6.33007 | -43.35741 | 2026-10-02 15:56:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 32853848-9cbc-3c65-a61d-735f7c5d7316 | -4.05622 | -38.59723 | 2026-10-02 15:56:00 | NOAA-21 | GUAIÚBA | CEARÁ | Brasil | 2304954 | 23 | 33 | nan | nan | nan | Caatinga | 13.1 |
| 60382e60-49b0-33b6-8efd-a7868c943dd4 | -2.14186 | -45.8608 | 2026-10-02 15:56:00 | NOAA-21 | GOVERNADOR NUNES FREIRE | MARANHÃO | Brasil | 2104677 | 21 | 33 | nan | nan | nan | Amazônia | 10.9 |
| d3785afc-b6d2-38ff-b9b4-187797134564 | -5.95019 | -43.65421 | 2026-10-02 15:56:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 34.6 |
| 97e73490-c5cf-38fa-b7dd-8d1aa352c752 | -5.74381 | -45.13985 | 2026-10-02 15:56:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 46.9 |
| 409bc887-fb84-36ca-8754-5642e25e05c3 | -6.61529 | -44.71662 | 2026-10-02 15:56:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 12.9 |
| f22d38de-e2d1-30cc-80b3-33a7d02fe177 | -5.74035 | -45.1524 | 2026-10-02 15:56:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 63.1 |
| d38afd7d-d4a8-31df-8766-0ee08470b0ca | -1.25717 | -49.30273 | 2026-10-02 15:56:00 | NOAA-21 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| dca3ac06-5105-3ce9-a5a2-5991324becb1 | -5.9495 | -43.64932 | 2026-10-02 15:56:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 34.6 |
| 0e32ffc8-3aab-32a4-8408-c88e8cb66976 | -2.05175 | -45.8026 | 2026-10-02 15:56:00 | NOAA-21 | GOVERNADOR NUNES FREIRE | MARANHÃO | Brasil | 2104677 | 21 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 415bb8fa-51bb-3fd1-86a4-0bef6d25e7e3 | -5.73355 | -45.14115 | 2026-10-02 15:56:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 34.8 |
| ef4e1a4f-784a-328f-8ffb-3b1ecabc55e5 | -3.47086 | -39.59294 | 2026-10-02 15:56:00 | NOAA-21 | ITAPIPOCA | CEARÁ | Brasil | 2306405 | 23 | 33 | nan | nan | nan | Caatinga | 7.7 |
| 81e2245d-6bc0-3d22-8ed5-e53ac50193a9 | -1.15533 | -49.16444 | 2026-10-02 15:56:00 | NOAA-21 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| c5f3e168-88ee-3695-b0c2-2892fd3b8982 | -5.73952 | -45.1465 | 2026-10-02 15:56:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 32.7 |
| 5cc09a25-c747-3e3a-9901-64b9f70f4eb8 | -5.06345 | -45.20427 | 2026-10-02 15:56:00 | NOAA-21 | SÃO RAIMUNDO DO DOCA BEZERRA | MARANHÃO | Brasil | 2111631 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 96deceb1-e2a9-3814-b152-c8c83e477eaf | -1.1391 | -48.84988 | 2026-10-02 15:56:00 | NOAA-21 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| f3e43f23-c1dc-3060-9afc-76dfe458db93 | -0.9789 | -47.5051 | 2026-10-02 15:56:00 | NOAA-21 | MARACANÃ | PARÁ | Brasil | 1504307 | 15 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 9778dc01-86a0-3170-94fe-ce032fa50042 | -5.49957 | -40.95974 | 2026-10-02 15:56:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 11.7 |
| f76c8578-20d4-39fc-88c6-9a27f9741dd8 | -3.98556 | -41.51761 | 2026-10-02 15:56:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 13.8 |
| 563a42d7-b5e1-36a7-a415-86b438d58c67 | -6.24635 | -43.76883 | 2026-10-02 15:56:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 16.0 |
| 61de2590-5284-3900-a7c7-79e6f6bab70a | -3.47144 | -39.5968 | 2026-10-02 15:56:00 | NOAA-21 | ITAPIPOCA | CEARÁ | Brasil | 2306405 | 23 | 33 | nan | nan | nan | Caatinga | 7.2 |
| e54a0f87-10ab-3f49-85a7-003a6a71131e | -1.03181 | -47.80609 | 2026-10-02 15:56:00 | NOAA-21 | TERRA ALTA | PARÁ | Brasil | 1507961 | 15 | 33 | nan | nan | nan | Amazônia | 25.7 |
| dcdc1e9e-ad08-37b9-91f1-9c74c7682ee0 | -5.14401 | -37.38821 | 2026-10-02 15:56:00 | NOAA-21 | MOSSORÓ | RIO GRANDE DO NORTE | Brasil | 2408003 | 24 | 33 | nan | nan | nan | Caatinga | 9.2 |
| 7f23981f-1ae0-34ea-b3ca-1f918658fb2c | -1.25423 | -49.30778 | 2026-10-02 15:56:00 | NOAA-21 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| ce738eea-f998-379a-af94-e16213a11a0a | -1.23394 | -49.01515 | 2026-10-02 15:56:00 | NOAA-21 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 18.9 |
| e2768f2a-2dbe-3e41-a6e8-0cf9f0b98430 | -6.0701 | -44.80527 | 2026-10-02 15:56:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 8.6 |
| cc3b0652-49d3-30e8-a521-18e2d2fd747e | -2.73879 | -45.76717 | 2026-10-02 15:56:00 | NOAA-21 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 11.6 |
| f847e64e-c8d8-3eab-a88a-2213a40c4546 | -2.64115 | -44.30625 | 2026-10-02 15:56:00 | NOAA-21 | SÃO LUÍS | MARANHÃO | Brasil | 2111300 | 21 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 41948cad-bc6f-36ba-a8c6-5cdfc8edb3b3 | -2.95192 | -42.72973 | 2026-10-02 15:56:00 | NOAA-21 | PAULINO NEVES | MARANHÃO | Brasil | 2108058 | 21 | 33 | nan | nan | nan | Cerrado | 8.6 |
| e2183782-1e62-3047-be94-15995f433452 | -3.54822 | -42.65883 | 2026-10-02 15:56:00 | NOAA-21 | MILAGRES DO MARANHÃO | MARANHÃO | Brasil | 2106672 | 21 | 33 | nan | nan | nan | Cerrado | 159.3 |
| 1cdea079-f81c-31ed-be61-78e4ac399a3b | -6.3405 | -43.36541 | 2026-10-02 15:56:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 3f71e760-aa94-3951-bd40-2a408167717c | -3.98039 | -41.51582 | 2026-10-02 15:56:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 18.2 |
| d860b264-965b-3305-af5d-12d810b72e95 | -5.31659 | -37.4292 | 2026-10-02 15:56:00 | NOAA-21 | GOVERNADOR DIX-SEPT ROSADO | RIO GRANDE DO NORTE | Brasil | 2404309 | 24 | 33 | nan | nan | nan | Caatinga | 5.2 |
| 77a600d0-d118-3631-9cca-843cd12eedd4 | -5.75534 | -45.14755 | 2026-10-02 15:56:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 17.7 |
| 0d1dacfe-1629-3e78-bb1d-848e9d367f92 | -1.24107 | -50.16692 | 2026-10-02 15:56:00 | NOAA-21 | BREVES | PARÁ | Brasil | 1501808 | 15 | 33 | nan | nan | nan | Amazônia | 12.6 |
| e25a4a9d-c1bb-3a88-96e6-56d2e46ce19c | -2.13632 | -45.85849 | 2026-10-02 15:56:00 | NOAA-21 | GOVERNADOR NUNES FREIRE | MARANHÃO | Brasil | 2104677 | 21 | 33 | nan | nan | nan | Amazônia | 5.8 |
| b061e397-3286-3fb7-8f1d-6e97d6040951 | -5.95482 | -43.65353 | 2026-10-02 15:56:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 34.6 |
| 8a0f4931-659c-3428-b47e-a93dc72e7853 | -5.15064 | -37.38721 | 2026-10-02 15:56:00 | NOAA-21 | MOSSORÓ | RIO GRANDE DO NORTE | Brasil | 2408003 | 24 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 1cf1e519-7b0c-3ab4-ae43-a553167e54ae | -5.74424 | -45.14288 | 2026-10-02 15:56:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 46.9 |
| ce7b3cde-f4c6-3751-bb4c-a6007ad93230 | -3.58859 | -45.48406 | 2026-10-02 15:56:00 | NOAA-21 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 14.3 |
| c6a593a5-de72-34b3-b4cc-cafce1597ee6 | -5.73398 | -45.14416 | 2026-10-02 15:56:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 34.8 |
| babfd5ec-9cfe-344a-8093-920e24c4abb3 | -2.21707 | -44.80401 | 2026-10-02 15:56:00 | NOAA-21 | CENTRAL DO MARANHÃO | MARANHÃO | Brasil | 2103125 | 21 | 33 | nan | nan | nan | Amazônia | 9.1 |
| b7388ac5-72ca-39ee-8697-1f8757261377 | -2.83572 | -43.65818 | 2026-10-02 15:56:00 | NOAA-21 | MORROS | MARANHÃO | Brasil | 2107100 | 21 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 3b888aff-c56b-3b6a-8a47-1be532a88e22 | -5.74634 | -45.15788 | 2026-10-02 15:56:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 45.9 |
| f77a15b7-2c07-30a3-9ee7-fbd35de98c98 | -5.95088 | -43.65908 | 2026-10-02 15:56:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 21.7 |
| def8b38f-c19a-3be2-a4f1-bff40f4928a9 | -0.78435 | -49.27936 | 2026-10-02 15:56:00 | NOAA-21 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 33178279-81b7-33d0-a2ed-ffb0e173b69a | -0.77809 | -49.28024 | 2026-10-02 15:56:00 | NOAA-21 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| a5ac18d2-805a-37e9-925d-c685dcf6ce81 | -2.13834 | -45.86028 | 2026-10-02 15:56:00 | NOAA-21 | GOVERNADOR NUNES FREIRE | MARANHÃO | Brasil | 2104677 | 21 | 33 | nan | nan | nan | Amazônia | 20.1 |
| b2302525-93fa-310a-b1a3-4963e7e587ce | -6.12971 | -43.72459 | 2026-10-02 15:56:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 0c39f32e-8c0d-3adf-8fd7-8a2071afa9a1 | -3.08443 | -49.25473 | 2026-10-02 15:56:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| a1cb5ced-9e73-3e58-9d5a-590e16a28a6a | -4.07425 | -45.85633 | 2026-10-02 15:56:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 3.5 |
| d0ccbeb1-6f7e-3fb3-a9e4-70d421a07230 | -5.73439 | -45.14714 | 2026-10-02 15:56:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 40.4 |
| d59e3a36-2150-3bf7-9ce6-64fcfd415349 | -3.60717 | -38.94127 | 2026-10-02 15:56:00 | NOAA-21 | SÃO GONÇALO DO AMARANTE | CEARÁ | Brasil | 2312403 | 23 | 33 | nan | nan | nan | Caatinga | 3.4 |
| fa777c39-3941-32d2-b8e1-08826fa6fffe | -5.74077 | -45.15541 | 2026-10-02 15:56:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 63.1 |
| 7ef04f5c-1a78-392e-b641-196c5520b105 | -0.99404 | -48.96837 | 2026-10-02 15:56:00 | NOAA-21 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| e70ed237-d216-363e-b274-0e87fb6373b1 | -5.74549 | -45.15182 | 2026-10-02 15:56:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 63.1 |
| 5de493e0-9f27-3084-bb57-b48ad609047f | -0.90422 | -46.86411 | 2026-10-02 15:56:00 | NOAA-21 | TRACUATEUA | PARÁ | Brasil | 1508035 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| f622da43-ad69-39ca-9c26-e365973ebaf2 | -5.94694 | -43.66467 | 2026-10-02 15:56:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 0a02f52a-83b7-30a1-b690-c0d8c20e63f9 | -1.03441 | -47.8084 | 2026-10-02 15:56:00 | NOAA-21 | TERRA ALTA | PARÁ | Brasil | 1507961 | 15 | 33 | nan | nan | nan | Amazônia | 13.5 |
| 1855a24f-461c-37b4-b43b-b58289adfcaa | -0.78907 | -49.26863 | 2026-10-02 15:56:00 | NOAA-21 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 19.9 |
| 34cab225-3ae1-31fc-a212-79a55272f0e0 | -5.75021 | -45.14821 | 2026-10-02 15:56:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 17.7 |
| 641e8b86-3183-37e8-ac21-f4ec021a89dc | -4.07456 | -45.85719 | 2026-10-02 15:56:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 0838d8e6-c137-3386-86c4-5abb006cb86a | -5.94487 | -43.64998 | 2026-10-02 15:56:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 29.6 |
| 582a8268-0f71-34e9-ac2b-13b8b37ef6be | -2.8313 | -43.65883 | 2026-10-02 15:56:00 | NOAA-21 | MORROS | MARANHÃO | Brasil | 2107100 | 21 | 33 | nan | nan | nan | Cerrado | 9.3 |
| b950b4b2-b28f-37c0-b211-e7317d825143 | -5.73994 | -45.14944 | 2026-10-02 15:56:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 32.7 |
| e9a6268c-a596-359e-865f-b511220eb0a6 | -5.94625 | -43.65976 | 2026-10-02 15:56:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 33ec6a64-4f03-3be1-b952-7eca076a41b7 | -2.69563 | -42.6909 | 2026-10-02 15:56:00 | NOAA-21 | BARREIRINHAS | MARANHÃO | Brasil | 2101707 | 21 | 33 | nan | nan | nan | Cerrado | 22.4 |
| 6879c9c8-6446-3b3c-acf4-850928653759 | -5.75063 | -45.15121 | 2026-10-02 15:56:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 19.3 |
| 5bb26ca0-55d3-3e58-8dbe-fa221c2a37df | -6.63645 | -44.42872 | 2026-10-02 15:56:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 18.8 |
| 4696d5db-3e11-3599-8662-62c15c4779e9 | -1.23469 | -49.01994 | 2026-10-02 15:56:00 | NOAA-21 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 18.9 |
| 7a78573d-b47f-3dd8-a4ae-edcc21d10ad7 | -3.09087 | -49.25384 | 2026-10-02 15:56:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 719e7ee6-2d56-3451-a520-38d3777a45bc | -1.1818 | -49.29729 | 2026-10-02 15:56:00 | NOAA-21 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 5861b7cb-1433-331c-a503-272f86c05069 | -2.49886 | -44.172 | 2026-10-02 15:56:00 | NOAA-21 | PAÇO DO LUMIAR | MARANHÃO | Brasil | 2107506 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 12b3885c-c955-314d-8231-2e5ed1e64d75 | -1.23335 | -49.0153 | 2026-10-02 15:56:00 | NOAA-21 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 15.9 |
| 098901c5-59be-38a6-9bc8-bd5a3e354857 | -5.2297 | -37.61769 | 2026-10-02 15:56:00 | NOAA-21 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 5.2 |
| 09c7f665-35f1-3b72-ba11-8a5d7b55a16d | -0.99379 | -48.96767 | 2026-10-02 15:56:00 | NOAA-21 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 12.7 |
| 228abc27-c974-3d36-bb87-ba26a908918c | -2.25456 | -48.74943 | 2026-10-02 15:56:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 10.4 |
| eeefd92e-77b1-3db1-bd2c-1be1c03dfaf3 | -0.79532 | -49.26775 | 2026-10-02 15:56:00 | NOAA-21 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 19.9 |
| 56079f2f-4444-34bb-8573-2dcf0ea93716 | -4.07997 | -45.8588 | 2026-10-02 15:56:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 8a0288f2-5b95-389b-8540-badef8e0f162 | -1.46012 | -45.75453 | 2026-10-02 15:56:00 | NOAA-21 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 1bf9fe0c-082a-3c2a-bdf8-b889610f66d1 | -1.44393 | -49.58715 | 2026-10-02 15:56:00 | NOAA-21 | SÃO SEBASTIÃO DA BOA VISTA | PARÁ | Brasil | 1507706 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 76a7d084-46a7-3641-a971-8302006d48b5 | -6.0651 | -44.80406 | 2026-10-02 15:56:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| d5495707-1d98-3a09-8a9c-2e0b29a07fc9 | -6.19866 | -39.26342 | 2026-10-02 15:56:00 | NOAA-21 | QUIXELÔ | CEARÁ | Brasil | 2311355 | 23 | 33 | nan | nan | nan | Caatinga | 7.2 |
| 87f8e617-289d-3b49-8d22-4f1201bbea4c | -4.08026 | -45.85965 | 2026-10-02 15:56:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 7.5 |
| d041f819-3c41-3dc4-94e9-60424f81b4a9 | -5.0407 | -45.29844 | 2026-10-02 15:56:00 | NOAA-21 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 4974b10b-19b2-3247-9058-097b4d604a95 | -3.06813 | -49.36635 | 2026-10-02 15:56:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 8dbf0da5-d653-38a3-b1e2-92eb1fa0495a | -3.12956 | -40.59669 | 2026-10-02 15:56:00 | NOAA-21 | MARTINÓPOLE | CEARÁ | Brasil | 2307908 | 23 | 33 | nan | nan | nan | Caatinga | 10.5 |
| cd73d935-41ba-34b8-8e40-bc32b13425b8 | -1.45968 | -45.75169 | 2026-10-02 15:56:00 | NOAA-21 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 690b19f3-33e7-3ff1-96a6-c47f01b9f9b5 | -1.13227 | -48.84609 | 2026-10-02 15:56:00 | NOAA-21 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| c3d7252c-2e61-3f43-ad6b-89e1b0c8f81f | -0.8924 | -47.86115 | 2026-10-02 15:56:00 | NOAA-21 | CURUÇÁ | PARÁ | Brasil | 1502905 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 1504e461-afa4-3743-9ea5-7e0768ea22db | -2.48334 | -49.73177 | 2026-10-02 15:56:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 12.8 |
| cac7cf94-bf84-358f-9150-e25c23778c65 | -2.19971 | -50.98732 | 2026-10-02 15:56:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 23.6 |


[Clique aqui para ver as próximas entradas](README105.md)
