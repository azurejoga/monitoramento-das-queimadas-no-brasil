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

## Dados Diários - Página 16

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| baad8c84-24a7-3fef-a8b2-d48de22743e0 | -8.81946 | -42.48572 | 2025-11-04 04:12:00 | NPP-375D | CORONEL JOSÉ DIAS | PIAUÍ | Brasil | 2202851 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| b8797454-9555-3c32-a076-4a4a3150baaa | -9.94521 | -44.82112 | 2025-11-04 04:12:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2fc8b4fc-8c13-3260-99ac-ba03e182baac | -7.50096 | -47.0388 | 2025-11-04 04:12:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| eab67b3e-cbcc-3d65-b872-6c2489b50f86 | -9.85207 | -44.13937 | 2025-11-04 04:12:00 | NPP-375D | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 0.2 |
| 460e12d2-003d-3c22-97cd-b303e4aeca38 | -11.84205 | -43.72787 | 2025-11-04 04:12:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 519133dd-a788-31fe-adeb-c6d55632e889 | -7.8192 | -44.44455 | 2025-11-04 04:12:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1433a8b9-017f-3d97-b425-06a125c6f94c | -8.99961 | -35.27122 | 2025-11-04 04:12:00 | NPP-375D | MARAGOGI | ALAGOAS | Brasil | 2704500 | 27 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| fc28ad02-9e93-3476-85cf-f6a3a0a9b7c2 | -12.84792 | -43.32801 | 2025-11-04 04:12:00 | NPP-375D | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 87564e5f-7ae6-357e-bcc8-943268bb9d05 | -11.27765 | -41.74373 | 2025-11-04 04:12:00 | NPP-375D | IRECÊ | BAHIA | Brasil | 2914604 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| c308997f-0a3f-3625-aa41-f2ea17ac2f57 | -11.69074 | -44.1413 | 2025-11-04 04:12:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| aade5159-405a-37c8-8fae-fd3ecebc2f6e | -7.85365 | -44.20922 | 2025-11-04 04:12:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 23e7d9fe-bc41-31ac-82b2-e440ca94d61f | -7.50199 | -47.0392 | 2025-11-04 04:12:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3bc51d46-0f62-3edb-b76d-16115223e839 | -12.91279 | -45.0876 | 2025-11-04 04:12:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0f3eb5c1-dd40-3902-9498-bf9743527b54 | -12.91091 | -45.09908 | 2025-11-04 04:12:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c731614b-9d33-375a-904a-f34221349e5e | -8.99931 | -35.26925 | 2025-11-04 04:12:00 | NPP-375D | MARAGOGI | ALAGOAS | Brasil | 2704500 | 27 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 7a721f55-4fe6-319d-8214-dc60553c2673 | -7.49381 | -47.03777 | 2025-11-04 04:12:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f5b724f7-31c4-38e6-97a4-279a8ba4c10a | -9.88055 | -43.09385 | 2025-11-04 04:12:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| a79442d9-de29-3159-bbbe-66ac8a56a91e | -7.85652 | -44.21364 | 2025-11-04 04:12:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c7534dfc-79d2-3385-9f76-4b88851eae3a | -12.01693 | -43.84903 | 2025-11-04 04:12:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 2ca57847-4e73-3de6-85cc-266f74bdcc82 | -12.85181 | -43.32502 | 2025-11-04 04:12:00 | NPP-375D | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 88d9b8a3-d176-309d-843e-6a0885af36e5 | -7.64473 | -43.72461 | 2025-11-04 04:12:00 | NPP-375D | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 613a3c6e-28f6-35bf-8faa-74313d0d36b6 | -12.90746 | -45.09848 | 2025-11-04 04:12:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e0fc23ca-b098-3f28-8ab5-7512791ffa79 | -9.73629 | -43.8632 | 2025-11-04 04:12:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 9cae2afe-6a5b-3d5f-a2ae-72b9c8b5e39f | -9.31819 | -43.09729 | 2025-11-04 04:12:00 | NPP-375D | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| c67a1db9-6c5d-3dc0-b88d-269a743a7687 | -7.4979 | -47.03847 | 2025-11-04 04:12:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 69f771dd-9515-3714-a00c-e651636e37c4 | -10.9405 | -44.19492 | 2025-11-04 04:12:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 3697bcac-3bc0-391e-96fb-d9f01b5ec672 | -11.14675 | -44.02555 | 2025-11-04 04:12:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| dc5c6a70-06b7-3030-a56a-3ee51204254e | -10.8703 | -44.40846 | 2025-11-04 04:12:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f48247c2-d6b3-339e-8d59-609db71efbbc | -12.13934 | -41.81318 | 2025-11-04 04:12:00 | NPP-375D | SOUTO SOARES | BAHIA | Brasil | 2930808 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 9c9a1bde-e2d0-3083-b227-5e483852486c | -7.06608 | -46.73523 | 2025-11-04 04:12:00 | NPP-375D | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 80d902fb-4764-3aeb-99b8-09108d752c49 | -10.62176 | -44.66345 | 2025-11-04 04:12:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c9ecbca6-f3ec-3b98-b60e-766dd92e0846 | -11.68404 | -41.12291 | 2025-11-04 04:12:00 | NPP-375D | MORRO DO CHAPÉU | BAHIA | Brasil | 2921708 | 29 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 06b09212-8bd7-35e7-9195-b60fda612f79 | -9.31762 | -43.10083 | 2025-11-04 04:12:00 | NPP-375D | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 9fa45995-3cbb-3409-a529-3b24a2b18e72 | -11.11254 | -41.62245 | 2025-11-04 04:12:00 | NPP-375D | SÃO GABRIEL | BAHIA | Brasil | 2929255 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| fbbf50f5-84f1-37ba-ab15-42b4643053d0 | -11.1802 | -41.7976 | 2025-11-04 04:12:00 | NPP-375D | SÃO GABRIEL | BAHIA | Brasil | 2929255 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 7dd44144-e7ee-3fde-9474-087a19a87839 | -9.70742 | -43.93374 | 2025-11-04 04:12:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| ad0dcd8a-86a6-3c1e-8dcc-eed52f997c69 | -13.31929 | -42.41887 | 2025-11-04 04:12:00 | NPP-375D | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| a2808cbc-bab9-3790-81f1-a6debb990d6d | -10.9343 | -44.19009 | 2025-11-04 04:12:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| fabe3465-bef9-3366-b7b9-722d048a9901 | -6.94422 | -45.18179 | 2025-11-04 04:12:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b967184e-9e3b-3197-a62c-bb544e73f56c | -12.2243 | -41.49111 | 2025-11-04 04:12:00 | NPP-375D | IRAQUARA | BAHIA | Brasil | 2914406 | 29 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 49a71c74-39ef-3f8f-9b48-cb8ac5db028b | -8.10809 | -43.82159 | 2025-11-04 04:12:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| ed0c733c-e88e-35b5-98d5-57d625409b54 | -10.85815 | -44.01557 | 2025-11-04 04:12:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 577351c4-63cc-3a4f-b4ca-80ca3b37e3ee | -11.2731 | -41.96136 | 2025-11-04 04:12:00 | NPP-375D | PRESIDENTE DUTRA | BAHIA | Brasil | 2925600 | 29 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 0389391f-db90-3619-9f5c-3aa9ccf62528 | -7.85713 | -44.20983 | 2025-11-04 04:12:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 758fe9e3-ef27-338e-b8d4-92433945614e | -7.61532 | -46.47068 | 2025-11-04 04:12:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 98ddde38-27ab-36ff-82e1-590d2404c81f | -10.93929 | -44.20231 | 2025-11-04 04:12:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| eb2407a8-de59-311f-b966-54b3b664b307 | -9.57197 | -45.13105 | 2025-11-04 04:12:00 | NPP-375D | MONTE ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2206605 | 22 | 33 | nan | nan | nan | Cerrado | 0.4 |
| bba590fa-0bbd-3aac-8f63-7b778f02acd1 | -11.14735 | -44.0219 | 2025-11-04 04:12:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 6dc8ee46-716e-34ba-bf83-7ef334d38269 | -13.32305 | -44.47945 | 2025-11-04 04:12:00 | NPP-375D | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 889779ce-753d-318f-b9d6-543432b59318 | -10.93151 | -44.18583 | 2025-11-04 04:12:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 70dd67a2-38d8-3690-9808-577789c6def7 | -12.13598 | -41.81267 | 2025-11-04 04:12:00 | NPP-375D | SOUTO SOARES | BAHIA | Brasil | 2930808 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 9a123741-79b6-3ef2-ab45-44b917303ae1 | -7.07071 | -46.73238 | 2025-11-04 04:12:00 | NPP-375D | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 43209eaf-6746-35d1-9308-b35edd45f5ef | -8.20979 | -44.82953 | 2025-11-04 04:12:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 76a662f0-9245-3e94-b9cf-c2cb326c6567 | -11.281 | -41.74426 | 2025-11-04 04:12:00 | NPP-375D | IRECÊ | BAHIA | Brasil | 2914604 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 48c841db-7367-399b-bcbe-cdfadac76e23 | -11.8405 | -43.72811 | 2025-11-04 04:12:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 36211a65-5848-3dc8-a8d8-048f3db40b40 | -12.44538 | -43.85712 | 2025-11-04 04:12:00 | NPP-375D | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4bd71fcd-546f-3275-a562-6c7c0bd155ba | -11.73078 | -44.74727 | 2025-11-04 04:12:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ae452013-ad58-3d12-9e3d-4203cf1d9a06 | -7.6184 | -46.47637 | 2025-11-04 04:12:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a7759235-3451-3b76-adf5-78633571f6a6 | -12.41333 | -44.92995 | 2025-11-04 04:12:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 7d8e1d62-bd06-37a2-ad3f-73804bb274e2 | -6.84319 | -46.30131 | 2025-11-04 04:12:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 7cf5a632-cda1-3cbe-916a-31eb545a23d8 | -11.68736 | -44.14074 | 2025-11-04 04:12:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8b4c8fa9-b0e9-3a1f-8a1a-8dfd3b072e0c | -15.7927 | -42.0262 | 2025-11-04 04:14:00 | NPP-375D | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 39def696-f04f-3bce-a40f-1a63f0bb3808 | -13.74709 | -44.00642 | 2025-11-04 04:14:00 | NPP-375D | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8128dc1f-8c55-3b67-8e3d-66708759c9ae | -16.1857 | -42.19536 | 2025-11-04 04:14:00 | NPP-375D | SALINAS | MINAS GERAIS | Brasil | 3157005 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 952b0017-8e69-3b39-8a2d-9eff52554927 | -16.2642 | -45.58134 | 2025-11-04 04:14:00 | NPP-375D | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7296263f-daf0-3e20-ab03-997b1e9bbd23 | -15.83079 | -42.21322 | 2025-11-04 04:14:00 | NPP-375D | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 679d51e3-ea51-3e83-8ce3-a572fadd824b | -15.36473 | -42.73877 | 2025-11-04 04:14:00 | NPP-375D | SANTO ANTÔNIO DO RETIRO | MINAS GERAIS | Brasil | 3160454 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 25c5eda6-2907-345a-9a7c-aa7f7008eb3c | -13.60147 | -43.56495 | 2025-11-04 04:14:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 05ca64be-36f1-3ca3-af33-7ea0c1d035e1 | -15.30173 | -42.97672 | 2025-11-04 04:14:00 | NPP-375D | MONTE AZUL | MINAS GERAIS | Brasil | 3142908 | 31 | 33 | nan | nan | nan | Caatinga | 0.7 |
| a93d6741-d0b2-36e3-8d6d-49a52932037e | -13.42904 | -44.11304 | 2025-11-04 04:14:00 | NPP-375D | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 30d6b48b-be34-3eb0-ad3f-78e929c8fb25 | -15.78528 | -41.46544 | 2025-11-04 04:14:00 | NPP-375D | ÁGUAS VERMELHAS | MINAS GERAIS | Brasil | 3101003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 2fb5fefb-02f7-3717-a0df-169b88f317d6 | -15.5635 | -40.6249 | 2025-11-04 04:14:00 | NPP-375D | RIBEIRÃO DO LARGO | BAHIA | Brasil | 2926657 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| b0d74411-5aa1-3e4e-8dcb-7f1f6975f52c | -15.47568 | -42.87494 | 2025-11-04 04:14:00 | NPP-375D | MATO VERDE | MINAS GERAIS | Brasil | 3141009 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c07e3112-8c05-329a-8bdc-547ae7a5b857 | -14.04692 | -41.7948 | 2025-11-04 04:14:00 | NPP-375D | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 1f1a2ae2-9203-3766-951e-40d21e86ecbb | -15.78876 | -41.46599 | 2025-11-04 04:14:00 | NPP-375D | ÁGUAS VERMELHAS | MINAS GERAIS | Brasil | 3101003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| b9ed9fee-f03f-3045-a4e3-13d7e1628f30 | -14.1571 | -42.21833 | 2025-11-04 04:14:00 | NPP-375D | LAGOA REAL | BAHIA | Brasil | 2918753 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| d3430868-d5f9-33e3-9681-29986dc9c1ca | -14.19686 | -42.2061 | 2025-11-04 04:14:00 | NPP-375D | RIO DO ANTÔNIO | BAHIA | Brasil | 2926806 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 77f241eb-ded2-38b3-b593-8982cc05f02d | -16.26609 | -45.56995 | 2025-11-04 04:14:00 | NPP-375D | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c72d2a2b-0985-33fe-b40d-4c1df9733223 | -14.56245 | -43.26743 | 2025-11-04 04:14:00 | NPP-375D | SEBASTIÃO LARANJEIRAS | BAHIA | Brasil | 2930006 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c8d67223-c7a4-3953-92f1-d92068f879d4 | -15.36417 | -42.74242 | 2025-11-04 04:14:00 | NPP-375D | SANTO ANTÔNIO DO RETIRO | MINAS GERAIS | Brasil | 3160454 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d88d244d-9c5e-3953-b071-9025999a617c | -13.71983 | -43.6101 | 2025-11-04 04:14:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e3c9f9a7-161f-3471-9b0f-01bcd26315d8 | -14.86078 | -40.72947 | 2025-11-04 04:14:00 | NPP-375D | VITÓRIA DA CONQUISTA | BAHIA | Brasil | 2933307 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| d27c3756-c040-3dbb-bb31-69dee1dfa7a3 | -16.26672 | -45.56615 | 2025-11-04 04:14:00 | NPP-375D | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 89914a9f-9c96-37fb-a4a1-6f777dfbae51 | -16.26483 | -45.57755 | 2025-11-04 04:14:00 | NPP-375D | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3ee123f9-453b-37d3-9409-c5de37977265 | -15.79326 | -42.02244 | 2025-11-04 04:14:00 | NPP-375D | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 92e7f960-5025-3c6f-9c74-67b1a4b51623 | -14.68876 | -43.15283 | 2025-11-04 04:14:00 | NPP-375D | ESPINOSA | MINAS GERAIS | Brasil | 3124302 | 31 | 33 | nan | nan | nan | Caatinga | 0.6 |
| bf8fdacb-d609-367e-8ccd-300256aeb602 | -17.50069 | -44.49607 | 2025-11-04 04:14:00 | NPP-375D | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d96b1ba1-f1af-30df-bbaa-d8e0afd9fab1 | -15.58739 | -42.9417 | 2025-11-04 04:14:00 | NPP-375D | PORTEIRINHA | MINAS GERAIS | Brasil | 3152204 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 25e3dab8-d51f-379d-9411-551bbf3fd2df | -16.27658 | -45.59138 | 2025-11-04 04:14:00 | NPP-375D | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9be742f3-0541-3ea6-beec-260bc07164a3 | -15.34251 | -42.86095 | 2025-11-04 04:14:00 | NPP-375D | MATO VERDE | MINAS GERAIS | Brasil | 3141009 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 95116270-df72-381d-a561-e6dbf06033b9 | -14.15373 | -42.21782 | 2025-11-04 04:14:00 | NPP-375D | LAGOA REAL | BAHIA | Brasil | 2918753 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| d82a5bb0-f635-3407-b5b4-a8f4645630cf | -16.26394 | -45.56175 | 2025-11-04 04:14:00 | NPP-375D | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 3a823506-d60d-3286-ab9d-5317717cbe8d | -16.26546 | -45.57375 | 2025-11-04 04:14:00 | NPP-375D | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 29a60066-d2ef-38c5-9e4d-81aee43f401e | -16.02276 | -42.90093 | 2025-11-04 04:14:00 | NPP-375D | RIACHO DOS MACHADOS | MINAS GERAIS | Brasil | 3154507 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9821a562-df06-3aad-b271-ad925cb69d6a | -20.17246 | -49.68219 | 2025-11-04 04:14:00 | NPP-375D | PONTES GESTAL | SÃO PAULO | Brasil | 3540309 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 142727d0-cea2-3dbb-8c94-4dbd2f5dd85b | -14.69209 | -43.15339 | 2025-11-04 04:14:00 | NPP-375D | ESPINOSA | MINAS GERAIS | Brasil | 3124302 | 31 | 33 | nan | nan | nan | Caatinga | 0.6 |
| b0371cbe-8556-3bf5-a810-62159a39a595 | -15.30507 | -42.97727 | 2025-11-04 04:14:00 | NPP-375D | MONTE AZUL | MINAS GERAIS | Brasil | 3142908 | 31 | 33 | nan | nan | nan | Caatinga | 1.3 |
| fd6fd287-42af-3857-b237-ddd21b62f119 | -16.02896 | -45.16182 | 2025-11-04 04:14:00 | NPP-375D | PINTÓPOLIS | MINAS GERAIS | Brasil | 3150570 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6c4e2f0f-9997-3725-a17a-189d754116dc | -16.26331 | -45.56555 | 2025-11-04 04:14:00 | NPP-375D | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2feecd8a-132f-3f5f-a827-8ea48b685c5a | -15.32748 | -41.73775 | 2025-11-04 04:14:00 | NPP-375D | NINHEIRA | MINAS GERAIS | Brasil | 3144656 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |


[Clique aqui para ver as próximas entradas](README17.md)
