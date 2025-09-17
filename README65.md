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
| 7cd18f67-c7be-3011-8026-51e66ee43ef2 | -8.9533 | -46.3099 | 2025-09-17 13:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 101.3 |
| 3317e8ee-d3d9-30dd-8d96-0ea00c12e915 | -8.5611 | -47.5492 | 2025-09-17 13:50:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 65.9 |
| 22c7920e-35a7-36ef-ac7e-f74524bf7850 | -7.5998 | -44.5642 | 2025-09-17 13:50:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 521.8 |
| 1e7e442b-42be-3f84-bf25-db937ecc5b0b | -15.0549 | -42.4653 | 2025-09-17 13:50:00 | GOES-19 | MONTEZUMA | MINAS GERAIS | Brasil | 3143450 | 31 | 33 | nan | nan | nan | Caatinga | 123.7 |
| 9d8aeb36-aeee-3bb8-a402-309e3556fef6 | -8.6699 | -46.3618 | 2025-09-17 13:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 94.1 |
| 60871636-57d4-3ae1-b437-45b1d7f706e9 | -3.8042 | -44.1072 | 2025-09-17 13:50:00 | GOES-19 | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 154.7 |
| d918fed8-2cae-3363-a585-ba090ce8daff | -6.2055 | -45.1187 | 2025-09-17 13:50:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 121.6 |
| 46b4fcdd-9441-3aef-8776-6f19026e2e81 | -6.3799 | -44.5122 | 2025-09-17 13:50:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 128.6 |
| e5ad80a8-071b-3d5b-80d4-b94abbd4e460 | -11.1108 | -45.3452 | 2025-09-17 13:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 152.0 |
| d79fd3c9-e0d3-3826-a324-5d15ad3a001b | -8.6887 | -46.3599 | 2025-09-17 13:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 168.9 |
| 52d6b81c-4c02-3fa1-acc2-72430736877d | -7.5272 | -44.3413 | 2025-09-17 13:50:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 115.0 |
| 058d9db5-5912-3af9-b646-4d4e83cdffc9 | -13.9648 | -44.9445 | 2025-09-17 13:50:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 249.0 |
| 05d86784-39cc-359c-b18c-b9a1479f6f81 | -8.9445 | -45.5438 | 2025-09-17 13:50:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 87.3 |
| 729719eb-f742-3a59-a80a-54257d098992 | -7.6574 | -44.4667 | 2025-09-17 13:50:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 172.4 |
| 4e59702e-6ac0-3531-ba88-65e1b6728a8b | -8.9356 | -46.222 | 2025-09-17 13:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 56.9 |
| ae97be0f-3b10-3b38-8597-be702fce07b4 | -6.8734 | -43.9636 | 2025-09-17 13:50:00 | GOES-19 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 113.8 |
| a67fe358-7c05-3291-9af4-cde667d47a34 | -7.8256 | -46.1754 | 2025-09-17 13:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 58.5 |
| 92877f17-7bbb-3feb-a747-57f0565a7686 | -6.1252 | -47.8355 | 2025-09-17 13:50:00 | GOES-19 | CACHOEIRINHA | TOCANTINS | Brasil | 1703826 | 17 | 33 | nan | nan | nan | Cerrado | 64.5 |
| c6cbfd33-851d-3943-bf75-8d08891f198a | -14.7913 | -60.2091 | 2025-09-17 13:50:00 | GOES-19 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 79.5 |
| ef2d36cf-b3f9-331f-bafc-b31e4e464fc8 | -12.7106 | -47.9649 | 2025-09-17 13:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 122.3 |
| 36139bb3-f5d3-3cb3-8e29-4bcd8db36c7e | -11.1299 | -45.3426 | 2025-09-17 13:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 91.5 |
| 50190bd8-e428-369e-8d92-20070bd80f47 | -10.9643 | -47.3514 | 2025-09-17 13:50:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 67.0 |
| 90dd9d16-7049-3164-a31c-58a3e2c956f6 | -8.1807 | -44.8043 | 2025-09-17 13:50:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 89.7 |
| 225143e0-d739-3c8f-8fbf-03c766d0cb8f | -14.7716 | -60.2503 | 2025-09-17 13:50:00 | GOES-19 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 108.8 |
| 635b6a36-5949-3923-af9f-3e5c5c211564 | -11.8927 | -48.8454 | 2025-09-17 13:50:00 | GOES-19 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 71.3 |
| e79dec8f-da10-36e7-b002-ac690157c388 | -8.9536 | -46.2874 | 2025-09-17 13:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 95.2 |
| fd68bbe3-21b1-3069-aa2d-e2ff6cd94301 | -5.8807 | -45.8865 | 2025-09-17 13:50:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 75.0 |
| a569b596-f48d-3bea-888d-994d15dd25d5 | -11.211 | -47.3872 | 2025-09-17 13:50:00 | GOES-19 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 110.0 |
| 257c294c-18c1-339b-8cc7-5eed9eb3ea62 | -6.4102 | -43.3534 | 2025-09-17 13:50:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 71.0 |
| 239c30fa-2c3c-3667-84a1-84652d817b27 | -8.6885 | -46.3823 | 2025-09-17 13:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 185.5 |
| b28a5e1e-3f36-3c4a-bdee-f9b1295b8493 | -9.0851 | -44.9352 | 2025-09-17 13:50:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 96.6 |
| 9322b477-5d78-3f5f-88c0-4bc5e32e2ac1 | -8.9725 | -46.2854 | 2025-09-17 13:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 75.5 |
| 82d68322-2b50-3d19-ae51-6e22fb38c55c | -8.0005 | -45.6864 | 2025-09-17 13:50:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 76.1 |
| 413381da-f603-3e94-83a6-e29474861004 | -8.5797 | -47.5694 | 2025-09-17 13:50:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 72.0 |
| 416ebb5b-525a-3712-aa3c-807745837cca | -7.5269 | -44.3644 | 2025-09-17 13:50:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 120.3 |
| d57d0466-592f-3767-a56a-a2799e034c46 | -5.8964 | -44.1369 | 2025-09-17 13:50:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 111.1 |
| 2ce858b3-c0bb-35cf-8171-7fa5ea5c50ce | -6.0069 | -44.3354 | 2025-09-17 13:50:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 118.2 |
| 08dba0c6-141d-3f03-9c9b-af10ded0c6f9 | -7.4503 | -46.1647 | 2025-09-17 13:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 84.3 |
| f5742ec2-4f2c-343b-bec1-6367a1823717 | -14.7911 | -60.2289 | 2025-09-17 13:50:00 | GOES-19 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 403.4 |
| e25667c0-aac3-31db-81ca-030e1f7d632e | -9.1425 | -44.8828 | 2025-09-17 13:50:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 97.1 |
| 5ac864e3-1aff-3891-90bb-8ed53aeac7c0 | -7.4688 | -46.1854 | 2025-09-17 13:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 99.9 |
| 1f5e7f93-a1a1-312d-86a3-23c8fb94c09d | -8.4467 | -47.692 | 2025-09-17 13:50:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 73.2 |
| 9276d73d-9376-3658-bf4b-e86473fe6f95 | -12.0047 | -46.6989 | 2025-09-17 13:50:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 288.1 |
| 2e1ea009-0869-3827-8085-1993f6d4c115 | -12.729 | -48.0068 | 2025-09-17 13:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 135.4 |
| b32ee644-945e-384c-b107-e959aff99690 | -3.8756 | -41.6188 | 2025-09-17 13:50:00 | GOES-19 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 136.1 |
| 5ea57fd4-2b17-3768-bedf-4e588e42bc40 | -7.5415 | -44.7303 | 2025-09-17 13:50:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 95.4 |
| 6d54406f-ac4b-33a0-9ed4-682834151dc1 | -12.0051 | -46.6763 | 2025-09-17 13:50:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 138.3 |
| 9fc36f80-494b-3e49-940d-e1146cfb47fd | -7.5412 | -44.7532 | 2025-09-17 13:50:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 169.1 |
| 30231de2-ee37-3d17-acca-fb25c7ff96ee | -3.3816 | -42.9689 | 2025-09-17 13:50:00 | GOES-19 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 143.6 |
| 847c7250-8824-3c70-8cac-2b0e58ad106e | -8.9347 | -46.2894 | 2025-09-17 13:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 55.2 |
| 81f52b1f-5d7a-3962-a27c-06327ad5f792 | -7.5227 | -44.7321 | 2025-09-17 13:50:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 111.3 |
| 639783b9-c8da-3bc7-9a3f-5c6496157c05 | -12.7294 | -47.9845 | 2025-09-17 13:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 88.5 |
| 74ec8fb8-60b2-339b-9ee8-0e52fbd52671 | -12.7145 | -47.7419 | 2025-09-17 13:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 102.7 |
| a8c0ccfa-3184-379e-9cae-3da160972844 | -6.3917 | -43.3317 | 2025-09-17 13:50:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 68.8 |
| 6f3359b6-6b7e-332a-925a-cf9900a1657f | -11.1681 | -45.3373 | 2025-09-17 13:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 72.2 |
| f64569a1-001e-33c7-ac88-51060de46697 | -6.3915 | -43.3551 | 2025-09-17 13:50:00 | GOES-19 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 68.2 |
| 36d3c495-eae5-338b-a457-391f38a9ead8 | -7.45 | -46.1871 | 2025-09-17 13:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 226.8 |
| 846cb605-3707-347b-bdc1-3192f3e67391 | -8.8987 | -46.1585 | 2025-09-17 13:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 75.8 |
| 5e9d8235-c9c8-3eab-8730-c7635100941a | -8.4137 | -45.7583 | 2025-09-17 13:50:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 78.3 |
| e8e70671-8090-3d5d-8cdb-e53e24c45e2a | -12.7141 | -47.7642 | 2025-09-17 13:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 85.0 |
| 7a2b1824-b8c6-386e-834e-d40929965ac1 | -8.5421 | -47.573 | 2025-09-17 13:50:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 77.1 |
| d3a99e75-09a2-3b71-af40-65160985f523 | -12.7482 | -48.0041 | 2025-09-17 13:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 116.9 |
| 57279c70-5aec-3ba6-88af-6369be49f605 | -6.4804 | -45.7296 | 2025-09-17 13:50:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 87.1 |
| 4fd90dc0-8a3e-33ec-8050-885c26a45606 | -8.631 | -46.4553 | 2025-09-17 13:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 94.2 |
| 7fa0aee7-1eea-311f-abee-f883a1b6bfbf | -4.5902 | -43.7648 | 2025-09-17 13:50:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 83.3 |
| 7d0875d0-6082-3908-9c41-afbca494c99c | -8.5609 | -47.5712 | 2025-09-17 13:50:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 114.1 |
| 2e81ba7c-c236-3925-aec9-4383e0bad909 | -6.2053 | -45.1414 | 2025-09-17 13:50:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 79.1 |
| 5d4f1697-e307-33cc-a8a8-91a692bf36f3 | -8.9728 | -46.263 | 2025-09-17 13:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 73.0 |
| 07f5db80-4d92-3be0-8dfa-b62e9262f2f5 | -8.6702 | -46.3394 | 2025-09-17 13:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 70.8 |
| ce81e9aa-0f53-38c4-8753-4a235d34d0bd | -8.6882 | -46.4047 | 2025-09-17 13:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 75.5 |
| 92c48b2b-fb90-35ce-a91a-7c038369dd00 | -8.6499 | -46.4534 | 2025-09-17 13:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 90.6 |
| 94172fe1-8903-3c0d-8805-a56412810ca0 | -8.9638 | -45.519 | 2025-09-17 13:50:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 103.6 |
| 2fee17c6-ec37-3ea0-a94e-4ada3baff759 | -6.3073 | -42.3975 | 2025-09-17 13:50:00 | GOES-19 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 77.3 |
| e27b269e-57d4-31ee-8363-747c22c6df66 | -3.804 | -44.1302 | 2025-09-17 13:50:00 | GOES-19 | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 80.9 |
| 98c03379-8098-3ab7-a38a-597fe4b6855b | -11.1108 | -45.3452 | 2025-09-17 14:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 114.2 |
| 2eacc899-2929-373d-bd33-289b583cf836 | -8.6499 | -46.4534 | 2025-09-17 14:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 92.1 |
| 07affa6e-f3ca-3b07-be59-39931b738329 | -12.7482 | -48.0041 | 2025-09-17 14:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 99.4 |
| 4bd8a09a-0a82-37f9-a512-b40204008065 | -6.1252 | -47.8355 | 2025-09-17 14:00:00 | GOES-19 | CACHOEIRINHA | TOCANTINS | Brasil | 1703826 | 17 | 33 | nan | nan | nan | Cerrado | 67.0 |
| 4ff0b051-a07b-3190-ac23-86a4229f4a51 | -8.6885 | -46.3823 | 2025-09-17 14:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 223.2 |
| 76922146-441c-394d-a604-b607732d74ba | -9.4747 | -48.2698 | 2025-09-17 14:00:00 | GOES-19 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 78.5 |
| 8298af0b-4bcd-332e-8b4a-0c9b1878ef3b | -9.1239 | -44.862 | 2025-09-17 14:00:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 86.0 |
| d62dce7d-4cde-3fb3-85b3-6afb3c88cfa9 | -8.6882 | -46.4047 | 2025-09-17 14:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 91.5 |
| c336bfd7-bef3-308f-b1b2-d1ec43e872b7 | -10.6334 | -44.2324 | 2025-09-17 14:00:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 107.9 |
| 9476ed79-bdc5-3960-8530-2c8d5371031b | -9.1429 | -44.8598 | 2025-09-17 14:00:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 92.8 |
| 798e5ace-d722-324a-825f-8d0bfe0424eb | -5.8807 | -45.8865 | 2025-09-17 14:00:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 160.1 |
| 63a66c93-be5d-3106-8636-93a08016e1d7 | -12.6949 | -47.7669 | 2025-09-17 14:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 219.2 |
| 6220bc36-dd9c-3f87-9bd5-1ea672305243 | -12.6821 | -45.3209 | 2025-09-17 14:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 89.4 |
| ef520cf0-2381-307a-bd40-a73292331436 | -12.7141 | -47.7642 | 2025-09-17 14:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 135.9 |
| 2062be9e-9543-3178-bf5d-2028cc4e63d9 | -12.7018 | -45.2947 | 2025-09-17 14:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 111.1 |
| 0c92472a-ab79-3113-8e46-b6882a20d841 | -10.6338 | -44.2091 | 2025-09-17 14:00:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 78.7 |
| cc932e89-50d0-386d-8573-721b07553af7 | -7.6386 | -44.4686 | 2025-09-17 14:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 83.0 |
| 129ce183-eb3a-369e-a7ec-6b450549f6af | -5.8809 | -45.8641 | 2025-09-17 14:00:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 91.4 |
| 4a37b395-663e-32ab-8c5c-2e9032847d38 | -8.5759 | -46.349 | 2025-09-17 14:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 89.3 |
| dbe8ecce-79e1-39ab-be43-6bbe502f2ceb | -9.0851 | -44.9352 | 2025-09-17 14:00:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 93.3 |
| 85cbfef2-42bf-3ae0-a7df-d0e53bdb5495 | -10.08 | -48.1836 | 2025-09-17 14:00:00 | GOES-19 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 40.2 |
| b57baa00-3e11-3cec-a8d0-76f94ab5fc99 | -3.3816 | -42.9689 | 2025-09-17 14:00:00 | GOES-19 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 220.9 |
| 0d2861a4-506f-3efb-a939-a449d69bd84b | -8.6887 | -46.3599 | 2025-09-17 14:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 143.6 |
| e95191e7-2987-3a1e-915d-5f959d7eaa59 | -7.5412 | -44.7532 | 2025-09-17 14:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 451.9 |
| 98b73d7f-8a17-344b-8fc2-759442681f0e | -7.45 | -46.1871 | 2025-09-17 14:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 213.3 |
| 423d3301-8f9f-3d73-b458-7e0c625fe535 | -12.729 | -48.0068 | 2025-09-17 14:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 143.2 |


[Clique aqui para ver as próximas entradas](README66.md)
