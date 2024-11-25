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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d5341802-0d61-3a9c-b600-464996117164 | -3.9489 | -50.842701 | 2024-11-25 00:00:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| dcb66c4c-d167-3902-b057-fab3ba8bbe4f | -5.653 | -46.640099 | 2024-11-25 00:00:00 | METOP-B | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 5df46ddd-9bb3-300e-bc18-ef9533dce23a | -4.1509 | -44.271599 | 2024-11-25 00:00:00 | METOP-B | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 5a8b5015-d837-32a3-a7e0-aafc22f383bf | -3.3795 | -43.406898 | 2024-11-25 00:00:00 | METOP-B | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 4412a113-0322-3e06-80f1-ba078bfaeee0 | -6.5279 | -35.1516 | 2024-11-25 00:00:00 | METOP-B | PEDRO VELHO | RIO GRANDE DO NORTE | Brasil | 2409803 | 24 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 79cc5d94-7277-3ed9-8c80-e0d152ca2182 | -3.9554 | -50.825401 | 2024-11-25 00:00:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1b8524ff-6001-31df-ad69-2becb525d64e | -3.9338 | -47.9701 | 2024-11-25 00:00:00 | METOP-B | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6ed55434-1023-3e49-bec7-3886a8adf2c2 | -4.5368 | -43.5583 | 2024-11-25 00:00:00 | METOP-B | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 26ebb1b8-8cc9-3ab3-93bf-858ed3b1767c | -4.0144 | -43.251598 | 2024-11-25 00:00:00 | METOP-B | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 72723f13-c250-3fc3-ab89-ccf0e4442e53 | -4.5102 | -44.588699 | 2024-11-25 00:00:00 | METOP-B | PEDREIRAS | MARANHÃO | Brasil | 2108207 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a695c202-5494-32b9-831c-728e28289023 | -4.8014 | -40.682098 | 2024-11-25 00:00:00 | METOP-B | ARARENDÁ | CEARÁ | Brasil | 2301257 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 1d64463f-8ac3-3ee1-9682-cea2de580b93 | -3.9414 | -47.958199 | 2024-11-25 00:00:00 | METOP-B | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1a440653-9f7d-39ed-aa7b-5ceafc7f5bb3 | -3.7082 | -52.404301 | 2024-11-25 00:00:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3381c2d9-4233-3d48-85a2-afb7bcf6c32f | -3.1385 | -44.349998 | 2024-11-25 00:00:00 | METOP-B | SANTA RITA | MARANHÃO | Brasil | 2110203 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| feb7befd-f9e0-353f-abd8-bfee206e8277 | -3.9458 | -47.977901 | 2024-11-25 00:00:00 | METOP-B | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 28c01533-b093-36e4-bc33-6174fc87396c | -3.7138 | -52.382801 | 2024-11-25 00:00:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3dcc0c52-d30b-3863-b87f-7aa0e1e0b3bb | -3.378 | -43.400101 | 2024-11-25 00:00:00 | METOP-B | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 90c7ce14-ef4d-364c-9969-696fe150d52c | -3.704 | -52.3848 | 2024-11-25 00:00:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d07f3d80-5cb2-3e01-bd4b-5f13cd11da4f | -5.8942 | -42.768002 | 2024-11-25 00:00:00 | METOP-B | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 76a1b684-0cc7-3800-b9ac-261d3eee03b1 | -3.1632 | -51.075001 | 2024-11-25 00:00:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5d365e4b-d86c-3d35-8549-efcaad0373f0 | -4.4741 | -45.535599 | 2024-11-25 00:00:00 | METOP-B | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| dadf582d-d754-3f04-8d9a-c0a25d86b7d2 | -3.4514 | -50.8069 | 2024-11-25 00:00:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6c995fee-abc5-3fca-a45b-882a64114336 | -20.2059 | -43.459801 | 2024-11-25 00:00:00 | METOP-B | MARIANA | MINAS GERAIS | Brasil | 3140001 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 46cb4780-af52-3b55-9932-665007ccf087 | -4.4191 | -43.814301 | 2024-11-25 00:00:00 | METOP-B | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c317e089-5b16-3b76-be70-ad7c013b3519 | -4.3757 | -48.488701 | 2024-11-25 00:00:00 | METOP-B | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f2793360-42fa-3b17-8ad5-9da2ff9e69c1 | -5.2443 | -42.719002 | 2024-11-25 00:00:00 | METOP-B | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| c7aecde6-55bd-35f8-a0d0-acd0f5495a8b | -3.2251 | -46.301601 | 2024-11-25 00:00:00 | METOP-B | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 45a7f865-c58a-332e-9753-de99424e88e9 | -4.5249 | -42.8652 | 2024-11-25 00:00:00 | METOP-B | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| f0a5b555-af29-345a-b4e8-b4004d93d881 | -4.4725 | -45.528099 | 2024-11-25 00:00:00 | METOP-B | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| fb31e54e-2a5a-3dee-ba90-2ac6168addb8 | -5.6108 | -43.478001 | 2024-11-25 00:00:00 | METOP-B | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 0d9a8739-9b23-3e89-a29d-d0c17ce9bfb7 | -4.0159 | -43.2584 | 2024-11-25 00:00:00 | METOP-B | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 03f88745-87a0-3cd0-adb7-c25ad3999bcc | -4.4193 | -45.658798 | 2024-11-25 00:00:00 | METOP-B | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| d62c1502-4477-3bce-a334-1a85159b7cc5 | -1.6675 | -47.936699 | 2024-11-25 00:00:00 | METOP-B | BUJARU | PARÁ | Brasil | 1501907 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a378766b-1d57-3f0c-a08c-e71b64af5c9b | -5.619 | -43.469002 | 2024-11-25 00:00:00 | METOP-B | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 41b2a266-87ac-3559-b039-fc34040e1eb6 | -4.5441 | -48.931 | 2024-11-25 00:00:00 | METOP-B | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0ce61007-0e16-31f0-b047-df8d02cbd3bd | -3.9456 | -50.827499 | 2024-11-25 00:00:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6e029ac5-cd61-3ea7-8bee-eaf8f0a465b4 | -3.5879 | -49.3325 | 2024-11-25 00:00:00 | METOP-B | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3c2a553f-b0d0-3f7a-bed8-2c8d990b137c | -1.6696 | -47.945801 | 2024-11-25 00:00:00 | METOP-B | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a68bbd6a-57ad-3e23-b9fc-ba834e3b41dd | -3.6835 | -45.358299 | 2024-11-25 00:00:00 | METOP-B | SANTA INÊS | MARANHÃO | Brasil | 2109908 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 3fa24da9-0a62-3baf-a5d8-45ed19f82a43 | -4.1654 | -43.053101 | 2024-11-25 00:00:00 | METOP-B | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 443d1b06-3ec1-37b6-9aee-03097d0dbfda | -2.8277 | -45.122799 | 2024-11-25 00:00:00 | METOP-B | SÃO BENTO | MARANHÃO | Brasil | 2110500 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 63b35710-f670-34d0-b354-cfac781c5c6d | -4.279 | -45.9072 | 2024-11-25 00:00:00 | METOP-B | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| acaf9c1a-7e40-307b-af72-8f5aebdd9fa3 | -4.2709 | -45.917 | 2024-11-25 00:00:00 | METOP-B | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 99c5030e-d98b-351d-8da1-16fa5db10c3d | -4.2928 | -46.8983 | 2024-11-25 00:00:00 | METOP-B | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 26f4956f-1d98-3914-8cb3-08f9593c673e | -6.6448 | -43.588902 | 2024-11-25 00:00:00 | METOP-B | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 134d0549-a437-31e5-87c2-b55c333295ae | -3.048 | -45.1866 | 2024-11-25 00:00:00 | METOP-B | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 971fa0a0-5452-3a2e-a316-c112cfcd57bb | -4.1427 | -44.280602 | 2024-11-25 00:00:00 | METOP-B | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 93edf867-0d63-31e8-b613-d7d969b98aa6 | -3.5905 | -49.344398 | 2024-11-25 00:00:00 | METOP-B | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bcb52d78-3f1f-3504-ba12-828ed95145e0 | -4.3 | -46.558899 | 2024-11-25 00:00:00 | METOP-B | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 882a4842-1d4c-32e8-ae23-c7e08477ab62 | -4.5378 | -42.876701 | 2024-11-25 00:00:00 | METOP-B | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e580740a-f636-3036-8377-7f88a3b14bb3 | -5.5467 | -45.316898 | 2024-11-25 00:00:00 | METOP-B | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 34a6c448-1bf2-382f-9a51-df31e0de63b4 | -3.2912 | -43.426601 | 2024-11-25 00:00:00 | METOP-B | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d25f6f50-a093-34bf-a3bd-9279cd3f104d | -9.8752 | -41.821602 | 2024-11-25 00:00:00 | METOP-B | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| a128fa1d-57a3-3eac-a779-f5e1f7cc74e2 | -5.1308 | -46.179901 | 2024-11-25 00:00:00 | METOP-B | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| c9d3675b-9219-3dad-b9b5-11628e80c4ea | -2.811 | -46.797001 | 2024-11-25 00:00:00 | METOP-B | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ae5c65da-9f7d-30c6-a782-886c2938f90f | -6.6433 | -43.582001 | 2024-11-25 00:00:00 | METOP-B | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| cd2fc058-2f60-3e63-a985-af7fe5caed79 | -1.6655 | -47.927601 | 2024-11-25 00:00:00 | METOP-B | BUJARU | PARÁ | Brasil | 1501907 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0eaa7186-591a-3afc-a926-b5e603901e66 | -3.936 | -47.98 | 2024-11-25 00:00:00 | METOP-B | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e84c74e8-364a-3d29-8a8c-e11db87ef60b | -5.5484 | -45.324501 | 2024-11-25 00:00:00 | METOP-B | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 1635aeb4-9e16-367f-b8a3-57a993fca69b | -5.1587 | -44.5425 | 2024-11-25 00:00:00 | METOP-B | SÃO JOSÉ DOS BASÍLIOS | MARANHÃO | Brasil | 2111250 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 777c2db1-7bdc-36a4-97cf-3be6e73eb9ff | -3.0291 | -45.056099 | 2024-11-25 00:00:00 | METOP-B | MATINHA | MARANHÃO | Brasil | 2106508 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| b166e0b8-0181-308a-bdfd-3c4bdd4c6ef9 | -4.199 | -50.209999 | 2024-11-25 00:00:00 | METOP-B | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2c1f5407-d48a-30be-9c58-bb0e616a2ad3 | -4.2807 | -45.914902 | 2024-11-25 00:00:00 | METOP-B | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| dbb44b3e-fcea-35af-910c-ce166132d5db | -4.1975 | -42.9669 | 2024-11-25 00:00:00 | METOP-B | MIGUEL ALVES | PIAUÍ | Brasil | 2206209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 6c476f1e-2254-3a5d-89b2-552075a6b5d8 | -4.5862 | -46.087399 | 2024-11-25 00:00:00 | METOP-B | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 6ded3b6f-c283-3045-93d8-1cd703a2af37 | -4.5086 | -44.5816 | 2024-11-25 00:00:00 | METOP-B | PEDREIRAS | MARANHÃO | Brasil | 2108207 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 0e2ac776-ebac-3c86-b471-aafb9be1031d | -4.5393 | -42.883598 | 2024-11-25 00:00:00 | METOP-B | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e5b4098a-dfe8-3aa5-a782-57a6a04cc0ac | -3.8132 | -41.002998 | 2024-11-25 00:00:00 | METOP-B | TIANGUÁ | CEARÁ | Brasil | 2313401 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 49b38587-d8b1-34b7-8e0f-a19686a11911 | -3.366 | -44.033001 | 2024-11-25 00:00:00 | METOP-B | PRESIDENTE VARGAS | MARANHÃO | Brasil | 2109304 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 6f2994a3-e949-3725-879c-10767bd21653 | -4.8506 | -44.73 | 2024-11-25 00:00:00 | METOP-B | ESPERANTINÓPOLIS | MARANHÃO | Brasil | 2104008 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 06c6d57c-d6ff-3265-8122-f3f90d0ede43 | -4.8646 | -38.370899 | 2024-11-25 00:00:00 | METOP-B | MORADA NOVA | CEARÁ | Brasil | 2308708 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| c7571aad-c861-3139-9935-777bc4a9b351 | -4.5491 | -42.881401 | 2024-11-25 00:00:00 | METOP-B | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a4384f44-08d9-3765-8ced-aa811f1aa32e | -2.8092 | -46.788799 | 2024-11-25 00:00:00 | METOP-B | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d45b6d39-ac9b-3123-9304-1ec03d4271bf | -4.2007 | -48.111198 | 2024-11-25 00:00:00 | METOP-B | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e0ca53ed-14f7-3edd-be9a-b98e28c34dec | -4.66 | -49.369701 | 2024-11-25 00:00:00 | METOP-B | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| beba416d-5e27-39fa-8991-145c4655c82a | -3.3395 | -50.481899 | 2024-11-25 00:04:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 46ee697e-3f6c-3902-b7fc-6dafdc818586 | -2.8965 | -51.5317 | 2024-11-25 00:04:00 | METOP-B | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 630ed2d5-d977-3564-b045-ed495fe00b54 | -2.719 | -45.6936 | 2024-11-25 00:04:00 | METOP-B | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 7e111662-ad66-3f0e-b2f5-5113a70f9271 | -0.0411 | -50.787701 | 2024-11-25 00:04:00 | METOP-B | AFUÁ | PARÁ | Brasil | 1500305 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a485cf58-ea2f-3e6a-8248-a5ce3b69bd2c | -2.9186 | -46.679199 | 2024-11-25 00:04:00 | METOP-B | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2acd79fe-bfd0-347f-bfe3-2b54fe32d00a | -4.2526 | -48.7211 | 2024-11-25 00:04:00 | METOP-B | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 318caebf-2b4e-3af2-90b1-a327af526470 | -0.815 | -48.076199 | 2024-11-25 00:04:00 | METOP-B | VIGIA | PARÁ | Brasil | 1508209 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e41cb7c3-a76c-338a-ab58-0c02893144ef | -4.2381 | -48.6549 | 2024-11-25 00:04:00 | METOP-B | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cc904f96-1aa4-3373-bb8c-baa1d17b8cb2 | -2.8464 | -45.4809 | 2024-11-25 00:04:00 | METOP-B | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| ea2ab2aa-1112-39c1-897b-ad64b2370b88 | -2.3048 | -53.553699 | 2024-11-25 00:04:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b1bb52e5-1140-3fdb-899b-33687012b41d | -3.6427 | -51.354698 | 2024-11-25 00:04:00 | METOP-B | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 47eef0d8-de56-3ec2-82f2-f8df337d24b0 | -1.7651 | -52.681099 | 2024-11-25 00:04:00 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5337b852-570b-3ac9-9199-af175e317d6b | -3.7045 | -47.117298 | 2024-11-25 00:04:00 | METOP-B | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1f883cc7-bb24-3195-90c0-058069c90332 | -3.2807 | -51.098301 | 2024-11-25 00:04:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 13873ee5-1cc1-3569-8d65-50695e808b45 | -3.4674 | -47.6698 | 2024-11-25 00:04:00 | METOP-B | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 46db8d71-c83d-347d-b795-6f1cab3df68e | -4.0145 | -48.056599 | 2024-11-25 00:04:00 | METOP-B | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fadfe646-3ddd-37ad-ad40-56a2e6de1b1d | -3.1841 | -49.033001 | 2024-11-25 00:04:00 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cf6d2918-47de-36bd-a0c6-7a648fba6c58 | -4.0385 | -48.0723 | 2024-11-25 00:04:00 | METOP-B | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5ff0537c-3eca-3172-a515-07b615995b12 | -2.8904 | -51.550201 | 2024-11-25 00:04:00 | METOP-B | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 769f0361-fbbd-3d24-beb6-c1068c8e1e05 | -3.7081 | -51.748199 | 2024-11-25 00:04:00 | METOP-B | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b07ad7d2-a56c-36f3-90d4-15c7eb3a9d2e | -3.3426 | -50.496101 | 2024-11-25 00:04:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e9925e66-83d4-31ad-8e3e-00d6f55b26a2 | -4.2478 | -48.698898 | 2024-11-25 00:04:00 | METOP-B | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 120d9ddc-0e52-37e9-96ca-a7a5b2f4d743 | -0.3391 | -51.515499 | 2024-11-25 00:04:00 | METOP-B | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| b35dd31e-248b-3fc2-a3ce-91eb2f6d6c09 | -2.3097 | -53.576 | 2024-11-25 00:04:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f643924c-909b-3d2c-a191-794278e2f1b4 | -3.1495 | -44.260899 | 2024-11-25 00:04:00 | METOP-B | SANTA RITA | MARANHÃO | Brasil | 2110203 | 21 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README3.md)
