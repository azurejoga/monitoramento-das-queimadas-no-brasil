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

## Dados Diários - Página 17

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c6aa8906-5cb0-38f3-ba1d-97d79ac66f19 | -8.9491 | -45.202 | 2026-08-04 14:30:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 187.4 |
| 95453260-a721-36bb-a073-420a02b1dd82 | -6.5514 | -55.1569 | 2026-08-04 14:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 81.1 |
| 4e5a5236-cd8e-3225-9c5b-25cbb27f419b | -4.3874 | -43.3827 | 2026-08-04 14:30:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 74.3 |
| 4c60163d-529c-3a0f-bb3e-d0326d887c2f | -10.8121 | -65.091 | 2026-08-04 14:30:00 | GOES-19 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 79.1 |
| 026b21ad-5859-36ab-8955-466ab72413a9 | -8.9302 | -45.2041 | 2026-08-04 14:30:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 117.3 |
| 6173d618-15c1-3ce1-b81f-8f3059605345 | -6.5699 | -55.156 | 2026-08-04 14:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 80.0 |
| 7bbf9221-f17c-3840-8283-be8de9564f3c | -3.6638 | -49.4898 | 2026-08-04 14:40:00 | GOES-19 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 72.1 |
| 884e562f-b665-3843-85cd-6daaaddfdff6 | -3.6639 | -49.4686 | 2026-08-04 14:40:00 | GOES-19 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 125.5 |
| 1ea227ec-341a-36e5-9099-fc67cd2b8705 | -10.8121 | -65.091 | 2026-08-04 14:40:00 | GOES-19 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 57.7 |
| c297984d-f78e-3f21-9e97-90597e253fd2 | -11.1279 | -50.4057 | 2026-08-04 14:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 93.9 |
| 6070b7f7-05b9-3d36-9c44-b78928090aa2 | -11.1282 | -50.3843 | 2026-08-04 14:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 70.0 |
| bebeba28-e131-3bdc-8a98-5d5ed8ac0e3c | -10.8308 | -65.0902 | 2026-08-04 14:40:00 | GOES-19 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 79.7 |
| 35bf60a8-4093-3d12-b3a8-f693c8fe5417 | -6.5699 | -55.156 | 2026-08-04 14:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 113.2 |
| d9208aef-ac52-31f2-9110-dfb4240456de | -6.5514 | -55.1569 | 2026-08-04 14:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 82.6 |
| 189413cf-5f79-31e0-95d0-87a794d23b1b | -8.3544 | -45.9897 | 2026-08-04 14:40:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 58.3 |
| 74fcdaa3-3573-3e94-82b2-c29fa9607ad8 | -4.3874 | -43.3827 | 2026-08-04 14:40:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 93.7 |
| cd21c50a-6a8c-3b41-9006-530038a7998d | -10.8121 | -65.091 | 2026-08-04 14:50:00 | GOES-19 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 81.9 |
| 54b3d790-8fb7-3db3-9558-550b6fcd64f7 | -8.3544 | -45.9897 | 2026-08-04 14:50:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 66.2 |
| 8a4c6cb6-ed28-320f-96ba-d6965cdeb5ee | -4.3687 | -43.3838 | 2026-08-04 14:50:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 87.8 |
| 9a21abb4-71b9-30c5-a1bb-b4c3b68b6ee3 | -11.9269 | -55.9077 | 2026-08-04 14:50:00 | GOES-19 | IPIRANGA DO NORTE | MATO GROSSO | Brasil | 5104526 | 51 | 33 | nan | nan | nan | Amazônia | 66.8 |
| c4e50ea2-cb07-3244-937b-a6f813abe62a | -6.5699 | -55.156 | 2026-08-04 14:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 108.4 |
| c3fb6993-d932-3da2-bd8d-3cf2f0b3defd | -3.6824 | -49.4679 | 2026-08-04 14:50:00 | GOES-19 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 88.3 |
| fa130cbc-f114-3476-aa9b-662cca71d60a | -12.1184 | -45.6827 | 2026-08-04 14:50:00 | GOES-19 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 72.1 |
| 6a4373fc-3adf-3d3a-a97d-3b643103f45f | -3.6639 | -49.4686 | 2026-08-04 14:50:00 | GOES-19 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 111.6 |
| 49c60d4b-dbdd-38f3-81da-2a4b8d2bb71e | -11.1282 | -50.3843 | 2026-08-04 14:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 81.7 |
| 708a2107-18c3-39ba-aa6c-5b203a5c23af | -6.5514 | -55.1569 | 2026-08-04 14:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 99.6 |
| cea8520a-93af-3d9c-b65c-0ddac53fbbed | -10.8121 | -65.091 | 2026-08-04 15:00:00 | GOES-19 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 102.9 |
| 8f87ff26-9911-3140-84c1-bde8491fc625 | -3.6824 | -49.4679 | 2026-08-04 15:00:00 | GOES-19 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 100.7 |
| 04ebdeb7-f36c-328e-9527-3c97186103ac | -6.5329 | -55.1578 | 2026-08-04 15:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 58.8 |
| d80e9e0f-b747-3683-a822-cee34dcccdb4 | -11.9269 | -55.9077 | 2026-08-04 15:00:00 | GOES-19 | IPIRANGA DO NORTE | MATO GROSSO | Brasil | 5104526 | 51 | 33 | nan | nan | nan | Amazônia | 66.4 |
| 141924dc-a9e8-3cba-a07e-5d5875a03ad4 | -3.6639 | -49.4686 | 2026-08-04 15:00:00 | GOES-19 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 116.3 |
| e7e3b85d-35ff-33a7-8564-d5ca6ebf034e | -6.5514 | -55.1569 | 2026-08-04 15:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 118.3 |
| 43cfb683-5ebf-303e-8318-e6a95beeb573 | -6.5512 | -55.1769 | 2026-08-04 15:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 56.7 |
| a2ee174e-0795-3400-82b7-97eb2a79e5dc | -11.1282 | -50.3843 | 2026-08-04 15:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 74.5 |
| bd89edd5-5c98-31d0-ac1e-a761e5402352 | -10.0517 | -46.1861 | 2026-08-04 15:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 88.6 |
| 487802ec-c6f0-307a-96fd-32a1b9b027c8 | -6.5699 | -55.156 | 2026-08-04 15:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 115.6 |
| 66231740-184f-3542-92ef-0489f30d2d03 | -11.9269 | -55.9077 | 2026-08-04 15:10:00 | GOES-19 | IPIRANGA DO NORTE | MATO GROSSO | Brasil | 5104526 | 51 | 33 | nan | nan | nan | Amazônia | 139.8 |
| 5a4a01fb-cf58-3efa-8b78-5729fd24b725 | -6.5329 | -55.1578 | 2026-08-04 15:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 76.4 |
| 3ed7e444-7829-373a-bc62-559aff317b54 | -4.3687 | -43.3838 | 2026-08-04 15:10:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 93.3 |
| 9362e7b6-cfdd-3859-a905-25c8961f217c | -10.144 | -46.3553 | 2026-08-04 15:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 77.6 |
| 753c52b1-b583-3cec-98f5-4618ebc51a4b | -3.6639 | -49.4686 | 2026-08-04 15:10:00 | GOES-19 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 112.2 |
| bf341bb8-8edd-3c30-aed7-1353d7090e31 | -11.1282 | -50.3843 | 2026-08-04 15:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 77.8 |
| 255e8bfa-d4b8-316e-8e56-f83f0d4cd2e7 | -6.5699 | -55.156 | 2026-08-04 15:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 128.3 |
| 3dcf0e06-9e70-31e9-a35f-4c150f56a592 | -5.886 | -52.3331 | 2026-08-04 15:10:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 100.4 |
| 0c39a98c-40dc-3e3a-946c-25db58117b1f | -6.5514 | -55.1569 | 2026-08-04 15:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 147.2 |
| f0a1b460-6ebe-37a8-82a6-8b8e6fc04f5f | -3.6824 | -49.4679 | 2026-08-04 15:10:00 | GOES-19 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 92.7 |
| 0c8feab6-2c60-38aa-a039-b2b5bb73a720 | -6.5512 | -55.1769 | 2026-08-04 15:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 59.0 |
| 304a3375-5e2e-3d40-bab7-27f7b55342fc | -4.3874 | -43.3827 | 2026-08-04 15:10:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 77.3 |
| 6274e473-a924-3b82-8402-c4f7dfc62f9c | -3.0256 | -43.2874 | 2026-08-04 15:10:00 | GOES-19 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 75.5 |
| 45a4f837-75d7-3242-948b-a7498362d5c1 | -11.9079 | -55.9093 | 2026-08-04 15:10:00 | GOES-19 | IPIRANGA DO NORTE | MATO GROSSO | Brasil | 5104526 | 51 | 33 | nan | nan | nan | Amazônia | 76.0 |
| 54c0fa99-cfea-3c4d-a5fc-8b95e632ebaa | -6.5699 | -55.156 | 2026-08-04 15:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 148.5 |
| 81bfc5bc-6115-32ff-b254-b37a2c7c2a41 | -6.5512 | -55.1769 | 2026-08-04 15:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 61.8 |
| 2c17b011-10af-3ff6-87e5-584b54155519 | -11.9269 | -55.9077 | 2026-08-04 15:20:00 | GOES-19 | IPIRANGA DO NORTE | MATO GROSSO | Brasil | 5104526 | 51 | 33 | nan | nan | nan | Amazônia | 113.0 |
| bbe5f2d4-7a2a-391d-8822-ca0af5b53bfe | -3.6639 | -49.4686 | 2026-08-04 15:20:00 | GOES-19 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 116.4 |
| 26d87c60-08f8-3822-aa6a-07bad07360c6 | -5.886 | -52.3331 | 2026-08-04 15:20:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 90.3 |
| 2a08d441-c948-35f9-ba16-14a1ad9735cf | -10.1634 | -46.3304 | 2026-08-04 15:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 82.1 |
| 5bf3032a-ce5a-3ea1-863f-bacb4211935f | -6.57 | -55.136 | 2026-08-04 15:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 62.8 |
| 336c6602-8a0c-359f-a2b4-3d1fb89d288e | -6.5514 | -55.1569 | 2026-08-04 15:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 153.6 |
| bbcd0e29-b345-39ae-8f8d-3a83370344b0 | -8.3544 | -45.9897 | 2026-08-04 15:20:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 69.5 |
| 9dcd097e-146e-3ce4-9c6d-19471edc12cf | -11.5485 | -47.7218 | 2026-08-04 15:20:00 | GOES-19 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 79.8 |
| 6099ddef-17a4-32be-885a-c3b83f6bd9c9 | -10.0704 | -46.2064 | 2026-08-04 15:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 74.1 |
| 9adfabb8-8feb-3931-a3e8-72a6c32a07ef | -6.5329 | -55.1578 | 2026-08-04 15:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 87.4 |
| 611651d2-e480-3468-891e-923f5474dfc2 | -7.0784 | -62.9878 | 2026-08-04 15:30:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 50.8 |
| bf332cfe-5897-3854-9b39-00bee98da1a7 | -3.6638 | -49.4898 | 2026-08-04 15:30:00 | GOES-19 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 73.1 |
| 4dfe17fc-839b-3d95-8a8a-a244ec476a08 | -6.5512 | -55.1769 | 2026-08-04 15:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 58.9 |
| 1bfbe209-1606-3bae-847b-39d67b0f3d64 | -5.886 | -52.3331 | 2026-08-04 15:30:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 62.1 |
| 1766e04d-6da8-3b2b-9444-2770a91189f3 | -10.0517 | -46.1861 | 2026-08-04 15:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 97.8 |
| ab4401bb-5908-37f1-82ef-14b387110145 | -3.6639 | -49.4686 | 2026-08-04 15:30:00 | GOES-19 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 149.0 |
| 5af380af-6db2-3a00-a296-ff195fa38599 | -11.9269 | -55.9077 | 2026-08-04 15:30:00 | GOES-19 | IPIRANGA DO NORTE | MATO GROSSO | Brasil | 5104526 | 51 | 33 | nan | nan | nan | Amazônia | 92.3 |
| c1d6c9e4-cfd2-3e3c-b704-e7de42149829 | -8.3544 | -45.9897 | 2026-08-04 15:30:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 68.8 |
| f9025ffa-dd1a-3ca0-a41e-5b472a1803b8 | -14.3516 | -53.1612 | 2026-08-04 15:40:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 157.2 |
| b52ca188-819c-34de-9a17-4eead1c13c3b | -3.6639 | -49.4686 | 2026-08-04 15:40:00 | GOES-19 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 183.1 |
| 72869c84-89b8-3de9-ab32-5dcf7682193d | -8.3544 | -45.9897 | 2026-08-04 15:40:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 63.2 |
| bf9c6a1d-591d-34a7-899b-96cc4c8934b9 | -6.5329 | -55.1578 | 2026-08-04 15:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 92.5 |
| cfa04791-378d-366a-9aac-1769a06d1882 | -11.9269 | -55.9077 | 2026-08-04 15:40:00 | GOES-19 | IPIRANGA DO NORTE | MATO GROSSO | Brasil | 5104526 | 51 | 33 | nan | nan | nan | Amazônia | 108.8 |
| 5b29039c-226a-3ddd-bb56-9f065ab0ff54 | -4.3874 | -43.3827 | 2026-08-04 15:40:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 75.0 |
| 1731509b-7072-3cd0-b778-fdce8db5b502 | -6.57 | -55.136 | 2026-08-04 15:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 50.0 |
| 184650be-aa3e-36e6-bf1b-6eb358c97177 | -3.6638 | -49.4898 | 2026-08-04 15:40:00 | GOES-19 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 102.1 |
| ae8b981b-95e6-335a-a413-68e4e8979a9c | -3.6824 | -49.4679 | 2026-08-04 15:40:00 | GOES-19 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 108.2 |
| cf696faf-96b1-3cf4-877f-42028602d69a | -14.352 | -53.1402 | 2026-08-04 15:40:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 170.3 |


