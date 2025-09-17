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

## Dados Diários - Página 66

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d4731df9-1c35-33f8-b0f2-2cd2d2f18239 | -7.6574 | -44.4667 | 2025-09-17 14:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 145.7 |
| 8e27d762-04f5-3926-b415-5ce80f658d6e | -6.6129 | -45.584 | 2025-09-17 14:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 89.3 |
| 0e803eca-1eed-3420-a009-78aeb7da0757 | -7.4688 | -46.1854 | 2025-09-17 14:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 84.7 |
| f163649b-0d34-3e4d-a989-d6e355a6b930 | -8.9356 | -46.222 | 2025-09-17 14:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 63.0 |
| c7efeb3f-ce97-33cb-8205-b6476cc2aaf0 | -12.7106 | -47.9649 | 2025-09-17 14:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 103.5 |
| 163d52f6-7c9a-3d1b-9a34-ae1b44048f0c | -9.1236 | -44.8849 | 2025-09-17 14:00:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 116.9 |
| 4caf80af-fd12-34d1-aca2-65429236220e | -6.3799 | -44.5122 | 2025-09-17 14:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 83.3 |
| 14d46e0f-a3be-3b0d-bb79-41fd69fb2fff | -8.9449 | -45.521 | 2025-09-17 14:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 123.8 |
| d3221033-5b89-3089-9311-959b132c3201 | -8.9638 | -45.519 | 2025-09-17 14:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 92.4 |
| c1aa03f2-feca-3bf5-a2e8-6f503979324e | -6.0069 | -44.3354 | 2025-09-17 14:00:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 133.0 |
| 13fc70a5-3a13-31f2-bd6d-e8e9391bec5e | -12.7294 | -47.9845 | 2025-09-17 14:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 204.5 |
| 338438bd-6f6b-3181-ae73-9f5f83d701e3 | -11.8927 | -48.8454 | 2025-09-17 14:00:00 | GOES-19 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 96.3 |
| 16122356-5939-3961-aff6-18e6cc2a507a | -10.9643 | -47.3514 | 2025-09-17 14:00:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 108.5 |
| 5cbd9a2d-14c2-345d-b155-a1a51a4b99d6 | -5.943 | -45.1838 | 2025-09-17 14:00:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 107.1 |
| eac55db6-e1f4-389e-86d4-b7ce14e46314 | -6.8734 | -43.9636 | 2025-09-17 14:00:00 | GOES-19 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 117.9 |
| b150d4ff-f7a9-32f6-8ed9-c1f2ea34d9ec | -3.804 | -44.1302 | 2025-09-17 14:00:00 | GOES-19 | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 86.0 |
| b2f31de8-b364-36dd-9cea-e13cf0a3759b | -8.899 | -46.136 | 2025-09-17 14:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 101.3 |
| b8e61c39-630e-3601-b000-06828d24399b | -7.5227 | -44.7321 | 2025-09-17 14:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 168.3 |
| 4c525bac-dc90-367f-9efc-b94dbc6d96c1 | -8.9445 | -45.5438 | 2025-09-17 14:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 90.2 |
| 15854259-cc72-309d-9766-0bbdec694036 | -8.631 | -46.4553 | 2025-09-17 14:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 78.3 |
| 1457d090-d2ee-3946-9370-7a60f73caa56 | -3.8042 | -44.1072 | 2025-09-17 14:00:00 | GOES-19 | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 157.1 |
| 864bddd2-4323-34cd-918f-88b64339101f | -6.4102 | -43.3534 | 2025-09-17 14:00:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 70.5 |
| 799584b2-bb99-36fa-890b-3ab42e6aa69a | -12.7102 | -47.9872 | 2025-09-17 14:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 123.3 |
| 31555b08-7d1f-32f8-bbf0-0edfe0c1f3e5 | -9.9418 | -45.9281 | 2025-09-17 14:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 67.5 |
| 488535f7-c920-3c87-ad8a-83233b7eb2b3 | -8.0005 | -45.6864 | 2025-09-17 14:00:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 64.7 |
| c7d835fc-bd8f-3a5d-b8e6-cd92dffc817b | -7.5998 | -44.5642 | 2025-09-17 14:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 111.7 |
| d3c33cb5-57d1-33fb-96e9-6990b32f55b0 | -12.0051 | -46.6763 | 2025-09-17 14:00:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 133.5 |
| eb08cab2-2876-39b9-81f8-034d1d42aba7 | -9.0478 | -44.8936 | 2025-09-17 14:00:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 84.1 |
| 6ccdbc41-02cf-3299-8fa9-6f747e544b2f | -10.7115 | -46.488 | 2025-09-17 14:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 89.3 |
| b99e9224-e93a-371a-ad15-0483b1ed9ddc | -8.6699 | -46.3618 | 2025-09-17 14:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 79.4 |
| e8a6ad16-1baa-33e1-a8ab-479a704eff32 | -6.2055 | -45.1187 | 2025-09-17 14:00:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 134.0 |
| c098cebe-2fa5-3bad-93e5-578a5e54b01e | -5.786 | -43.9147 | 2025-09-17 14:00:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 103.6 |
| 6c2e822d-35a5-34ca-a6ba-aa40691a8a83 | -10.7959 | -45.9575 | 2025-09-17 14:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 35.9 |
| f5e29709-5a6f-3f73-8124-dfd7b4a9f3f0 | -14.7719 | -60.2305 | 2025-09-17 14:00:00 | GOES-19 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 79.2 |
| a707a7f2-f463-3f4a-92da-00eb9d39c1db | -7.6572 | -44.4897 | 2025-09-17 14:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 96.9 |
| 09508962-aa97-332f-ab3b-12fbf1adc79f | -6.2053 | -45.1414 | 2025-09-17 14:00:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 170.9 |
| c65d7114-a194-3788-93a4-ab67005e8176 | -8.9728 | -46.263 | 2025-09-17 14:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 77.1 |
| 2bbd5f4b-4dfd-372d-81a6-dc4246a7ed70 | -7.581 | -44.566 | 2025-09-17 14:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 130.4 |
| 810dedfc-1fd1-3385-9d1c-65bdae71bf30 | -8.4467 | -47.692 | 2025-09-17 14:00:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 116.4 |
| c1c12ea8-5c52-3b1d-a26d-aa21c4b02418 | -10.6925 | -46.4904 | 2025-09-17 14:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 133.0 |
| d19d023a-435d-3029-b1c2-0ef804bd811a | -7.5415 | -44.7303 | 2025-09-17 14:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 145.1 |
| cd49b173-e0a2-3302-ae1d-24c91948e09e | -11.1681 | -45.3373 | 2025-09-17 14:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 84.9 |
| ed5a4337-57c4-323a-b7d5-a060cac7a790 | -7.8259 | -46.153 | 2025-09-17 14:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 63.7 |
| b6cab324-503d-3808-9ef4-15ee6dcf90ac | -15.0549 | -42.4653 | 2025-09-17 14:00:00 | GOES-19 | MONTEZUMA | MINAS GERAIS | Brasil | 3143450 | 31 | 33 | nan | nan | nan | Caatinga | 117.9 |
| 9fa42b16-f06d-31fd-afa9-f4329afc7fab | -13.9653 | -44.921 | 2025-09-17 14:00:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 162.2 |
| c7186e05-8c19-3fa6-8fe1-b7702e59ada7 | -11.211 | -47.3872 | 2025-09-17 14:00:00 | GOES-19 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 109.1 |
| 0294d55c-cf4b-3b0c-a38e-1cb2ec9a24e4 | -8.4279 | -47.6937 | 2025-09-17 14:00:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 64.3 |
| 128e570f-274a-35e6-afb6-93bc8cf63766 | -5.7858 | -43.9378 | 2025-09-17 14:00:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 95.5 |
| 0b939a64-64fc-3a6b-afb7-a6648011a0b4 | -8.8987 | -46.1585 | 2025-09-17 14:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 93.9 |
| 08d1bdb8-1b31-39d8-abbf-e941cf3321a6 | -3.3815 | -42.9923 | 2025-09-17 14:00:00 | GOES-19 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 108.8 |
| 57cdbf19-4004-372b-af1c-0d88e5b9261a | -8.9167 | -46.224 | 2025-09-17 14:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 91.6 |
| 89d8ac8f-79f1-3354-b205-a4c694dee1df | -9.1425 | -44.8828 | 2025-09-17 14:00:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 170.4 |
| 0fa7f612-3d89-3a19-a366-63dcdaa0fe49 | -13.9648 | -44.9445 | 2025-09-17 14:00:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 160.6 |
| 309ad364-6181-36cc-996d-48e179cda0f9 | -14.7911 | -60.2289 | 2025-09-17 14:00:00 | GOES-19 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 108.3 |
| b9bb17a8-2e50-3f62-9b9e-e8ba124112fb | -8.6699 | -46.3618 | 2025-09-17 14:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 88.0 |
| 6cbec1eb-43ab-3d39-b110-764abac51536 | -8.899 | -46.136 | 2025-09-17 14:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 65.9 |
| 465d4369-2059-33e5-889f-602990768c01 | -7.581 | -44.566 | 2025-09-17 14:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 123.7 |
| 52691f0c-3a01-38a1-bb5c-ab40a1715f55 | -11.467 | -43.5485 | 2025-09-17 14:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 91.5 |
| b29cc194-2720-37f4-89ba-e55796c04556 | -11.6626 | -46.5884 | 2025-09-17 14:10:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 123.2 |
| 981f143a-33f8-343a-b5a8-df5f748c2545 | -8.0005 | -45.6864 | 2025-09-17 14:10:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 75.6 |
| f50feccd-16fe-3add-b4bd-6b23bdc15be4 | -15.0549 | -42.4653 | 2025-09-17 14:10:00 | GOES-19 | MONTEZUMA | MINAS GERAIS | Brasil | 3143450 | 31 | 33 | nan | nan | nan | Caatinga | 101.4 |
| 3e189f12-f2da-32ef-a397-ed03d735e292 | -8.9356 | -46.222 | 2025-09-17 14:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 131.9 |
| 1f65ff51-5efd-3fd3-92d8-c7bd8e1d642a | -8.6502 | -46.431 | 2025-09-17 14:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 83.9 |
| b746b4d1-0134-3421-8b4a-e4592456e42c | -14.7719 | -60.2305 | 2025-09-17 14:10:00 | GOES-19 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 59.2 |
| 8672636f-b440-33d7-b203-11a7daa8ca7a | -3.8002 | -41.6947 | 2025-09-17 14:10:00 | GOES-19 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 234.7 |
| b1c2376e-1993-32f9-810e-f5ef1555d72e | -3.8228 | -44.1063 | 2025-09-17 14:10:00 | GOES-19 | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 103.1 |
| 14d22fbe-8cc4-3458-b7a2-c498b3821fcf | -12.6821 | -45.3209 | 2025-09-17 14:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 94.9 |
| 92d214ec-f25c-351f-8799-6d8e4962c8b8 | -6.3799 | -44.5122 | 2025-09-17 14:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 87.2 |
| 05e8dab2-c117-3de6-aaeb-82a5c560cffb | -13.9648 | -44.9445 | 2025-09-17 14:10:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 227.1 |
| df6a2eb8-e9e5-3146-aabf-2a011afb8ac6 | -8.001 | -45.6412 | 2025-09-17 14:10:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 69.0 |
| 374fdc68-202a-3fc1-b164-7005e168af82 | -12.7018 | -45.2947 | 2025-09-17 14:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 95.5 |
| 5965363e-9d4b-30d3-a699-5d6b85752dfe | -7.45 | -46.1871 | 2025-09-17 14:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 145.0 |
| 9cd39014-24dc-3ffa-937f-67da5e628578 | -7.5415 | -44.7303 | 2025-09-17 14:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 116.9 |
| 3fb25781-8724-3db6-85e7-d12f09cf26ad | -12.0051 | -46.6763 | 2025-09-17 14:10:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 137.7 |
| 36aef8b6-4d71-3b09-891c-243658fc0335 | -8.5611 | -47.5492 | 2025-09-17 14:10:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 73.0 |
| fbdb7a77-207f-3818-8e95-199a4c5a3307 | -3.8756 | -41.6188 | 2025-09-17 14:10:00 | GOES-19 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 157.4 |
| feee7917-0099-3bb2-8f9b-7b71033caf0c | -5.8807 | -45.8865 | 2025-09-17 14:10:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 84.8 |
| 35c008f0-8ffb-369d-894d-ee44861538d2 | -9.4935 | -48.2679 | 2025-09-17 14:10:00 | GOES-19 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 58.7 |
| 1edec759-addc-354c-b6ff-1d3d5bd97b47 | -7.5412 | -44.7532 | 2025-09-17 14:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 872.9 |
| 68bcfcf8-857d-3716-b42b-589bb9c29d9d | -8.6887 | -46.3599 | 2025-09-17 14:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 132.4 |
| 9aa38252-31ed-326c-abba-8910cd65e815 | -8.8987 | -46.1585 | 2025-09-17 14:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 71.1 |
| 3abeca72-d58a-36a8-9f30-ba356da311d9 | -8.9449 | -45.521 | 2025-09-17 14:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 160.2 |
| 8e2eff25-93fc-363b-9a77-ad2f1bd19e58 | -8.5609 | -47.5712 | 2025-09-17 14:10:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 129.0 |
| b7863bcb-b026-315b-8118-fae0d24819c3 | -9.0661 | -44.9374 | 2025-09-17 14:10:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 93.4 |
| d5fce893-93da-37e7-8ea0-c0f3104e0879 | -3.804 | -44.1302 | 2025-09-17 14:10:00 | GOES-19 | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 120.5 |
| 216a02e7-408b-3b40-a8a1-6cab54180e11 | -3.3816 | -42.9689 | 2025-09-17 14:10:00 | GOES-19 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 147.7 |
| c869f643-0d8b-35ad-a4f5-98eed908c3b7 | -8.6882 | -46.4047 | 2025-09-17 14:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 97.8 |
| 4af56aaa-8b8b-369d-954e-97d4a3eb8925 | -5.786 | -43.9147 | 2025-09-17 14:10:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 108.2 |
| bed1a44d-40ac-3ab4-aaad-9c6010736795 | -6.1252 | -47.8355 | 2025-09-17 14:10:00 | GOES-19 | CACHOEIRINHA | TOCANTINS | Brasil | 1703826 | 17 | 33 | nan | nan | nan | Cerrado | 74.6 |
| 950964d9-aff6-38b5-baf9-a0fbf58f4f82 | -8.9638 | -45.519 | 2025-09-17 14:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 78.6 |
| 36d1cc22-5405-3b03-8cb7-c2a775350c9f | -8.1569 | -46.7693 | 2025-09-17 14:10:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 88.2 |
| 7e9263d1-3ae4-3371-8f07-7bc3bc029971 | -9.1697 | -47.0681 | 2025-09-17 14:10:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 96.0 |
| 8684f586-c687-3102-be33-a6a6ab968428 | -12.6949 | -47.7669 | 2025-09-17 14:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 112.0 |
| 2bac592f-6896-3cf2-b313-2868395eaf0c | -10.9643 | -47.3514 | 2025-09-17 14:10:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 175.4 |
| b72de45e-64d8-3eb4-b760-e90ba925e202 | -11.6438 | -46.5684 | 2025-09-17 14:10:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 80.0 |
| a82b80f5-458a-3cec-b2b4-8fdb9631e0b2 | -9.0478 | -44.8936 | 2025-09-17 14:10:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 88.9 |
| fa6f3345-0583-3540-bc61-15f8cb0ad24f | -7.4688 | -46.1854 | 2025-09-17 14:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 77.4 |
| 471a1faa-36ab-3ad1-bf11-5856eb23df34 | -6.8734 | -43.9636 | 2025-09-17 14:10:00 | GOES-19 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 133.2 |
| 00d484e4-8400-3735-8b38-b50514daa54f | -8.6499 | -46.4534 | 2025-09-17 14:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 107.6 |
| 79c4393f-2fff-3e94-8898-89c8e7cb88dd | -6.2055 | -45.1187 | 2025-09-17 14:10:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 77.1 |


[Clique aqui para ver as próximas entradas](README67.md)
