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

## Dados Diários - Página 38

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| cab00771-9789-31ff-865b-3a52a7f8708a | -11.40722 | -43.48288 | 2026-10-01 04:14:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a6af8f0d-8e1b-3280-b00a-0ecbd7a5ff43 | -7.03898 | -50.72899 | 2026-10-01 04:14:00 | NPP-375D | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 26dd92cc-0445-3024-80fc-1cf5c1edb0c0 | -12.6062 | -42.16926 | 2026-10-01 04:14:00 | NPP-375D | IBITIARA | BAHIA | Brasil | 2913002 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| e150d613-4d12-3d58-8e3c-053ab4b2ea30 | -11.43085 | -43.4062 | 2026-10-01 04:14:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| eb7c673c-17fd-3009-92c5-62b2a83ed92a | -4.26546 | -50.7337 | 2026-10-01 04:14:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 6ad29874-b65b-32ac-ae23-a7d240eadd16 | -9.78244 | -44.80677 | 2026-10-01 04:14:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 00769e39-d2a9-3d45-a017-a6b375404b57 | -7.32096 | -42.07863 | 2026-10-01 04:14:00 | NPP-375D | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 9bd535b7-66c5-323a-8540-5763e8deb6c7 | -10.83823 | -48.71034 | 2026-10-01 04:14:00 | NPP-375D | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| f2210ee5-10d3-385d-a09b-17c0745e4371 | -7.07151 | -42.32444 | 2026-10-01 04:14:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 6.8 |
| 7ae141a2-954b-3ba1-915c-159482165806 | -11.36365 | -43.35489 | 2026-10-01 04:14:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| d39dc979-c33a-3f41-b66d-22f5cb7a981e | -11.4549 | -43.43454 | 2026-10-01 04:14:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 6.0 |
| a0718c37-3019-3cde-b59c-af480dd982f8 | -4.27477 | -50.76331 | 2026-10-01 04:14:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 19.8 |
| 3ba1f64c-c68f-3248-aa4c-652dbb296b47 | -4.25623 | -50.82048 | 2026-10-01 04:14:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 5cfe587e-6f51-372b-abf9-526535b8559d | -5.70775 | -43.63697 | 2026-10-01 04:14:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| b290abc7-cdea-30c9-88cd-6f2006fb105d | -7.78485 | -49.8799 | 2026-10-01 04:14:00 | NPP-375D | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8a99ef81-8858-35d3-a601-512786fb5e2e | -11.62126 | -43.54214 | 2026-10-01 04:14:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 50ddaa4f-b698-320f-a2fd-1ff9102628f9 | -12.63369 | -42.1481 | 2026-10-01 04:14:00 | NPP-375D | IBITIARA | BAHIA | Brasil | 2913002 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 3fefdc22-fe6b-3350-b76b-32da452f5375 | -4.27284 | -50.79911 | 2026-10-01 04:14:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 651dd792-027e-3425-88cc-924ec83ca603 | -11.46279 | -43.45205 | 2026-10-01 04:14:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 33644f27-bf52-3722-9614-e53095cf3fb2 | -4.26153 | -50.82657 | 2026-10-01 04:14:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| afebd9dd-2965-31f7-8633-d8584c861b5b | -5.76375 | -45.15339 | 2026-10-01 04:14:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| b0c8864f-934d-34a1-83db-96e55b8cdb6b | -4.28487 | -50.73184 | 2026-10-01 04:14:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2890a629-7f96-3b0e-a862-4905ea88bb40 | -11.42036 | -43.4044 | 2026-10-01 04:14:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0b894884-b7b5-3e49-8814-0d0b59d1c83f | -4.29126 | -50.81602 | 2026-10-01 04:14:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 5e0fbdb3-136b-34a9-bd84-a1620ad7afe0 | -10.71558 | -44.4155 | 2026-10-01 04:14:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2465b81f-43ee-340e-89a1-abe345c2b44b | -4.29849 | -50.79847 | 2026-10-01 04:14:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 06a797ff-e60d-3919-b0bb-835946a260c4 | -10.76563 | -47.71595 | 2026-10-01 04:14:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b6bc23d4-68bd-312f-bf49-ce28ffcb0184 | -13.02202 | -41.04895 | 2026-10-01 04:14:00 | NPP-375D | ITAETÉ | BAHIA | Brasil | 2915007 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| b7ee8b42-59d6-39d2-bba4-f3e36864d6b4 | -9.75705 | -44.81702 | 2026-10-01 04:14:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b98558e0-69f0-3f6f-9831-d33eb9e35451 | -5.7571 | -45.16773 | 2026-10-01 04:14:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0721bbca-0a4d-3ab7-8645-132df708a9c3 | -9.16371 | -45.59426 | 2026-10-01 04:14:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ce25141f-c76e-321a-9d60-fa72780b2cce | -4.31425 | -50.7815 | 2026-10-01 04:14:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 31a736ca-f465-3e62-8270-b8cde6763943 | -11.17752 | -44.83404 | 2026-10-01 04:14:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| df27b967-0cab-3d68-bbe0-9c75511fd1b2 | -10.90525 | -43.8476 | 2026-10-01 04:14:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| cd605e7e-094d-3ca1-91d7-b500ab769986 | -4.45422 | -47.92006 | 2026-10-01 04:14:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 7ccb6966-f008-36f7-a173-c5440bc2e8d6 | -11.40372 | -43.48228 | 2026-10-01 04:14:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a9f0ece9-0a82-3db4-ba04-a5efba57bc35 | -11.39353 | -43.37167 | 2026-10-01 04:14:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| afbb7e54-f232-3fbc-9037-e7f51497ce8b | -8.21157 | -45.47312 | 2026-10-01 04:14:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| ae13fc2f-993a-337b-b311-97b3527f0c1d | -11.71528 | -43.43621 | 2026-10-01 04:14:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 952036bb-08e2-347c-a5d8-dfc041d684d5 | -4.26034 | -50.81013 | 2026-10-01 04:14:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| fa3f6eb3-7fbf-3f24-9f62-c3870db210d6 | -4.26444 | -50.78633 | 2026-10-01 04:14:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 33.7 |
| 2bfeae0b-2bdb-3a24-8d70-7a60ad3bfc9b | -4.27351 | -50.80779 | 2026-10-01 04:14:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 8d670fb2-59a3-3360-b95b-d13196631508 | -4.27017 | -50.75307 | 2026-10-01 04:14:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 15.3 |
| 382adb76-c06e-37fc-819b-15c196a42cd6 | -6.2838 | -44.14069 | 2026-10-01 04:14:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| d01c74c8-43e6-3752-acfc-de8d2f0265da | -11.22667 | -45.20039 | 2026-10-01 04:14:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| cb586bad-a3a4-3d38-b1c4-b08cacae3bc7 | -9.87126 | -44.94193 | 2026-10-01 04:14:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 106979e8-7029-3198-9760-15f52a419281 | -11.67881 | -43.49937 | 2026-10-01 04:14:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 99fd83b4-7183-3fbf-b9fd-8bec8dbe5127 | -4.26755 | -50.79303 | 2026-10-01 04:14:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 20.4 |
| e15f8085-cc5d-3790-9fbf-dec658ad935c | -4.27014 | -50.77857 | 2026-10-01 04:14:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 81.2 |
| 30aef974-5d58-33d7-8a54-7c8be90dd517 | -4.27783 | -50.73568 | 2026-10-01 04:14:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ad0029b7-dbf6-31f9-b222-54ee0cb423c7 | -6.92577 | -44.56343 | 2026-10-01 04:14:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 62adfe2f-8b60-35c1-8c5f-80068def8ec0 | -4.24915 | -50.76414 | 2026-10-01 04:14:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| a5591303-9364-3746-b50b-b04fcfb915c5 | -4.45934 | -47.92094 | 2026-10-01 04:14:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 4b2c7b3b-d2eb-3dd6-8490-ca2557639ef4 | -11.41423 | -43.48408 | 2026-10-01 04:14:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c7537fc6-d159-358e-b8dd-af6327415475 | -9.86825 | -44.93636 | 2026-10-01 04:14:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| caf1bcb9-502d-3e89-905c-c1755dd05d75 | -11.44856 | -43.42939 | 2026-10-01 04:14:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.9 |
| e3c62b02-9614-361e-ba28-13458cd8b5e4 | -4.26865 | -50.82252 | 2026-10-01 04:14:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 297714f6-dbf3-3179-b67e-9b98287f7d82 | -4.28052 | -50.8041 | 2026-10-01 04:14:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 70abbeb8-6f99-32b4-80f1-da6ec478cfd6 | -4.27029 | -50.82656 | 2026-10-01 04:14:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 34c3c635-f8cb-3f79-a1ec-ee670dc0c4c8 | -7.1218 | -43.15628 | 2026-10-01 04:14:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 8.4 |
| a2df9229-4b9c-388c-9580-6665249a1945 | -9.22186 | -45.84027 | 2026-10-01 04:14:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d5f430ec-cd58-31e1-96ac-3ce53632ce02 | -6.33226 | -51.12528 | 2026-10-01 04:14:00 | NPP-375D | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0ef9c4b7-c788-32e5-9095-022ed553972c | -11.83433 | -44.75206 | 2026-10-01 04:14:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| a3ca0512-a397-3c09-b21b-5b58acf039ce | -7.83308 | -45.82093 | 2026-10-01 04:14:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6907defd-f8aa-3f3a-b07e-65a83e6e749a | -4.28428 | -48.56096 | 2026-10-01 04:14:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| da77badb-7613-33e2-848b-ebc8567cfbf2 | -4.27456 | -50.78952 | 2026-10-01 04:14:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 20.4 |
| 12994a1b-23ba-3aa3-81a2-93c1c0634fa9 | -5.7164 | -46.19833 | 2026-10-01 04:14:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1b7e827b-cba9-3b60-8d6c-bdee9b25f1c4 | -12.56738 | -43.06628 | 2026-10-01 04:14:00 | NPP-375D | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 3626e322-27dc-3723-b75e-f1306333373c | -11.41141 | -43.41494 | 2026-10-01 04:14:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 64adf913-7c11-3477-93f1-efff5b9a44b7 | -4.29488 | -50.78289 | 2026-10-01 04:14:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 2ce62280-60de-3f4c-aedb-b8b0a7e62e4b | -12.50889 | -43.10716 | 2026-10-01 04:14:00 | NPP-375D | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 2.6 |
| bb6884fd-f14e-3e13-9741-38c07204e28f | -4.27893 | -50.81345 | 2026-10-01 04:14:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 968317e0-879f-3610-8093-1b23d1d3a535 | -11.70218 | -43.45003 | 2026-10-01 04:14:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c2888040-0e47-3d91-b70c-7f2cee742e85 | -7.02669 | -45.27601 | 2026-10-01 04:14:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| c6f66093-b31c-3428-b04c-b0d88cb09f13 | -8.21318 | -45.48109 | 2026-10-01 04:14:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 4a9d9c37-30f7-38ce-a8bc-187499429dec | -7.07625 | -42.31729 | 2026-10-01 04:14:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| dcf369e7-be41-347a-9e95-85021c9c3c96 | -11.71877 | -43.4368 | 2026-10-01 04:14:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| adcebd0f-2b76-342b-b11b-11e570f82873 | -9.90413 | -50.17046 | 2026-10-01 04:14:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 02d03a41-2eb6-3408-91aa-662c6cb7cbce | -4.27355 | -50.75956 | 2026-10-01 04:14:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 38.5 |
| e39b515f-fb1a-3c28-98c1-07ec48646d82 | -5.9098 | -53.48788 | 2026-10-01 04:14:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6b46bbed-355c-35f7-b841-35043d055b2d | -11.83506 | -44.74782 | 2026-10-01 04:14:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b4b17ea4-ae38-317e-b6c8-9c37650d5a01 | -5.18204 | -46.19781 | 2026-10-01 04:14:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 8.9 |
| e6682a2a-0308-3867-ba1c-fd05430f9c63 | -12.52481 | -43.08956 | 2026-10-01 04:14:00 | NPP-375D | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 9dc8b2a1-258b-3d74-a816-799ac73c2685 | -6.72099 | -45.99217 | 2026-10-01 04:14:00 | NPP-375D | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 92c68ae0-daf4-35bf-9ad6-2c89d78381a9 | -4.28888 | -50.81665 | 2026-10-01 04:14:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 16d0deba-63a4-34d8-9969-b6dd829af2ac | -4.63833 | -50.61778 | 2026-10-01 04:14:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ad3fa9ab-9739-3f63-9541-b6fba5227264 | -9.78626 | -44.80742 | 2026-10-01 04:14:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 239a36d6-7529-315d-97d8-a80fa64b373a | -8.62806 | -45.32191 | 2026-10-01 04:14:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b40336b5-a26f-3065-8585-7b6f394a6cbc | -11.4355 | -43.50797 | 2026-10-01 04:14:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ef792581-a30c-3410-a81e-07e50cc13aec | -4.29144 | -50.80225 | 2026-10-01 04:14:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| e87902fc-1365-3a9a-b65a-04fadf608ac1 | -4.26569 | -50.76781 | 2026-10-01 04:14:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 14.3 |
| d0f8fbbf-e1d6-36c8-87ea-a2bad4937abb | -9.21042 | -50.6848 | 2026-10-01 04:14:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1d42b354-25ae-33c9-81dc-2daf57bb2e60 | -11.17207 | -45.11577 | 2026-10-01 04:14:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 32c8dce1-8a69-3152-8c96-948f6aa3e30c | -4.26411 | -50.81219 | 2026-10-01 04:14:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| a6cda6a0-dc1a-3a5c-8083-9e51e57e35b0 | -11.12224 | -44.59377 | 2026-10-01 04:14:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5d07d2cb-e866-3e23-8d7d-79d26946889f | -4.26156 | -50.76606 | 2026-10-01 04:14:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 45.6 |
| e6a1cd6c-13a5-3279-9131-5b65d435ef3e | -5.5372 | -44.83676 | 2026-10-01 04:14:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c228fce8-587e-3a61-af61-51bcc97aa2a5 | -8.24715 | -47.98601 | 2026-10-01 04:14:00 | NPP-375D | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b412b481-be54-323e-8152-dd0a9d70340e | -10.32506 | -47.78769 | 2026-10-01 04:14:00 | NPP-375D | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e22c7c45-b516-3bd7-a132-555da5d51093 | -4.28881 | -50.83043 | 2026-10-01 04:14:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |


[Clique aqui para ver as próximas entradas](README39.md)
