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

## Dados Diários - Página 150

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b384dc3e-08c0-33d0-888d-d3449a557ccf | -18.11285 | -56.39856 | 2024-10-09 04:42:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.9 |
| 7592d4da-eba9-36a0-bbb0-ffcbfc08afb4 | -18.11081 | -56.38794 | 2024-10-09 04:42:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.0 |
| f0ae1b64-ab9c-3696-8cbf-60db266c6ecd | -18.10991 | -56.39286 | 2024-10-09 04:42:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.0 |
| b80a3ae4-9496-3d1a-b10f-82ff8fa93944 | -18.10902 | -56.3978 | 2024-10-09 04:42:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.7 |
| a93a4721-2025-3726-8f80-a3ccf632b454 | -18.10609 | -56.39211 | 2024-10-09 04:42:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.0 |
| c2e02e48-65ac-3e31-871f-c156eb4713a3 | -18.1052 | -56.39705 | 2024-10-09 04:42:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.7 |
| dc6d072a-2cb0-31f6-9021-1264217cbf39 | -18.09729 | -56.37503 | 2024-10-09 04:42:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 4f07d9fc-deeb-305b-b56a-8244b52b3fc3 | -18.0964 | -56.37996 | 2024-10-09 04:42:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 5bebc1dc-e5d8-39e3-a495-d0784f4ebb97 | -17.96359 | -56.47027 | 2024-10-09 04:42:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| e88cb2e9-e133-3a76-acc4-61fd1bd9cfae | -19.11025 | -57.52137 | 2024-10-09 04:42:00 | NPP-375D | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 9859a6a4-2559-3eca-879c-1ba49784cb65 | -19.10622 | -57.52055 | 2024-10-09 04:42:00 | NPP-375D | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 0.8 |
| afb19e5e-d03f-3f88-8182-51d19b472084 | -18.87009 | -57.73513 | 2024-10-09 04:42:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| af71e7b1-dce2-3351-b2dd-d7c8170cb38e | -18.64971 | -57.20779 | 2024-10-09 04:42:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 003ef27b-d908-355b-8cae-4ea902e26dfc | -18.64872 | -57.21318 | 2024-10-09 04:42:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| d25329b3-667b-3feb-8b12-89007287971e | -18.64474 | -57.21238 | 2024-10-09 04:42:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.0 |
| f3fa136c-347e-32aa-8d69-a27abcf54f26 | -18.63635 | -57.30365 | 2024-10-09 04:42:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| e7b878e5-7171-3f8d-be16-44d271e395a3 | -18.63368 | -57.29556 | 2024-10-09 04:42:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 3b6baa63-85a4-3c69-84d5-7f7bef364917 | -18.62968 | -57.29473 | 2024-10-09 04:42:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.3 |
| cfd734e0-33bf-37c5-a078-d4d2e9d98543 | -18.62187 | -57.22451 | 2024-10-09 04:42:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 16376fef-7774-3d6f-b0e2-50438883722f | -18.62087 | -57.22992 | 2024-10-09 04:42:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 1928b35b-f593-3a0f-8614-07a7507c02f7 | -18.60792 | -57.23288 | 2024-10-09 04:42:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 2e91df97-0335-3183-b25f-b12e7cb06e6e | -18.60692 | -57.23829 | 2024-10-09 04:42:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.2 |
| e5bbb50c-9bdc-3670-9e45-cbaa96b3f2bf | -18.60293 | -57.23747 | 2024-10-09 04:42:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 1c62c595-e8d5-38e2-8bbe-cee165cf9f59 | -18.6019 | -57.26544 | 2024-10-09 04:42:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.5 |
| e46f5c8b-d011-340d-9b39-36353994588c | -18.59891 | -57.25918 | 2024-10-09 04:42:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.5 |
| b7af4262-1916-3a97-b680-561b527a5b0a | -18.59794 | -57.24208 | 2024-10-09 04:42:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 7bd05554-dd77-3e7a-8ace-68b960f652f1 | -18.5979 | -57.26462 | 2024-10-09 04:42:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.5 |
| e7e3b2e1-7a05-338a-bd87-339681d349a8 | -18.59694 | -57.2475 | 2024-10-09 04:42:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| d3a4c229-961f-39e1-aade-9504d72fe036 | -18.5969 | -57.27006 | 2024-10-09 04:42:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| e2c81aeb-9349-363d-8109-309d581e8620 | -18.59593 | -57.25293 | 2024-10-09 04:42:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 2e3ad92d-e8b7-3baa-9f2f-cdb111876411 | -18.59492 | -57.25836 | 2024-10-09 04:42:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.9 |
| f0d4dce6-8574-3a54-a873-1a09a8a130de | -18.59395 | -57.24125 | 2024-10-09 04:42:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 9433e755-90b3-3edf-8525-485935f47a53 | -18.59391 | -57.2638 | 2024-10-09 04:42:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.9 |
| 155b782e-cbd6-3f1b-af88-9bc1faa28a97 | -18.59295 | -57.24668 | 2024-10-09 04:42:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 27b130fc-e4a4-3724-9b28-f67762c5d940 | -18.5929 | -57.26924 | 2024-10-09 04:42:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 4b4a5197-4634-3d36-9e6b-9a0ee9ce2ac6 | -18.59194 | -57.25211 | 2024-10-09 04:42:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 7d3223e0-6a71-392b-8c2e-38917059620a | -18.59093 | -57.25755 | 2024-10-09 04:42:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.9 |
| 9fc56345-580d-32f2-9ade-3403abf08833 | -18.58992 | -57.26299 | 2024-10-09 04:42:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.9 |
| 99869c15-2eab-341d-b3b9-a7548116319a | -24.5022 | -50.25962 | 2024-10-09 04:42:00 | NPP-375D | TIBAGI | PARANÁ | Brasil | 4127502 | 41 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 10162135-75ed-353e-b2aa-972542b328ae | -22.82188 | -48.42847 | 2024-10-09 04:42:00 | NPP-375D | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 5.7 |
| ac5dbc8e-f5ea-3ad5-919b-4b4e50721f38 | -22.8212 | -48.43378 | 2024-10-09 04:42:00 | NPP-375D | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 8de0a3c4-2a43-3c4b-9889-76aace29c604 | -22.81871 | -48.4221 | 2024-10-09 04:42:00 | NPP-375D | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6671769e-252e-3737-9b4e-c0da4da95f41 | -22.81731 | -48.43311 | 2024-10-09 04:42:00 | NPP-375D | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 7caac3df-6957-3de4-a6bf-c32d2cae92a4 | -22.81482 | -48.42141 | 2024-10-09 04:42:00 | NPP-375D | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 50b2e02b-6d5e-3f34-ab30-8f68109d3c0e | -22.81341 | -48.43245 | 2024-10-09 04:42:00 | NPP-375D | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c5c106fd-3328-3c24-97c2-31ed1943adeb | -22.81209 | -48.44284 | 2024-10-09 04:42:00 | NPP-375D | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 20259e4a-082c-36f5-ba36-aba68cb6ac1a | -22.81162 | -48.41523 | 2024-10-09 04:42:00 | NPP-375D | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ccc1564b-a285-317d-a709-9652beb77b25 | -22.81144 | -48.44797 | 2024-10-09 04:42:00 | NPP-375D | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 93225e6f-19f4-3665-98f1-d84424ddcdcc | -22.81092 | -48.42078 | 2024-10-09 04:42:00 | NPP-375D | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cabdb662-0994-39b6-845c-5fd53e5440ff | -22.81081 | -48.45289 | 2024-10-09 04:42:00 | NPP-375D | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f23dd8ef-96bb-32d6-8773-b436c8f636f0 | -22.8102 | -48.42647 | 2024-10-09 04:42:00 | NPP-375D | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4ebebfb8-e140-33ab-9670-61c9f357b515 | -22.80951 | -48.43183 | 2024-10-09 04:42:00 | NPP-375D | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d410e434-0ffe-3c7d-8323-a3a15a6354ab | -22.8082 | -48.44215 | 2024-10-09 04:42:00 | NPP-375D | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 052ff561-3bbf-323b-a31d-d72d0d94051f | -22.80754 | -48.44737 | 2024-10-09 04:42:00 | NPP-375D | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5311e02d-d88a-363e-a70e-23a694b5f52f | -22.80691 | -48.45227 | 2024-10-09 04:42:00 | NPP-375D | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 413d1fa6-b401-3513-935a-eec0a6728d46 | -22.80561 | -48.43122 | 2024-10-09 04:42:00 | NPP-375D | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 8.4 |
| f7f94ad9-3592-34af-959f-02fc9a1622d7 | -22.80431 | -48.44147 | 2024-10-09 04:42:00 | NPP-375D | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3569bf37-0b53-3580-98d3-39200905efcb | -22.80363 | -48.4468 | 2024-10-09 04:42:00 | NPP-375D | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 1.9 |
| eea28785-1f66-3569-9467-a0c619943203 | -22.80301 | -48.45171 | 2024-10-09 04:42:00 | NPP-375D | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ce725cdf-f0b2-3e44-87f8-e2c6589799c6 | -22.80172 | -48.43056 | 2024-10-09 04:42:00 | NPP-375D | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 996a44cc-6184-382b-8645-ad087ffb8c26 | -22.80042 | -48.44082 | 2024-10-09 04:42:00 | NPP-375D | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4156cbbb-95da-38c3-a4b3-572c442834c1 | -22.79973 | -48.44627 | 2024-10-09 04:42:00 | NPP-375D | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9312509e-2304-3c64-bb4b-8c904554e74c | -22.7991 | -48.45122 | 2024-10-09 04:42:00 | NPP-375D | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 978d7932-a3ee-3f78-b886-3a74d9c6d749 | -22.79783 | -48.42987 | 2024-10-09 04:42:00 | NPP-375D | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 7.8 |
| dfed35b8-5803-3e94-8150-00eb356b5657 | -22.7972 | -48.43486 | 2024-10-09 04:42:00 | NPP-375D | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7f7def6f-af3c-3947-931b-94a7cf480e05 | -22.79653 | -48.44014 | 2024-10-09 04:42:00 | NPP-375D | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ed21d86d-d908-3ff7-9091-d8a25a7b838e | -22.79582 | -48.44572 | 2024-10-09 04:42:00 | NPP-375D | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 37c41a26-c8ad-371e-b427-73f7b27a38dd | -22.79519 | -48.45075 | 2024-10-09 04:42:00 | NPP-375D | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 996e8732-a921-3aa0-bf5d-850d0ac2dbcb | -22.79394 | -48.42915 | 2024-10-09 04:42:00 | NPP-375D | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 7.8 |
| e470d76d-cd4b-3008-9952-d92f5b6aceac | -22.79331 | -48.43417 | 2024-10-09 04:42:00 | NPP-375D | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 680e7a2d-c4f7-372d-8fb5-b100506fe7c2 | -22.79193 | -48.44507 | 2024-10-09 04:42:00 | NPP-375D | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7cb18382-6f22-3586-bcb7-4537af0b94db | -22.58099 | -49.22041 | 2024-10-09 04:42:00 | NPP-375D | PAULISTÂNIA | SÃO PAULO | Brasil | 3536570 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f9aaba3e-bfa3-33da-998d-c786678c93cc | -22.57726 | -49.21987 | 2024-10-09 04:42:00 | NPP-375D | PAULISTÂNIA | SÃO PAULO | Brasil | 3536570 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 425b5db4-dfaf-336b-abf6-51474b4cdf9e | -22.18979 | -48.15324 | 2024-10-09 04:42:00 | NPP-375D | BROTAS | SÃO PAULO | Brasil | 3507902 | 35 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 37a318e3-b969-3918-a99b-8adf80bf6f22 | -22.18846 | -48.16378 | 2024-10-09 04:42:00 | NPP-375D | BROTAS | SÃO PAULO | Brasil | 3507902 | 35 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 39c2dc16-d7ec-3af9-965f-cbc0a131394d | -22.18467 | -48.09819 | 2024-10-09 04:42:00 | NPP-375D | BROTAS | SÃO PAULO | Brasil | 3507902 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2bec2783-df83-3890-a6ed-477029c23bbb | -22.18124 | -48.15747 | 2024-10-09 04:42:00 | NPP-375D | BROTAS | SÃO PAULO | Brasil | 3507902 | 35 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 51086a2b-780d-3804-8bfa-4d7d3dbaa255 | -22.17991 | -48.168 | 2024-10-09 04:42:00 | NPP-375D | BROTAS | SÃO PAULO | Brasil | 3507902 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 39137c6c-8a91-31a8-a273-3e7b99affb35 | -22.17663 | -48.16223 | 2024-10-09 04:42:00 | NPP-375D | BROTAS | SÃO PAULO | Brasil | 3507902 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 89de339e-f7b0-30b1-ad18-448a271f2c01 | -22.17351 | -48.09088 | 2024-10-09 04:42:00 | NPP-375D | BROTAS | SÃO PAULO | Brasil | 3507902 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 31c43523-69d5-3b88-bf55-1ce978dcf0a8 | -22.17216 | -48.1017 | 2024-10-09 04:42:00 | NPP-375D | RIBEIRÃO BONITO | SÃO PAULO | Brasil | 3542909 | 35 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 7b809dd3-e93b-3c17-8060-c5e630d3c37c | -22.15699 | -48.12679 | 2024-10-09 04:42:00 | NPP-375D | RIBEIRÃO BONITO | SÃO PAULO | Brasil | 3542909 | 35 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4f5d2b91-c772-362a-8511-153170242b3d | -22.15563 | -48.08727 | 2024-10-09 04:42:00 | NPP-375D | RIBEIRÃO BONITO | SÃO PAULO | Brasil | 3542909 | 35 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2ed80e90-f569-3d24-96c3-bc074b928b85 | -22.15537 | -48.12013 | 2024-10-09 04:42:00 | NPP-375D | RIBEIRÃO BONITO | SÃO PAULO | Brasil | 3542909 | 35 | 33 | nan | nan | nan | Cerrado | 4.3 |
| e53a0148-bf83-3ce6-b31d-7772d1ed50b7 | -22.15468 | -48.12543 | 2024-10-09 04:42:00 | NPP-375D | RIBEIRÃO BONITO | SÃO PAULO | Brasil | 3542909 | 35 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 40ef86c0-4433-39f6-8ceb-45f3def4a093 | -22.15375 | -48.08803 | 2024-10-09 04:42:00 | NPP-375D | RIBEIRÃO BONITO | SÃO PAULO | Brasil | 3542909 | 35 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e6c97f36-55b0-3be3-ac27-f5cab26fe79b | -22.15371 | -48.1209 | 2024-10-09 04:42:00 | NPP-375D | RIBEIRÃO BONITO | SÃO PAULO | Brasil | 3542909 | 35 | 33 | nan | nan | nan | Cerrado | 3.2 |
| c3706962-ff7d-336c-bc74-d8d598ce0326 | -22.15167 | -48.08677 | 2024-10-09 04:42:00 | NPP-375D | RIBEIRÃO BONITO | SÃO PAULO | Brasil | 3542909 | 35 | 33 | nan | nan | nan | Cerrado | 1.7 |
| fe2fbb2d-064b-3e87-99ea-5ff086550bbb | -22.15144 | -48.1195 | 2024-10-09 04:42:00 | NPP-375D | RIBEIRÃO BONITO | SÃO PAULO | Brasil | 3542909 | 35 | 33 | nan | nan | nan | Cerrado | 4.0 |
| fcddf85c-bb21-386d-b99d-474c961dfe3d | -22.15075 | -48.12479 | 2024-10-09 04:42:00 | NPP-375D | RIBEIRÃO BONITO | SÃO PAULO | Brasil | 3542909 | 35 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 4d97a172-4d38-3a55-9f5f-ecea451c39e2 | -22.14977 | -48.12023 | 2024-10-09 04:42:00 | NPP-375D | RIBEIRÃO BONITO | SÃO PAULO | Brasil | 3542909 | 35 | 33 | nan | nan | nan | Cerrado | 3.2 |
| b3dd5be5-32cc-3386-a69c-3bf86ef83e2d | -22.14938 | -48.13533 | 2024-10-09 04:42:00 | NPP-375D | RIBEIRÃO BONITO | SÃO PAULO | Brasil | 3542909 | 35 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 1bc6b7f5-9ae7-3478-a0d6-340f6517855e | -22.14846 | -48.13083 | 2024-10-09 04:42:00 | NPP-375D | RIBEIRÃO BONITO | SÃO PAULO | Brasil | 3542909 | 35 | 33 | nan | nan | nan | Cerrado | 4.7 |
| c9866b16-68d8-3fcc-9493-cf02d552b44f | -22.14781 | -48.1361 | 2024-10-09 04:42:00 | NPP-375D | RIBEIRÃO BONITO | SÃO PAULO | Brasil | 3542909 | 35 | 33 | nan | nan | nan | Cerrado | 2.1 |
| bd2ea431-c22d-355e-b1c5-e7d85b5d9204 | -22.14544 | -48.13469 | 2024-10-09 04:42:00 | NPP-375D | RIBEIRÃO BONITO | SÃO PAULO | Brasil | 3542909 | 35 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d8dc7b58-41ff-3985-9d10-28dddb279354 | -22.14255 | -48.11366 | 2024-10-09 04:42:00 | NPP-375D | RIBEIRÃO BONITO | SÃO PAULO | Brasil | 3542909 | 35 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 71fa8561-29f0-36bc-ad36-2ba2c0dc1cae | -22.1419 | -48.11892 | 2024-10-09 04:42:00 | NPP-375D | RIBEIRÃO BONITO | SÃO PAULO | Brasil | 3542909 | 35 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 26db1688-5426-3e9c-86ca-c4c2f83ac340 | -22.13502 | -48.12222 | 2024-10-09 04:42:00 | NPP-375D | RIBEIRÃO BONITO | SÃO PAULO | Brasil | 3542909 | 35 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 3310ad29-8837-303f-9abd-98c1398c0cac | -22.1312 | -48.08951 | 2024-10-09 04:42:00 | NPP-375D | RIBEIRÃO BONITO | SÃO PAULO | Brasil | 3542909 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5688e2b3-c979-38db-b603-9d509394a9e5 | -22.12713 | -48.12111 | 2024-10-09 04:42:00 | NPP-375D | RIBEIRÃO BONITO | SÃO PAULO | Brasil | 3542909 | 35 | 33 | nan | nan | nan | Cerrado | 2.2 |


[Clique aqui para ver as próximas entradas](README151.md)
