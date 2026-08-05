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

## Dados Diários - Página 25

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 258b393a-cb1c-3d7e-b846-8169b829ab0c | -6.3343 | -55.73331 | 2026-08-05 05:40:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| b35a04d1-cd64-3748-a802-7a3b3b07bb9c | -6.5343 | -55.16618 | 2026-08-05 05:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 23a27cf0-b032-3d58-92a2-2c7b5701e1eb | -2.91747 | -54.16578 | 2026-08-05 05:40:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| bb56bc58-0a9e-3fc2-b38a-f9b67b880960 | -4.95698 | -62.35398 | 2026-08-05 05:40:00 | NOAA-20 | BERURI | AMAZONAS | Brasil | 1300631 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0212b2e6-4db2-36f2-80e8-d4ffc80865f6 | -3.32896 | -54.67535 | 2026-08-05 05:40:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 30649b05-2063-3b8a-af27-0a0447672bf9 | -6.55607 | -55.17081 | 2026-08-05 05:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d57e6d27-81c0-3cca-b9cc-e13e43f8f606 | -3.39691 | -59.57124 | 2026-08-05 05:40:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7d68bce9-d3c8-34df-9b9e-ddc5c6f1458b | -4.9191 | -62.31915 | 2026-08-05 05:40:00 | NOAA-20 | BERURI | AMAZONAS | Brasil | 1300631 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d6f94ff0-bfaf-35df-a62f-73c4a60f883a | -6.53614 | -55.15358 | 2026-08-05 05:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6426717c-48da-30db-9762-7162920f1b90 | -6.55394 | -55.1479 | 2026-08-05 05:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 05e43a58-4002-35ca-bf20-49287dc23dd9 | -6.53049 | -55.15588 | 2026-08-05 05:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7e9183e4-8504-3350-85bf-a8fb8f7c6149 | -6.64929 | -56.41743 | 2026-08-05 05:40:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0eb2904f-5a97-33f5-bf3f-b498484e0f05 | -6.58257 | -56.54382 | 2026-08-05 05:40:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 78e9adc7-6919-3294-8fd6-17b451f625eb | -6.57342 | -55.16058 | 2026-08-05 05:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 21a37092-dc87-3ce5-bd22-7b4d09d877db | -4.05485 | -56.23087 | 2026-08-05 05:40:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| dc395dfb-8dc2-3285-9c4b-f80dd8d11ab3 | -6.33927 | -55.73414 | 2026-08-05 05:40:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 6a90b2c6-19be-3d91-85dd-52cceb0345a8 | -6.55956 | -55.14571 | 2026-08-05 05:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2339d000-a414-348e-a596-5d160457c637 | -6.5409 | -55.16541 | 2026-08-05 05:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e9c6bcbd-c36d-34ce-a158-8572349de625 | -6.5721 | -55.16999 | 2026-08-05 05:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 78acfc0d-aa3d-3d46-ae41-28f0cb1bfd1a | -6.53567 | -55.15676 | 2026-08-05 05:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d4f982b9-94b0-3555-9c03-492574fc0212 | -6.53139 | -55.15737 | 2026-08-05 05:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 37fd7499-f580-3e13-a1ba-9c251680376f | -6.5366 | -55.15039 | 2026-08-05 05:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 063f24d9-37a1-3bcf-b130-ef10ce32fb45 | -6.22609 | -55.59521 | 2026-08-05 05:40:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4555c3c5-c6b0-3e55-bc1a-b88cca56bf2e | -3.32849 | -54.67847 | 2026-08-05 05:40:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| de330380-7330-35d9-8c50-7098d9c47826 | -6.53226 | -55.15104 | 2026-08-05 05:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9227760d-6738-3ba4-bb02-1c0ca4728732 | -6.56733 | -55.16613 | 2026-08-05 05:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ef00ee06-3f7f-3a9c-a574-4b54de1c9e97 | -6.54784 | -55.1536 | 2026-08-05 05:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 7d8bcfbf-db61-3351-8420-b2d00e93f161 | -6.5833 | -56.53868 | 2026-08-05 05:40:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d8e3b113-0ec7-3397-a8f3-74be3f4ce3d2 | -6.56518 | -55.14351 | 2026-08-05 05:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b2a77bfb-1ff5-389b-9a66-b72ccbc81ffe | -2.91675 | -54.16604 | 2026-08-05 05:40:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 310e1850-7835-3384-b809-2bf65fa044ff | -2.9122 | -54.16499 | 2026-08-05 05:40:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1b3b3c9d-c70e-3098-82e6-5b7a3f4dca52 | -6.33395 | -55.7336 | 2026-08-05 05:40:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b9c3a4a1-fcce-3c9b-a64a-ba695263e20d | -6.53476 | -55.16306 | 2026-08-05 05:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5f5fe3e9-3b7f-3dfd-ab5a-8e0fac7fd8b2 | -6.56983 | -56.53142 | 2026-08-05 05:40:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b8889551-5352-3f1f-93fa-fd78f9982099 | -6.3339 | -55.73613 | 2026-08-05 05:40:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 73904040-4a86-3440-9499-5f48cb961a61 | -6.55173 | -55.16384 | 2026-08-05 05:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d6bd68f9-9ea1-3304-a66d-f8056868683f | -6.5743 | -55.15433 | 2026-08-05 05:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 262a505e-3c9b-3f3d-b446-4b3c48d0362a | -6.53745 | -55.1519 | 2026-08-05 05:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b725a70c-8d73-3278-9616-f4ebbdebfff7 | -6.4223 | -55.79377 | 2026-08-05 05:40:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6ffeb912-ccc1-31e4-a11a-3c89fd14b775 | -6.55437 | -55.14481 | 2026-08-05 05:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 77952e29-9534-3137-b836-8c5e53ffaf51 | -4.9096 | -62.33585 | 2026-08-05 05:40:00 | NOAA-20 | BERURI | AMAZONAS | Brasil | 1300631 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b61d6e66-9c30-3589-8fdb-05d1cc8f61a8 | -6.55261 | -55.15751 | 2026-08-05 05:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 319f27c1-90f2-3f47-b0c3-1950e39822be | -6.53571 | -55.16457 | 2026-08-05 05:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8e62189d-8209-31f3-b15e-97ceffc2b02a | -6.57773 | -55.16769 | 2026-08-05 05:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 02215b42-8905-3618-b375-d803f5227b66 | -6.5565 | -55.1677 | 2026-08-05 05:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 520280d4-903f-3d8b-b2a8-7a7f058ee597 | -6.33313 | -55.73925 | 2026-08-05 05:40:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 31b26943-d535-3050-a0c2-0e18218421b0 | -6.54695 | -55.16001 | 2026-08-05 05:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ac87d2aa-ff86-3071-a605-2954c2208c69 | -6.55217 | -55.16069 | 2026-08-05 05:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f8aaa145-3f26-3bc9-9041-0021551b254b | -3.18648 | -52.88168 | 2026-08-05 05:40:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5597524c-55c9-3f27-bd71-af8a99a1b0c4 | -6.56909 | -55.15358 | 2026-08-05 05:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| df4782cb-f459-3c52-b841-00999bae0ae9 | -6.56865 | -55.15672 | 2026-08-05 05:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 645f88a5-8a86-3243-a0a2-96c86a729531 | -6.5535 | -55.1511 | 2026-08-05 05:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e8b97cc2-a448-3b56-a3c4-18c28c90cb71 | -6.53658 | -55.15829 | 2026-08-05 05:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 13492a37-a235-3d0a-8544-e8d1830244e2 | -6.57298 | -55.16371 | 2026-08-05 05:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ed43de73-71bb-3f53-8eff-f1287b68678d | -3.39497 | -59.57358 | 2026-08-05 05:40:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f476bb40-b8a6-3ff0-8d0f-820fb4cd9457 | -3.18589 | -52.88564 | 2026-08-05 05:40:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 625d5871-0731-3db3-bc7d-aed7306868c0 | -6.53095 | -55.15272 | 2026-08-05 05:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8ae20757-6056-3535-bafa-1cdf8045ebf2 | -6.09854 | -55.81332 | 2026-08-05 05:40:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| cc853932-3f54-3d61-b062-38b1dcfc940c | -6.10239 | -55.81271 | 2026-08-05 05:40:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1c6a0ae3-4fd7-3cff-9bc5-779d799d3823 | -6.54998 | -55.17643 | 2026-08-05 05:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 87bf98b2-8ac3-30a1-9fb7-94f0eb941f91 | -2.51843 | -57.73855 | 2026-08-05 05:40:00 | NOAA-20 | URUCARÁ | AMAZONAS | Brasil | 1304302 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| dd4003a6-ab1a-366e-98f1-abeb00fbfc55 | -6.56646 | -55.17236 | 2026-08-05 05:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2453afdd-6759-3e1b-a8e9-5967999b4e34 | -6.22566 | -55.59813 | 2026-08-05 05:40:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e9c6fea7-fd23-3365-9d68-c24733d591bd | -6.57055 | -56.52631 | 2026-08-05 05:40:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0adf21cb-d5b8-3ee1-8c65-6bfccd308e02 | -2.86887 | -50.47353 | 2026-08-05 05:40:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 9a35163c-85b7-3204-9318-ae97d7b1f4d9 | -6.53521 | -55.15992 | 2026-08-05 05:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d2ff80d3-2979-39ff-90c0-5b2558bf445f | -6.54953 | -55.17965 | 2026-08-05 05:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b2a12a76-2046-3e98-913b-7326cd2467cc | -6.53183 | -55.15421 | 2026-08-05 05:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| af0dcce9-642b-3723-a7b9-d026ad681281 | -6.55913 | -55.1488 | 2026-08-05 05:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b295970c-7093-38ce-8b34-ed2853cd84f7 | -6.55869 | -55.15196 | 2026-08-05 05:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4112e136-8773-3947-a87e-a8c392f8acd7 | -4.95643 | -62.35752 | 2026-08-05 05:40:00 | NOAA-20 | BERURI | AMAZONAS | Brasil | 1300631 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 375a6c03-cd62-31f4-a951-175f39dd0278 | -6.33967 | -55.73128 | 2026-08-05 05:40:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6c36d022-07b9-3ee7-b1f8-c1532e5b8431 | -6.56777 | -55.16301 | 2026-08-05 05:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 31a786de-a821-34a2-8af7-09a7c5146554 | -6.5669 | -55.16924 | 2026-08-05 05:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 95c7db25-9906-39bf-b4a8-b7b02e86807f | -6.55562 | -55.17399 | 2026-08-05 05:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| aaa96546-4dc0-3e35-8d71-b5e911c118aa | -6.54652 | -55.16315 | 2026-08-05 05:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8d981a53-8238-31df-b27d-5b930f385c8d | -6.53701 | -55.1551 | 2026-08-05 05:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7d6f5931-02b5-3b23-be0a-00dc71745107 | -6.55305 | -55.15431 | 2026-08-05 05:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 29f9bdca-db10-38c5-8eb1-78b3f94ab249 | -6.33893 | -55.73442 | 2026-08-05 05:40:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 0251ae5e-72a8-34da-a20e-d215f69ae6ef | -6.55087 | -55.17001 | 2026-08-05 05:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8acc0279-e75e-3d48-8e3f-9b309d60e4b8 | -6.53614 | -55.16145 | 2026-08-05 05:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 349dfd38-a4d8-39bb-91c0-e34aae0d01d8 | -11.17612 | -54.89772 | 2026-08-05 05:42:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| f2961041-4c93-3ded-b996-f8ccd4ecbea5 | -11.17473 | -54.90907 | 2026-08-05 05:42:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 924bf607-4fd9-38c1-9d4e-c980e1eb96d3 | -11.19311 | -54.89972 | 2026-08-05 05:42:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 16fee254-c066-3355-bc98-adc4c359f3fe | -11.18365 | -54.8832 | 2026-08-05 05:42:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 413e8c8c-c9d9-3240-9fea-7cc88a3489ba | -11.17844 | -54.87877 | 2026-08-05 05:42:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f2770483-8ea7-3bf4-87f3-ac6dd904238b | -11.19934 | -54.8493 | 2026-08-05 05:42:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 82c53ade-f466-3124-aba2-9021930f8f72 | -10.82332 | -65.09512 | 2026-08-05 05:42:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 070c0e1d-f940-3d29-b8f9-d2dcbb332149 | -11.18557 | -54.86757 | 2026-08-05 05:42:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3cf7a491-6b64-3c27-9053-21547bf2988c | -6.72006 | -58.94697 | 2026-08-05 05:42:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9678a007-5f11-3e20-adb9-2c46b1cab599 | -11.19972 | -54.89275 | 2026-08-05 05:42:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| efddbe8a-4823-3a33-8d2a-a634bc237b15 | -11.17278 | -54.87806 | 2026-08-05 05:42:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 51ed67e5-eb82-33ff-98f1-0ef74f0ea6e6 | -11.16558 | -54.91263 | 2026-08-05 05:42:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 44490781-f9b1-313e-ac96-217f4e1ec842 | -11.17519 | -54.90529 | 2026-08-05 05:42:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| f1b46a01-d391-3c14-8d39-55fabe6485fa | -11.16571 | -54.88884 | 2026-08-05 05:42:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 39deba1a-3971-37ae-96e0-5c82da63e543 | -11.20299 | -54.91265 | 2026-08-05 05:42:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ea7b0690-f04a-343b-8ccf-3b892f205280 | -9.97107 | -64.94218 | 2026-08-05 05:42:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a8f1c997-4186-3c9a-a257-8403146e3198 | -10.82276 | -65.09863 | 2026-08-05 05:42:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d18e4783-2ea4-3873-b268-1cd751e02aa0 | -11.20441 | -54.90122 | 2026-08-05 05:42:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c76410eb-3c27-3fee-aa40-151e5e5ef1c5 | -11.1676 | -54.87331 | 2026-08-05 05:42:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |


[Clique aqui para ver as próximas entradas](README26.md)
