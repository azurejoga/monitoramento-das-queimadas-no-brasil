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

## Dados Diários - Página 66

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 025601bb-3156-3beb-bb4c-ec66c749421e | -17.94261 | -57.28491 | 2024-10-14 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 569ce2ba-31dd-3ccb-bca8-d88e6f68f75f | -17.93573 | -57.29092 | 2024-10-14 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| f323812e-270b-3929-a286-7363187fbd7e | -17.91886 | -57.29084 | 2024-10-14 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 76.5 |
| 47a0ad41-7a66-3111-b746-4abe54054c38 | -17.88585 | -57.2871 | 2024-10-14 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 11.2 |
| 9303df85-2f1c-393b-86a9-7463c3e80c6a | -17.87433 | -57.28826 | 2024-10-14 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 10.4 |
| b318a936-02da-302b-be58-cefc281f5c1c | -17.86818 | -57.29066 | 2024-10-14 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 10.4 |
| a09ee7dd-169e-3309-a829-1298014459b3 | -17.85795 | -57.27693 | 2024-10-14 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.5 |
| b6202502-7a4f-37ba-a73d-60a78cbc3323 | -17.8528 | -57.28344 | 2024-10-14 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 925a0e42-149f-39a9-803a-cf69f297b686 | -17.85203 | -57.28706 | 2024-10-14 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 3c5347bd-585a-3dc5-b912-c26390259dc7 | -17.85126 | -57.29067 | 2024-10-14 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 21.0 |
| 44c74297-a252-397f-9fde-ae46db3c4dba | -17.85109 | -57.28293 | 2024-10-14 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.0 |
| 5b16a15e-9472-3746-b281-7df51b48d312 | -17.95917 | -57.32265 | 2024-10-14 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.2 |
| 63941f1e-c257-317c-9f65-8e62cba73139 | -17.95839 | -57.32626 | 2024-10-14 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.2 |
| f447962b-ec34-36ae-a556-b7c2f3c69a53 | -17.95762 | -57.32988 | 2024-10-14 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 22.5 |
| dfe7ac66-90f2-34fc-9be2-dcc8f7ec07b5 | -17.95736 | -57.32238 | 2024-10-14 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 43.3 |
| e8808947-9300-37de-abd5-9d6011c80c51 | -17.95684 | -57.3335 | 2024-10-14 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 22.5 |
| b5c9acef-e725-3b55-bf0b-8683435cc9b0 | -17.95661 | -57.326 | 2024-10-14 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 43.3 |
| 4965253f-b4f8-3186-b1f9-f4bc5c14cc7d | -17.95607 | -57.33712 | 2024-10-14 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.8 |
| 5e90b9c3-d963-3c8a-97a0-ef0adcfcd5d4 | -17.95586 | -57.32964 | 2024-10-14 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 46.0 |
| 0e9a023a-c7df-3a09-824b-fb81790db93a | -17.95511 | -57.33326 | 2024-10-14 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 46.0 |
| e26ab3a6-3ca5-30b2-b792-747de4abe1a3 | -17.95436 | -57.33689 | 2024-10-14 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 37.3 |
| 22f595a8-9675-37c7-a485-a9adacf7fe55 | -17.95301 | -57.32505 | 2024-10-14 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 28.5 |
| 86eccc66-7fa1-384f-b29f-c28284822987 | -17.95223 | -57.32868 | 2024-10-14 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 28.8 |
| 2eff7097-bdb0-30be-8a3a-60fc1318dc05 | -17.95145 | -57.33229 | 2024-10-14 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 28.8 |
| 2d64b58c-a2bb-346a-9c5f-55b855100d84 | -17.95068 | -57.33591 | 2024-10-14 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 37.6 |
| c9ec430c-e474-3357-a0cf-267fc36f7dbc | -17.95048 | -57.32841 | 2024-10-14 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 46.0 |
| cb6210e1-ff99-3957-9b57-1666e44fd1dc | -17.94973 | -57.33205 | 2024-10-14 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 46.0 |
| 2dbc2428-48f7-3f92-812d-5a154c95d9f4 | -17.94897 | -57.33568 | 2024-10-14 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 37.3 |
| 7a31bd2c-73e9-3fb2-8e46-2bacf4922e62 | -17.94762 | -57.32384 | 2024-10-14 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 28.5 |
| fd532d68-9a5f-30ed-8e53-2f005b374f60 | -17.94685 | -57.32747 | 2024-10-14 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 28.8 |
| 611c7c45-4e8f-3fe1-8827-c6e4ea1ac1e0 | -17.94607 | -57.33108 | 2024-10-14 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 28.8 |
| ac4a0b9e-46b0-399b-882e-672cb677540a | -17.94585 | -57.32355 | 2024-10-14 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 9.1 |
| e069e1c1-f68e-3fc1-9896-ee3dbc420965 | -17.94529 | -57.3347 | 2024-10-14 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 37.6 |
| 757034b3-ab17-343a-92c4-62a20b76023e | -17.9451 | -57.32719 | 2024-10-14 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.5 |
| d176b864-277b-3488-966a-583138f4b3b1 | -17.94434 | -57.33081 | 2024-10-14 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.5 |
| 0235affb-c7e6-3a2a-b1a4-6ab89c83557a | -17.94359 | -57.33445 | 2024-10-14 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 8.0 |
| b3912084-18e1-3436-9cf9-4f8205a9f46e | -17.94224 | -57.32263 | 2024-10-14 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.8 |
| 9d48a90c-0433-3cee-9f50-060c2e1adab1 | -17.94068 | -57.32987 | 2024-10-14 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.8 |
| 82b1ae38-4e21-34d4-bcf4-dbc482cc4dd0 | -17.93991 | -57.33348 | 2024-10-14 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.2 |
| d189a283-541c-3528-8b43-9cd6cf358cd1 | -17.93913 | -57.33709 | 2024-10-14 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 2bc16883-8531-3b7b-9387-c8ab5fb6de6e | -17.93896 | -57.32958 | 2024-10-14 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.5 |
| 0bb95af0-40ca-36c3-aa3a-f4550a486f54 | -17.9382 | -57.33322 | 2024-10-14 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 8.0 |
| 31ccb436-1cf0-3788-a5ba-a510ced79e68 | -17.93745 | -57.33683 | 2024-10-14 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 8.0 |
| 4b49e22c-eefd-307b-9025-df90e15c37e7 | -17.93608 | -57.32504 | 2024-10-14 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.8 |
| 5da3fec3-537b-38fe-8e3b-e18db3294c3e | -17.9353 | -57.32865 | 2024-10-14 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.8 |
| 3b836d48-7c4f-3a22-9876-4e94db92adb6 | -17.93452 | -57.33227 | 2024-10-14 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 3d6acba4-5bec-3945-b373-cf951735faf5 | -17.93433 | -57.32473 | 2024-10-14 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.0 |
| b5c809d8-d109-33eb-b1dd-662dc85bbf2a | -17.93374 | -57.33589 | 2024-10-14 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.2 |
| b9121e61-3127-3fc8-b779-41a03f275a9b | -17.93357 | -57.32835 | 2024-10-14 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 34d53571-b4dd-3338-8ced-969652cfb775 | -17.93281 | -57.33199 | 2024-10-14 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 542c2b45-8969-33e9-8f29-fc16f6d2e92a | -17.93206 | -57.33562 | 2024-10-14 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 9ba2da27-f3a0-3f1f-8eab-f8e63f9fbf62 | -17.92348 | -57.29567 | 2024-10-14 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 20.8 |
| afa4eb3f-d151-36ec-a414-66cf24913172 | -17.91734 | -57.29808 | 2024-10-14 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 101.8 |
| 8b768649-5fd6-3cfc-b5f2-6753dc803c1c | -17.91196 | -57.29687 | 2024-10-14 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 101.8 |
| 788cbf5e-8318-3b56-872b-8f18d95bd8a7 | -17.89893 | -57.30525 | 2024-10-14 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.1 |
| 27dc6605-329d-3e3d-984a-ed3c0837dbba | -17.88817 | -57.3028 | 2024-10-14 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 11.5 |
| 6642efa2-3fd1-3344-b06d-d4fe1d56d944 | -17.88432 | -57.29432 | 2024-10-14 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 39.5 |
| 0434ea79-81d9-3706-b35a-30cc0d01ba77 | -17.87279 | -57.29552 | 2024-10-14 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 26.7 |
| 899c2f02-d9a1-3256-92bf-396ae78d5f6b | -17.86664 | -57.29792 | 2024-10-14 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 26.7 |
| 398d576e-21a0-37c3-9b07-2e455938d207 | -17.8597 | -57.30396 | 2024-10-14 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 9.7 |
| acc4b720-5454-3873-810e-0966fa620a3d | -17.85348 | -57.29865 | 2024-10-14 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 17.7 |
| fb4c6d13-9668-33d4-8695-8bd3a7fd6b65 | -17.84971 | -57.2979 | 2024-10-14 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 15.7 |
| c4ca6bbd-383f-3c57-b619-3ef026a506b4 | -17.84659 | -57.30467 | 2024-10-14 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.2 |
| e91291d7-1418-3ba0-a57e-9dbd401cb3e2 | -17.84278 | -57.30391 | 2024-10-14 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.5 |
| d1d78fe4-896d-39fa-bcbf-54555e86a899 | -17.83661 | -57.30632 | 2024-10-14 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 23.9 |
| 1cd2360f-96c4-345e-8161-0733a15b35f5 | -17.95305 | -57.29856 | 2024-10-14 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 24.6 |
| d573bf59-2773-36b8-8aaf-aaa51f00bcf4 | -17.95186 | -57.29455 | 2024-10-14 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.7 |
| b4987fb5-79ac-339f-b87b-8e5015c77d54 | -17.9515 | -57.30579 | 2024-10-14 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 37.3 |
| aedac7c3-6c66-39af-a559-78bb729d79e1 | -17.94845 | -57.29375 | 2024-10-14 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 0c361ac9-1cb1-36a2-866e-b0ca0e8a7790 | -17.9411 | -57.29213 | 2024-10-14 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 92837b20-f079-3f3b-bcad-c74dc31e63f8 | -17.94074 | -57.30336 | 2024-10-14 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 25.4 |
| ab1af679-d4e9-333c-a5d8-c9f2dc677b25 | -17.93997 | -57.30697 | 2024-10-14 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 25.4 |
| 002c8742-727b-3fee-a1c9-620014f274ab | -17.9381 | -57.30658 | 2024-10-14 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 26.3 |
| 2776d855-2049-3ab5-84f8-5130696fdfed | -17.93272 | -57.30536 | 2024-10-14 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 26.3 |
| e08c60cb-11d6-3caf-9782-72de1588ead2 | -17.96303 | -57.30456 | 2024-10-14 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 1b32ac23-f836-3418-abda-8bf86be2e6eb | -17.96261 | -57.29697 | 2024-10-14 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 0be8cad4-795a-36e0-93e7-0eee28b89ba9 | -17.95688 | -57.30698 | 2024-10-14 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 37.3 |
| 9997c185-f965-356d-878c-138e244ba401 | -17.95573 | -57.30301 | 2024-10-14 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 12.0 |
| d7091d37-4183-3e41-878a-19c4f68a6070 | -17.95111 | -57.29818 | 2024-10-14 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 64.4 |
| 19118c7b-f4c8-33ba-9bc3-bd30553da6a5 | -17.94612 | -57.30459 | 2024-10-14 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 25.4 |
| dd2bedb9-5cdc-378b-85ef-fe9f7a6464ab | -17.94423 | -57.3042 | 2024-10-14 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 26.2 |
| bf06467e-8a5b-3ddd-853d-1a0ffb6111c5 | -17.93885 | -57.30297 | 2024-10-14 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 26.3 |
| 3da0d397-f4d5-34fe-a0d0-0469bd319479 | -17.93498 | -57.29453 | 2024-10-14 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 43.0 |
| 8aea21c6-f1b2-3564-b65a-eebd33b3575c | -17.93348 | -57.30173 | 2024-10-14 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 26.3 |
| 4440cd78-2fe2-3bae-af58-c8e9ef25bff6 | -17.92196 | -57.30293 | 2024-10-14 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 8.6 |
| d8beefd4-985c-396c-afcc-75cddd962dba | -17.9212 | -57.30655 | 2024-10-14 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 266796c9-7270-3b9b-acf3-9ee41d7e2cc5 | -17.90583 | -57.29925 | 2024-10-14 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 62.0 |
| f43ed9f9-9b15-36d7-81aa-7b652b39264b | -17.90431 | -57.30648 | 2024-10-14 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.1 |
| a93d6827-2adc-31f2-808e-961794c2e532 | -17.90045 | -57.298 | 2024-10-14 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 62.0 |
| 32f7d319-7d00-3f84-8b90-d97cf5c559ff | -17.89969 | -57.30162 | 2024-10-14 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.1 |
| f61780cd-a615-3642-b6c7-b02fd8b32f68 | -17.89431 | -57.30039 | 2024-10-14 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 11.5 |
| 09509afa-c17f-353c-8444-3c8a24f1c1d1 | -17.89046 | -57.29193 | 2024-10-14 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 82.0 |
| 529fc8f2-b10a-3b59-bebc-b9cde970cc56 | -18.23359 | -56.61843 | 2024-10-14 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.1 |
| c66bfe0b-1973-3bf0-ae78-b706ac935cca | -18.02456 | -57.36032 | 2024-10-14 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 12.3 |
| 6e0107b8-820e-321d-ac3e-b0a2660cb43e | -18.02379 | -57.36396 | 2024-10-14 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 12.3 |
| 251cc066-0ac1-3e8b-a665-46ab26cd5413 | -18.02303 | -57.3676 | 2024-10-14 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 17.4 |
| 7d213546-7a16-3b04-838b-5f52ce14ee9d | -18.02145 | -57.34821 | 2024-10-14 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 639618b2-7bf1-330b-baf1-5d19b2d432e0 | -18.02069 | -57.35183 | 2024-10-14 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.9 |
| cb0dc7c2-5b0b-35b3-8368-1cf5eb59a3a5 | -18.01993 | -57.35546 | 2024-10-14 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.9 |
| ba5db40a-3fad-3c42-9e38-1fb8d1a8ec1b | -17.86117 | -57.37678 | 2024-10-14 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.8 |


[Clique aqui para ver as próximas entradas](README67.md)
