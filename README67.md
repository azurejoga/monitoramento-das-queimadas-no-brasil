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

## Dados Diários - Página 67

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f5bab3c4-850a-3d39-9cf8-40f2acc9c8ce | -3.8004 | -41.6708 | 2025-09-17 14:10:00 | GOES-19 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 269.6 |
| 9f8cc82d-6f00-3b85-b21d-47251e0b0414 | -6.0069 | -44.3354 | 2025-09-17 14:10:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 125.0 |
| dedd4ce4-c683-3437-adef-56ff4a82150d | -8.9167 | -46.224 | 2025-09-17 14:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 241.2 |
| 036d7424-e2d0-376f-b8a6-70722f515851 | -8.6885 | -46.3823 | 2025-09-17 14:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 225.2 |
| 8bda4f49-532e-31e2-837c-50322c99a921 | -8.4467 | -47.692 | 2025-09-17 14:10:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 80.1 |
| 0916f958-6b0e-35d9-9ec7-f855ff6a531e | -9.0851 | -44.9352 | 2025-09-17 14:10:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 86.2 |
| a37961f9-ffc5-312c-a3ec-422a4a249105 | -8.9725 | -46.2854 | 2025-09-17 14:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 105.7 |
| 5a68168c-a2ea-36b3-b1e4-f17fe4e2f2b0 | -8.631 | -46.4553 | 2025-09-17 14:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 152.2 |
| aeed8f9e-6d17-3ac3-adc8-5e8363470d7e | -12.7102 | -47.9872 | 2025-09-17 14:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 131.8 |
| 3c5dd88a-4d6a-3837-868e-cb861e793c45 | -10.6401 | -48.7332 | 2025-09-17 14:10:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 54.0 |
| 4269f694-a03c-3019-8bfb-cc8e957fa93e | -11.5024 | -43.7082 | 2025-09-17 14:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 107.0 |
| df7f710c-54f5-36d6-a734-7799672628d7 | -8.9728 | -46.263 | 2025-09-17 14:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 82.5 |
| 4daee3ff-6264-30f0-a2fe-c640663e688b | -8.8958 | -47.8683 | 2025-09-17 14:10:00 | GOES-19 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 61.0 |
| 57f73a5f-2697-3ed3-bafe-88fe0ae94d70 | -9.1429 | -44.8598 | 2025-09-17 14:10:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 108.7 |
| 4416c758-63bd-37c3-ada6-3e79fb0a53f8 | -7.5272 | -44.3413 | 2025-09-17 14:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 88.4 |
| c86ab3b2-1248-39a8-be19-ec37558453a2 | -5.7867 | -45.9603 | 2025-09-17 14:10:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 81.3 |
| 26483559-50c6-3536-aa69-a9099cd4e86a | -15.8417 | -59.4799 | 2025-09-17 14:10:00 | GOES-19 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 62.6 |
| aa7a5812-61bb-34d0-ba42-721d082f4214 | -7.5996 | -44.5872 | 2025-09-17 14:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 222.7 |
| 650a0672-0ad5-313a-902c-c8759dba4905 | -11.1681 | -45.3373 | 2025-09-17 14:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 150.4 |
| 64c8c560-b4fb-3762-b74c-6e2451ac72cf | -8.9445 | -45.5438 | 2025-09-17 14:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 106.0 |
| a7bff364-24d4-344d-abfa-8b6fde870589 | -8.9359 | -46.1995 | 2025-09-17 14:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 79.0 |
| 8dd670d0-0a3f-334c-a4cf-df61f9adcfca | -8.5797 | -47.5694 | 2025-09-17 14:10:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 96.9 |
| bf0ef69d-85cc-3cbe-9b70-8b177ef0ed79 | -11.211 | -47.3872 | 2025-09-17 14:10:00 | GOES-19 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 84.6 |
| 14366df2-4973-3577-acf1-f9e59341fcb2 | -14.7911 | -60.2289 | 2025-09-17 14:10:00 | GOES-19 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 90.6 |
| 126237d4-99e8-3571-851c-2855966c20af | -8.1757 | -46.7675 | 2025-09-17 14:10:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 65.1 |
| 3c20e1bc-2e81-30c6-9473-6b0256fd98a2 | -7.5227 | -44.7321 | 2025-09-17 14:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 111.8 |
| 784f0030-321b-38c5-b84c-c50638421e78 | -7.5998 | -44.5642 | 2025-09-17 14:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 137.7 |
| 80708a9a-35ba-3ce3-84cb-1183f9d700ff | -8.9536 | -46.2874 | 2025-09-17 14:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 131.6 |
| 69feac13-61ac-3bdc-be8f-f50528b94bde | -8.5421 | -47.573 | 2025-09-17 14:10:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 82.3 |
| b953c94b-26a6-372f-82a2-f8a7fef370e8 | -9.1236 | -44.8849 | 2025-09-17 14:10:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 146.1 |
| 16da075d-274c-35b6-91aa-152557f77e9c | -9.1425 | -44.8828 | 2025-09-17 14:10:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 199.1 |
| b6aa5326-2e1f-3b1e-92a2-ab5454b13849 | -7.6574 | -44.4667 | 2025-09-17 14:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 102.9 |
| 5ed7b497-2fdb-37e0-87b7-7db729527123 | -8.9164 | -46.2465 | 2025-09-17 14:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 84.7 |
| e475234a-f940-355b-83a7-b6a0253da318 | -12.7482 | -48.0041 | 2025-09-17 14:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 172.6 |
| c46efa0a-f97e-3c10-9039-6f9b110df757 | -12.7106 | -47.9649 | 2025-09-17 14:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 121.8 |
| e41af8b4-e0f0-3acb-8a32-a05aed15080c | -3.8463 | -40.3607 | 2025-09-17 14:10:00 | GOES-19 | FORQUILHA | CEARÁ | Brasil | 2304350 | 23 | 33 | nan | nan | nan | Caatinga | 104.8 |
| ae534f5d-b7bf-3341-921e-1851473ceb2b | -13.9658 | -44.8976 | 2025-09-17 14:10:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 82.7 |
| eadbf0d1-63ed-39fd-a62b-bfe9f4b8552f | -9.4747 | -48.2698 | 2025-09-17 14:10:00 | GOES-19 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 58.7 |
| 374c2868-8335-38ef-bac5-e30d47085a97 | -3.8042 | -44.1072 | 2025-09-17 14:10:00 | GOES-19 | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 220.9 |
| 6c1076c7-1830-30be-a281-58671628bcc1 | -6.6129 | -45.584 | 2025-09-17 14:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 78.8 |
| 17360b45-9b78-3e8a-a493-be8fbc521b95 | -5.7858 | -43.9378 | 2025-09-17 14:10:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 96.3 |
| 5f97ba09-93d0-31b6-8c7a-eadf11827380 | -8.917 | -46.2015 | 2025-09-17 14:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 111.3 |
| efad8eeb-4a48-34a8-a323-bc176cd1bc73 | -11.6434 | -46.591 | 2025-09-17 14:10:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 136.4 |
| b3a4fdb5-7f90-354a-8517-80cf455bd484 | -8.6313 | -46.4329 | 2025-09-17 14:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 91.0 |
| d68548ee-2c20-3bae-9ea5-c4edeb984a13 | -8.4279 | -47.6937 | 2025-09-17 14:10:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 65.5 |
| 16e05a60-5e41-3b2b-a513-4957b8b940fc | -12.729 | -48.0068 | 2025-09-17 14:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 321.1 |
| 89203f4e-a259-3c25-b02e-ef51cc0d26ba | -5.7869 | -45.9379 | 2025-09-17 14:10:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 77.7 |
| 95465656-bfdf-33e8-98db-4369d1799040 | -8.953 | -46.3324 | 2025-09-17 14:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 99.3 |
| 420c8f93-6e62-3a20-b962-bfcb03bd0a14 | -9.0289 | -44.8958 | 2025-09-17 14:10:00 | GOES-19 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 65.3 |
| 745855fd-de4e-3a37-8f36-03f029438e97 | -12.7102 | -47.9872 | 2025-09-17 14:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 151.1 |
| 633f0194-54b5-3507-a442-7f4ed4954e8a | -10.6738 | -46.4703 | 2025-09-17 14:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 69.4 |
| 6ac21819-fd85-305e-9d7b-1babc3af7fc8 | -7.6574 | -44.4667 | 2025-09-17 14:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 109.6 |
| 434fcc42-a1e8-3f63-9825-3dc8047c429b | -6.1253 | -47.8137 | 2025-09-17 14:20:00 | GOES-19 | CACHOEIRINHA | TOCANTINS | Brasil | 1703826 | 17 | 33 | nan | nan | nan | Cerrado | 63.1 |
| 0798545f-1fa3-3868-9c1a-3f50107b2c86 | -14.7911 | -60.2289 | 2025-09-17 14:20:00 | GOES-19 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 80.0 |
| deb52814-2642-3ad9-8383-38de01427df7 | -7.581 | -44.566 | 2025-09-17 14:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 134.1 |
| 32022018-d7db-37be-b514-eb48b2aeaaa0 | -9.4749 | -48.2479 | 2025-09-17 14:20:00 | GOES-19 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 66.2 |
| 77fc7da5-bad2-3ee2-9356-3b0f988036ae | -9.7126 | -47.4089 | 2025-09-17 14:20:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 60.0 |
| c4298884-11f9-3f10-ab66-906a8e6b6263 | -8.6313 | -46.4329 | 2025-09-17 14:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 94.7 |
| ee340b33-8d9c-31de-82de-b34b0a432b66 | -8.4467 | -47.692 | 2025-09-17 14:20:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 83.5 |
| a11ab914-7ad6-38ce-b864-73d20a330db3 | -8.9638 | -45.519 | 2025-09-17 14:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 103.4 |
| 413decbb-98d0-3498-8f49-e641d385a771 | -12.7286 | -48.029 | 2025-09-17 14:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 96.4 |
| 3479afa3-2116-3cfd-8a26-7a24faa956f7 | -8.6699 | -46.3618 | 2025-09-17 14:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 98.5 |
| 6bab280f-d20a-3fcd-9eb0-cc4be2f02a94 | -10.9643 | -47.3514 | 2025-09-17 14:20:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 86.4 |
| 88efc4f0-61eb-391b-802e-b2186ddd2758 | -3.8228 | -44.1063 | 2025-09-17 14:20:00 | GOES-19 | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 110.7 |
| fa81fc65-b8e6-3189-b131-9bae1a4ebbbe | -12.7106 | -47.9649 | 2025-09-17 14:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 148.1 |
| 48963fbf-832e-3191-826c-8228e63f56b7 | -8.9167 | -46.224 | 2025-09-17 14:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 131.4 |
| 917dec88-6b2b-3a8f-bbed-989ba5dd13a6 | -13.9688 | -44.7567 | 2025-09-17 14:20:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 126.6 |
| 891826d0-5224-33cf-9a99-dc185c0f8511 | -8.9356 | -46.222 | 2025-09-17 14:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 161.3 |
| 772d8a4d-914c-382a-8b38-ab6c97aa68a2 | -8.6887 | -46.3599 | 2025-09-17 14:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 237.1 |
| 21426701-b135-3fa8-8950-bc29aacc2294 | -9.0478 | -44.8936 | 2025-09-17 14:20:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 100.2 |
| adc0d910-1d2e-33c9-925c-b5a4d60a27a0 | -7.5272 | -44.3413 | 2025-09-17 14:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 83.1 |
| f12349a3-e70b-382e-88d3-35aff3858c53 | -8.5609 | -47.5712 | 2025-09-17 14:20:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 91.2 |
| 105b88d5-88cb-3879-b4a8-703a66110b4b | -3.8756 | -41.6188 | 2025-09-17 14:20:00 | GOES-19 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 231.6 |
| dbd467ad-75cf-3cd1-81f2-b2bf50303b50 | -7.5998 | -44.5642 | 2025-09-17 14:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 171.5 |
| 0001deac-cc7d-3605-8991-86d317078728 | -8.917 | -46.2015 | 2025-09-17 14:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 123.5 |
| 86c89fd4-0a4c-3e42-a3f2-98309428e824 | -8.5421 | -47.573 | 2025-09-17 14:20:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 70.3 |
| d5b0046b-cbf1-3db4-803a-60b96bf1f4c7 | -8.5797 | -47.5694 | 2025-09-17 14:20:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 122.4 |
| 89093238-bf7f-3a17-9bf2-58f87033a405 | -12.6729 | -45.8052 | 2025-09-17 14:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 137.1 |
| 5654a244-050a-33bc-bebb-a26bcf628bf2 | -9.7316 | -47.4068 | 2025-09-17 14:20:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 78.0 |
| 90c5b3f9-700e-355a-9461-f06d930cae55 | -3.8004 | -41.6708 | 2025-09-17 14:20:00 | GOES-19 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 117.1 |
| 047212a5-4493-3217-bb71-74d062f93025 | -7.8259 | -46.153 | 2025-09-17 14:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 57.0 |
| a309f362-4cf0-33b3-bd6e-3ac14f09636f | -6.3799 | -44.5122 | 2025-09-17 14:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 83.3 |
| fa580b3f-ff3a-3af3-8ead-a7803ba6e81e | -3.8002 | -41.6947 | 2025-09-17 14:20:00 | GOES-19 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 112.4 |
| 51eb58b2-47ed-3756-99ad-cb589fb90a84 | -3.3816 | -42.9689 | 2025-09-17 14:20:00 | GOES-19 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 136.3 |
| 9d36a7e3-f246-3411-8fb5-773e546a72d3 | -7.4688 | -46.1854 | 2025-09-17 14:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 100.7 |
| 22005eb1-e0a4-3f80-9e25-2d94eca5c246 | -7.5415 | -44.7303 | 2025-09-17 14:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 87.3 |
| 72c39a03-1d60-3e20-98c8-325fba6fcbb7 | -5.8807 | -45.8865 | 2025-09-17 14:20:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 93.2 |
| d6ddb9d1-b1f4-3019-ad5c-025c2b728632 | -14.7719 | -60.2305 | 2025-09-17 14:20:00 | GOES-19 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 59.7 |
| 1c022a6c-1b9f-3572-acc7-d6b636d50514 | -15.8417 | -59.4799 | 2025-09-17 14:20:00 | GOES-19 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 94.1 |
| 9537cb25-059f-35cb-8770-9bda0001406d | -3.804 | -44.1302 | 2025-09-17 14:20:00 | GOES-19 | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 157.9 |
| bbf3ba0f-7649-369d-a610-3966070389e2 | -8.4137 | -45.7583 | 2025-09-17 14:20:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 59.5 |
| 1c3586ac-2c99-388c-b4a2-1135abbfd0ae | -12.0051 | -46.6763 | 2025-09-17 14:20:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 151.9 |
| 02d08fb2-eb4a-3eab-951d-b7a89b45ab8b | -7.5227 | -44.7321 | 2025-09-17 14:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 102.5 |
| 43fcd800-4306-353a-9bd2-a1ee1db67f19 | -6.1868 | -45.1201 | 2025-09-17 14:20:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 87.2 |
| 863a8716-5732-341a-b8ef-11389160b0da | -9.0851 | -44.9352 | 2025-09-17 14:20:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 85.8 |
| ef1343e6-f9a9-3318-b618-c839dfda4c11 | -8.0005 | -45.6864 | 2025-09-17 14:20:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 61.1 |
| e687ce92-b302-3da8-8fa3-383660e67958 | -7.45 | -46.1871 | 2025-09-17 14:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 170.2 |
| ba6e2e05-75eb-3be3-aaee-1f7bfebf8dd3 | -8.6504 | -46.4086 | 2025-09-17 14:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 66.9 |
| ca90e182-8a42-3c60-a3a9-6c7a0befa920 | -11.467 | -43.5485 | 2025-09-17 14:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 70.9 |
| 9995524a-cb0c-3270-8484-1ba140ff9928 | -12.6953 | -47.7446 | 2025-09-17 14:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 94.7 |


[Clique aqui para ver as próximas entradas](README68.md)
