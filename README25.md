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

## Dados Diários - Página 25

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1fb09076-ee2f-3b66-b263-e51ea07b3ccb | -2.28703 | -48.57787 | 2025-09-04 04:25:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2656297d-5f22-3e91-b25c-950e9f3087fb | -3.40222 | -46.90479 | 2025-09-04 04:25:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c5aeae1d-2a8f-31c0-8b0f-2a7b7ceff21b | -6.80235 | -44.64009 | 2025-09-04 04:25:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| c9d721b0-9b89-3ca3-b14c-f7e3f03e379d | -6.42 | -44.68823 | 2025-09-04 04:25:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c488ef2b-bc58-3bbe-8bfc-b387de855107 | -6.4533 | -43.98554 | 2025-09-04 04:25:00 | NOAA-21 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| def72349-6736-3462-b0f6-5985cd0b637b | -8.03005 | -44.0467 | 2025-09-04 04:25:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e78de96a-2b9a-3c2c-9745-ce350a495211 | -5.31707 | -55.8555 | 2025-09-04 04:25:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 4c55d4ae-917a-3ddd-bf3a-f0864ba1c616 | -8.02292 | -44.11922 | 2025-09-04 04:25:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 09d5b318-12e2-3ce5-9dd1-f5b89a05a1c6 | -6.6863 | -48.41317 | 2025-09-04 04:25:00 | NOAA-21 | XAMBIOÁ | TOCANTINS | Brasil | 1722107 | 17 | 33 | nan | nan | nan | Amazônia | 5.1 |
| a8655f3f-b9d0-316e-9232-3c1649607102 | -6.25157 | -42.64418 | 2025-09-04 04:25:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| e5ab3d4b-afb2-3856-a402-06fa068d7a64 | -6.23484 | -43.53806 | 2025-09-04 04:25:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 667cc8e6-0fa0-3d42-ac1a-446519370579 | -6.69264 | -43.86396 | 2025-09-04 04:25:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f5cbe0a0-a092-3ea1-871a-5d5c58e39460 | -4.98216 | -49.90696 | 2025-09-04 04:25:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| eec26f90-4044-3107-833a-527566e71cce | -6.84285 | -46.40006 | 2025-09-04 04:25:00 | NOAA-21 | SÃO PEDRO DOS CRENTES | MARANHÃO | Brasil | 2111573 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| e289ec7a-d761-3b79-90cb-809939f008e9 | -6.41696 | -43.26292 | 2025-09-04 04:25:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c18bce81-82a1-3b96-9413-26843e95e579 | -6.26645 | -43.28486 | 2025-09-04 04:25:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 35e2e6e8-a35f-3451-a812-42b5e72d232f | -6.78736 | -44.4627 | 2025-09-04 04:25:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 11.0 |
| fbf19b1c-2ee7-3e22-b31f-424c6e0d83fa | -3.16699 | -48.80732 | 2025-09-04 04:25:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 065bea54-e4ab-3fa8-b6c2-be6d831aab89 | -6.05512 | -45.03195 | 2025-09-04 04:25:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c6653242-144b-3ed6-b554-959d17b2bead | -5.86657 | -46.11847 | 2025-09-04 04:25:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| aed0c8e5-6761-3245-9417-28d8b789a53a | -7.49854 | -44.81291 | 2025-09-04 04:25:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3e3c8fe5-77ae-392f-b471-259d58b21664 | -6.15974 | -43.32085 | 2025-09-04 04:25:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 0f92029d-0f53-3a6e-825c-c6814f744891 | -5.94667 | -43.02672 | 2025-09-04 04:25:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 92f73a7c-6f0a-3d0d-8a84-114853473e4c | -7.14461 | -44.44209 | 2025-09-04 04:25:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c1cfbe24-4c0d-3f33-920d-41b808de0b15 | -4.00072 | -47.14364 | 2025-09-04 04:25:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5d24bdbc-d6f3-3d0b-b4c9-455c012f13e8 | -5.69768 | -45.12245 | 2025-09-04 04:25:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bd0bfdab-1e8a-3291-818b-60c7314fef31 | -6.37937 | -43.01173 | 2025-09-04 04:25:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1fa22f2f-0b80-3a86-b248-20346ab67de5 | -6.26455 | -43.50911 | 2025-09-04 04:25:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 560a041c-9a90-3370-970b-75fb30e52140 | -6.16396 | -43.31724 | 2025-09-04 04:25:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 13.7 |
| db17f788-47dc-38e9-8169-ef2420944d2b | -8.02945 | -44.05077 | 2025-09-04 04:25:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 34884f07-0bb8-332f-8fd0-4920973939e3 | -4.90063 | -41.75813 | 2025-09-04 04:25:00 | NOAA-21 | SIGEFREDO PACHECO | PIAUÍ | Brasil | 2210656 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 8ffbfa19-cd93-3d5d-a96f-9b7e48ca8c78 | -6.75481 | -45.91852 | 2025-09-04 04:25:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c02d5b10-97f7-3522-9ff6-cd44119b7422 | -7.17613 | -44.92601 | 2025-09-04 04:25:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f70e7d3b-a584-32bc-a9d0-7d4b6d7070d2 | -5.6898 | -45.94263 | 2025-09-04 04:25:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e55c35bc-57aa-3b4d-8ab4-f92194e39700 | -6.02611 | -46.66304 | 2025-09-04 04:25:00 | NOAA-21 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8346d804-c3ef-3c17-b42f-ce9b48806f5b | -7.79865 | -45.42772 | 2025-09-04 04:25:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ea5f0bb9-48ba-3f80-aba0-b7d5cc597711 | -5.31581 | -55.86122 | 2025-09-04 04:25:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1aa634ab-4b28-341a-a2b4-6852eb45318c | -6.02725 | -46.67736 | 2025-09-04 04:25:00 | NOAA-21 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| da6beb63-504f-3dd4-bbe5-f400b4dfb826 | -7.18637 | -44.16674 | 2025-09-04 04:25:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0883dfe6-eae8-3c11-9497-fd5a44fb7e92 | -5.90174 | -45.95794 | 2025-09-04 04:25:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1d8e297a-6d50-3319-8bfc-6c13cd45160f | -8.02885 | -44.05483 | 2025-09-04 04:25:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| dfde446f-f64d-317f-b379-3c707fd9d7cb | -6.18847 | -44.18156 | 2025-09-04 04:25:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 99f86e1a-c6a3-36a2-ab56-cd90f7432ed3 | -3.79405 | -49.43225 | 2025-09-04 04:25:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c1292f11-07a8-350d-90c1-df9ca02c2ff0 | -4.56591 | -40.34885 | 2025-09-04 04:25:00 | NOAA-21 | HIDROLÂNDIA | CEARÁ | Brasil | 2305209 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| dd3ea931-7896-3622-8bf8-51c3bd914db5 | -7.509 | -45.36853 | 2025-09-04 04:25:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2ac211b6-bda2-35b5-95c9-2cce09a7b4cb | -5.91155 | -43.23506 | 2025-09-04 04:25:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 1.9 |
| c80aa8bd-8582-3a5e-a2f0-466226792d32 | -5.38116 | -45.95761 | 2025-09-04 04:25:00 | NOAA-21 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| bd3c73be-35b8-3c24-9473-6f1d341d71ca | -7.36576 | -44.32331 | 2025-09-04 04:25:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 95a929a5-1be7-3973-9c99-0ed57db4ec4f | -5.60734 | -45.02525 | 2025-09-04 04:25:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 444347d7-b307-3865-a789-90df8c19659c | -7.01468 | -43.24184 | 2025-09-04 04:25:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 922e04ff-8550-3021-b4cf-128d6ab77a58 | -6.49839 | -43.09034 | 2025-09-04 04:25:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 543b4d42-1c4c-307b-b9de-2fe69de86e82 | -6.26161 | -43.29253 | 2025-09-04 04:25:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2da0d1e5-ec24-34f4-b7d4-6c7f74544e0a | -6.31908 | -43.77442 | 2025-09-04 04:25:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| de7429f5-52fb-3b23-8775-42149c3541db | -6.17049 | -43.31248 | 2025-09-04 04:25:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 91f880c3-73bd-382e-bc70-e0c7255af83a | -5.845 | -45.29357 | 2025-09-04 04:25:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d7579c90-6d93-3db0-87f4-a12026a27ef3 | -5.38608 | -45.94779 | 2025-09-04 04:25:00 | NOAA-21 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 04887790-46a1-3b50-9400-b8543ecdbf09 | -8.0258 | -44.14829 | 2025-09-04 04:25:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| e94b0c9c-2142-3f4f-a02e-e177235fb8c1 | -6.69653 | -48.41487 | 2025-09-04 04:25:00 | NOAA-21 | XAMBIOÁ | TOCANTINS | Brasil | 1722107 | 17 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0d8d6436-c6df-3163-ae1b-ae7cd1e688d6 | -5.88968 | -45.97019 | 2025-09-04 04:25:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7131e4fd-c077-39b4-b6bc-0381bb03dfc4 | -6.25957 | -43.59122 | 2025-09-04 04:25:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| fc95846e-25a4-3227-82fb-26baa19914ad | -7.01041 | -43.24551 | 2025-09-04 04:25:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| bd7fcf95-ff3a-3749-80fc-b785ac4ae53d | -6.68132 | -48.4007 | 2025-09-04 04:25:00 | NOAA-21 | XAMBIOÁ | TOCANTINS | Brasil | 1722107 | 17 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 89056533-c7aa-3780-8021-a3e78e0f286d | -6.57278 | -44.71902 | 2025-09-04 04:25:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3a7506e3-e1dc-37ae-b7ea-46314fae9503 | -8.09209 | -42.42744 | 2025-09-04 04:25:00 | NOAA-21 | SÃO JOÃO DO PIAUÍ | PIAUÍ | Brasil | 2210003 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| c6769bde-da95-30ce-b3cb-b5ea2cd70557 | -6.53652 | -42.93723 | 2025-09-04 04:25:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e9eb958e-3eba-3653-a631-e08a5c6f6f45 | -6.81735 | -45.66744 | 2025-09-04 04:25:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 77b8e47c-6cf1-3cfd-a703-84334455ae6d | -6.41273 | -43.26657 | 2025-09-04 04:25:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 08bd435d-f8b6-3447-914a-b032193c4e9d | -5.69838 | -45.16235 | 2025-09-04 04:25:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 59c32d31-1756-3432-837d-b4dc4a67a382 | -6.82981 | -44.2753 | 2025-09-04 04:25:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0a46c4fe-dc5f-30bd-ba77-0e0e3fb047a6 | -5.81725 | -45.29646 | 2025-09-04 04:25:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a114375b-04eb-3db1-a9dc-eaad111a451f | -6.05373 | -43.4178 | 2025-09-04 04:25:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 68cf1147-7869-312a-9b49-042ec7eecad2 | -5.18295 | -46.07074 | 2025-09-04 04:25:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b491083a-b574-3f99-8db0-0b9c7bfbcb51 | -7.05498 | -50.86547 | 2025-09-04 04:25:00 | NOAA-21 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 9d0ea567-edc6-3ad8-acb1-dce44a3c79f4 | -6.17648 | -47.28554 | 2025-09-04 04:25:00 | NOAA-21 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 48b1329c-aa54-3a99-9db5-777b453498f4 | -5.89417 | -42.98011 | 2025-09-04 04:25:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 5ed6d055-074a-34a5-addd-a72f8360af34 | -4.5654 | -40.35233 | 2025-09-04 04:25:00 | NOAA-21 | HIDROLÂNDIA | CEARÁ | Brasil | 2305209 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 6513ac1c-8942-371b-9482-633187740312 | -5.77056 | -45.42208 | 2025-09-04 04:25:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2758af77-8199-39a5-90d3-61a0861d99c7 | -4.84096 | -42.74041 | 2025-09-04 04:25:00 | NOAA-21 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 355865c8-6e8a-3eca-b74c-938e5474da6f | -5.85271 | -45.65966 | 2025-09-04 04:25:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| eb5f015b-ad8a-3b88-a64b-deccce2b226d | -4.99838 | -56.2554 | 2025-09-04 04:25:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 25.1 |
| 7f1ab27b-1c41-3bc0-bbf6-0ec5c93d2728 | -6.88796 | -45.5632 | 2025-09-04 04:25:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 52b74cda-73d4-3ceb-b590-b15441959b27 | -6.31123 | -44.3884 | 2025-09-04 04:25:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ba4f6479-896c-3677-a9e5-3e7aeb95d236 | -7.13082 | -44.46329 | 2025-09-04 04:25:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b182733b-e4b4-3c30-a759-b9f01494f0ca | -5.90485 | -45.56445 | 2025-09-04 04:25:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 43fac8a5-6690-3120-938b-a041476b5487 | -5.72522 | -45.56145 | 2025-09-04 04:25:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 802b279d-06f0-3c4d-a9be-31a6d74f92fe | -6.16629 | -43.3161 | 2025-09-04 04:25:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 7164faab-9bad-3b9e-9f21-981db4ad1115 | -6.29315 | -43.31683 | 2025-09-04 04:25:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| b44d8a3b-e3fc-3ce5-be8c-1b29960898a7 | -6.76035 | -45.92648 | 2025-09-04 04:25:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c4c490d5-877a-3773-abac-78f60a9adf54 | -6.16332 | -43.32138 | 2025-09-04 04:25:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 10.9 |
| b6316658-2fc7-3305-a411-46cff96f5c8e | -6.87299 | -45.57183 | 2025-09-04 04:25:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 3478964c-cf0e-3575-a5c3-943ef3fe713a | -6.23543 | -43.55852 | 2025-09-04 04:25:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4aab38d8-6873-3c07-ae9c-013d878d4dd2 | -6.22373 | -42.44661 | 2025-09-04 04:25:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 526156fb-a894-372e-aed9-06c11a1a3655 | -6.23333 | -43.40609 | 2025-09-04 04:25:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| eae69083-3afb-364b-b737-8e89443863de | -5.89237 | -43.362 | 2025-09-04 04:25:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 323df43e-e4ac-391d-9178-5b87f9bdbb42 | -4.89991 | -41.76297 | 2025-09-04 04:25:00 | NOAA-21 | SIGEFREDO PACHECO | PIAUÍ | Brasil | 2210656 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 11cdf56b-237c-3f51-ac93-60d5259090a8 | -5.60788 | -45.02171 | 2025-09-04 04:25:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 15.2 |
| 2bac44d3-9af2-358b-b732-842fcfec891f | -6.50505 | -43.09555 | 2025-09-04 04:25:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 2d0bbfd7-a347-3898-b17b-8096e41e3cf7 | -8.0305 | -44.14086 | 2025-09-04 04:25:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 5.7 |
| a683b6d2-790c-3b67-811f-395b0dd0b8c0 | -6.22913 | -43.40968 | 2025-09-04 04:25:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b4bc419e-bfe1-3cdc-bc01-e922449753a2 | -6.26206 | -43.31362 | 2025-09-04 04:25:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |


[Clique aqui para ver as próximas entradas](README26.md)
