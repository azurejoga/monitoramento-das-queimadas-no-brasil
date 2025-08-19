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

## Dados Diários - Página 45

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d4f3ad9b-fdc7-3f64-9d78-4ca529566193 | -16.47727 | -45.08603 | 2025-08-19 04:55:00 | NPP-375D | PONTO CHIQUE | MINAS GERAIS | Brasil | 3152131 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 306b4c83-22ba-3a09-a81e-7ea1fa68b420 | -12.98127 | -56.86143 | 2025-08-19 04:55:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 79408942-634d-3bdd-abf5-050f9e679fc1 | -16.81762 | -49.36768 | 2025-08-19 04:55:00 | NPP-375D | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 3c7bf651-c7ac-3727-9532-2bc1b70b694b | -17.89262 | -48.60551 | 2025-08-19 04:55:00 | NPP-375D | CALDAS NOVAS | GOIÁS | Brasil | 5204508 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6a84194b-7099-32c1-9750-d00e06193bb2 | -17.34528 | -47.17159 | 2025-08-19 04:55:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 804c9463-2c8c-341b-97d3-48221c08eadc | -13.17119 | -54.94053 | 2025-08-19 04:55:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f4638678-e1a7-38d1-bf04-a698f92e2277 | -13.00474 | -56.85293 | 2025-08-19 04:55:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e2d770c1-ede6-38c0-911e-9d04743cdc2c | -16.79177 | -50.09659 | 2025-08-19 04:55:00 | NPP-375D | PALMEIRAS DE GOIÁS | GOIÁS | Brasil | 5215702 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3bc9cd0c-5c76-3d9b-9bb0-a5d23b10c751 | -15.15419 | -48.77731 | 2025-08-19 04:55:00 | NPP-375D | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ab2e4e0c-191e-317f-a34a-d093d299c1f9 | -13.0104 | -56.84125 | 2025-08-19 04:55:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b9363110-8eb5-3e07-a2f7-ddbfc4f3fe48 | -13.25558 | -50.80797 | 2025-08-19 04:55:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f21805a9-e5fd-3d01-bc76-e4c679b6fbfa | -14.96914 | -54.80169 | 2025-08-19 04:55:00 | NPP-375D | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 15c5bc09-51ab-3043-ab93-e49373a7f95f | -15.03511 | -54.81638 | 2025-08-19 04:55:00 | NPP-375D | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 2575a5be-4b50-3c35-9b17-fde8d75bf0f4 | -12.98252 | -56.84103 | 2025-08-19 04:55:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2bd45974-3fae-369a-9235-fefa63d50858 | -15.02789 | -54.81889 | 2025-08-19 04:55:00 | NPP-375D | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| b1fdde3c-b8ba-3bb8-98b0-cb5faf00c038 | -15.01848 | -54.81364 | 2025-08-19 04:55:00 | NPP-375D | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 16bb4460-002f-38f9-bba7-b18af3afee92 | -14.98635 | -54.8009 | 2025-08-19 04:55:00 | NPP-375D | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 1f9092a0-da0d-37f2-a9b6-40177e6c383c | -13.18066 | -54.94583 | 2025-08-19 04:55:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ed87e570-9152-3486-8bc5-5c3d0eaeaf97 | -14.87052 | -48.05478 | 2025-08-19 04:55:00 | NPP-375D | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 9135ae5b-b513-3d47-a04a-44e0af8d61d3 | -13.29978 | -50.81269 | 2025-08-19 04:55:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2e504e4f-8d04-3cbd-9920-c51b95da6db5 | -13.47014 | -47.05574 | 2025-08-19 04:55:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0bb59c52-4949-31b2-b6ff-29b081276fab | -13.48056 | -47.07435 | 2025-08-19 04:55:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e0c2eda9-a7cd-3f70-ae54-0883c1611cae | -12.98554 | -56.85793 | 2025-08-19 04:55:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 928f4c48-3410-388e-9a03-a2ab50fe15d8 | -13.16624 | -54.92859 | 2025-08-19 04:55:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 79bb7d48-907c-399f-84b7-f1b36e75799e | -16.62494 | -51.35329 | 2025-08-19 04:55:00 | NPP-375D | PALESTINA DE GOIÁS | GOIÁS | Brasil | 5215652 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c328cf53-673e-3d5b-933b-00a82c1ad51f | -12.97691 | -56.85271 | 2025-08-19 04:55:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2821d9b0-fc0b-35b1-aea7-771b07926b27 | -14.17346 | -45.3165 | 2025-08-19 04:55:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4289861e-8563-3a22-9395-2def1971764f | -14.97522 | -54.80639 | 2025-08-19 04:55:00 | NPP-375D | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 6.2 |
| f657c331-6ee1-3fbd-9e80-80829aaca299 | -13.18008 | -54.94943 | 2025-08-19 04:55:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 86729f2a-f837-3f2b-82d1-ee1e8c917ca6 | -14.17385 | -45.3133 | 2025-08-19 04:55:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| fcc7b644-f494-3bf1-9e81-086ff7888c5a | -14.73914 | -46.29511 | 2025-08-19 04:55:00 | NPP-375D | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7f638ed4-d333-362a-8123-20072531f7d4 | -14.84709 | -48.06666 | 2025-08-19 04:55:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| cb050965-7876-355c-8042-5e0610e37630 | -14.86782 | -48.04093 | 2025-08-19 04:55:00 | NPP-375D | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 9e3607b7-0e0c-3bf4-b3a4-b58f4121e588 | -13.2532 | -50.79887 | 2025-08-19 04:55:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 4be41e78-698a-34e1-b3b5-c42c6f83e980 | -16.84145 | -48.91651 | 2025-08-19 04:55:00 | NPP-375D | BELA VISTA DE GOIÁS | GOIÁS | Brasil | 5203302 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bbd2786b-0a1b-3317-a7a3-f5e90bf8ae3d | -13.16508 | -54.93579 | 2025-08-19 04:55:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c6a53c0d-870e-3c4e-bd9f-effa51c62e09 | -14.86937 | -48.0638 | 2025-08-19 04:55:00 | NPP-375D | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| a150c234-1d67-351d-9e9e-21e04c70c9f1 | -13.16057 | -54.94245 | 2025-08-19 04:55:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 12.1 |
| 1f2635cd-2492-3066-901f-76b451445895 | -16.50302 | -45.10446 | 2025-08-19 04:55:00 | NPP-375D | PONTO CHIQUE | MINAS GERAIS | Brasil | 3152131 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a1113188-5088-39ae-898d-9d470100608e | -13.09267 | -46.83896 | 2025-08-19 04:55:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ebb24df8-3201-3a05-ae74-fad97a89c989 | -17.42438 | -46.70926 | 2025-08-19 04:55:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 89be4ae9-d225-3684-b06f-d4025abbd61b | -14.97465 | -54.80997 | 2025-08-19 04:55:00 | NPP-375D | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 9f1a8eb5-8900-35c7-b1ad-fa2ac8ea2046 | -12.99552 | -56.86398 | 2025-08-19 04:55:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6c34a231-6327-37bc-a8c8-8dcc5a78a183 | -15.80951 | -48.27629 | 2025-08-19 04:55:00 | NPP-375D | ÁGUAS LINDAS DE GOIÁS | GOIÁS | Brasil | 5200258 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ab4a40c8-fd73-3b9e-a396-09287ddd71df | -14.44826 | -53.0321 | 2025-08-19 04:55:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 43eca40a-b418-3648-a457-ce87a16a32ba | -13.55903 | -47.01152 | 2025-08-19 04:55:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 52e117ef-9800-38c2-8586-46e31378b1ee | -13.01249 | -56.82896 | 2025-08-19 04:55:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8abb7d9f-3646-3398-83b4-8ba98052dc1e | -14.99186 | -54.8092 | 2025-08-19 04:55:00 | NPP-375D | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| f35a4ef0-fb73-3d55-9376-facad0aa04f3 | -13.14382 | -57.15075 | 2025-08-19 04:55:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 016da7c9-65a5-305a-8b36-d2b047138a73 | -13.47807 | -47.06649 | 2025-08-19 04:55:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f2d0c642-4af8-38d0-b4ca-98ef3c41a708 | -13.47316 | -47.0588 | 2025-08-19 04:55:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a7948eb2-169a-3b01-ae42-18d337793ddb | -14.87318 | -48.06889 | 2025-08-19 04:55:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 163a94ac-9133-35a3-a427-b6cb6a9267e6 | -13.59484 | -46.99002 | 2025-08-19 04:55:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 9543e365-7e5b-365d-b5cb-5877a0b2b4bc | -15.03787 | -54.82052 | 2025-08-19 04:55:00 | NPP-375D | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 35bab524-9129-3504-b683-d7b988346ad6 | -13.16392 | -54.94301 | 2025-08-19 04:55:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7e9369e3-b5e5-3509-8910-4c7004de8b02 | -14.87167 | -48.04585 | 2025-08-19 04:55:00 | NPP-375D | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8c776d17-eff8-3bdd-bc4b-cf23089d1c1b | -13.86848 | -45.54815 | 2025-08-19 04:55:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b52dfb1e-40c3-3d65-bfb9-a878789b5ef1 | -13.18835 | -54.9503 | 2025-08-19 04:55:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| be817c7f-b7ee-3f42-bc83-173caf2dca3d | -13.17789 | -54.94166 | 2025-08-19 04:55:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c7d48ad5-3cc0-396a-b073-9d15d6f4d8e4 | -15.01515 | -54.81308 | 2025-08-19 04:55:00 | NPP-375D | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| ea26f079-1c78-3130-acb5-7837f48a1383 | -15.74912 | -46.60669 | 2025-08-19 04:55:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ec5af219-c714-3f09-a112-bdc2451929d5 | -13.14277 | -57.16211 | 2025-08-19 04:55:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0b2c5921-79ad-3d40-9bdc-94ccb9c5349c | -15.0296 | -54.80809 | 2025-08-19 04:55:00 | NPP-375D | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 89103aa2-4bbb-35ea-a724-915fd02170a6 | -13.1821 | -46.87793 | 2025-08-19 04:55:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ccc4d69a-7baf-377b-b6f6-1bcdeccbcbac | -13.28464 | -50.81238 | 2025-08-19 04:55:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e437448c-56cd-31c8-b79f-bf273da02989 | -13.1578 | -54.93828 | 2025-08-19 04:55:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 12.1 |
| 73816b94-376f-3876-89f5-9fa85e27c406 | -13.73719 | -52.02275 | 2025-08-19 04:55:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b07c76af-dc65-3607-a65a-a5e32296da26 | -15.74591 | -56.02454 | 2025-08-19 04:55:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| b73749f1-c505-3d87-b642-d6573fad3899 | -14.1694 | -45.30611 | 2025-08-19 04:55:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e0f1d5e7-1e9a-362a-9052-25c5c43cc7b2 | -14.16824 | -45.3158 | 2025-08-19 04:55:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 238b652c-a4e7-3ebf-8767-a1e54886a71f | -13.31314 | -50.7972 | 2025-08-19 04:55:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8f986b58-da0c-3cdc-bd7a-5fd7c6f0dc27 | -17.41439 | -46.70825 | 2025-08-19 04:55:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 4.8 |
| aef32c1b-567b-3759-a4d0-2e29ab0540fc | -15.74841 | -46.61241 | 2025-08-19 04:55:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 62dd4f4a-5a3c-3e0a-92c2-1d45dd90cfa3 | -13.87819 | -54.04418 | 2025-08-19 04:55:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ca44a914-918d-31f2-af43-750f457f0ba0 | -12.6305 | -54.06569 | 2025-08-19 04:55:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 3895a908-aec5-30f3-ab1e-d72702c35fd4 | -14.9813 | -54.8111 | 2025-08-19 04:55:00 | NPP-375D | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6c8744b6-b23f-30cd-9355-d3a16f6b70f5 | -14.98577 | -54.80449 | 2025-08-19 04:55:00 | NPP-375D | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| e27ac737-12c1-39d7-b9b8-534e002ee8d1 | -23.99293 | -48.5612 | 2025-08-19 04:57:00 | NPP-375D | CAPÃO BONITO | SÃO PAULO | Brasil | 3510203 | 35 | 33 | nan | nan | nan | Mata Atlântica | 8.0 |
| 7c555436-1d7c-3de7-8ac6-8d1b807be831 | -20.82722 | -57.76801 | 2025-08-19 04:57:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 5d02bf0a-2628-323f-8553-95ab3a5fe032 | -20.86022 | -56.9375 | 2025-08-19 04:57:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a9f82a49-95a4-39c6-948d-fb143f5cd3b4 | -20.86572 | -54.98141 | 2025-08-19 04:57:00 | NPP-375D | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| df37a23d-2b27-3f7c-bed4-22b997468301 | -20.86958 | -54.98987 | 2025-08-19 04:57:00 | NPP-375D | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d137f373-6465-3c20-9b70-64a42f58e45f | -20.86757 | -56.9349 | 2025-08-19 04:57:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c775bf77-cf8a-3591-84c8-9aa690f4f645 | -20.86854 | -56.90772 | 2025-08-19 04:57:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c4433d50-4342-3e2d-b643-2c2b1cdcc318 | -20.87799 | -54.97978 | 2025-08-19 04:57:00 | NPP-375D | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4bff235c-317f-315c-a22b-cbe2ad677900 | -23.31285 | -46.88831 | 2025-08-19 04:57:00 | NPP-375D | CAJAMAR | SÃO PAULO | Brasil | 3509205 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 7a8121f8-6456-32bc-8cd7-b8b135c2fb77 | -20.88356 | -54.98837 | 2025-08-19 04:57:00 | NPP-375D | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 29944161-dcad-3269-b0f3-fe8926481387 | -21.8728 | -48.20984 | 2025-08-19 04:57:00 | NPP-375D | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5ed4b4da-a744-3e82-b44b-3dbd8d6ba28d | -23.30757 | -46.88745 | 2025-08-19 04:57:00 | NPP-375D | CAJAMAR | SÃO PAULO | Brasil | 3509205 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| cc1b4cd4-a603-327b-b846-40d2d316ccbd | -20.85722 | -56.91357 | 2025-08-19 04:57:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 90602acb-9d4c-3c78-a340-a2fa7d4cd88d | -20.86234 | -56.9457 | 2025-08-19 04:57:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 143bc0f9-2e98-3e83-b6e2-b528caf3e7c5 | -21.86623 | -46.55736 | 2025-08-19 04:57:00 | NPP-375D | POÇOS DE CALDAS | MINAS GERAIS | Brasil | 3151800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| f086a183-9d6d-39e7-8720-56d0f3eeec27 | -22.23025 | -56.0706 | 2025-08-19 04:57:00 | NPP-375D | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 5c52a02a-9f31-3874-9df5-d8ef31971ca6 | -20.87015 | -54.98613 | 2025-08-19 04:57:00 | NPP-375D | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a7a68f85-83de-3ec8-a8b9-c6ea78dffea1 | -20.86243 | -56.90282 | 2025-08-19 04:57:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 028edba0-c9ad-37cb-b92c-71b8b26a0c48 | -23.07589 | -46.3996 | 2025-08-19 04:57:00 | NPP-375D | PIRACAIA | SÃO PAULO | Brasil | 3538600 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| b2f53608-8e4b-3996-b2ea-e700e4878ddb | -24.85463 | -50.72094 | 2025-08-19 04:57:00 | NPP-375D | IPIRANGA | PARANÁ | Brasil | 4110508 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 4e5ce2fb-b4bc-3599-99b6-5e701f70382f | -20.8797 | -54.96856 | 2025-08-19 04:57:00 | NPP-375D | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 584d17fd-e5ad-329c-8cf2-769fb3858c38 | -20.87629 | -54.99101 | 2025-08-19 04:57:00 | NPP-375D | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3a6a1c87-8ca5-3166-9894-b88b0d529ff5 | -20.85625 | -56.94067 | 2025-08-19 04:57:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |


[Clique aqui para ver as próximas entradas](README46.md)
