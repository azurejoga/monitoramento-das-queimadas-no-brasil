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

## Dados Diários - Página 181

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 35240796-ef98-3301-9553-2db0e87bf5d2 | -3.64793 | -58.5663 | 2024-10-25 16:52:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| bdd61215-9683-3409-8f56-caeb6b57d9f8 | -3.59636 | -58.57859 | 2024-10-25 16:52:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 25e59c2d-23b6-3c0c-9cc0-e3ef6881a847 | -3.54736 | -58.97404 | 2024-10-25 16:52:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 13.0 |
| 39b27865-97ce-303c-b010-80b48b7ed6b7 | -3.54656 | -58.9687 | 2024-10-25 16:52:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 12.1 |
| 3749aed0-3ef4-3afc-8af8-756f2ad070f6 | -3.54457 | -59.37121 | 2024-10-25 16:52:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 8.1 |
| f81358fe-1abb-36c2-a37d-889f36b34fcc | -3.54446 | -59.36979 | 2024-10-25 16:52:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 15.6 |
| 003546d8-2c02-3acf-a637-8d19679749dd | -3.54413 | -59.36834 | 2024-10-25 16:52:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 4c53f4a9-52d6-3bd8-8b61-b96704355099 | -3.5162 | -59.49094 | 2024-10-25 16:52:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 10.5 |
| cc15c2f1-62bc-3c95-bed7-bdf929be8cd4 | -3.38925 | -58.83471 | 2024-10-25 16:52:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 8.4 |
| ae9c9cfe-a6f7-32ee-99a4-e0009e6d1588 | -4.60218 | -59.56499 | 2024-10-25 16:52:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 6ffd4c73-4a26-307a-864f-c6c3b0480bed | -4.38653 | -59.74256 | 2024-10-25 16:52:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 5467b5c4-ff96-35a8-88fa-d72c5a2945a9 | -4.38607 | -59.73937 | 2024-10-25 16:52:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 12.3 |
| a2af88d2-eeae-3652-b4b2-97967a7c8f16 | -4.2756 | -59.42901 | 2024-10-25 16:52:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 7119cbd3-c923-3433-a069-3140b799d6bf | -4.1617 | -59.89582 | 2024-10-25 16:52:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 31.2 |
| 91edcfd1-4abc-337f-9196-957408e6b4cf | -4.16142 | -59.89447 | 2024-10-25 16:52:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 44.3 |
| 51a9656e-23d5-3c04-bf0f-2f0776977227 | -4.16124 | -59.89258 | 2024-10-25 16:52:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 31.2 |
| f4e799e5-d603-33f9-a69f-dd53cf450fd9 | -4.16094 | -59.89125 | 2024-10-25 16:52:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 38.5 |
| 7ca79294-ea31-31d4-b9c9-ab5e4ab02af3 | -4.02626 | -59.37157 | 2024-10-25 16:52:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 5.8 |
| dc0f5145-0f4a-3c64-b2c3-98b0e3976e77 | -4.02315 | -59.28003 | 2024-10-25 16:52:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| fae2bafd-ee55-3245-ab8c-e1716a429a62 | -3.9545 | -58.51168 | 2024-10-25 16:52:00 | NOAA-21 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 2af09bf1-5d0f-3809-81ac-451ce7f30acf | -3.95342 | -58.50973 | 2024-10-25 16:52:00 | NOAA-21 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 12.5 |
| f54bead9-d817-349d-adf8-632e5ecfbb2e | -3.92528 | -59.13171 | 2024-10-25 16:52:00 | NOAA-21 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 15.6 |
| 3cca53d5-4b10-31a1-9918-9de5eb5bdbdd | -3.92441 | -59.13466 | 2024-10-25 16:52:00 | NOAA-21 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 15.4 |
| be94a89e-346b-3807-a000-4859dd67e73b | -3.91945 | -59.13539 | 2024-10-25 16:52:00 | NOAA-21 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 15.4 |
| 0055ae4a-1533-310d-bc3c-1a97137716f1 | -3.88234 | -59.22872 | 2024-10-25 16:52:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 01cb67b8-daa4-3fc0-b0ef-02e7952ef20d | -3.86869 | -59.72852 | 2024-10-25 16:52:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 0a34f644-b627-3fb1-9ce7-ee0d6d694628 | -3.86824 | -59.72543 | 2024-10-25 16:52:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 11.0 |
| c4fda131-465f-383a-bfc6-24a0437eb20d | -3.75023 | -58.95679 | 2024-10-25 16:52:00 | NOAA-21 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 45.5 |
| 304ba403-2349-32a3-a660-0ca110807f02 | -3.74623 | -58.92962 | 2024-10-25 16:52:00 | NOAA-21 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 16.5 |
| a079b4b4-b1dd-3f57-b7ac-de07ac4ace5a | -3.69281 | -59.63884 | 2024-10-25 16:52:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 12ea45cc-202f-3fa8-9446-4161ea2df321 | -6.32836 | -59.94758 | 2024-10-25 16:52:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 8.8 |
| d7b65ba7-f7bb-326f-81aa-fc97d2997178 | -6.32789 | -59.94412 | 2024-10-25 16:52:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 16.5 |
| ee522560-4172-324e-a8c2-ba32d67f9443 | -6.84174 | -59.99474 | 2024-10-25 16:52:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 12.3 |
| 66c6b42a-4260-319f-b321-8cc55e839a33 | -6.84128 | -59.99126 | 2024-10-25 16:52:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 12.3 |
| 5d9137d2-5391-3b6d-8baa-7ed7a0415b41 | -6.82058 | -60.13148 | 2024-10-25 16:52:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 896ed11d-8e4c-300c-a009-eb1ec974a987 | -6.69689 | -60.00875 | 2024-10-25 16:52:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 60.5 |
| 2b10fbd5-703b-3e04-b06d-ce8b921e2916 | -6.69188 | -60.01299 | 2024-10-25 16:52:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 0e47c672-e960-3325-acee-d3295442af6c | -6.69139 | -60.00941 | 2024-10-25 16:52:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 80979bd7-b40c-3342-ae0f-0e4b9dd9dbde | -6.53864 | -60.04333 | 2024-10-25 16:52:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 8d373a69-b711-38fa-a5f6-e310b020b1aa | -6.53314 | -60.04403 | 2024-10-25 16:52:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 9db07647-939e-34e2-97d5-7a8562f66c7c | -6.53264 | -60.04513 | 2024-10-25 16:52:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 15.2 |
| 5c6941a3-21de-3988-a1b9-3fb264babd4e | -6.52811 | -60.04829 | 2024-10-25 16:52:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 7c0a1170-6429-3d80-a819-818c524e3e9a | -6.52765 | -60.0448 | 2024-10-25 16:52:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 9.3 |
| cdd9cdab-bd44-3ef0-843e-bab1f2450d90 | -6.52715 | -60.04587 | 2024-10-25 16:52:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 13.1 |
| 450f7a62-d771-355e-b501-eeefbc464e6c | -6.52625 | -60.03432 | 2024-10-25 16:52:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 3440574b-435d-3892-9488-c4681dda8ec1 | -6.52568 | -60.0354 | 2024-10-25 16:52:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 4387eb11-8d73-39d7-9569-39dde3fcf0f6 | -6.5207 | -60.03977 | 2024-10-25 16:52:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 36b76cb6-48de-3f56-80b2-a4ffe21fc33c | -6.48975 | -60.05861 | 2024-10-25 16:52:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 5.9 |
| eb94d300-b5b2-329c-9a17-2d53aa4df6c1 | -7.38443 | -59.72204 | 2024-10-25 16:52:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| f94641e0-736e-3c9f-98ca-1a053f65303e | -7.32717 | -59.72001 | 2024-10-25 16:52:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.2 |
| c5189da0-fe9a-3877-9c6e-306e05e0bb39 | -7.3217 | -59.72052 | 2024-10-25 16:52:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 9b364417-40c4-3c37-80fa-0d70288d7b3f | -7.29313 | -59.63302 | 2024-10-25 16:52:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 1d140084-96fe-3c0d-a552-f94723a45793 | -7.27934 | -59.49253 | 2024-10-25 16:52:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 5dda6eff-5111-3b03-b8ab-45a2f7bc9eb3 | -7.22893 | -59.82514 | 2024-10-25 16:52:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 66d508d4-5aae-308b-9696-3d4393784e33 | -7.22705 | -59.4682 | 2024-10-25 16:52:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 15.7 |
| 1a3ec844-857a-36ea-8895-a4ad9d3a7f0f | -7.1957 | -59.62434 | 2024-10-25 16:52:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 7a2d5efc-4dbd-3faf-aabf-85cc4ef40cc4 | -7.15147 | -59.5814 | 2024-10-25 16:52:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 14.0 |
| 3dc4aa00-fe5c-37e6-9e94-8142e288a0b0 | -0.66437 | -47.44458 | 2024-10-25 16:54:00 | NOAA-21 | MARACANÃ | PARÁ | Brasil | 1504307 | 15 | 33 | nan | nan | nan | Amazônia | 20.9 |
| 36cbdd09-6311-3b43-844d-869d59af6cec | -1.53502 | -47.20517 | 2024-10-25 16:54:00 | NOAA-21 | OURÉM | PARÁ | Brasil | 1505403 | 15 | 33 | nan | nan | nan | Amazônia | 34.8 |
| f81fadaa-2b02-384d-b597-a468b40a5814 | -1.53427 | -47.20037 | 2024-10-25 16:54:00 | NOAA-21 | OURÉM | PARÁ | Brasil | 1505403 | 15 | 33 | nan | nan | nan | Amazônia | 42.8 |
| e8e65d06-0e84-3529-aae6-adf8b4eda721 | -1.53116 | -47.20583 | 2024-10-25 16:54:00 | NOAA-21 | OURÉM | PARÁ | Brasil | 1505403 | 15 | 33 | nan | nan | nan | Amazônia | 12.5 |
| f0555ee7-62ba-3796-829b-d898f76563c6 | -1.53041 | -47.20102 | 2024-10-25 16:54:00 | NOAA-21 | OURÉM | PARÁ | Brasil | 1505403 | 15 | 33 | nan | nan | nan | Amazônia | 39.6 |
| 0855fadc-4751-35de-9ea2-61c1f3db9059 | -1.47855 | -47.1992 | 2024-10-25 16:54:00 | NOAA-21 | OURÉM | PARÁ | Brasil | 1505403 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| c905bec1-439a-3379-b7b0-1d702d186238 | -1.3683 | -47.18935 | 2024-10-25 16:54:00 | NOAA-21 | BONITO | PARÁ | Brasil | 1501600 | 15 | 33 | nan | nan | nan | Amazônia | 28.1 |
| aaad6dcb-5493-38f0-8256-0412fde3ca09 | -1.36746 | -47.19135 | 2024-10-25 16:54:00 | NOAA-21 | BONITO | PARÁ | Brasil | 1501600 | 15 | 33 | nan | nan | nan | Amazônia | 14.6 |
| 0c452823-14b4-39c1-8584-39ee0616f43c | -1.36672 | -47.18646 | 2024-10-25 16:54:00 | NOAA-21 | CAPANEMA | PARÁ | Brasil | 1502202 | 15 | 33 | nan | nan | nan | Amazônia | 14.6 |
| 2603db82-4996-3d72-bca3-6fef036936f5 | -1.80578 | -48.62275 | 2024-10-25 16:54:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 1035086d-46d3-3d91-b33c-a91402d0e1c3 | -1.80356 | -48.62682 | 2024-10-25 16:54:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 13107628-9035-3056-b3b0-30197d35d076 | -1.80302 | -48.37172 | 2024-10-25 16:54:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 12.3 |
| 4b4a308b-1bda-383f-9c13-0bc64babebac | -1.80294 | -48.62278 | 2024-10-25 16:54:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| e806b640-7df1-38c0-9974-ff81f2fddb29 | -1.79711 | -48.38116 | 2024-10-25 16:54:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 39.4 |
| 84479208-e277-35ff-a74d-21587a7fa1c3 | -1.79545 | -48.3941 | 2024-10-25 16:54:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 9e79d2cf-1f2a-3d12-8ab4-b6f072d7bfc3 | -1.78564 | -48.37869 | 2024-10-25 16:54:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 347a88b3-29eb-3228-8507-c4f7bf24d89f | -1.77937 | -48.45578 | 2024-10-25 16:54:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| b6cc31ab-deb5-3757-acbd-9bfdad0d56bf | -1.77804 | -48.45966 | 2024-10-25 16:54:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| e5d20b08-9837-3dd5-b224-43815e9b5446 | -1.76366 | -48.46186 | 2024-10-25 16:54:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 37.9 |
| 2f27545a-cf32-314b-bb2b-2adec8634020 | -1.74297 | -48.17902 | 2024-10-25 16:54:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 332cfe57-621d-3137-8cc0-c73851616e52 | -1.74255 | -48.17824 | 2024-10-25 16:54:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 1766bd65-1d88-3684-a92c-648460124d91 | -1.72995 | -48.57601 | 2024-10-25 16:54:00 | NOAA-21 | ABAETETUBA | PARÁ | Brasil | 1500107 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 0ee7673e-8235-3c63-b612-663f38dfa0a1 | -1.70403 | -48.55083 | 2024-10-25 16:54:00 | NOAA-21 | ABAETETUBA | PARÁ | Brasil | 1500107 | 15 | 33 | nan | nan | nan | Amazônia | 13.2 |
| 6800e263-54d0-3a26-b9d8-ec80bc499a04 | -1.69788 | -48.53507 | 2024-10-25 16:54:00 | NOAA-21 | BARCARENA | PARÁ | Brasil | 1501303 | 15 | 33 | nan | nan | nan | Amazônia | 15.0 |
| ee16a68b-1ff5-3daf-9880-6e45a2eea251 | -1.69204 | -47.78569 | 2024-10-25 16:54:00 | NOAA-21 | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 280329ba-6b12-356f-9c4b-2d2e83117c49 | -1.69133 | -47.78123 | 2024-10-25 16:54:00 | NOAA-21 | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 45708c02-810a-3fe2-8997-7aa6e5a566b9 | -1.68831 | -47.78627 | 2024-10-25 16:54:00 | NOAA-21 | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 69a80fbb-1226-3056-8248-2e0baa392593 | -1.68035 | -47.66326 | 2024-10-25 16:54:00 | NOAA-21 | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 7a34acb1-6f28-374a-99f3-cef24e53db4e | -1.62402 | -48.18689 | 2024-10-25 16:54:00 | NOAA-21 | BUJARU | PARÁ | Brasil | 1501907 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 67608bad-ea52-3101-a591-9476cb7a5900 | -1.61614 | -48.08819 | 2024-10-25 16:54:00 | NOAA-21 | BUJARU | PARÁ | Brasil | 1501907 | 15 | 33 | nan | nan | nan | Amazônia | 42.8 |
| 30144b10-f684-3d3e-a48b-aefd4517163a | -1.59292 | -47.67545 | 2024-10-25 16:54:00 | NOAA-21 | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 5513143a-4dd6-322b-8bc7-5c879a23bfc0 | -1.57385 | -47.8335 | 2024-10-25 16:54:00 | NOAA-21 | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| db50f023-cf9b-380c-a4c2-3b9d70e5686a | -1.57213 | -47.83505 | 2024-10-25 16:54:00 | NOAA-21 | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 61750271-d395-3bc0-a8ef-b365484a3d1f | -1.38084 | -47.87947 | 2024-10-25 16:54:00 | NOAA-21 | INHANGAPI | PARÁ | Brasil | 1503408 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 012f4a7c-368d-365f-a91e-0ad9f50f3720 | -1.34006 | -47.77456 | 2024-10-25 16:54:00 | NOAA-21 | CASTANHAL | PARÁ | Brasil | 1502400 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 979ae44d-2ef1-3e7b-a872-a9b2c533bfc0 | -1.25813 | -47.71769 | 2024-10-25 16:54:00 | NOAA-21 | SÃO FRANCISCO DO PARÁ | PARÁ | Brasil | 1507409 | 15 | 33 | nan | nan | nan | Amazônia | 11.6 |
| e5ce2455-145a-3bb4-b1f5-c1cf9eecad85 | -1.16388 | -48.01757 | 2024-10-25 16:54:00 | NOAA-21 | SANTO ANTÔNIO DO TAUÁ | PARÁ | Brasil | 1507003 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 3784921f-a379-35c7-b26c-605982c53ce2 | -1.16321 | -48.01317 | 2024-10-25 16:54:00 | NOAA-21 | SANTO ANTÔNIO DO TAUÁ | PARÁ | Brasil | 1507003 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| b4828921-4eb9-3766-9b15-67471f825768 | -1.1595 | -48.01374 | 2024-10-25 16:54:00 | NOAA-21 | SANTO ANTÔNIO DO TAUÁ | PARÁ | Brasil | 1507003 | 15 | 33 | nan | nan | nan | Amazônia | 12.4 |
| b19f49f5-0061-3f3d-b103-e2e9259cc720 | -1.02663 | -47.75264 | 2024-10-25 16:54:00 | NOAA-21 | MARAPANIM | PARÁ | Brasil | 1504406 | 15 | 33 | nan | nan | nan | Amazônia | 12.1 |
| 9d3df1d3-10f2-3fee-998a-4420967b6857 | -1.02286 | -47.75327 | 2024-10-25 16:54:00 | NOAA-21 | MARAPANIM | PARÁ | Brasil | 1504406 | 15 | 33 | nan | nan | nan | Amazônia | 12.1 |
| 3832356a-7c6a-3e54-886f-2d23402bc6bd | -1.02284 | -47.75018 | 2024-10-25 16:54:00 | NOAA-21 | MARAPANIM | PARÁ | Brasil | 1504406 | 15 | 33 | nan | nan | nan | Amazônia | 17.4 |
| b57b24a2-3ca3-3481-b947-c38a270f3e64 | -0.98873 | -47.70692 | 2024-10-25 16:54:00 | NOAA-21 | MARAPANIM | PARÁ | Brasil | 1504406 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |


[Clique aqui para ver as próximas entradas](README182.md)
