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

## Dados Diários - Página 12

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b83d0eb4-46d5-35a1-b39f-a22ea4638f30 | -1.38216 | -48.8522 | 2025-10-12 04:12:00 | NOAA-21 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f4cf7670-a75a-308c-a265-3906140c116d | -4.41183 | -42.90211 | 2025-10-12 04:12:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e3763b44-c476-35d2-a1d7-01d214bde2ab | -3.73785 | -44.39315 | 2025-10-12 04:12:00 | NOAA-21 | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| cac2ce1b-7b29-37c6-9c8a-069a9c42c231 | -4.40532 | -43.11605 | 2025-10-12 04:12:00 | NOAA-21 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5d90baad-d0ee-3fc9-8fc1-b611ee7d1595 | -3.81458 | -43.10759 | 2025-10-12 04:12:00 | NOAA-21 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0e07698e-c9b0-3b85-b17d-e4e75bf41948 | -3.05577 | -40.81495 | 2025-10-12 04:12:00 | NOAA-21 | GRANJA | CEARÁ | Brasil | 2304707 | 23 | 33 | nan | nan | nan | Caatinga | 3.2 |
| d99eb104-4568-35c5-88bc-81c8be24a752 | -2.26623 | -47.85424 | 2025-10-12 04:12:00 | NOAA-21 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 682cd970-dddf-3eee-b91b-33d3db75dd77 | -3.29602 | -43.50366 | 2025-10-12 04:12:00 | NOAA-21 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 7b4d3d59-1da6-3f69-8162-5244cfff4f11 | -2.27042 | -47.85494 | 2025-10-12 04:12:00 | NOAA-21 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 62470091-e579-325b-8892-5d203d3ed6df | -5.2342 | -35.59864 | 2025-10-12 04:12:00 | NOAA-21 | TOUROS | RIO GRANDE DO NORTE | Brasil | 2414407 | 24 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 36d3a745-bd59-3eb9-b37b-6b395f668981 | -3.72764 | -44.1076 | 2025-10-12 04:12:00 | NOAA-21 | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3453c625-508e-3e32-b49c-496b3d7256e6 | -2.53825 | -47.80612 | 2025-10-12 04:12:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 17.9 |
| a21f0201-07ff-3f6e-aa10-67d3192ae2fe | -1.89936 | -51.00805 | 2025-10-12 04:12:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 0631f0b8-a167-3913-a0df-b7773fb1e206 | -4.42413 | -43.47366 | 2025-10-12 04:12:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bd4846c0-a430-3e7e-9a16-174f0f39eb58 | -0.90083 | -47.54635 | 2025-10-12 04:12:00 | NOAA-21 | MARACANÃ | PARÁ | Brasil | 1504307 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1dae175e-2f84-32df-8fac-fcc3afa48ef9 | -4.47917 | -41.42098 | 2025-10-12 04:12:00 | NOAA-21 | PEDRO II | PIAUÍ | Brasil | 2207900 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| ccc98d60-2bcb-37da-96ad-967ef706ca10 | -3.59726 | -41.62493 | 2025-10-12 04:12:00 | NOAA-21 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 87d5b9fc-90a7-36f0-a237-bbd2f52e9e5b | -2.29185 | -47.99045 | 2025-10-12 04:12:00 | NOAA-21 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 8a19b9cf-da91-343a-96b8-626003876291 | -2.53886 | -47.80234 | 2025-10-12 04:12:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 17.9 |
| 29ac9883-1bef-371e-b9c2-d7d51775ef2c | -4.40691 | -42.9119 | 2025-10-12 04:12:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 61130368-98ad-3922-8528-9966084ed11d | -3.56965 | -41.62779 | 2025-10-12 04:12:00 | NOAA-21 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 55b05e7b-0661-3062-9579-b8d4ffb2d573 | -3.60992 | -42.74421 | 2025-10-12 04:12:00 | NOAA-21 | BREJO | MARANHÃO | Brasil | 2102101 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6dcca4c7-d4d5-358c-b68e-742f909eab16 | -3.51404 | -45.85007 | 2025-10-12 04:12:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 18.6 |
| 0a7715f0-cc5c-3673-9584-b936c4f80f32 | -4.42136 | -43.46966 | 2025-10-12 04:12:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6a13799e-2859-30b5-b3c7-9333065ac0ed | -2.54717 | -47.80379 | 2025-10-12 04:12:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 15.4 |
| 9f84070c-a14b-3c87-ae88-5b24473eb8a0 | -4.72608 | -37.84443 | 2025-10-12 04:12:00 | NOAA-21 | ITAIÇABA | CEARÁ | Brasil | 2306207 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 7210cf97-3b3d-3b04-a6fc-bbe95cf9f571 | -3.87106 | -42.51103 | 2025-10-12 04:12:00 | NOAA-21 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 347d3185-b792-32c7-84e3-f70ba56615f4 | -3.53181 | -48.92946 | 2025-10-12 04:12:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9a833fc1-a6e6-33a5-8c02-24ac9da61e59 | -4.40586 | -43.11261 | 2025-10-12 04:12:00 | NOAA-21 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d3f65265-413c-3b22-87a2-3eed5aa843f2 | -2.43613 | -49.37561 | 2025-10-12 04:12:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| b7136165-3fda-3e3e-a4d1-c0a22931dff1 | -3.53624 | -48.93019 | 2025-10-12 04:12:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| dc251e59-4791-3508-b054-6cb30d432d14 | -3.60608 | -42.74714 | 2025-10-12 04:12:00 | NOAA-21 | BREJO | MARANHÃO | Brasil | 2102101 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b1baa5d9-2a5a-31fa-8e74-171466193a57 | -4.41192 | -43.11708 | 2025-10-12 04:12:00 | NOAA-21 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 27d285ec-305f-3b10-9ce4-bc3de8624210 | -3.61691 | -41.89031 | 2025-10-12 04:12:00 | NOAA-21 | CARAÚBAS DO PIAUÍ | PIAUÍ | Brasil | 2202539 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| d6c77534-e43b-3ce6-a97e-b04d66e0680c | -5.09037 | -38.83141 | 2025-10-12 04:12:00 | NOAA-21 | BANABUIÚ | CEARÁ | Brasil | 2301851 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| e20ef69a-442c-305e-a01c-9aae6e15ca4a | -4.02103 | -42.07008 | 2025-10-12 04:12:00 | NOAA-21 | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 0a150710-7d60-3c23-8082-936dafff469d | -3.6089 | -41.63742 | 2025-10-12 04:12:00 | NOAA-21 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 6368a1cd-fa97-3d80-9bbe-3c4cc0b5c589 | -3.60836 | -41.6409 | 2025-10-12 04:12:00 | NOAA-21 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 510e5a87-579e-38fe-b925-78f45dde0c9a | -3.87712 | -42.51548 | 2025-10-12 04:12:00 | NOAA-21 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 7.1 |
| adf2e3b9-13ae-3305-8e02-b67080aef6dc | -2.99886 | -48.73517 | 2025-10-12 04:12:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c033d916-51b7-3f7a-b418-32b97d0831ab | -1.48307 | -48.95696 | 2025-10-12 04:12:00 | NOAA-21 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5973dcda-fc5a-30fc-9a06-10c5bebc49bd | -4.41528 | -43.46515 | 2025-10-12 04:12:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 71114892-16c5-3265-af78-5246ce08465e | -3.51768 | -45.85066 | 2025-10-12 04:12:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 18.6 |
| 9746613a-a578-347c-9d63-149fba3ea16b | -3.22493 | -48.92936 | 2025-10-12 04:12:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b1c1ab31-384a-382e-b3c2-f06793fcc041 | -3.17224 | -48.61263 | 2025-10-12 04:12:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fd349c08-a8ea-3a1a-923d-ee5bb7872388 | -4.0089 | -38.73135 | 2025-10-12 04:12:00 | NOAA-21 | MARANGUAPE | CEARÁ | Brasil | 2307700 | 23 | 33 | nan | nan | nan | Caatinga | 8.7 |
| e1a17a9b-4eb2-3662-9f54-3e7b2931c00c | -3.97461 | -42.84734 | 2025-10-12 04:12:00 | NOAA-21 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Caatinga | 4.0 |
| b4508d94-494b-339a-bd4d-9099529febaf | -3.87052 | -42.51446 | 2025-10-12 04:12:00 | NOAA-21 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 641bf50c-08c5-3414-9a79-ff69e7ae8955 | -3.92483 | -44.32415 | 2025-10-12 04:12:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 823ed901-fd40-3d14-900f-b809e3cd0345 | -3.87436 | -42.51154 | 2025-10-12 04:12:00 | NOAA-21 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| fd96adfc-8fd5-367e-8a8e-8b28ab3853e3 | -2.29122 | -47.99437 | 2025-10-12 04:12:00 | NOAA-21 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 2843e0f9-33fa-39e6-8b2d-03e3e0de2998 | -4.44841 | -40.77006 | 2025-10-12 04:12:00 | NOAA-21 | IPUEIRAS | CEARÁ | Brasil | 2305902 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 84a2d00f-8a49-3759-9edc-34ec37657f7f | -4.40263 | -43.52379 | 2025-10-12 04:12:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 6a613d16-d119-3181-97cf-8adf127dfd02 | -2.99373 | -48.73882 | 2025-10-12 04:12:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 58bc02fc-c350-33eb-bf83-7a1945f92ff8 | -3.50972 | -45.85376 | 2025-10-12 04:12:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 16.4 |
| c300dcc8-2a97-3b59-91c7-f6fbe79b5f81 | -2.54777 | -47.80002 | 2025-10-12 04:12:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0bcebf02-8e3c-3ff5-a75a-52b925885db7 | -2.29547 | -47.99498 | 2025-10-12 04:12:00 | NOAA-21 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b1150a3d-cc63-3012-9d5c-79a92bad9469 | -3.35041 | -42.15839 | 2025-10-12 04:12:00 | NOAA-21 | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Caatinga | 8.4 |
| bc39c40a-03ef-3edc-9bed-2e87647f4fc5 | -2.43798 | -49.37339 | 2025-10-12 04:12:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 3201801b-7a83-307b-a473-a772a866c15d | -4.52121 | -37.79209 | 2025-10-12 04:12:00 | NOAA-21 | ARACATI | CEARÁ | Brasil | 2301109 | 23 | 33 | nan | nan | nan | Caatinga | 2.7 |
| bf9300f0-4529-3829-bcec-9fc6043f38da | -1.48232 | -48.96167 | 2025-10-12 04:12:00 | NOAA-21 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1cb567df-94df-3cbb-a180-210d7c1815e0 | -2.32038 | -49.16513 | 2025-10-12 04:12:00 | NOAA-21 | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9682d022-acee-3055-b75b-8fb6d5380752 | -3.53696 | -48.92581 | 2025-10-12 04:12:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| a79dcd5f-d3dc-33b7-be14-e62de76eed8a | -2.63524 | -47.30262 | 2025-10-12 04:12:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a1db064b-cdbd-31da-9758-80e86cc1bacf | -2.43952 | -49.36362 | 2025-10-12 04:12:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| bdfb8698-d880-3b65-898f-f93570cc34b8 | -3.57296 | -41.62831 | 2025-10-12 04:12:00 | NOAA-21 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 43161f6e-fcd7-3d6d-ae12-8ca96a86cce2 | -4.42799 | -43.47069 | 2025-10-12 04:12:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6794b029-c357-35c2-bcad-1ef3bf265814 | -3.84647 | -42.1662 | 2025-10-12 04:12:00 | NOAA-21 | ESPERANTINA | PIAUÍ | Brasil | 2203701 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 511d3daa-7277-3b01-bde3-b20900fa6bb8 | -0.90504 | -47.54697 | 2025-10-12 04:12:00 | NOAA-21 | MARACANÃ | PARÁ | Brasil | 1504307 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 3505e8e6-d85a-334f-a6a5-a278d6da4923 | -2.44263 | -49.37413 | 2025-10-12 04:12:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 324b6771-f079-339c-9a12-155b395dbdfc | -4.90344 | -40.08556 | 2025-10-12 04:12:00 | NOAA-21 | MONSENHOR TABOSA | CEARÁ | Brasil | 2308609 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| e0883d38-c935-3cd2-818e-42fe5d08aaea | -2.44079 | -49.37634 | 2025-10-12 04:12:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 2829f2bb-8598-34c2-8e42-e1650db496f9 | -3.48543 | -41.60052 | 2025-10-12 04:12:00 | NOAA-21 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| b5f78bb5-f0c0-3f3f-a49f-342566fe4c6b | -4.39986 | -43.51978 | 2025-10-12 04:12:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 46c51164-d163-348f-9bf6-e4a5d6fda2e9 | -4.02211 | -42.06317 | 2025-10-12 04:12:00 | NOAA-21 | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 33b7d5fd-19c9-3c32-be10-b04ff23ac68f | -4.42522 | -43.4667 | 2025-10-12 04:12:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 122dd214-a687-3df0-a707-0857828946fb | -4.04268 | -42.5206 | 2025-10-12 04:12:00 | NOAA-21 | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 5.6 |
| 352927fa-9cbb-368a-8efd-ec765562d281 | -3.74242 | -44.38631 | 2025-10-12 04:12:00 | NOAA-21 | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f45114f7-a142-352d-869b-7a1764b0a4f9 | -4.40041 | -43.5163 | 2025-10-12 04:12:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b3a750e3-6562-35d6-a8fb-0e02db7eddfe | -3.86141 | -38.62492 | 2025-10-12 04:12:00 | NOAA-21 | MARACANAÚ | CEARÁ | Brasil | 2307650 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 44eea6e3-3e9a-3e2d-94f1-02af1843eeea | -3.34711 | -42.15788 | 2025-10-12 04:12:00 | NOAA-21 | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Caatinga | 8.4 |
| fbf743ba-acf5-3e66-ad2a-e3d2126099fa | -2.54241 | -47.80685 | 2025-10-12 04:12:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 15.4 |
| 9c127b81-00f2-35b5-9dc8-7fdc64342f64 | -2.99815 | -48.73951 | 2025-10-12 04:12:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 06786d45-ef57-302c-bd4f-59b5b009f952 | -3.61322 | -42.74472 | 2025-10-12 04:12:00 | NOAA-21 | BREJO | MARANHÃO | Brasil | 2102101 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bda817da-3d23-344b-acc4-64b330da7131 | -4.89992 | -40.08504 | 2025-10-12 04:12:00 | NOAA-21 | MONSENHOR TABOSA | CEARÁ | Brasil | 2308609 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 17f8b18b-c36a-3d79-9deb-bfb2c392d8a9 | -3.1459 | -44.42669 | 2025-10-12 04:12:00 | NOAA-21 | SANTA RITA | MARANHÃO | Brasil | 2110203 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 0c2b83af-98cb-36c1-87b3-6c175bf48464 | -3.6116 | -42.75502 | 2025-10-12 04:12:00 | NOAA-21 | BREJO | MARANHÃO | Brasil | 2102101 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2f780005-f9df-3235-a3d4-c133245008fd | -4.40862 | -43.11657 | 2025-10-12 04:12:00 | NOAA-21 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9d951348-2226-39aa-9d6f-eebc365d67a7 | -3.60938 | -42.74765 | 2025-10-12 04:12:00 | NOAA-21 | BREJO | MARANHÃO | Brasil | 2102101 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 31401728-20c6-3a7b-8e7c-6898514a842d | -2.53765 | -47.80991 | 2025-10-12 04:12:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| b5ee78dd-2b72-3e59-8c0a-331ed771dc68 | -2.54301 | -47.80309 | 2025-10-12 04:12:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 15.4 |
| e118af3f-022b-380a-ac92-739243c39133 | -3.26191 | -42.27108 | 2025-10-12 04:12:00 | NOAA-21 | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 23ad198e-52f3-3294-a37a-f1209679305b | -1.89883 | -51.01128 | 2025-10-12 04:12:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 40e1c0e9-106c-38d0-a107-ba432d7e3e7c | -3.73843 | -44.38946 | 2025-10-12 04:12:00 | NOAA-21 | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 34b1254e-a4c5-30ad-a5be-0e67bfe866e2 | -2.44159 | -49.37147 | 2025-10-12 04:12:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 367b350a-b475-3526-a971-c87e3f56c417 | -3.14649 | -44.42296 | 2025-10-12 04:12:00 | NOAA-21 | SANTA RITA | MARANHÃO | Brasil | 2110203 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| cef7be3e-0abb-3a62-9a6c-7d44996c024e | -3.50607 | -45.85317 | 2025-10-12 04:12:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 16.4 |
| e04042b6-c175-3d92-8cc2-a040b6fdc0b9 | 0.25457 | -51.08397 | 2025-10-12 04:12:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| be8b98b0-4d59-3eb3-b52f-fe70a1216230 | -3.22196 | -50.21527 | 2025-10-12 04:12:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 53600970-065c-366a-9814-de567e7e546b | -3.5104 | -45.84949 | 2025-10-12 04:12:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 16.4 |


[Clique aqui para ver as próximas entradas](README13.md)
