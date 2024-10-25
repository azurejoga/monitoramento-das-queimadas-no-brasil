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

## Dados Diários - Página 134

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d58f56f2-6352-3021-96a9-88d9a8ebc4cd | -11.89185 | -56.41564 | 2024-10-25 16:50:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 20.7 |
| 234cfafd-8441-3fc4-8ba3-cf16d9b26751 | -11.88514 | -56.22086 | 2024-10-25 16:50:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 12.2 |
| 8798fbcc-0dee-3dfc-a1c9-94a71dc9dddd | -11.88452 | -56.21616 | 2024-10-25 16:50:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 12.2 |
| 07a7bba8-4ec9-39f6-b358-970319c226eb | -11.87933 | -56.21202 | 2024-10-25 16:50:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 24dba596-c1e7-34ad-ac62-e54ced8edd82 | -11.47199 | -55.67528 | 2024-10-25 16:50:00 | NOAA-21 | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 24.9 |
| ea4b90c2-e667-3afa-a15a-a38cd843dce3 | -11.11813 | -55.44702 | 2024-10-25 16:50:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 8.9 |
| c8fd444a-1ae7-3713-a4b3-9f7c10973713 | -12.73428 | -56.97426 | 2024-10-25 16:50:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 19.6 |
| cf46b5e3-b7aa-3e43-83d4-e611165b31f8 | -13.74177 | -56.08654 | 2024-10-25 16:50:00 | NOAA-21 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 4f7e2687-6b92-338f-bdb9-03252de78fef | -13.74054 | -56.08869 | 2024-10-25 16:50:00 | NOAA-21 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 30.6 |
| 455eef1b-6ea2-3a6e-a063-c710de4fd693 | -13.73712 | -56.0872 | 2024-10-25 16:50:00 | NOAA-21 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 15.5 |
| 69e0503f-b074-3100-96c9-f5628ebdc270 | -15.65532 | -56.5873 | 2024-10-25 16:50:00 | NOAA-21 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 9.1 |
| ce4dd972-d9d9-3648-9336-cc3e7c7b51c2 | -17.84488 | -57.61174 | 2024-10-25 16:50:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 11.3 |
| 467244e9-7055-348a-a4ac-8492ce91b2e9 | -17.84447 | -57.60793 | 2024-10-25 16:50:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 9.8 |
| 47a48faf-d86f-3745-9a60-be097a8ce58e | -17.83906 | -57.60889 | 2024-10-25 16:50:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 9.8 |
| 221f52ba-953d-3ca0-88c7-5928b1662ac0 | -17.77111 | -57.59085 | 2024-10-25 16:50:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 14.3 |
| 17a35d45-44b5-3b20-bab8-21683285da00 | -17.76387 | -57.59114 | 2024-10-25 16:50:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 11.2 |
| 9fcea780-12e9-3b68-9f81-fa354ee9e736 | -17.7548 | -57.59261 | 2024-10-25 16:50:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 47.3 |
| a3fe2368-41c4-3412-8d49-f52fc1a22ebf | -17.753 | -57.59229 | 2024-10-25 16:50:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 17.9 |
| aa69300e-2efc-3af2-9da5-4c5956b8d731 | -17.74899 | -57.58957 | 2024-10-25 16:50:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 66.5 |
| f9a36d0a-23cf-3367-b61d-e5e2e8f1654e | -17.74717 | -57.58925 | 2024-10-25 16:50:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 40.8 |
| 6fc6f597-7e44-3f25-8792-4714317e69b9 | -17.74173 | -57.58982 | 2024-10-25 16:50:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 40.8 |
| 9ab9ac4d-32e9-3a71-842d-c1e413b7da94 | -17.7363 | -57.5904 | 2024-10-25 16:50:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 19.5 |
| a9ad9b5b-d067-3f19-9097-7437adb8237a | -17.73591 | -57.5868 | 2024-10-25 16:50:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 19.5 |
| fad54a76-72b9-3011-8061-593daa3c7c7d | -18.11485 | -57.30673 | 2024-10-25 16:50:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 9.3 |
| f4eee61e-ae32-3b16-ba23-15611eb1fd64 | -18.10076 | -57.27646 | 2024-10-25 16:50:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.4 |
| 9932af9d-d5fc-3ea2-b2ec-459d6e906c61 | -18.09043 | -57.28109 | 2024-10-25 16:50:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 12.2 |
| e5b3ea10-4138-3d76-81a7-4f90c813a2ee | -18.09006 | -57.2776 | 2024-10-25 16:50:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 22.1 |
| 2a0aab56-5b05-344d-a75a-c2a9ddcd501b | -18.08969 | -57.27412 | 2024-10-25 16:50:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 22.1 |
| eb1a6e44-0a9a-30ba-814b-4d4a4aed0f8f | -18.06429 | -57.23827 | 2024-10-25 16:50:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.6 |
| b6ed21d2-1ad6-3d76-9029-da708c8d37aa | -18.05782 | -57.36267 | 2024-10-25 16:50:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.9 |
| 6a8e918e-8a69-30f1-84da-dd07fe46bc6f | -18.05562 | -57.36285 | 2024-10-25 16:50:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 12.4 |
| 4eb1fa10-5b38-3650-b545-83e34b095003 | -18.05526 | -57.35933 | 2024-10-25 16:50:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 11.3 |
| 3d5d509f-2d2f-312a-9623-f32ddcb677d3 | -18.05322 | -57.37031 | 2024-10-25 16:50:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 13.9 |
| e3621650-8fe8-3115-8641-8ae56175b87a | -18.05284 | -57.36677 | 2024-10-25 16:50:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 14.0 |
| fd547d14-8c71-3a3d-9a44-79d0903b61d5 | -18.05245 | -57.36324 | 2024-10-25 16:50:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 14.0 |
| 445923c2-2aab-334d-bef5-b4434e25d794 | -18.05206 | -57.35972 | 2024-10-25 16:50:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 13.2 |
| 87bcbdf0-4fdd-35e7-9b9e-3c0d2f36e9af | -18.05134 | -57.37405 | 2024-10-25 16:50:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 15.2 |
| 87e7ccc7-d921-3ed4-8525-653a32583dd8 | -18.05098 | -57.37051 | 2024-10-25 16:50:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 15.2 |
| a0aa38a4-a75d-3e6c-aa5a-50d4ecef9763 | -18.05061 | -57.36698 | 2024-10-25 16:50:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 25.1 |
| 9395af70-eaa1-3ada-bd92-d9716930c9fc | -18.04988 | -57.35991 | 2024-10-25 16:50:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 11.3 |
| 43d441b2-a315-343a-a459-538769004f27 | -18.04824 | -57.37442 | 2024-10-25 16:50:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 13.9 |
| 1de1ffe1-7b5a-3fc3-9234-2d12fb2115aa | -18.04785 | -57.37088 | 2024-10-25 16:50:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 13.9 |
| 95629a4b-8dfa-36d1-9731-d234438b0ba0 | -18.04702 | -57.31417 | 2024-10-25 16:50:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 20.2 |
| b03e32fa-7813-3ec3-80bb-f77ca0009202 | -18.04596 | -57.37463 | 2024-10-25 16:50:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 15.2 |
| 897a2f58-0936-37a7-a22f-d11ac4883ce7 | -18.04552 | -57.34975 | 2024-10-25 16:50:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 22.9 |
| 655a467f-c2f8-3d97-b668-e7147b8f82b2 | -18.04518 | -57.31425 | 2024-10-25 16:50:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 43.8 |
| c14999ff-4bf4-36b1-a949-37c85176c78b | -18.04379 | -57.35344 | 2024-10-25 16:50:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 13.2 |
| 0488e576-7e4d-3d56-8fd3-fbb3ac02aaad | -18.04342 | -57.34992 | 2024-10-25 16:50:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 13.2 |
| 0d0debd7-0659-3986-ad7a-5038e0a9db1f | -18.04286 | -57.37499 | 2024-10-25 16:50:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 12.7 |
| b681d1ce-e2bb-3f20-8f7c-fb04b2d07eb3 | -18.04166 | -57.31473 | 2024-10-25 16:50:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 20.2 |
| 6a7ec332-6864-34c5-abc7-d49fca45a5af | -18.03977 | -57.34679 | 2024-10-25 16:50:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 14.4 |
| 48638d97-acb5-3b74-abe6-180d8db0c6c0 | -18.03787 | -57.37909 | 2024-10-25 16:50:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 15.1 |
| 1edc16ad-b11d-375e-9af5-02380de196ab | -18.03748 | -57.37556 | 2024-10-25 16:50:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 12.7 |
| 0b238c7e-632a-3cd0-a23c-101c2f3602bf | -18.03709 | -57.37203 | 2024-10-25 16:50:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 12.7 |
| 9add2072-fccc-3317-a2c9-c9aad6894760 | -18.02597 | -57.31993 | 2024-10-25 16:50:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 45.7 |
| ca130f59-fdf2-3813-a58f-5fd958224d79 | -18.01799 | -57.247 | 2024-10-25 16:50:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 13.6 |
| 6e79e074-5195-3824-af11-9789358d847c | -18.01762 | -57.24354 | 2024-10-25 16:50:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.5 |
| a45fc392-4b36-3859-aef3-2e91fa4cc98e | -17.99545 | -57.44092 | 2024-10-25 16:50:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 14.1 |
| aea89d32-975a-3938-a5b9-0662bf5ed5c2 | -17.93723 | -57.19662 | 2024-10-25 16:50:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.0 |
| 418e6d3d-2a1c-31f0-9841-1e8d8557c7df | -17.93548 | -57.21904 | 2024-10-25 16:50:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 4cf8fb9f-7c23-338f-bab6-5721925071e5 | -17.93407 | -57.21777 | 2024-10-25 16:50:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 8.7 |
| 14557113-6991-3e12-99bd-f489d4b052ca | -17.93371 | -57.21432 | 2024-10-25 16:50:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 8.7 |
| ed013101-5798-34bd-a438-cd94337cbb29 | -17.93335 | -57.2109 | 2024-10-25 16:50:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.5 |
| 77468479-23f9-38e4-a61b-8cd0c59f9d9d | -17.93016 | -57.21961 | 2024-10-25 16:50:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 26.8 |
| a5f35e3d-2b4e-366e-8df8-600880c93257 | -17.92978 | -57.21618 | 2024-10-25 16:50:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 26.8 |
| 3b2db68a-d8c8-3589-93fb-e6d29486fde3 | -17.9294 | -57.21275 | 2024-10-25 16:50:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 23.6 |
| 7e1d2b54-a2cb-3b24-bc7f-841b6ffcac85 | -17.92911 | -57.22179 | 2024-10-25 16:50:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 12.3 |
| 2cb26911-0f36-38d7-a4d0-dc6d32736850 | -17.92875 | -57.21836 | 2024-10-25 16:50:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 19.0 |
| f4a04524-dd01-3fa3-a5f8-0d763cc8a3d7 | -17.92839 | -57.21492 | 2024-10-25 16:50:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 19.0 |
| 4645d8aa-3813-3793-a9f4-597abb6abc31 | -17.92561 | -57.22705 | 2024-10-25 16:50:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 14.1 |
| 5a71adee-c901-3eb0-aded-35a042d4f400 | -17.92523 | -57.22361 | 2024-10-25 16:50:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 14.1 |
| d167460a-5df8-3963-b3c8-51c268429541 | -17.92484 | -57.22019 | 2024-10-25 16:50:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 26.8 |
| fbe052ea-693d-38bb-b21d-d48f82a76839 | -17.92415 | -57.22581 | 2024-10-25 16:50:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 12.3 |
| d189e34d-87c2-3577-b01f-a7b1839529a0 | -17.92379 | -57.22238 | 2024-10-25 16:50:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 12.3 |
| a8724f96-e50f-3d49-9260-4eaa4643683a | -17.92344 | -57.21895 | 2024-10-25 16:50:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 19.0 |
| 1faaf5f4-55ad-3886-a16a-7b12bc50b3bf | -17.91991 | -57.22419 | 2024-10-25 16:50:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.3 |
| c5b374bd-c55c-3fa2-9d80-4caa5ab562a3 | -17.91078 | -57.23906 | 2024-10-25 16:50:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.5 |
| 5f08b0b6-1dbb-39a7-80c6-937b3d7f6c9c | -17.9104 | -57.23562 | 2024-10-25 16:50:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.3 |
| bfb7c6de-1c1a-3f76-9188-cced0da465d0 | -17.30832 | -57.47191 | 2024-10-25 16:50:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.3 |
| d0d4ac50-e7ac-3969-93e2-b5e968a5e327 | -17.3014 | -57.45854 | 2024-10-25 16:50:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 17.0 |
| e1d4be2f-d898-3625-89be-3c0a9b1abb5d | -17.29288 | -57.29458 | 2024-10-25 16:50:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 14.9 |
| f141adac-6eef-3784-b0d6-650e26c2ed42 | -17.2841 | -57.30388 | 2024-10-25 16:50:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 12.3 |
| 83be7112-b9b2-3799-8a22-c52a92390197 | -17.27842 | -57.30107 | 2024-10-25 16:50:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 11.1 |
| 29b042c6-eaca-37ef-a857-3ad5b8af7540 | -17.25924 | -57.51973 | 2024-10-25 16:50:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 16.5 |
| 29593307-daf3-3dd8-8d3f-6aa6b00ff5fe | -17.25768 | -57.21123 | 2024-10-25 16:50:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 11.8 |
| a57a0dd5-aa73-3621-853b-88f4ed4f8508 | -17.25697 | -57.4987 | 2024-10-25 16:50:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 14.1 |
| 908fee8f-a3c6-3568-b187-64cd5092778d | -17.25198 | -57.50279 | 2024-10-25 16:50:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 14.1 |
| e8e7a096-5d3a-3624-8a1f-b41e1b6e1454 | -17.2513 | -57.2018 | 2024-10-25 16:50:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 8.0 |
| cff4ea9b-db9d-3129-9629-7dcb6c75259c | -17.25092 | -57.19846 | 2024-10-25 16:50:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 22.9 |
| 24bc5994-b234-3a96-9f1b-727dffa51865 | -17.24677 | -57.20905 | 2024-10-25 16:50:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 8.7 |
| b382d818-08ed-3cac-a653-aeee682686f1 | -17.24603 | -57.20238 | 2024-10-25 16:50:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.4 |
| 8fea3a6f-6861-3b14-beea-85fb880b5710 | -17.24492 | -57.19233 | 2024-10-25 16:50:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 53.0 |
| 2cbd8c5e-a2f2-3847-aa58-d21574a2e493 | -17.2415 | -57.20963 | 2024-10-25 16:50:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 8.7 |
| 61bbe0bb-d16c-337e-b2e3-ff98bbc13ac6 | -17.24113 | -57.20629 | 2024-10-25 16:50:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.4 |
| ea463295-1d9c-3e98-af36-f575c0b293f0 | -17.24039 | -57.19959 | 2024-10-25 16:50:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 19.0 |
| 7ca9c93f-3972-395f-a2e4-a6e931a410f9 | -17.24002 | -57.19624 | 2024-10-25 16:50:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 19.0 |
| c3f217be-88e2-3244-9481-61317e208d00 | -17.23928 | -57.18957 | 2024-10-25 16:50:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 53.0 |
| 60069c24-a9f7-3f6e-bcfb-9186b4e12748 | -17.23886 | -57.53262 | 2024-10-25 16:50:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 9.5 |
| 88c7bbc7-f69f-39b4-b58b-a876327b18e8 | -17.23771 | -57.22359 | 2024-10-25 16:50:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 13.8 |
| ab52a166-e075-3ec8-9f6b-301642e7cc04 | -17.23097 | -57.21077 | 2024-10-25 16:50:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 20.2 |


[Clique aqui para ver as próximas entradas](README135.md)
