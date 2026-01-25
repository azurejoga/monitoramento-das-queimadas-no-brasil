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

## Dados Diários - Página 7

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7e56f92d-3a77-3c35-bdab-315fed3503f6 | -20.57378 | -55.56433 | 2026-01-25 05:20:00 | NPP-375D | DOIS IRMÃOS DO BURITI | MATO GROSSO DO SUL | Brasil | 5003488 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bf0f9856-b0aa-3706-8b8c-b5b9847c4e93 | -19.6454 | -57.28895 | 2026-01-25 05:20:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 305abb0e-c7bb-32df-b400-1644cdb00d87 | -19.61508 | -57.26614 | 2026-01-25 05:20:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 30.9 |
| 63047359-c16e-329b-b564-f5a7a2d1bf4a | -19.63997 | -57.27453 | 2026-01-25 05:20:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 69.4 |
| 7d09160a-04f6-38d9-a238-79c9e571ea6d | -19.63093 | -57.23231 | 2026-01-25 05:20:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 257eeecf-9550-3c2f-8700-00a0d99aa33e | -15.60321 | -59.94326 | 2026-01-25 05:20:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f5d781d2-3904-3f95-8f40-3bc530763324 | -20.6372 | -51.67877 | 2026-01-25 05:20:00 | NPP-375D | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d29aaeb7-57ce-399d-88f3-110915fc4621 | -19.61873 | -57.2667 | 2026-01-25 05:20:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 30.9 |
| 1ce50316-b55f-327c-b890-1e177d0f3cd0 | -19.63633 | -57.27397 | 2026-01-25 05:20:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 69.4 |
| 331927af-4a1e-3473-8b3a-e72b2fa77767 | -19.64726 | -57.27567 | 2026-01-25 05:20:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.0 |
| 39152042-003c-328f-9108-73dfe27d7edf | -19.64121 | -57.26567 | 2026-01-25 05:20:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 77e90dec-3754-30c8-9dea-b2a1a8eb88e3 | -19.64862 | -57.2123 | 2026-01-25 05:20:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 822bd049-85d2-318c-96de-6a86113b99c4 | -19.6509 | -57.27623 | 2026-01-25 05:20:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.0 |
| b9d24ab4-bd0c-3382-9258-1aaa9839f6fa | -19.6533 | -57.28566 | 2026-01-25 05:20:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| a74ea43e-af73-33cb-8904-5baed529c283 | -19.65841 | -57.19558 | 2026-01-25 05:20:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 51906357-26b1-37eb-a38e-bf823a925bd5 | -19.64973 | -57.25793 | 2026-01-25 05:20:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.7 |
| 89bfdbef-7cc6-349f-af7e-baedacc29976 | -18.79654 | -57.65564 | 2026-01-25 05:20:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.0 |
| 0d7008e7-d4c7-3e04-a504-e4ac69f429ef | -19.64008 | -57.22008 | 2026-01-25 05:20:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.6 |
| 8093a0af-3e88-3ecd-a71a-5a3b63c06da0 | -20.32644 | -57.83193 | 2026-01-25 05:20:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.3 |
| c6c55e9c-2c8e-3872-b907-7eef1ff846fe | -19.6859 | -57.18613 | 2026-01-25 05:20:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 7e0bafd8-cd95-34a4-b621-4675183167bd | -19.62179 | -57.24451 | 2026-01-25 05:20:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 8b8ecf6e-2865-3e7b-bf59-2953bb08b24e | -17.5829 | -53.0723 | 2026-01-25 05:20:00 | NPP-375D | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7ec2ce25-56f0-36e7-bbce-e35a456d387d | -20.91524 | -56.37923 | 2026-01-25 05:20:00 | NPP-375D | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 60fa60e0-cb5e-32d0-9026-cc5a492a872f | -19.64911 | -57.26237 | 2026-01-25 05:20:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.2 |
| 6a0048ce-0e9f-329f-8e4d-1fc3eb2f7e8b | -20.34789 | -57.83534 | 2026-01-25 05:20:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 6efcfc42-f9ea-3d98-b92e-d551bf8c0fa9 | -19.64664 | -57.28009 | 2026-01-25 05:20:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 8a0db756-96ef-338d-9c0f-eb67b3e5df26 | -19.68389 | -56.8458 | 2026-01-25 05:20:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 69915e61-165e-3d15-96b9-0c26c033cdc5 | -19.65352 | -57.20395 | 2026-01-25 05:20:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.9 |
| cfab1ff9-fa67-3762-a6f8-62e7970e44b2 | -20.34493 | -57.83049 | 2026-01-25 05:20:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 77bcca33-4e13-3176-84e7-b6733c926791 | -20.32287 | -57.83136 | 2026-01-25 05:20:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.4 |
| 43e8c303-7359-32b5-b1db-d9dbce1d57e8 | -19.68224 | -57.18557 | 2026-01-25 05:20:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| c7e28935-783a-3e42-a007-e240eacb1891 | -21.35652 | -56.86854 | 2026-01-25 05:20:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 1.8 |
| dba69919-a2c0-3bae-95a0-940819ad5cd7 | -19.66698 | -57.18777 | 2026-01-25 05:20:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.7 |
| a8fa1314-2950-36e7-85b7-470c6a20ca16 | -19.62605 | -57.24063 | 2026-01-25 05:20:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| aaae8eaf-ddbc-35d4-947d-389302d3cdcd | -19.65152 | -57.27181 | 2026-01-25 05:20:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 5f836fc9-77fc-3eac-ada3-0018d20ddb68 | -19.64361 | -57.2751 | 2026-01-25 05:20:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.0 |
| 3b5c4e19-9eb7-3b16-a6b7-ad14d1a11578 | -21.35426 | -56.8667 | 2026-01-25 05:20:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a59a9310-1259-39fb-8d25-cc448e5f8396 | -18.81284 | -51.60585 | 2026-01-25 05:20:00 | NPP-375D | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 40877d30-3981-3128-bd0c-1281cef07a2b | -19.64602 | -57.28453 | 2026-01-25 05:20:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 38f70dcf-b2e4-3cf5-bf9f-012029f4c212 | -19.64238 | -57.28396 | 2026-01-25 05:20:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 29ad70cb-fad7-3ee6-8be4-03ba8bd2d648 | -16.01803 | -59.90586 | 2026-01-25 05:20:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 10258dc1-ad45-37dd-8458-46a745ada82e | -19.6175 | -57.27556 | 2026-01-25 05:20:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 32.9 |
| 9e79d849-99bc-3827-aa57-f8b6a7bd2b89 | -19.63935 | -57.27897 | 2026-01-25 05:20:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 39.8 |
| 2b715666-104b-3fc8-9f7e-dee3221c4e81 | -20.33002 | -57.8325 | 2026-01-25 05:20:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.3 |
| fa9b0490-3f9d-3a16-9f0d-34aafa741dfd | -19.63268 | -57.2734 | 2026-01-25 05:20:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.7 |
| 09419f6c-c504-3635-83a6-d6b154fe0451 | -19.63571 | -57.2784 | 2026-01-25 05:20:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 39.8 |
| 1b740f18-48f9-3e8c-b062-77b0692409d4 | -19.6157 | -57.2617 | 2026-01-25 05:20:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.4 |
| 80960c64-80a4-3340-9739-e24540b435db | -18.79003 | -57.65033 | 2026-01-25 05:20:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 0f255cad-b6fc-3f71-8e1e-e4308b7a4f91 | -18.7924 | -57.65925 | 2026-01-25 05:20:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.8 |
| cc7f9809-28fc-3c88-b196-278a45cf74f2 | -19.67858 | -57.185 | 2026-01-25 05:20:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| fe6d5830-e3e0-3ad9-900a-13f119262c98 | -19.62843 | -57.27726 | 2026-01-25 05:20:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 54.2 |
| f86bbce8-81ea-338c-800c-9cca2f85ca4a | -19.64176 | -57.28838 | 2026-01-25 05:20:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.0 |
| c90620be-1016-3e2d-bbca-be6c79b766d9 | -19.29832 | -53.17932 | 2026-01-25 05:20:00 | NPP-375D | PARAÍSO DAS ÁGUAS | MATO GROSSO DO SUL | Brasil | 5006275 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fda40250-8f6d-3bfb-b924-22847f306881 | -21.07472 | -49.53226 | 2026-01-25 05:20:00 | NPP-375D | NOVA ALIANÇA | SÃO PAULO | Brasil | 3532801 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| b9a93c20-d898-3796-8d31-02f0cf68ff07 | -19.67126 | -57.18386 | 2026-01-25 05:20:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| e2b3ead2-9095-3371-9265-3233b6ef3543 | -19.67492 | -57.18443 | 2026-01-25 05:20:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| ad8cf6b3-f853-3111-bee9-ee06f2b0946b | -19.62115 | -57.27613 | 2026-01-25 05:20:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 57.0 |
| fb576386-4a0a-3f42-a15c-0add2a4b6379 | -19.643 | -57.27953 | 2026-01-25 05:20:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| f72acee1-9e3c-387a-a06c-0ae8eea7f0ed | -19.69443 | -56.85215 | 2026-01-25 05:20:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 489fee74-47df-30ea-87d3-f00d064bdbe9 | -19.63207 | -57.27783 | 2026-01-25 05:20:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 54.2 |
| 295f8bbc-fddf-35f3-b42a-0625fe307da9 | -17.58747 | -53.07298 | 2026-01-25 05:20:00 | NPP-375D | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4010a534-8b30-34cd-8a14-733e0edf4d66 | -19.61022 | -57.27443 | 2026-01-25 05:20:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| bb7186dc-161a-334b-a76a-f8ea66d1a415 | -18.79062 | -57.64616 | 2026-01-25 05:20:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.6 |
| f7a52f76-21a5-39fc-b05c-16adadfb37a0 | -19.9969 | -54.36942 | 2026-01-25 05:20:00 | NPP-375D | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2b97347b-16c2-32da-b048-46367a6b0867 | -19.66269 | -57.19168 | 2026-01-25 05:20:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.6 |
| 6e007344-4a74-3a19-9dcc-0c2d372fbe37 | -19.99638 | -54.37377 | 2026-01-25 05:20:00 | NPP-375D | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6bfa6120-c9eb-3f0c-90fa-e2ec23aed7bd | -20.34851 | -57.83106 | 2026-01-25 05:20:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| a645c1b6-8732-30bb-8aeb-452b1e3c5bf2 | -19.65454 | -57.27681 | 2026-01-25 05:20:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 2fc1372f-7cc2-3a26-b93b-c4a3901440be | -19.65414 | -57.19948 | 2026-01-25 05:20:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.9 |
| d0b2a6db-fbb9-3869-9d7e-6b046f41dd0a | -16.18561 | -59.33483 | 2026-01-25 05:20:00 | NPP-375D | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5327396f-13db-384f-a475-a071580f1baf | -19.6907 | -56.85159 | 2026-01-25 05:20:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 4.3 |
| ba4b8804-9275-399d-aaf3-96d2e4a9f20b | -20.34135 | -57.82993 | 2026-01-25 05:20:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| a2b8288e-3d91-3410-83bb-66251c979d69 | -19.62176 | -57.2717 | 2026-01-25 05:20:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.9 |
| 6fac250a-ab9b-3aed-9b3c-73a44c9708db | -20.31869 | -57.83507 | 2026-01-25 05:20:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 33fec1ab-75d2-3751-924d-109537bbca77 | -19.61812 | -57.27114 | 2026-01-25 05:20:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 30.9 |
| 8626200f-0444-32be-a9a4-17c56f7bbb38 | -16.0247 | -59.90699 | 2026-01-25 05:20:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 02158116-35ed-3236-b752-9a98fbe44928 | -19.66339 | -56.85688 | 2026-01-25 05:20:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| dff36607-d686-3a17-9d64-6aed3dd5c190 | -19.64423 | -57.27067 | 2026-01-25 05:20:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.0 |
| e9d5b2f9-11b7-3ff7-84ae-56ba6d70c86a | -19.61934 | -57.26227 | 2026-01-25 05:20:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.4 |
| 480a1b1b-8b95-3b4b-9a10-c25a268c8d7c | -19.66711 | -56.85746 | 2026-01-25 05:20:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| e042c681-dd54-377e-9fb0-b09978fc9b91 | -19.65214 | -57.26737 | 2026-01-25 05:20:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| d810f316-5889-33d9-9bfb-d2b69a366a88 | -21.0687 | -49.53172 | 2026-01-25 05:20:00 | NPP-375D | NOVA ALIANÇA | SÃO PAULO | Brasil | 3532801 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 02f22e3c-e832-3ce0-a926-6b89be7e4a18 | -18.81318 | -51.60267 | 2026-01-25 05:20:00 | NPP-375D | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9d0365cd-14cd-35bc-8061-c44b566059d6 | -16.02803 | -59.90756 | 2026-01-25 05:20:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c32f2c07-4a71-31c2-8f44-2c7e8ccb5de7 | -19.62667 | -57.23619 | 2026-01-25 05:20:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 4ea08c33-eb13-33a3-8d53-a1f6a5365f6b | -19.63874 | -57.2834 | 2026-01-25 05:20:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 39.8 |
| dab28b81-682e-3cfc-8a2c-9ae9a39676f9 | -16.44386 | -58.16671 | 2026-01-25 05:20:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.0 |
| 154123a9-2884-3331-94a5-953975638fbe | -19.63947 | -57.22454 | 2026-01-25 05:20:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 6b61c6fb-6be0-3fd2-b114-2efdc9aeda01 | -19.68761 | -56.84637 | 2026-01-25 05:20:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.2 |
| d3c5c535-590b-31ce-b023-f1a5b7169397 | -19.2989 | -53.17433 | 2026-01-25 05:20:00 | NPP-375D | PARAÍSO DAS ÁGUAS | MATO GROSSO DO SUL | Brasil | 5006275 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 88d7d98a-03d3-394d-847c-b0cbae345b8e | -19.64435 | -57.21619 | 2026-01-25 05:20:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| d8d654a3-e49e-344c-b44c-7374a97e9d38 | -19.61386 | -57.27499 | 2026-01-25 05:20:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 32.9 |
| 732ad8a6-2bdf-3e07-b954-b37f3b484d69 | -19.64485 | -57.26624 | 2026-01-25 05:20:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.2 |
| 1afa65e6-2c88-38db-a42c-2aafc2f1a38f | -16.02412 | -59.91059 | 2026-01-25 05:20:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 31f5b9e2-5d47-37da-a7f6-a011c152c89e | -19.64787 | -57.27124 | 2026-01-25 05:20:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.0 |
| ba16ad6e-d5a7-3bdb-9b8e-20de86e432b6 | -19.64182 | -57.26123 | 2026-01-25 05:20:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 48099ea7-0d51-3b0a-abbb-fcd42139a468 | -20.33717 | -57.83364 | 2026-01-25 05:20:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 7aa897f4-c5e5-329f-b59e-492d1edb1cbe | -19.68527 | -57.19061 | 2026-01-25 05:20:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 6e9e6254-981b-3c10-8cee-2c61af7d06d1 | -20.31929 | -57.8308 | 2026-01-25 05:20:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.4 |
| 7ce73081-450c-3ede-845b-4411f3523d1f | -19.64547 | -57.2618 | 2026-01-25 05:20:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.2 |


[Clique aqui para ver as próximas entradas](README8.md)
