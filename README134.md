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
| 01b7ba8e-120c-3923-ab88-dde28935d9f9 | -17.15836 | -57.35255 | 2024-10-07 05:44:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.5 |
| 42b16a89-27b6-3da1-ae21-04e8dcb7116a | -18.7169 | -57.29042 | 2024-10-07 05:44:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| de76e429-2e8d-3bd6-a77e-583c618558f0 | -17.15732 | -57.41702 | 2024-10-07 05:44:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| dc6bfa9c-7415-3750-8f83-41b559f72091 | -17.15394 | -57.33987 | 2024-10-07 05:44:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 8.1 |
| cf716f4d-f1ad-3a25-98fa-17619fe015bf | -17.15352 | -57.34388 | 2024-10-07 05:44:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 10.7 |
| 34c74943-acc7-3c91-9eec-3e5f3e8d82c7 | -17.1531 | -57.34788 | 2024-10-07 05:44:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 10.7 |
| 1ab5bd9e-6593-3704-b154-943570efcb97 | -17.15269 | -57.35189 | 2024-10-07 05:44:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.5 |
| 832ca8b9-ba99-36d7-a339-62b0da82477e | -17.15227 | -57.3559 | 2024-10-07 05:44:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.5 |
| 1243d56b-aa3e-311e-81cd-c29a28a86b40 | -17.15125 | -57.42032 | 2024-10-07 05:44:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.8 |
| 348919f1-51ed-3f78-9c25-da8506e242f5 | -17.15084 | -57.4243 | 2024-10-07 05:44:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.6 |
| 9956f6f9-30b5-3c25-8f1c-987243a863f0 | -17.14659 | -57.35524 | 2024-10-07 05:44:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 5498c7f2-1615-37cd-a27d-7e70843e34c7 | -17.14617 | -57.35926 | 2024-10-07 05:44:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 88b4e5da-6bcb-3adc-b77b-5e74067ef9a6 | -17.1456 | -57.41966 | 2024-10-07 05:44:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.8 |
| a5f3a208-0105-3bb4-a4f4-9ef2f2867bd5 | -17.14518 | -57.42364 | 2024-10-07 05:44:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.6 |
| ecf3891c-f9a1-349f-9d29-b8d2efb8e202 | -17.14477 | -57.42763 | 2024-10-07 05:44:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.6 |
| a27dec30-08ad-3fc9-a4b7-8296b882ba5c | -17.72194 | -57.07882 | 2024-10-07 05:44:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 8.8 |
| 7ae79a7b-7850-3434-9a64-c349248cd1cf | -17.15048 | -56.75279 | 2024-10-07 05:44:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 047c9739-1b3e-30c4-aca9-5271281cce3b | -17.13867 | -56.80898 | 2024-10-07 05:44:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 38526d26-9366-38c2-8c88-b785b6e54f6d | -17.13821 | -56.81334 | 2024-10-07 05:44:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| af46edf7-b12a-3872-bc55-f5c3604701fe | -17.13415 | -56.79528 | 2024-10-07 05:44:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 3dee685e-05ab-36ab-b5fa-76aed0bc229a | -17.1337 | -56.79963 | 2024-10-07 05:44:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 9dfccdfe-d38a-3eb8-8df6-923208ebdea5 | -17.13324 | -56.80397 | 2024-10-07 05:44:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.7 |
| 1ebfad04-9d5b-32ea-bbb5-6b9c5460ccda | -17.13279 | -56.80833 | 2024-10-07 05:44:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.7 |
| 202b3cb9-2176-3d76-b2f9-3de2dbc6b23c | -17.13234 | -56.81268 | 2024-10-07 05:44:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 16.9 |
| 08a31708-811d-3db2-9283-7f189eb82aa8 | -17.13189 | -56.81703 | 2024-10-07 05:44:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 16.9 |
| d268245f-e49c-31cb-b122-6c39a1b10281 | -17.13144 | -56.82137 | 2024-10-07 05:44:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.8 |
| 7bcabe8c-013d-3ad4-aa64-0be323ad3200 | -17.13098 | -56.82574 | 2024-10-07 05:44:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.8 |
| d4a4fe53-f057-39f9-b019-a0430a6b5500 | -17.13053 | -56.83008 | 2024-10-07 05:44:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 3e035590-a53e-3db9-a568-acd1b7be3e8d | -17.13008 | -56.83442 | 2024-10-07 05:44:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 1df6dce4-7517-31c0-b612-e7967bbc6ebe | -17.12963 | -56.83878 | 2024-10-07 05:44:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 3ac62ef7-0df4-352a-9099-9c613ad33bba | -17.12962 | -56.78154 | 2024-10-07 05:44:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 16ac4173-5e21-37b2-ab6d-5a60d8561457 | -17.12917 | -56.78592 | 2024-10-07 05:44:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 77127f75-2e81-3d37-9722-320bdd37fa09 | -17.12872 | -56.79028 | 2024-10-07 05:44:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| d4c2a635-bcff-3225-b5a3-4d4a7763efae | -17.12826 | -56.79464 | 2024-10-07 05:44:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 1ecaf3fc-8dc5-3e9c-b4b1-df8f9402780e | -17.12782 | -56.79898 | 2024-10-07 05:44:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| c8be3eeb-f57e-3fb5-8bac-475ac0425a7b | -17.12737 | -56.80333 | 2024-10-07 05:44:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.7 |
| 37735a29-0dd1-3a2d-b16b-34192eb6fd36 | -17.12691 | -56.80768 | 2024-10-07 05:44:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.7 |
| 584189d9-2ae3-3950-ad52-9d3c6f1bb38d | -17.12646 | -56.81203 | 2024-10-07 05:44:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 16.9 |
| c12d46be-9763-3ef1-a3d1-d67cad1709d2 | -17.12601 | -56.81638 | 2024-10-07 05:44:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 16.9 |
| 2b32a086-bbd2-32e8-b78d-59fd01b32a0c | -17.12556 | -56.82072 | 2024-10-07 05:44:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.8 |
| 781ef4ed-f0ec-3c17-8c87-4cbac1000763 | -17.12511 | -56.82508 | 2024-10-07 05:44:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.8 |
| 49061ce0-6a71-3ab7-9d60-04258dc655cc | -17.12466 | -56.82943 | 2024-10-07 05:44:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 73662bd6-d23f-35f4-81db-a48c8da93271 | -17.12463 | -56.77214 | 2024-10-07 05:44:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 78f0794f-3d3f-3d8b-93d2-de3bc4734c52 | -17.12421 | -56.83377 | 2024-10-07 05:44:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| d6f620c6-75e2-3282-9d36-ff9d9cef15ac | -17.12418 | -56.77652 | 2024-10-07 05:44:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| cb00c44b-d32d-34fe-8756-031d11c19a52 | -17.12376 | -56.83812 | 2024-10-07 05:44:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| b03547fb-0497-3b20-b747-9692a49923cd | -17.12373 | -56.78088 | 2024-10-07 05:44:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 0106e8a3-cf36-3ad7-b566-c78877dc1f3b | -17.12331 | -56.84247 | 2024-10-07 05:44:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| c69b05d8-9a95-3589-b2de-b39c96df940a | -17.12328 | -56.78524 | 2024-10-07 05:44:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 4c2fc855-387d-3a37-896d-71d6584fb2e8 | -17.12283 | -56.78961 | 2024-10-07 05:44:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 144c7572-af30-3523-8163-b023974e7dbd | -17.12238 | -56.79398 | 2024-10-07 05:44:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| d5537e3e-e4ea-3a6b-8de8-327b37e80242 | -17.12193 | -56.79833 | 2024-10-07 05:44:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 8e910fac-c5d8-3e8c-bdf2-7721b7b40419 | -17.12149 | -56.80267 | 2024-10-07 05:44:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 0bf89d7d-75e3-358b-bcf4-2488ba242a8e | -17.12104 | -56.80702 | 2024-10-07 05:44:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 56d446cc-afa5-3aef-8e57-b3ecd9d0e864 | -17.12059 | -56.81139 | 2024-10-07 05:44:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 62877b0a-d5e6-30df-ae67-5bf329b50ced | -17.12014 | -56.81574 | 2024-10-07 05:44:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 019eac45-ffe5-3e08-9bb9-7a877e05fe40 | -17.11969 | -56.82009 | 2024-10-07 05:44:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 3cfc2998-979c-3fa6-9b92-0d61f6a10ed9 | -17.11924 | -56.82443 | 2024-10-07 05:44:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| e5ce7182-9c00-3759-bf6b-bc8e0d5a1a96 | -17.11745 | -56.8418 | 2024-10-07 05:44:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| a581f3ce-80b8-3bb3-8843-d8abc291e746 | -17.11605 | -56.79769 | 2024-10-07 05:44:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 5ea336ee-9698-359a-a5ce-52b0e538a77c | -17.11561 | -56.80202 | 2024-10-07 05:44:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 72dc9730-4ea5-38af-92f4-c0133cb4fd55 | -17.11159 | -56.84114 | 2024-10-07 05:44:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| b776c2f3-7b7e-3c85-98da-fc182b2efc61 | -17.10528 | -56.84482 | 2024-10-07 05:44:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| e1620eb4-7c84-3f93-a7e3-c8b26a3b1d11 | -17.10031 | -56.83549 | 2024-10-07 05:44:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 893ee4c1-cbe9-357a-8622-fb940510683a | -17.09986 | -56.83982 | 2024-10-07 05:44:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| e93bf2db-1926-3651-96be-05215187d1c6 | -17.09444 | -56.83483 | 2024-10-07 05:44:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 0.5 |
| 2e747b8e-5d08-325b-ae34-5b3225b7b812 | -17.094 | -56.83916 | 2024-10-07 05:44:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 0.5 |
| bf71c21a-935f-3386-b43e-d73e848bc486 | -17.08858 | -56.83416 | 2024-10-07 05:44:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 0.5 |
| d98d4837-affe-3642-8a54-6d4adec9b5b9 | -17.08814 | -56.83849 | 2024-10-07 05:44:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 0.5 |
| 8bc78ee4-f872-3281-b092-1c3393a14387 | -17.08339 | -56.83459 | 2024-10-07 05:44:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 0.4 |
| bbe73cf3-5f47-315b-b70c-7b0b1cd85c3b | -17.08292 | -56.83891 | 2024-10-07 05:44:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 0.4 |
| 2fc89b5d-bcc7-3959-990f-5efe59947c54 | -17.08228 | -56.83783 | 2024-10-07 05:44:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 0.8 |
| cae0f04f-c93e-3576-a3b8-2e9f70d6fc6f | -17.07753 | -56.83393 | 2024-10-07 05:44:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 0.4 |
| 82c4f3f0-67ec-31ac-b8c4-9a4034f07c34 | -17.07706 | -56.83826 | 2024-10-07 05:44:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 0.4 |
| db863496-d7ad-32ce-9d94-11609f220cd2 | -17.0766 | -56.84257 | 2024-10-07 05:44:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 4034ca74-6fa1-31b2-89d2-8cbfe755775e | -17.07642 | -56.83715 | 2024-10-07 05:44:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 071758a5-81e3-3bcd-83a9-7fa36d97bb97 | -17.07598 | -56.84147 | 2024-10-07 05:44:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 01299651-ebb1-3be1-8bbd-70506a5ec888 | -17.0712 | -56.83759 | 2024-10-07 05:44:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| e2780f87-0f21-314b-ae11-9d92b722fd54 | -17.07074 | -56.84191 | 2024-10-07 05:44:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 0.4 |
| 56034c25-a896-3cd2-bc84-757f2f82a31a | -17.07012 | -56.8408 | 2024-10-07 05:44:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 09255e18-2a4c-3607-994c-631342ad2e97 | -17.06469 | -56.83582 | 2024-10-07 05:44:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 38e0d2e5-efe9-3809-8d7c-768919eb9863 | -17.05883 | -56.83515 | 2024-10-07 05:44:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 4016cc0a-90c5-3a64-81b5-e2ff0b1fd16c | -16.79774 | -57.40024 | 2024-10-07 05:44:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| 667dab87-d2e7-3af9-bc14-22ffd74f81b0 | -16.79731 | -57.40417 | 2024-10-07 05:44:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.3 |
| c4c682eb-acce-311b-b00e-bd623dbf9433 | -16.7956 | -57.39976 | 2024-10-07 05:44:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.0 |
| a950c290-971a-334a-af8d-b6821cde3659 | -16.79519 | -57.40369 | 2024-10-07 05:44:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.6 |
| 7d901e6c-3434-3966-9e3a-a2059e77481f | -16.79254 | -57.39567 | 2024-10-07 05:44:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| 1fda1248-95a4-30fa-bb2b-94798b8a9e78 | -16.79211 | -57.3996 | 2024-10-07 05:44:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| 655ae264-c4bb-3313-a054-18a6b1f001de | -16.79168 | -57.40352 | 2024-10-07 05:44:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.3 |
| 23215b7e-e9b3-345e-a406-2020fd978588 | -16.79124 | -57.40744 | 2024-10-07 05:44:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.3 |
| 70b9f3d8-5493-3d5e-a28a-ae76c10697b5 | -16.79072 | -57.44676 | 2024-10-07 05:44:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 2fc1b401-15d2-3321-9146-84be5ddcd1fd | -16.79037 | -57.39516 | 2024-10-07 05:44:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| 0949a258-2f98-3481-a8f8-73f634e4efe1 | -16.78996 | -57.39909 | 2024-10-07 05:44:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| 37900776-0a82-3030-9d30-116f8be1a40c | -16.78955 | -57.40302 | 2024-10-07 05:44:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.1 |
| 76610ec4-f0a4-3106-9ef3-15082db0d71d | -16.78915 | -57.40696 | 2024-10-07 05:44:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.1 |
| 9c05f508-a8ed-3341-8eb3-d1e677d36971 | -16.78874 | -57.41087 | 2024-10-07 05:44:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| f9e4529a-d5b5-36aa-b1d3-1535babcf833 | -16.78691 | -57.44652 | 2024-10-07 05:44:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.0 |
| 70d82878-87ab-347c-a62e-e42500550b33 | -16.78691 | -57.39502 | 2024-10-07 05:44:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 17822cfd-cc7c-3507-8fe7-3a03a29cfefb | -16.78672 | -57.43047 | 2024-10-07 05:44:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.8 |
| cd8396a9-3855-3148-b939-79b94f06bd6b | -16.78631 | -57.43438 | 2024-10-07 05:44:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |


[Clique aqui para ver as próximas entradas](README135.md)
