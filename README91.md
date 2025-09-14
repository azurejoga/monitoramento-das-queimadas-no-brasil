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

## Dados Diários - Página 91

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 205d7ee8-5c85-39f6-85e0-f0fa683057a5 | -12.9294 | -54.7333 | 2025-09-14 14:30:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 709.5 |
| da01475a-af77-36d7-a6fe-24a58b22fd21 | -14.3285 | -46.1088 | 2025-09-14 14:30:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 220.1 |
| fed908c0-a139-3931-b77f-d094088f9ff0 | -8.9365 | -46.1545 | 2025-09-14 14:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 124.3 |
| a35ca2be-dcf2-3dd2-ad92-e42c06363f79 | -10.7661 | -50.5513 | 2025-09-14 14:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 73.9 |
| 40c83448-4a11-321e-9d68-d2412537da59 | -8.7683 | -46.0373 | 2025-09-14 14:30:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 134.8 |
| 8750c871-8cb8-3184-80d9-20f8c2478fe5 | -15.7786 | -53.482 | 2025-09-14 14:30:00 | GOES-19 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 88.6 |
| 63a7f7cf-63b8-3625-af60-cdc14b1421ee | -11.2698 | -51.093 | 2025-09-14 14:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 121.5 |
| 8179b293-e9ed-35d1-8b57-9d76e5eb3dfa | -11.43 | -50.5005 | 2025-09-14 14:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 75.6 |
| d1eb9021-1848-3dd7-bd7b-e1c102a4646c | -8.9079 | -45.457 | 2025-09-14 14:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 107.0 |
| 369ef827-b72a-38d7-addc-56f2085c513b | -11.5048 | -50.5775 | 2025-09-14 14:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 61.3 |
| b9855c5d-8b2b-3851-b734-d8d2fac76670 | -7.5269 | -44.3644 | 2025-09-14 14:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 90.8 |
| 5f7322af-b9a8-35bf-afef-966478bce6d8 | -10.7579 | -44.7721 | 2025-09-14 14:40:00 | GOES-19 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 175.8 |
| d08cfd4a-a885-34fc-b6a4-840f56e29256 | -9.019 | -47.0616 | 2025-09-14 14:40:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 87.9 |
| 3bee60ca-2b6f-3098-87f0-b6259ca16c73 | -12.9101 | -54.7558 | 2025-09-14 14:40:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 114.1 |
| 01b41cfa-eae9-316a-b1ef-19410d67ab73 | -8.9079 | -45.457 | 2025-09-14 14:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 184.2 |
| 2685f11c-f7bb-31c9-8739-00664c87a9c8 | -11.5263 | -50.404 | 2025-09-14 14:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 56.7 |
| 074c0b09-d5df-3712-8079-e5c9d0cd606b | -12.8019 | -47.1474 | 2025-09-14 14:40:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 87.4 |
| 0422fed2-b321-37b9-9b70-2c7c729b99f6 | -11.5616 | -50.5925 | 2025-09-14 14:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 57.2 |
| cfd29c73-3aaf-3b6f-885a-16f7bf3b9eed | -12.7634 | -47.153 | 2025-09-14 14:40:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 100.6 |
| 9fc9e815-cab9-3a36-8440-db6ac17ccc91 | -13.5879 | -51.6502 | 2025-09-14 14:40:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 97.9 |
| 10f064ea-8e25-3071-8cdc-d75e34c42f53 | -10.5451 | -51.5476 | 2025-09-14 14:40:00 | GOES-19 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 76.2 |
| 95ea1c5b-1e5c-381a-8969-20455f22a6f9 | -11.1149 | -51.3423 | 2025-09-14 14:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 86.7 |
| 85f1725b-5756-32f2-b97a-66d0e250c8c7 | -10.3699 | -50.507 | 2025-09-14 14:40:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 76.9 |
| 89f263c6-253c-3c0a-9bba-70d05805272f | -9.8835 | -50.1933 | 2025-09-14 14:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 63.4 |
| 1444f0b5-21ac-3595-8298-83a550eb38db | -8.8893 | -45.4363 | 2025-09-14 14:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 106.3 |
| 5c310325-3b5c-3369-97c2-8e842b4db45e | -12.9292 | -54.7538 | 2025-09-14 14:40:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 263.8 |
| 64ea4dfb-7259-3c41-8251-dfce0be3f039 | -12.9103 | -54.7352 | 2025-09-14 14:40:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 188.0 |
| 18541c56-8465-33a7-a7e1-3b40474333fc | -15.7591 | -53.4846 | 2025-09-14 14:40:00 | GOES-19 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 85.5 |
| 7d2fa0f6-2f04-3154-9959-a044e48d5674 | -14.3285 | -46.1088 | 2025-09-14 14:40:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 203.4 |
| d13955b4-44ff-3e1c-9c03-7344a5b4a871 | -8.9976 | -45.8098 | 2025-09-14 14:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 90.8 |
| 1ef49eb3-2f9d-3cea-9728-cbdbb22b42f2 | -9.9754 | -50.3761 | 2025-09-14 14:40:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 70.8 |
| 0589dd85-9abb-3254-ae4e-b6e4c6dc54b3 | -8.7871 | -46.0353 | 2025-09-14 14:40:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 112.3 |
| 434fbf8a-072d-3eac-83f9-8dcb94dac7c4 | -10.5482 | -49.8899 | 2025-09-14 14:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 72.3 |
| 7ade8bd0-b457-34d8-b50a-09a3e8b978f5 | -11.4285 | -43.5544 | 2025-09-14 14:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 139.5 |
| e5bbd95a-0345-39b9-ba84-4b8efd02c486 | -12.7671 | -48.0236 | 2025-09-14 14:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 113.0 |
| da962cde-249e-31e4-adf5-382eacd12bb9 | -11.43 | -50.5005 | 2025-09-14 14:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 62.4 |
| 3501f530-e8a3-3161-824e-4fd872d9b42c | -8.4334 | -47.2306 | 2025-09-14 14:40:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 94.8 |
| b91872d6-7c11-3b92-bc24-c232ff1d6ebb | -14.394 | -52.9245 | 2025-09-14 14:40:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 64.4 |
| 7bc7ebda-065e-3fa1-a0a0-fa72a9bb3946 | -8.4143 | -47.2545 | 2025-09-14 14:40:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 74.5 |
| b3d14ed1-5268-33cd-8ae7-04a6343c6e91 | -10.5586 | -51.9661 | 2025-09-14 14:40:00 | GOES-19 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 118.0 |
| fdcfdc0a-c6df-3de6-bca7-4ad4ff8a5172 | -10.0506 | -50.39 | 2025-09-14 14:40:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 63.7 |
| 69d16d91-7d20-3e4f-b704-de37119e4b67 | -12.9482 | -54.7519 | 2025-09-14 14:40:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 92.6 |
| 48ed3b38-1a27-3813-9c5a-26633d742124 | -6.1065 | -47.8368 | 2025-09-14 14:40:00 | GOES-19 | CACHOEIRINHA | TOCANTINS | Brasil | 1703826 | 17 | 33 | nan | nan | nan | Cerrado | 71.9 |
| 8f84af42-f95b-33ab-b19f-d00d02ce5601 | -8.7683 | -46.0373 | 2025-09-14 14:40:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 151.5 |
| 295edd92-f324-38e3-8ac7-85750bd053b6 | -10.3512 | -50.4876 | 2025-09-14 14:40:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 105.7 |
| 5963ec85-c67c-3562-ac78-32cde3b7f65f | -8.4331 | -47.2527 | 2025-09-14 14:40:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 73.6 |
| b185db5d-0ed4-360e-ab36-47ac1c6260c1 | -11.3831 | -47.3429 | 2025-09-14 14:40:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 122.0 |
| f16367c5-1615-30e6-8a3a-6641e5713523 | -12.7675 | -48.0013 | 2025-09-14 14:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 106.1 |
| a9f8d1cc-05d0-3fb6-8f03-f7ede3dc49c8 | -9.9943 | -50.3742 | 2025-09-14 14:40:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 71.6 |
| e4caf858-92a2-3402-b113-0c842147bef7 | -11.4477 | -43.5514 | 2025-09-14 14:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 157.9 |
| 461d1de8-a81a-3ef4-ae51-3c41e6274f39 | -11.4453 | -50.7549 | 2025-09-14 14:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 64.9 |
| bf0deab3-18b2-34fa-be9a-32f55eae45d8 | -10.9096 | -47.2023 | 2025-09-14 14:40:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 155.9 |
| 9490929b-5cc8-39d3-ab9f-d1613398c676 | -14.4137 | -52.901 | 2025-09-14 14:40:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 65.3 |
| 2ec86d7d-3c81-3eba-94dc-9d02501cb0d4 | -10.3885 | -50.5264 | 2025-09-14 14:40:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 76.9 |
| 5ed5c13d-49bd-349b-8be7-540339735292 | -10.3509 | -50.5089 | 2025-09-14 14:40:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 78.2 |
| cf449619-d7c4-3811-80bb-6c7144766ba4 | -7.5985 | -44.679 | 2025-09-14 14:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 54.4 |
| 26defbfe-94ab-3d1c-a06a-35f843a53283 | -15.1995 | -50.1101 | 2025-09-14 14:40:00 | GOES-19 | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 62.1 |
| b15babf3-c44d-38a7-8c98-e96044495457 | -8.9076 | -45.4797 | 2025-09-14 14:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 159.2 |
| d64382dc-b494-38f8-9f6a-dce1f26768fa | -15.7786 | -53.482 | 2025-09-14 14:40:00 | GOES-19 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 88.2 |
| 842e1f6f-58a9-3062-b2e7-a95e79db1f3b | -11.5048 | -50.5775 | 2025-09-14 14:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 65.2 |
| 74b6d8df-8746-3e47-a238-6b8158d1d166 | -11.4665 | -43.5722 | 2025-09-14 14:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 111.2 |
| 62a34676-efe9-3faa-a80b-3b33c602a211 | -14.3747 | -52.927 | 2025-09-14 14:40:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 118.9 |
| 642c7048-3fe6-30ce-bd0f-edb59b06d07d | -15.2069 | -52.8613 | 2025-09-14 14:40:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 76.6 |
| 83f64301-5eea-3f1b-9f89-0bc83c956f33 | -11.5235 | -50.5968 | 2025-09-14 14:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 73.2 |
| 0ffa90f1-1351-3363-a72a-4d12c84b7dc8 | -8.9173 | -46.179 | 2025-09-14 14:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 384.0 |
| b6e9493e-f660-3fe8-8c34-0fd93c311738 | -8.9362 | -46.177 | 2025-09-14 14:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 292.0 |
| 4d4daf8d-d636-350a-acad-193ddccb6f34 | -9.8644 | -50.2165 | 2025-09-14 14:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 62.7 |
| 8a6bfcf2-f30e-3a72-a883-b71248a8a604 | -11.6945 | -50.5988 | 2025-09-14 14:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 72.9 |
| ccc53ff7-3c5e-3023-9f1d-0543ac3402f4 | -8.9979 | -45.7871 | 2025-09-14 14:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 107.2 |
| c2951607-c891-3cc5-beee-c0df054a7dae | -11.0959 | -51.3443 | 2025-09-14 14:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 81.2 |
| 17f92c87-6dda-3316-bb0d-428e1840795a | -14.4779 | -47.3368 | 2025-09-14 14:40:00 | GOES-19 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 178.3 |
| 9a6b9a28-4550-36ad-bab7-ed872c017e63 | -13.5876 | -51.6715 | 2025-09-14 14:40:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 84.0 |
| 84441f15-6e8a-3357-967a-63950d1c7f11 | -14.3554 | -52.9294 | 2025-09-14 14:40:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 53.6 |
| 284ce1aa-c8b1-3beb-ab9d-c288e720353f | -15.1991 | -50.132 | 2025-09-14 14:40:00 | GOES-19 | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 43.6 |
| 94e4fa28-c4d2-3c92-9707-f610ea24617b | -10.3696 | -50.5283 | 2025-09-14 14:40:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 86.0 |
| 73b55907-ba69-34cc-993e-274e0a7d9a84 | -9.8646 | -50.1951 | 2025-09-14 14:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 86.1 |
| 72b24648-510d-3654-be2e-f0f1f9ea3dad | -10.3507 | -50.5303 | 2025-09-14 14:40:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 67.2 |
| 4cd77b17-6df3-3bff-8579-94f8669f5215 | -8.9368 | -46.132 | 2025-09-14 14:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 117.3 |
| e1476cfa-77a5-3c8e-b98b-628805b328b4 | -11.3886 | -50.7399 | 2025-09-14 14:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 68.2 |
| 83505f92-2606-3aa8-be17-d8ef0d7be9d3 | -9.9946 | -50.3529 | 2025-09-14 14:40:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 67.5 |
| 7dae1793-5e6f-36ff-9437-925e68337809 | -15.18 | -50.113 | 2025-09-14 14:40:00 | GOES-19 | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 61.9 |
| 5e6e653e-1e80-3c24-b014-43fe755fe48c | -15.0477 | -47.9856 | 2025-09-14 14:40:00 | GOES-19 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 60.3 |
| 978090ea-3ef1-3d7a-a42b-2a2afaf3e580 | -10.75 | -46.4607 | 2025-09-14 14:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 112.3 |
| d39d156a-88a4-3326-88ea-85d300f50978 | -11.5037 | -43.6373 | 2025-09-14 14:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 113.8 |
| 2046380f-091e-3f5d-bd0f-5062510a4cdb | -11.4473 | -46.9097 | 2025-09-14 14:40:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 77.1 |
| 3a404acb-eab3-32f9-8315-2b07792193cb | -7.8995 | -46.2805 | 2025-09-14 14:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 56.8 |
| c167226c-6638-33e6-af03-25e55334769b | -8.9176 | -46.1565 | 2025-09-14 14:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 123.6 |
| 30b411ba-0225-38a0-8f08-3dba43d88410 | -11.7215 | -46.49 | 2025-09-14 14:40:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 209.6 |
| facaf0a4-a522-33d0-8141-79938ee5184d | -8.8984 | -46.181 | 2025-09-14 14:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 181.3 |
| 9af1efb8-f1cd-3697-9caa-e60b5d2a5853 | -11.7323 | -51.9305 | 2025-09-14 14:40:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 91.4 |
| 0bef6b75-0175-3c87-95a7-06d48b73c011 | -11.1146 | -51.3634 | 2025-09-14 14:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 65.2 |
| f2aa96ff-e327-375b-a73a-389112d6d7f4 | -11.7024 | -46.4927 | 2025-09-14 14:40:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 162.8 |
| b45f6e35-1ae4-3399-bf19-3eca4d730ea0 | -11.4661 | -43.5959 | 2025-09-14 14:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 119.3 |
| 1434370d-05c2-38d5-b135-0b39660e6bd6 | -8.6404 | -45.7122 | 2025-09-14 14:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 100.2 |
| c1b65805-5197-39dc-be88-40ef8a0c9e87 | -8.979 | -45.7892 | 2025-09-14 14:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 85.1 |
| 6097c31f-9172-3a67-b29d-dfd1e3cb3cb0 | -11.364 | -47.3454 | 2025-09-14 14:40:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 83.8 |
| 0819b187-9f6d-326c-81da-2fb61eaad7fd | -15.943 | -47.2407 | 2025-09-14 14:40:00 | GOES-19 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 141.1 |
| 8dce2fc1-6e94-3f41-816a-d873290b9e2a | -14.329 | -46.0857 | 2025-09-14 14:40:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 378.3 |
| 3516dee2-6544-3864-9436-ed9d514a31f7 | -11.0178 | -51.5212 | 2025-09-14 14:40:00 | GOES-19 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Cerrado | 87.5 |
| aa2cd8ca-9e08-30c1-8683-c6988daeb47c | -9.0193 | -47.0394 | 2025-09-14 14:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 96.4 |


