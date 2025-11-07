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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9867db85-ccd0-30ca-8b96-75d44357b80f | -4.4415 | -46.4204 | 2025-11-07 00:00:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 69.8 |
| 0901cb83-6350-3bad-89f2-0ed9e562be62 | -5.1053 | -44.8103 | 2025-11-07 00:00:00 | GOES-19 | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 83.0 |
| 33b9a8dc-fde0-351c-88ef-e6a98a5d720b | -5.0866 | -44.8115 | 2025-11-07 00:00:00 | GOES-19 | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 138.0 |
| ca82ec24-3b64-358c-bcc5-215c65644dce | -3.4594 | -45.8657 | 2025-11-07 00:00:00 | GOES-19 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 48.7 |
| 0348c4f2-e02d-304a-a0b7-5c9f0f0c107c | 3.1094 | -60.765 | 2025-11-07 00:00:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 91.1 |
| 876fc87e-9dfa-3f03-add7-cb9408a15830 | -9.4589 | -35.7735 | 2025-11-07 00:00:00 | GOES-19 | MACEIÓ | ALAGOAS | Brasil | 2704302 | 27 | 33 | nan | nan | nan | Mata Atlântica | 71.7 |
| ba0bf960-a094-3952-a76f-d228162d2830 | -5.0868 | -44.7887 | 2025-11-07 00:00:00 | GOES-19 | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 172.8 |
| 41d01b83-70e5-36f0-a380-6d963c845c28 | -9.4782 | -35.7702 | 2025-11-07 00:00:00 | GOES-19 | MACEIÓ | ALAGOAS | Brasil | 2704302 | 27 | 33 | nan | nan | nan | Mata Atlântica | 112.0 |
| 8e0cc63c-e310-3e4c-8760-43a2fd3f4398 | 3.0911 | -60.7653 | 2025-11-07 00:00:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 76.9 |
| e722badc-2c1d-31dd-9e8e-fbd994637860 | -6.5722 | -44.0362 | 2025-11-07 00:00:00 | GOES-19 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 53.5 |
| 4d45c2e0-6043-3df8-84c8-51d504ad43de | -2.831 | -45.1267 | 2025-11-07 00:00:00 | GOES-19 | SÃO BENTO | MARANHÃO | Brasil | 2110500 | 21 | 33 | nan | nan | nan | Amazônia | 120.2 |
| 54d753a0-7c6a-3be8-a976-e56a4c7f792f | -2.8721 | -48.6851 | 2025-11-07 00:00:00 | GOES-19 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 61.4 |
| 1eae50ca-81ee-37ef-bdea-ccf5e7aef42d | -4.7206 | -46.4276 | 2025-11-07 00:00:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 110.2 |
| 8e9cefe8-eb38-3aeb-8119-4d2adce92913 | -3.5252 | -47.5389 | 2025-11-07 00:00:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 50.2 |
| 7706997e-0975-3814-b2a6-cb5e3e100ffd | -2.9435 | -49.3443 | 2025-11-07 00:00:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 59.0 |
| 32ba27b5-ab96-30d4-95b5-8c601fdd838f | -4.46 | -46.4416 | 2025-11-07 00:00:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 107.0 |
| 7ceef2c1-34b1-30fb-bfe5-cf764b075e72 | -2.8496 | -45.1261 | 2025-11-07 00:00:00 | GOES-19 | SÃO BENTO | MARANHÃO | Brasil | 2110500 | 21 | 33 | nan | nan | nan | Amazônia | 217.0 |
| 87030e89-d469-3174-8aa6-06181ef9722c | -2.8497 | -45.1035 | 2025-11-07 00:00:00 | GOES-19 | SÃO BENTO | MARANHÃO | Brasil | 2110500 | 21 | 33 | nan | nan | nan | Amazônia | 124.9 |
| 8ace4041-767b-38ba-ac2a-7cf566b562a0 | -5.1054 | -44.7875 | 2025-11-07 00:00:00 | GOES-19 | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 100.5 |
| 846e8f46-fe76-3074-99e0-bb8144b74f05 | -2.8311 | -45.1042 | 2025-11-07 00:00:00 | GOES-19 | SÃO BENTO | MARANHÃO | Brasil | 2110500 | 21 | 33 | nan | nan | nan | Amazônia | 73.9 |
| d383232e-66d2-399d-a459-6422f35eb026 | -4.4602 | -46.4194 | 2025-11-07 00:00:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 74.2 |
| 47c862f1-71fc-3333-8544-1125738c61b1 | -2.872 | -48.7065 | 2025-11-07 00:00:00 | GOES-19 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 59.9 |
| a294a0bb-0032-316d-b793-8db72917a5d0 | -4.4414 | -46.4425 | 2025-11-07 00:00:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 110.6 |
| ba0aa03b-ce04-3d43-bf6d-c750c2d90e68 | -4.9239 | -44.1129 | 2025-11-07 00:00:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 40.8 |
| b0981b7c-33d1-3772-baa7-abd7e2076e31 | -4.4042 | -46.4445 | 2025-11-07 00:00:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 99.3 |
| f81f67e7-26a4-307d-b585-2a9e300acfbb | -5.7589 | -40.81 | 2025-11-07 00:10:00 | GOES-19 | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 57.5 |
| 9ab33a34-b0d6-332c-8062-ab38c278e2ed | -4.46 | -46.4416 | 2025-11-07 00:10:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 97.4 |
| 9d7c1cb5-b076-3c02-9f38-9fd6fd46b7c1 | -5.0868 | -44.7887 | 2025-11-07 00:10:00 | GOES-19 | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 159.2 |
| 4dade41c-295d-3577-9694-317b1449b8d5 | -2.872 | -48.7065 | 2025-11-07 00:10:00 | GOES-19 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 62.3 |
| 83da0552-db77-3ef7-a8d2-5d2f0d2ccdb5 | 3.1094 | -60.765 | 2025-11-07 00:10:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 88.4 |
| 147822e9-6bdf-3e7c-bb0a-22bf7cf798dc | -2.8497 | -45.1035 | 2025-11-07 00:10:00 | GOES-19 | SÃO BENTO | MARANHÃO | Brasil | 2110500 | 21 | 33 | nan | nan | nan | Amazônia | 50.7 |
| 2cd8704d-c53b-3f69-b200-ee0a6242d0cd | -3.5252 | -47.5389 | 2025-11-07 00:10:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 47.3 |
| f794fc32-cc57-3a92-9af1-afcbf81269f3 | -2.9434 | -49.3655 | 2025-11-07 00:10:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 43.0 |
| e8f72cab-cea5-31d5-85fc-5dd4ffae32bf | -2.9435 | -49.3443 | 2025-11-07 00:10:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 55.3 |
| 5e3f4d0e-e917-3b50-88ac-3fff05a56daa | -3.4594 | -45.8657 | 2025-11-07 00:10:00 | GOES-19 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 59.9 |
| 9ef43f41-3928-377f-848c-e2d43388308d | -4.4042 | -46.4445 | 2025-11-07 00:10:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 94.9 |
| ef8d44f7-739c-3120-a027-36452efd09e5 | -5.7591 | -40.7856 | 2025-11-07 00:10:00 | GOES-19 | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 52.0 |
| cf97fecf-af6d-3958-8019-05cae52d3541 | -5.1053 | -44.8103 | 2025-11-07 00:10:00 | GOES-19 | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 93.2 |
| e5a338d6-671e-397c-ad8a-2fa041bd624a | -4.4414 | -46.4425 | 2025-11-07 00:10:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 107.6 |
| 33bc486a-16f2-3c2e-9ac9-c7dd66804b77 | 3.0911 | -60.7653 | 2025-11-07 00:10:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 75.8 |
| 613ebe87-1ed8-3184-94a5-2ff52bc1003f | -2.8496 | -45.1261 | 2025-11-07 00:10:00 | GOES-19 | SÃO BENTO | MARANHÃO | Brasil | 2110500 | 21 | 33 | nan | nan | nan | Amazônia | 63.2 |
| 1e68baf8-5d08-358c-be52-af64a545d02e | -3.5901 | -49.4501 | 2025-11-07 00:10:00 | GOES-19 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 62.9 |
| 1c48a3f8-5680-3e99-8c78-bb640c9a012e | -4.7206 | -46.4276 | 2025-11-07 00:10:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 107.5 |
| b82fbcac-39e8-3fe1-945f-22b7b554cfc4 | -5.0866 | -44.8115 | 2025-11-07 00:10:00 | GOES-19 | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 127.8 |
| 24356695-93a5-3121-9e50-dd003510c877 | -2.8721 | -48.6851 | 2025-11-07 00:10:00 | GOES-19 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 51.6 |
| 0fe218c0-487a-3c9b-97e3-f9252065c64a | -5.1054 | -44.7875 | 2025-11-07 00:10:00 | GOES-19 | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 109.2 |
| 813b4e26-a340-3b50-9935-1b1cff2786d3 | 3.1094 | -60.765 | 2025-11-07 00:20:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 82.7 |
| 5ad83c7c-f707-32e6-b22d-541ad2c88dc0 | 3.0911 | -60.7653 | 2025-11-07 00:20:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 75.0 |
| b40580eb-c21a-30ec-9559-daa5c860076d | -4.2961 | -45.8938 | 2025-11-07 00:20:00 | GOES-19 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 103.0 |
| 4009cf23-16ad-3cc5-b064-88d827455434 | -5.1054 | -44.7875 | 2025-11-07 00:20:00 | GOES-19 | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 68.9 |
| f29b51f3-f3fb-3d0c-ac32-22ccba3f4cf8 | -5.7589 | -40.81 | 2025-11-07 00:20:00 | GOES-19 | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 44.9 |
| 57a74bc0-27dd-3205-bc08-13b3e55ad6ef | -4.4414 | -46.4425 | 2025-11-07 00:20:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 76.3 |
| fa24bb5e-1b37-3c0b-a752-f52d85da30d8 | -5.0868 | -44.7887 | 2025-11-07 00:20:00 | GOES-19 | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 119.3 |
| c0123a63-1d7a-3eaa-afba-1659690b21de | -4.46 | -46.4416 | 2025-11-07 00:20:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 98.9 |
| 8a1be1a9-d5a1-308d-a290-879ab99dbe61 | -4.7206 | -46.4276 | 2025-11-07 00:20:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 103.9 |
| a061bf3e-faee-36ef-a8e1-e0a3f38b35c4 | -3.5252 | -47.5389 | 2025-11-07 00:20:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 42.7 |
| 10db809d-13fa-3efb-ab04-632190cebafc | -4.2962 | -45.8715 | 2025-11-07 00:20:00 | GOES-19 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 70.5 |
| 585cd79e-7b1c-3dc7-9131-a0399801041a | -4.2775 | -45.8948 | 2025-11-07 00:20:00 | GOES-19 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 42.9 |
| 6d3aae30-621a-3276-a37f-8d58919609bc | -5.0866 | -44.8115 | 2025-11-07 00:20:00 | GOES-19 | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 85.8 |
| 788f3c07-7a60-3797-9b09-0b253632d0f1 | -4.4042 | -46.4445 | 2025-11-07 00:20:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 83.7 |
| fcc6a468-f1ab-3ced-95a3-ee79b51f1ca0 | -3.3547 | -44.5395 | 2025-11-07 00:20:00 | GOES-19 | ANAJATUBA | MARANHÃO | Brasil | 2100709 | 21 | 33 | nan | nan | nan | Amazônia | 64.8 |
| 732824e7-c877-3fe0-b9cf-e98826b84c85 | -6.6517 | -43.6121 | 2025-11-07 00:30:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 60.7 |
| 652ba4c4-3ea4-34ca-8559-1328da3a6f9b | -3.5252 | -47.5389 | 2025-11-07 00:30:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 47.3 |
| 50dea5e0-b8a2-37ae-a92d-7cebed5c7776 | 3.0911 | -60.7653 | 2025-11-07 00:30:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 76.5 |
| 32b171e1-616a-34e9-a938-f2aab2c61e16 | -4.7206 | -46.4276 | 2025-11-07 00:30:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 77.8 |
| 5c115a03-b1f5-31c4-a5da-7f1ef6916c10 | -4.4602 | -46.4194 | 2025-11-07 00:30:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 72.1 |
| b8ed348f-6513-3113-9ff6-bb2bf3ae2050 | -2.9434 | -49.3655 | 2025-11-07 00:30:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 46.3 |
| 54e438a2-c776-3f35-b91c-1d04ba3de045 | 3.1094 | -60.765 | 2025-11-07 00:30:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 62.4 |
| a1d4bb4a-684f-3e2c-a156-1dec0b60a86b | -4.46 | -46.4416 | 2025-11-07 00:30:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 120.1 |
| 9c3d757d-7033-31f4-9546-de04758d5013 | -5.0868 | -44.7887 | 2025-11-07 00:30:00 | GOES-19 | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 61.4 |
| 3d7cd280-640d-3be8-9e0a-f7ac12910b90 | -4.4042 | -46.4445 | 2025-11-07 00:30:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 78.9 |
| 80714ef8-3b7c-3495-b117-884bea760475 | -4.4414 | -46.4425 | 2025-11-07 00:30:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 73.6 |
| ba1134d5-4b6c-353b-9563-a4072f942c05 | -2.9435 | -49.3443 | 2025-11-07 00:30:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 49.9 |
| 7fb8abf9-2459-3d2b-87b1-21d21ab40f65 | -4.7206 | -46.4276 | 2025-11-07 00:40:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 89.5 |
| 917edc5e-25e1-38c6-96dc-d2c9bf9758cd | -3.5252 | -47.5389 | 2025-11-07 00:40:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 50.9 |
| 45eddbfd-a69f-3e7d-b928-211145fd7f57 | -5.1054 | -44.7875 | 2025-11-07 00:40:00 | GOES-19 | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 66.2 |
| bd71626f-6c80-3bef-b6db-4087cf46191c | -5.0868 | -44.7887 | 2025-11-07 00:40:00 | GOES-19 | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 128.8 |
| 20491f2d-a6ac-3d37-9795-2b854e9def0b | -4.2961 | -45.8938 | 2025-11-07 00:40:00 | GOES-19 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 65.1 |
| a9afcd91-e0c7-3574-8713-1e5233c50970 | -4.2962 | -45.8715 | 2025-11-07 00:40:00 | GOES-19 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 59.9 |
| 237bfc95-f771-3ba9-b7a3-7ca637ff875b | -4.46 | -46.4416 | 2025-11-07 00:40:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 94.2 |
| cb7f97c8-1e54-3167-adeb-96e728ce42e2 | -5.0866 | -44.8115 | 2025-11-07 00:40:00 | GOES-19 | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 91.4 |
| 082664b3-7c67-372c-a5bf-363820dff13c | -4.4042 | -46.4445 | 2025-11-07 00:40:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 65.3 |
| 14adb1eb-e850-3780-926f-edd6621d2e14 | -4.4414 | -46.4425 | 2025-11-07 00:40:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 98.5 |
| bfac0e21-5ed3-3955-a3af-706fe62ea9d1 | -3.5901 | -49.4501 | 2025-11-07 00:40:00 | GOES-19 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 71.4 |
| 820f00cf-ab83-3072-a3fd-e20c20507188 | 3.1094 | -60.765 | 2025-11-07 00:40:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 65.2 |
| aa96a2ce-1af5-39bd-a70b-0f72b421c74a | -29.14994 | -55.00428 | 2025-11-07 00:47:00 | TERRA_M-M | SANTIAGO | RIO GRANDE DO SUL | Brasil | 4317400 | 43 | 33 | nan | nan | nan | Pampa | 18.0 |
| 91139078-f88a-3ccc-a614-c9dcac7e5493 | -23.43392 | -47.77806 | 2025-11-07 00:49:00 | TERRA_M-M | TATUÍ | SÃO PAULO | Brasil | 3554003 | 35 | 33 | nan | nan | nan | Mata Atlântica | 87.9 |
| a393ad66-09e6-3ebc-ab76-cab7ba697ea1 | -23.43595 | -47.79072 | 2025-11-07 00:49:00 | TERRA_M-M | TATUÍ | SÃO PAULO | Brasil | 3554003 | 35 | 33 | nan | nan | nan | Mata Atlântica | 7.7 |
| 4264d73b-fa3e-3419-96e6-feb54ad21d81 | -23.59882 | -49.01672 | 2025-11-07 00:49:00 | TERRA_M-M | ITAÍ | SÃO PAULO | Brasil | 3521804 | 35 | 33 | nan | nan | nan | Cerrado | 6.4 |
| c565d1c1-01da-3dcd-a190-fbb9e9ef97c0 | -19.33029 | -54.32076 | 2025-11-07 00:49:00 | TERRA_M-M | SÃO GABRIEL DO OESTE | MATO GROSSO DO SUL | Brasil | 5007695 | 50 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 75d5357d-5da2-393d-b684-43b78a2eaac7 | -5.0866 | -44.8115 | 2025-11-07 00:50:00 | GOES-19 | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 76.2 |
| 4f5cec12-db43-3e86-aeb3-adaf7b6808d1 | -5.0868 | -44.7887 | 2025-11-07 00:50:00 | GOES-19 | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 127.1 |
| cfeba81c-647a-332b-b72e-aaaaeb6435e3 | -4.7206 | -46.4276 | 2025-11-07 00:50:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 76.2 |
| 1d4cb7db-ae91-35ae-91d2-847a21ad6440 | -4.4414 | -46.4425 | 2025-11-07 00:50:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 69.0 |
| b6af601f-51a8-3b3e-941c-44a1cf291a5c | -5.1054 | -44.7875 | 2025-11-07 00:50:00 | GOES-19 | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 66.8 |
| b40a46ae-8849-3d58-b30a-a2d4cc647432 | -9.6261 | -36.0973 | 2025-11-07 00:50:00 | GOES-19 | PILAR | ALAGOAS | Brasil | 2706901 | 27 | 33 | nan | nan | nan | Mata Atlântica | 92.3 |
| b2e190b4-9798-3418-b11f-71b8b6d3a2ee | -4.46 | -46.4416 | 2025-11-07 00:50:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 97.9 |
| c67d5180-9252-3e55-bdcd-e9e45ee4d2ae | -4.2961 | -45.8938 | 2025-11-07 00:50:00 | GOES-19 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 51.8 |
| 2bf375d7-db7d-33b6-af02-0d473199aba0 | -3.7794 | -45.1556 | 2025-11-07 00:50:00 | GOES-19 | PIO XII | MARANHÃO | Brasil | 2108702 | 21 | 33 | nan | nan | nan | Amazônia | 51.5 |
| f9140b72-36c4-3a33-94f9-3f31680c63da | -14.97631 | -53.64278 | 2025-11-07 00:52:00 | TERRA_M-M | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 4.7 |


[Clique aqui para ver as próximas entradas](README2.md)
