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

## Dados Diários - Página 65

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 041b3f49-f8f6-3cad-b2fd-fe78b7762651 | -10.6285 | -67.7285 | 2024-10-17 05:53:00 | NOAA-20 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 45d8bb55-c33d-33b5-88b1-177f1239128a | -10.62815 | -67.84515 | 2024-10-17 05:53:00 | NOAA-20 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 49297b96-6c86-3a49-9e40-b33cce2af19a | -10.62755 | -67.82631 | 2024-10-17 05:53:00 | NOAA-20 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 65c15ca3-060d-3e9c-ae05-dc4cd3369169 | -10.627 | -67.82998 | 2024-10-17 05:53:00 | NOAA-20 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9461cbaf-6d17-3b7e-a233-713845302653 | -10.62644 | -67.83365 | 2024-10-17 05:53:00 | NOAA-20 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cbb3ddaa-001f-3309-94f9-b9c3c89dff8d | -10.6251 | -67.72798 | 2024-10-17 05:53:00 | NOAA-20 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 29fa04d9-c235-3e2e-8166-193f8a44843c | -10.62417 | -67.8258 | 2024-10-17 05:53:00 | NOAA-20 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bd5137e9-308d-3c8e-b035-27edcb125a00 | -10.62283 | -67.72004 | 2024-10-17 05:53:00 | NOAA-20 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 3.1 |
| a91d5d35-dda4-3068-9e05-6215d2b09c97 | -10.62227 | -67.72375 | 2024-10-17 05:53:00 | NOAA-20 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 259b09ab-6598-3f44-9d40-5689da34892c | -10.62078 | -67.82528 | 2024-10-17 05:53:00 | NOAA-20 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 34affb88-7e9e-39b6-9dbb-e8cd6ce79e1b | -10.62022 | -67.82894 | 2024-10-17 05:53:00 | NOAA-20 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4e7b0ef3-38af-3e0b-b598-ad0c59d68d4b | -10.61856 | -67.83992 | 2024-10-17 05:53:00 | NOAA-20 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f79780b5-b4e7-3c65-b927-235396c15285 | -10.61684 | -67.82841 | 2024-10-17 05:53:00 | NOAA-20 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 28488f9d-c1e4-367c-85d3-0513c230fbc8 | -10.61573 | -67.83572 | 2024-10-17 05:53:00 | NOAA-20 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fe87c02d-a14b-361c-bbf6-77b65b1890c1 | -10.61518 | -67.83939 | 2024-10-17 05:53:00 | NOAA-20 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2747786d-ee9a-34c9-8b39-4b7052bdd26c | -10.6118 | -67.83885 | 2024-10-17 05:53:00 | NOAA-20 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8fdf25de-5f63-37e5-85fb-2f52a0bb01bc | -10.58396 | -67.77073 | 2024-10-17 05:53:00 | NOAA-20 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 11.3 |
| 4dd1d792-ff51-3a67-95bc-84434110cdff | -10.58355 | -67.76731 | 2024-10-17 05:53:00 | NOAA-20 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4f36c74a-9467-301f-8d42-489a92d60148 | -10.58298 | -67.771 | 2024-10-17 05:53:00 | NOAA-20 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 13.3 |
| 180fb657-6bb6-3429-be77-dc19945016b1 | -10.58016 | -67.76679 | 2024-10-17 05:53:00 | NOAA-20 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6c7ff477-8b54-38ab-bf9f-2b5ed29e7096 | -10.57959 | -67.77048 | 2024-10-17 05:53:00 | NOAA-20 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 13.3 |
| 7574cc80-85ac-3d04-bb4e-d8bc26ff04bf | -10.57902 | -67.68347 | 2024-10-17 05:53:00 | NOAA-20 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 03de4536-6146-3c12-a848-99574a3b104a | -10.57845 | -67.68716 | 2024-10-17 05:53:00 | NOAA-20 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 665912a8-7156-3475-aab6-3804effe8b93 | -10.5762 | -67.76994 | 2024-10-17 05:53:00 | NOAA-20 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 29c839f2-1671-3f25-a8b7-d4aa671bef6c | -10.57506 | -67.68664 | 2024-10-17 05:53:00 | NOAA-20 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b2d585ff-af06-3935-9ada-d4d1e43657f8 | -10.55532 | -67.77042 | 2024-10-17 05:53:00 | NOAA-20 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 906977da-eae2-3cce-8dcc-0bd05e815c25 | -10.55476 | -67.77409 | 2024-10-17 05:53:00 | NOAA-20 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| db268c52-a24d-3049-829c-022c3035fd86 | -10.55421 | -67.77775 | 2024-10-17 05:53:00 | NOAA-20 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1a622bee-615b-3ced-ab0d-d8e5bf0bb17b | -10.53003 | -67.84537 | 2024-10-17 05:53:00 | NOAA-20 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 45da88bb-c030-35cf-9499-341ad66fc196 | -10.52212 | -67.82919 | 2024-10-17 05:53:00 | NOAA-20 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f7867351-1d19-337d-806f-5f7c7735ced2 | -10.51985 | -67.82132 | 2024-10-17 05:53:00 | NOAA-20 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ed21370c-894a-3d16-909d-403ed3aeb481 | -10.51818 | -67.83232 | 2024-10-17 05:53:00 | NOAA-20 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b3365bf5-9c4d-3463-b2ec-c1765b4b12e2 | -10.51647 | -67.82079 | 2024-10-17 05:53:00 | NOAA-20 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 459dbcbf-ee8d-32c3-af08-b38ec5fc8808 | -10.49031 | -67.64396 | 2024-10-17 05:53:00 | NOAA-20 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7e124537-a27e-31b9-8eae-26a90cc7cf72 | -10.46148 | -67.74155 | 2024-10-17 05:53:00 | NOAA-20 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e7ed1e55-288c-3674-9f85-1a554c17c6b0 | -10.44971 | -67.84099 | 2024-10-17 05:53:00 | NOAA-20 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3c97ddad-fc03-3b4b-b228-487d582f2bc3 | -10.40583 | -67.85662 | 2024-10-17 05:53:00 | NOAA-20 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 908eb334-9338-347a-9317-fe176de56ebf | -9.52841 | -68.59647 | 2024-10-17 05:53:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5a001421-bbbf-3653-bcd7-18e291582b80 | -9.52538 | -68.72493 | 2024-10-17 05:53:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 2.4 |
| bd2059f9-4143-3624-9dd1-51e4f23b8a9e | -9.52152 | -68.72791 | 2024-10-17 05:53:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a27d21ab-9329-3356-a167-a36301eb5d26 | -9.51214 | -68.72284 | 2024-10-17 05:53:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1abba333-d420-3e80-9573-2eaef23951c1 | -9.50322 | -68.47391 | 2024-10-17 05:53:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 16cadaf4-12af-3c29-b7a5-169ee2da78af | -9.4999 | -68.4734 | 2024-10-17 05:53:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6a563f49-ac43-3c04-ba61-29ac54835ba9 | -9.47475 | -68.5698 | 2024-10-17 05:53:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 586d73ac-44d9-3b4b-93ff-2c9b52a692bb | -9.46799 | -68.50411 | 2024-10-17 05:53:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 2909771f-4840-3f0f-9f7e-43ddb28c1d39 | -9.46795 | -68.48252 | 2024-10-17 05:53:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 590d57f5-403d-3ae1-8340-74214a551e9b | -9.46085 | -68.52814 | 2024-10-17 05:53:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4e38e483-f912-36a6-8f9e-ae39247f1a92 | -9.46031 | -68.53165 | 2024-10-17 05:53:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 57fa496e-5299-3fdb-8e6e-66e1efa6ad5c | -9.45872 | -68.5637 | 2024-10-17 05:53:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 24c05f46-205d-3c22-8269-506efb27bfb1 | -9.44302 | -68.88345 | 2024-10-17 05:53:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ed005d7f-5316-38b7-ad27-8731674b8faf | -9.43991 | -68.55356 | 2024-10-17 05:53:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9e46aef6-f054-30f2-a48d-289792e7de1f | -9.41927 | -68.70791 | 2024-10-17 05:53:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d21926b3-902b-3d8d-bed1-6dbc363e9807 | -9.38226 | -68.68417 | 2024-10-17 05:53:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d00f699e-1421-38a0-8e92-b57712361fa4 | -9.38172 | -68.68768 | 2024-10-17 05:53:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f4077552-5bcc-3883-baa3-3add8df48490 | -9.38009 | -68.69814 | 2024-10-17 05:53:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6bdde29d-0a24-3ba8-8970-9b58eaea1107 | -9.37226 | -68.90042 | 2024-10-17 05:53:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 30195c0c-4d3b-3b02-988d-c97617cdbfc0 | -9.37171 | -68.9039 | 2024-10-17 05:53:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f9713d4d-692c-3afd-879f-2d4fd9073c6f | -9.37016 | -68.69657 | 2024-10-17 05:53:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5d47731e-ce13-3ec1-8364-f439325bd214 | -9.36962 | -68.70006 | 2024-10-17 05:53:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| db72a592-7249-3a47-bc25-9f0420626069 | -9.34779 | -68.79669 | 2024-10-17 05:53:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1d712e24-3846-3e33-a842-b6414a8e10d0 | -9.34725 | -68.80017 | 2024-10-17 05:53:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ce4a1c6a-bf2d-358e-beaa-72e473aaee12 | -9.34636 | -68.67496 | 2024-10-17 05:53:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1dce5a2a-580d-361b-9097-eab3f99a78d1 | -9.34448 | -68.79617 | 2024-10-17 05:53:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c7ca8e89-a148-31f4-a6b8-99d0c2ba8cfa | -9.34394 | -68.79965 | 2024-10-17 05:53:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 2f6ef3b8-2fdc-3349-a452-abc0ce005fe0 | -10.8624 | -69.1448 | 2024-10-17 05:53:00 | NOAA-20 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ed0acb86-be23-3c5f-8c9d-2c524c562323 | -10.84255 | -69.14164 | 2024-10-17 05:53:00 | NOAA-20 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 73c7ea72-2328-315b-842c-faf08984a6ef | -10.8152 | -69.01223 | 2024-10-17 05:53:00 | NOAA-20 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ea83de72-1dc1-37f5-9c87-6ea266010833 | -10.81189 | -69.0117 | 2024-10-17 05:53:00 | NOAA-20 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 16a175b2-320a-3f67-9c44-5a852011d152 | -10.7579 | -69.05341 | 2024-10-17 05:53:00 | NOAA-20 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 338f00bb-f85b-3e32-8878-92c626292f05 | -10.95623 | -68.24845 | 2024-10-17 05:53:00 | NOAA-20 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| edd9ad23-707c-3f30-b995-82c3d8a3989f | -10.93975 | -68.33433 | 2024-10-17 05:53:00 | NOAA-20 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d84dd5d6-6fc4-30f3-9c17-18daa5df2854 | -10.90906 | -68.38541 | 2024-10-17 05:53:00 | NOAA-20 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ab7666f4-5938-30a1-909b-72c5df68b609 | -10.90351 | -68.39922 | 2024-10-17 05:53:00 | NOAA-20 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d5747f9f-f751-3939-bc81-8eea9d0ed393 | -10.90224 | -68.29618 | 2024-10-17 05:53:00 | NOAA-20 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6b2ac6c3-d5f3-3d71-9de8-99ccdf0113b0 | -10.88475 | -68.2086 | 2024-10-17 05:53:00 | NOAA-20 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 306c9ee6-8040-3937-b261-f401d6e6d1bb | -10.8814 | -68.20808 | 2024-10-17 05:53:00 | NOAA-20 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c77a0f28-8a19-3bfd-b5e9-0aed1fa847ed | -10.97577 | -68.50126 | 2024-10-17 05:53:00 | NOAA-20 | EPITACIOLÂNDIA | ACRE | Brasil | 1200252 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5ac0baa0-2cbb-3e14-aa4b-8cc95f39a854 | -10.89727 | -68.63443 | 2024-10-17 05:53:00 | NOAA-20 | EPITACIOLÂNDIA | ACRE | Brasil | 1200252 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3fda21e8-3986-3bd6-bb75-01d8fb60fda8 | -10.80995 | -68.82772 | 2024-10-17 05:53:00 | NOAA-20 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ab460c2f-e094-31ca-bec7-67966e121ef0 | -10.80214 | -68.79039 | 2024-10-17 05:53:00 | NOAA-20 | EPITACIOLÂNDIA | ACRE | Brasil | 1200252 | 12 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 184e7730-0330-3608-aa6d-031b081819be | -10.78472 | -68.92464 | 2024-10-17 05:53:00 | NOAA-20 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b3f943e9-c0b6-38cf-9179-e179d54e2d81 | -17.88064 | -56.86122 | 2024-10-17 05:55:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.3 |
| 7657bf67-5976-3a97-a7ec-095e5368ab16 | -17.87737 | -56.86178 | 2024-10-17 05:55:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.8 |
| dd5ed960-2907-373f-8667-ffdafc779f9a | -17.87673 | -56.86903 | 2024-10-17 05:55:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 7229dbdc-8592-33f2-9276-e5de5e6c3fca | -17.87275 | -56.83204 | 2024-10-17 05:55:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 15160f90-6d5e-31ef-a02a-7e9002f68bf3 | -17.87233 | -56.87502 | 2024-10-17 05:55:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 2ffef1fd-6521-3c28-a77f-a2a70c0873a3 | -17.86897 | -56.87558 | 2024-10-17 05:55:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| b6ee65f2-9fc9-3703-934a-99eccb9fccbc | -17.86869 | -56.83072 | 2024-10-17 05:55:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 60d81036-9f1a-354b-aa83-cb1b54d5788c | -17.86811 | -56.83799 | 2024-10-17 05:55:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.4 |
| cc4d6892-9363-382f-be81-17d866917365 | -17.86753 | -56.84529 | 2024-10-17 05:55:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 6d1501c4-379c-31da-bbad-a0df7abfef9a | -17.86559 | -56.83142 | 2024-10-17 05:55:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.5 |
| 7ce02a63-16fe-31fb-b64e-c3ac12289312 | -17.85979 | -56.85189 | 2024-10-17 05:55:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 308eca48-6725-3613-9259-5815b60ff448 | -17.2093 | -56.6854 | 2024-10-17 05:55:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 6e8847a9-021b-3a56-ac5b-d9f149bdcd74 | -17.20213 | -56.68468 | 2024-10-17 05:55:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| db2b7a7b-4d50-3569-b4b8-e117eb42f2c5 | -18.22225 | -56.86064 | 2024-10-17 05:55:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 38d2c31b-2001-3967-a2cb-f64df9576af8 | -18.21508 | -56.85995 | 2024-10-17 05:55:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 977de439-57f1-3dfc-a2d2-3b9ede6903f6 | -9.57452 | -55.80231 | 2024-10-17 05:55:00 | NOAA-20 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 092abe6e-9e66-3b34-a0df-ec34f9746736 | -9.57373 | -55.80884 | 2024-10-17 05:55:00 | NOAA-20 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 405088b0-8946-30a6-b54c-5c6838a412c6 | -17.98046 | -57.42641 | 2024-10-17 05:55:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 0df2f721-a7ac-36c5-8a68-09096e838797 | -17.97373 | -57.42427 | 2024-10-17 05:55:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.1 |


[Clique aqui para ver as próximas entradas](README66.md)
