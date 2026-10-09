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

## Dados Diários - Página 139

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a5d2c6ee-3e75-3461-8043-a82e4c4a0fb8 | -2.88271 | -54.19968 | 2026-10-09 05:04:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7f825dd4-9725-321c-ac3d-0b3a3c3c84b8 | -3.01585 | -54.04567 | 2026-10-09 05:04:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 92612f77-b3fa-3b5d-8681-8307055bfab3 | -3.02383 | -58.94005 | 2026-10-09 05:04:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e319cd0b-0a04-31e6-9c2f-35ab05400ae6 | -2.89847 | -57.21175 | 2026-10-09 05:04:00 | NPP-375D | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 04a3e399-ac24-31d9-bab7-2aace7de51cc | -3.89624 | -58.9598 | 2026-10-09 05:04:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ca2e80ea-b6d9-3ad5-a6b8-4061083c26a4 | -11.65945 | -43.69288 | 2026-10-09 05:04:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7f485ee5-d4cd-3ba5-ac2c-bfdb15055455 | -11.46734 | -43.38582 | 2026-10-09 05:04:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 631c794a-895c-3506-b139-29c27f058066 | -3.1804 | -54.7468 | 2026-10-09 05:04:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c183d3b7-7c71-3b01-8551-0f3ebd6af46d | -11.82955 | -43.59735 | 2026-10-09 05:04:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 19.1 |
| 498e2ca2-13ca-3857-be1a-a16acb7c244c | -11.40572 | -47.59081 | 2026-10-09 05:04:00 | NPP-375D | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| daac8885-1c76-30e7-844c-cf3a08437f82 | -6.12528 | -55.68116 | 2026-10-09 05:04:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 75f23e7c-cee9-3d74-bb16-90cc1f09aa8d | -2.91863 | -54.13373 | 2026-10-09 05:04:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 5f65df32-85e7-32c4-bd60-1a4068868a8e | -8.72688 | -45.14715 | 2026-10-09 05:04:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 4b283384-76fc-3560-822d-e79785b7dee7 | -3.10556 | -53.95436 | 2026-10-09 05:04:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 2bc9672b-2359-30b2-a6b4-2b7953ec050f | -9.61467 | -55.07733 | 2026-10-09 05:04:00 | NPP-375D | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c78e89fd-f26b-327c-b93e-78e462272574 | -10.28933 | -46.60584 | 2026-10-09 05:04:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| bed54c86-95f0-3150-aa79-f398b43154c8 | -3.78931 | -50.79747 | 2026-10-09 05:04:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d68716b3-8e4f-3017-b14f-bd44b63f11ce | -6.49202 | -55.29502 | 2026-10-09 05:04:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 6176ec95-ba59-32f5-89a9-60fca344b1ad | -2.58587 | -56.17493 | 2026-10-09 05:04:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 40a1e76e-c6cb-34fc-b08e-59491cf8d0f7 | -3.05877 | -53.9352 | 2026-10-09 05:04:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 31aebf38-95d9-3dcf-9a0e-1ebd66b4be14 | -3.1103 | -53.76962 | 2026-10-09 05:04:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 30199e6a-ed27-3ae8-836d-0b1c52885aab | -5.09957 | -46.22051 | 2026-10-09 05:04:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 6895e27b-e1c9-36b3-99ac-c4820e7e921a | -3.0362 | -54.27541 | 2026-10-09 05:04:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| eb2412c4-298e-3e36-a9cc-96716be7bca9 | -3.11255 | -53.77765 | 2026-10-09 05:04:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| affb678d-7271-3a11-8ef6-99e122d64b2a | -3.56473 | -54.67249 | 2026-10-09 05:04:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| a987b5a0-b085-3e9c-be19-8928805bb3d0 | -5.70467 | -53.47193 | 2026-10-09 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a790acfe-2bf4-3e10-aa0e-d5edff371b38 | -9.10268 | -48.80602 | 2026-10-09 05:04:00 | NPP-375D | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 94afb16d-181a-33b8-a875-301311bfd271 | -6.39008 | -55.258 | 2026-10-09 05:04:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| ad19cfaa-d30c-3d5f-854e-8720debc9207 | -3.59727 | -54.30899 | 2026-10-09 05:04:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9993f19e-4cf4-3d25-b742-82978b152eb5 | -9.806 | -44.7729 | 2026-10-09 05:04:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3134f467-7473-3a78-8038-875923432ed7 | -6.48946 | -62.85183 | 2026-10-09 05:04:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 99e525fe-1d52-3479-90d9-73587befd5f4 | -8.91385 | -45.23215 | 2026-10-09 05:04:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 7e85f444-921d-3cbb-a728-3fe0205cc25e | -11.40895 | -46.68493 | 2026-10-09 05:04:00 | NPP-375D | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 3007c6a3-8e61-36a2-9369-50ea98972c82 | -4.57612 | -54.95192 | 2026-10-09 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| fbddd58f-c917-355b-9c25-067951fd2b61 | -11.19311 | -45.32317 | 2026-10-09 05:04:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 2979e768-586d-3c54-84fd-690612b1a208 | -10.29326 | -46.61121 | 2026-10-09 05:04:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| ec00fc9b-fab9-3f25-9844-7259179239c5 | -3.01872 | -54.05006 | 2026-10-09 05:04:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0f2f503b-5b53-368c-ba92-618d7e3138d7 | -9.30013 | -47.42868 | 2026-10-09 05:04:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 78fa0e5c-8508-3fd7-aea9-b182fc7549eb | -11.76354 | -44.95196 | 2026-10-09 05:04:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 04c62a84-d217-3b56-900b-116edc6de45c | -8.83606 | -61.46401 | 2026-10-09 05:04:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 79cafecb-fbed-3730-b2a5-d8d1c279d99d | -3.85597 | -51.9407 | 2026-10-09 05:04:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6c32285d-55c4-3171-9b80-6e310fd6ee5a | -5.61617 | -44.83857 | 2026-10-09 05:04:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 7e4d33ad-4eb6-37c5-87e1-17ae63012068 | -2.6317 | -57.72081 | 2026-10-09 05:04:00 | NPP-375D | URUCARÁ | AMAZONAS | Brasil | 1304302 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b9c60a94-31a3-3691-9a99-ad7c542dcfe9 | -4.2003 | -55.63429 | 2026-10-09 05:04:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| cf358fde-f20d-30ab-9d4d-18f37a4daff7 | -4.22288 | -46.93343 | 2026-10-09 05:04:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a429d3f7-7617-3898-8f9b-9932c4605085 | -9.27776 | -47.43357 | 2026-10-09 05:04:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 145413e9-9c32-3487-aab6-8caf848d4df0 | -5.698 | -53.46391 | 2026-10-09 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 89f3bda7-f98c-31b4-807e-dc24c2362f8c | -4.46232 | -55.40178 | 2026-10-09 05:04:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fba43823-bac7-3efa-be73-4cc93aaef80e | -2.56477 | -56.15638 | 2026-10-09 05:04:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 777a3f97-2570-3945-a097-ca742716af99 | -6.4772 | -53.68303 | 2026-10-09 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 34e56303-b5bf-3d66-a572-12b2cfc55214 | -6.92081 | -44.56526 | 2026-10-09 05:04:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 89615add-3fe7-356c-b058-a1014e65f3e0 | -5.69913 | -53.45684 | 2026-10-09 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 80137275-7804-377e-82f5-0cf42f9d1dc7 | -3.90634 | -55.89376 | 2026-10-09 05:04:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 33eca2db-0326-3f49-90e8-9365c8bf7751 | -3.55019 | -54.69482 | 2026-10-09 05:04:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| f4fc16a8-e97d-397b-bae9-1edd572045b1 | -3.00413 | -54.11568 | 2026-10-09 05:04:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 10f04f45-f125-39de-9050-b6862062e1fa | -2.9349 | -54.14428 | 2026-10-09 05:04:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| aa4b42a6-a13c-31b3-bfd4-d943e8a7402c | -5.87511 | -53.62332 | 2026-10-09 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a712f456-67d2-3c08-9f7b-0a393475e156 | -4.12084 | -53.80831 | 2026-10-09 05:04:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 32aa5a4c-f4c6-3e7c-ae1a-400676de0a08 | -3.08192 | -54.3946 | 2026-10-09 05:04:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 36d089fe-c5d0-30df-aac2-8bbe3cddc7ea | -3.08002 | -53.95807 | 2026-10-09 05:04:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f42ede2e-bfae-3baf-92d2-082dcfed8a5c | -7.89361 | -55.00586 | 2026-10-09 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 37387d92-3128-3738-bc7e-079861d544d3 | -3.02745 | -54.10662 | 2026-10-09 05:04:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ed78c8ab-2aff-30a4-8196-f088f50f30b1 | -3.01538 | -54.2478 | 2026-10-09 05:04:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a551ffb1-7bc8-3b3f-9ea1-481cebc8b160 | -6.21987 | -52.79877 | 2026-10-09 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f9d164f2-e2e5-3d32-be47-d6538e4741ad | -6.00934 | -52.07799 | 2026-10-09 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2c5d787a-a7cc-3e0d-9ac1-159c2236ffbc | -11.65386 | -43.67533 | 2026-10-09 05:04:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 131a73fc-ee36-332d-adf1-338f30d35ec2 | -10.86602 | -45.53366 | 2026-10-09 05:04:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 2f1baf3c-f68c-38ef-a260-5a4cd0505fc3 | -6.23871 | -52.88713 | 2026-10-09 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2deaaadc-58c7-3278-9939-1b5e62c5ac7d | -11.00172 | -47.47503 | 2026-10-09 05:04:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4992b365-1c44-3573-a7fa-685648ae94ed | -5.24072 | -60.19274 | 2026-10-09 05:04:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ddf1d336-012a-345e-bf92-7aa34b31b15b | -2.97612 | -54.11124 | 2026-10-09 05:04:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 53f7821b-e710-3eae-a849-c41a00c9cf23 | -4.12265 | -59.87734 | 2026-10-09 05:04:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2e978ee7-a432-3c77-96aa-c65660ac8c8e | -3.4664 | -60.24945 | 2026-10-09 05:04:00 | NPP-375D | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bcc719fc-6a93-3c61-a771-f904842f4d16 | -4.29917 | -60.01317 | 2026-10-09 05:04:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 88d31ec4-4d4f-39ef-95ed-096f5c595302 | -3.10892 | -54.16237 | 2026-10-09 05:04:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6eaae29d-fc06-3de0-bee7-915c602898df | -3.29749 | -54.08503 | 2026-10-09 05:04:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 70378954-7ade-3d45-af38-f5ea54c1c560 | -4.11217 | -54.62703 | 2026-10-09 05:04:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| c3b86ee2-f218-31f1-bf3a-d9882f1ac478 | -6.49001 | -55.30705 | 2026-10-09 05:04:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 112fae3d-5b63-3d13-b9f1-5d1151fc2b4c | -5.95807 | -55.36161 | 2026-10-09 05:04:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| ead020f1-553f-3e5c-a2ab-83af26d6be7c | -6.82322 | -50.80608 | 2026-10-09 05:04:00 | NPP-375D | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 0519f099-ccb5-3020-8a44-5223bf82136b | -2.56564 | -56.17888 | 2026-10-09 05:04:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| afd8ed85-b668-3fdd-8a67-46106ee96d7f | -4.29707 | -60.95279 | 2026-10-09 05:04:00 | NPP-375D | BERURI | AMAZONAS | Brasil | 1300631 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 70a62999-c617-3d77-86ba-5a68a6ddf96a | -3.43637 | -54.54621 | 2026-10-09 05:04:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 19046ac5-639b-3606-9da1-c6f1e4ebd981 | -6.5767 | -53.02008 | 2026-10-09 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2420d152-87a2-38da-8928-c38bda4e15a2 | -3.08141 | -54.28635 | 2026-10-09 05:04:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4bfbb380-06ce-3bfd-8b5b-be4ebe6be978 | -5.90002 | -52.04326 | 2026-10-09 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 19b5eb12-0c3e-377a-b44e-48ed514df6d3 | -6.05918 | -44.03485 | 2026-10-09 05:04:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 007830cb-0b0a-3228-aed1-1ee6cc105b1d | -6.01741 | -40.97371 | 2026-10-09 05:04:00 | NPP-375D | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 7.1 |
| 1d229576-6406-309e-819d-54d26c5bbdd8 | -3.07533 | -53.9651 | 2026-10-09 05:04:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 11fcad08-425a-3f3e-b4c3-84b87127003b | -3.55467 | -54.66673 | 2026-10-09 05:04:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| cce67124-c609-3172-83b2-e7f4517e4167 | -2.99337 | -54.07053 | 2026-10-09 05:04:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b7e96b13-4e6b-3fd2-859f-5f1314db3669 | -7.27599 | -46.17039 | 2026-10-09 05:04:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 1ba0d21c-dcca-31bc-a461-6428e96b9b4e | -11.77212 | -43.53126 | 2026-10-09 05:04:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 1380c835-da91-3df9-84c8-71e8614fe9de | -3.47801 | -60.50154 | 2026-10-09 05:04:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4c655aa6-47b9-3dfb-a7cd-bca0778058a7 | -2.99668 | -53.84885 | 2026-10-09 05:04:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 10751fc0-7084-3a3f-b708-479747c1284e | -3.08323 | -54.29774 | 2026-10-09 05:04:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 55981ce0-f323-3e0c-9518-3ec3f035db82 | -5.09698 | -56.1925 | 2026-10-09 05:04:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0d97df94-8b30-3382-b08f-52ec80b165d6 | -8.18536 | -46.35505 | 2026-10-09 05:04:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 568b631e-72e6-3110-bd5f-70bac4823d5d | -4.54142 | -54.24978 | 2026-10-09 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6012205a-7e4f-343e-9c37-13fc22b8e810 | -7.18531 | -52.61741 | 2026-10-09 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |


[Clique aqui para ver as próximas entradas](README140.md)
