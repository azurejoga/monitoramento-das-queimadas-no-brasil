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

## Dados Diários - Página 166

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1427a82d-24a2-37b6-ab5d-334050e752fb | -9.31113 | -67.6684 | 2024-10-02 05:33:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5a203366-5754-3923-b6ee-698f6ea406e8 | -9.3082 | -67.66349 | 2024-10-02 05:33:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 93aa7534-9203-3ac9-8c0b-86e7ed75454e | -9.30749 | -67.66778 | 2024-10-02 05:33:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5aad3a90-474a-3b87-aca6-b050976dd10c | -9.29998 | -68.81618 | 2024-10-02 05:33:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 99419bcb-7bc1-3fc6-940d-4089dd0fd1fd | -9.28446 | -67.8287 | 2024-10-02 05:33:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 0b1fc3e1-3628-385e-bf49-92d01046dcf5 | -9.28155 | -67.84615 | 2024-10-02 05:33:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8735b54e-25ba-3d91-947a-0f381c5071ca | -9.28083 | -67.8505 | 2024-10-02 05:33:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 98dcefc0-c6cb-311d-bba0-116b738ce3f2 | -9.28079 | -67.82804 | 2024-10-02 05:33:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 0d0cecd2-2930-3d39-aa2a-fb4238c15963 | -9.2801 | -67.85487 | 2024-10-02 05:33:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 388c06c6-885d-364f-8a42-35d06735b236 | -9.28006 | -67.83241 | 2024-10-02 05:33:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 92368806-98df-3eff-8a72-3ca6da80a7d1 | -9.27933 | -67.83678 | 2024-10-02 05:33:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b71e2413-fecf-3f65-bc9a-4f1d4d14906a | -9.27861 | -67.84114 | 2024-10-02 05:33:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 98d8edbc-fdad-319e-b005-bbc1cd328808 | -9.27788 | -67.84549 | 2024-10-02 05:33:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 84be6f42-b007-30ad-8814-80b85ce9cf96 | -9.2775 | -67.60106 | 2024-10-02 05:33:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9c538f67-dab8-39e3-be15-2366534505bf | -9.27639 | -67.83174 | 2024-10-02 05:33:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| afe6bbc3-7009-3fab-9f8a-df068ce7998a | -9.27387 | -67.60045 | 2024-10-02 05:33:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 86702f11-7817-3a29-a2df-49389a586fe7 | -9.27315 | -67.60471 | 2024-10-02 05:33:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1c148fca-7253-36f1-96f1-6002f4abb456 | -9.27243 | -67.60899 | 2024-10-02 05:33:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0e4068a2-cf74-3798-88f9-5bc9fba2773a | -9.27171 | -67.61326 | 2024-10-02 05:33:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b639789c-3da9-37fa-9ba5-73266617469a | -9.27024 | -67.59985 | 2024-10-02 05:33:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b6426e65-0db6-3184-a39a-55c31f565bb2 | -9.26952 | -67.6041 | 2024-10-02 05:33:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3e0f98b0-5989-3d52-9d35-cec1ed1df69c | -9.2688 | -67.60838 | 2024-10-02 05:33:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3da0fda9-e70a-3278-a424-09c4b8427e9c | -9.26761 | -68.8411 | 2024-10-02 05:33:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 23b33246-5124-36ba-845a-34390fbdf54f | -9.2676 | -68.83865 | 2024-10-02 05:33:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 42345f97-aeb8-3874-b652-266ff902d8f4 | -9.26733 | -67.59498 | 2024-10-02 05:33:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| dc1a9a41-2ade-3137-ae85-0e16d05a3605 | -9.26661 | -67.59924 | 2024-10-02 05:33:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bae1bf99-171b-3547-acbd-6fb439843b62 | -9.26661 | -67.59615 | 2024-10-02 05:33:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7fe58976-7663-3196-8396-4d9ab13611ba | -9.26591 | -67.60043 | 2024-10-02 05:33:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5d901922-26a5-35a3-b54a-f16557977047 | -9.26516 | -67.60776 | 2024-10-02 05:33:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2c399852-1b9a-3aa1-a7fa-78138e41e8f3 | -9.26158 | -67.60407 | 2024-10-02 05:33:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| f7e027e0-6b61-3a7e-88d5-46d927049a72 | -9.26153 | -67.60715 | 2024-10-02 05:33:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 8194e704-4e82-3858-9b12-1aff5505dee3 | -9.26088 | -67.60834 | 2024-10-02 05:33:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 3bda2ef5-a54f-3dce-9151-855540bfff50 | -9.26081 | -67.61142 | 2024-10-02 05:33:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 13f17aae-a2ab-360c-a8e8-7238b0bcce47 | -9.25795 | -67.60345 | 2024-10-02 05:33:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 439ad230-69e5-3d49-b90e-edfd18a084da | -9.2579 | -67.60654 | 2024-10-02 05:33:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 71555ca6-3afb-393e-8c9a-1ddb88e515b6 | -9.25725 | -67.60774 | 2024-10-02 05:33:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3685d48b-4c0f-38d5-99c9-ffebce15a38f | -9.25507 | -67.82358 | 2024-10-02 05:33:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 050e0bd2-5766-37a5-abd3-c257d59df1bf | -9.25213 | -67.81859 | 2024-10-02 05:33:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 935eac43-9d29-332a-9cec-3fc299c8cb72 | -9.24755 | -68.81469 | 2024-10-02 05:33:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| dafebc9a-fea8-3c72-91fd-b976eef7fdaa | -9.24552 | -67.81296 | 2024-10-02 05:33:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a170dc30-eb2f-3634-87be-3316be00304f | -9.24479 | -67.81734 | 2024-10-02 05:33:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 13be837d-f772-3bf4-bb95-8095243f3859 | -9.23392 | -68.77683 | 2024-10-02 05:33:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 013164b6-cc7c-36f4-a493-d63b7effed8a | -9.21728 | -67.78275 | 2024-10-02 05:33:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 28be8afa-edc0-347a-bc93-3ea7195f7ca2 | -9.2084 | -68.30685 | 2024-10-02 05:33:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c4d359da-1a0f-327c-b3f5-d3dc347a78dd | -9.19543 | -67.39761 | 2024-10-02 05:33:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4fae1916-c148-360e-ba1b-36c5fbc755dd | -9.19049 | -68.39035 | 2024-10-02 05:33:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b0c06383-096e-3deb-b446-aa952105b095 | -9.1843 | -68.2884 | 2024-10-02 05:33:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b01417df-fadf-3f46-a0c9-d6fcefcd2025 | -9.18351 | -68.29306 | 2024-10-02 05:33:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b6b19088-9714-3325-807c-fff16d091c61 | -9.18052 | -68.28779 | 2024-10-02 05:33:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9562eecd-016d-3ada-8a93-4e9f8c5ab18d | -9.17973 | -68.29243 | 2024-10-02 05:33:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 97a3e189-7b8b-3e0c-b44d-c2fad7545bed | -9.17611 | -68.26798 | 2024-10-02 05:33:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bb23160e-6d22-3871-b928-070aad2f4132 | -9.47314 | -67.48072 | 2024-10-02 05:33:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ad0b7e19-e699-3629-8762-87fef1ad7f58 | -9.37459 | -67.48716 | 2024-10-02 05:33:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d44ef286-50cf-3f12-bb24-0dd482cc2073 | -9.36216 | -67.56293 | 2024-10-02 05:33:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cde858eb-4927-3c58-a694-e185b2246a86 | -9.36184 | -67.5196 | 2024-10-02 05:33:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 250b590a-87df-367c-a15a-a2b386663a70 | -9.36146 | -67.56717 | 2024-10-02 05:33:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c5efd19d-c6cc-3e23-910d-91d66e61b1ff | -9.35853 | -67.56231 | 2024-10-02 05:33:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e9f6d948-06f3-36a3-9b9c-a45f022ede08 | -9.39099 | -67.75105 | 2024-10-02 05:33:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9c33dc66-7cd7-3a8e-a86d-cc8946b4c64a | -9.36613 | -67.74239 | 2024-10-02 05:33:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 77d6739f-313d-3485-b3e2-0d10b6c439c4 | -9.35692 | -68.20676 | 2024-10-02 05:33:00 | NOAA-20 | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 3.0 |
| c13ffdab-396c-3509-8e59-159e573fd73c | -9.35317 | -68.20612 | 2024-10-02 05:33:00 | NOAA-20 | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 8981a45a-dac0-35d6-8420-4023697c96fa | -8.9279 | -67.60574 | 2024-10-02 05:33:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a957e9dd-c4de-366b-a8fe-0c9c61f519b8 | -8.92425 | -67.60514 | 2024-10-02 05:33:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ec37e2d6-f455-389c-a7f4-b2815388434e | -8.92225 | -67.39058 | 2024-10-02 05:33:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 348477cb-1b83-33e0-8cdb-76cb71585748 | -8.92155 | -67.39477 | 2024-10-02 05:33:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d07903b9-da1a-3605-851c-6d458339dade | -8.92086 | -67.39897 | 2024-10-02 05:33:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9de8a710-5663-3ba0-ad45-90be695528b4 | -8.91864 | -67.38997 | 2024-10-02 05:33:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d542871a-947c-3eab-949c-ac72b158ef54 | -8.91794 | -67.39417 | 2024-10-02 05:33:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fd7580a1-63de-305d-8e58-78c45ef987d6 | -8.91725 | -67.39838 | 2024-10-02 05:33:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e56de01c-c692-3c37-a363-7340337e988e | -8.91503 | -67.38936 | 2024-10-02 05:33:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a488ff23-f245-32c5-adee-1aa4cef6cad6 | -8.91433 | -67.39356 | 2024-10-02 05:33:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8d9bab4e-3d1d-3199-85f5-ecb59334ec97 | -8.87496 | -67.72158 | 2024-10-02 05:33:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f78bcab5-6781-3dbb-8f82-004fc683a60d | -8.82856 | -67.38892 | 2024-10-02 05:33:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ec9caa97-4b3e-335f-8b9e-cfbd4d2711a4 | -8.79892 | -67.255 | 2024-10-02 05:33:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6efd3167-11f5-328b-ba98-a42849396104 | -8.79038 | -68.75819 | 2024-10-02 05:33:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 04abe4be-0e45-31ec-b388-220ecf7ebc4a | -8.78953 | -68.76319 | 2024-10-02 05:33:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d9570201-a780-36d2-93cf-2cb67eb5d852 | -8.78547 | -67.29127 | 2024-10-02 05:33:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 93e427e9-943b-33f0-b998-ba97171c7157 | -8.78374 | -68.72634 | 2024-10-02 05:33:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 07080b5b-3c5b-36fc-a9ed-2d80b6390188 | -8.77985 | -68.72564 | 2024-10-02 05:33:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e8379a21-f31a-3f13-a760-49c272b4a50f | -9.13833 | -68.51308 | 2024-10-02 05:33:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 04a6e213-5651-367f-8002-315e7b150cee | -9.1129 | -67.48524 | 2024-10-02 05:33:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 759a5c41-78e0-3eb7-a3b6-d40ba197c47c | -9.10028 | -67.78793 | 2024-10-02 05:33:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6e19d09a-45f5-3650-953f-79714ab1adda | -9.10022 | -67.56149 | 2024-10-02 05:33:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3ccc3c18-9bed-38dc-a5fc-0a28b0b97986 | -9.09871 | -67.5481 | 2024-10-02 05:33:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 912acc05-3223-33d2-ac48-ac029c7a917f | -9.098 | -67.55235 | 2024-10-02 05:33:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 12837e8c-a6f8-3641-aa8c-82bc8009894d | -9.09658 | -67.56087 | 2024-10-02 05:33:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d2c03bd9-f8a0-33e3-bf0f-b84b9d1e4d9e | -9.09516 | -67.5694 | 2024-10-02 05:33:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| c8aeb0bc-fe0f-3bd2-bdbb-4a1cf54bd1f5 | -9.0922 | -67.79105 | 2024-10-02 05:33:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 675c1440-97ba-36cc-abd4-8374b5a60fec | -9.08852 | -67.79044 | 2024-10-02 05:33:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 28c588b8-3e76-3e7f-9598-c6e45dab42e8 | -9.07991 | -67.57121 | 2024-10-02 05:33:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3cb26e4b-a0ac-36e6-b897-6e949cc26f1a | -9.0792 | -67.57547 | 2024-10-02 05:33:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 28d6b7e2-4b83-324f-a56a-521177fe0e97 | -9.05027 | -67.79299 | 2024-10-02 05:33:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 4e8f4591-e692-397b-80b6-d0554565b0b7 | -9.04868 | -67.55397 | 2024-10-02 05:33:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 10955de6-c95d-3f06-9da2-241b2fc4868f | -9.04505 | -67.55335 | 2024-10-02 05:33:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1b3f0ba4-1978-364d-adf1-7a2633903079 | -9.02319 | -67.41474 | 2024-10-02 05:33:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9e0144bc-a931-35c9-ba15-7efa414eb83e | -9.01723 | -67.38358 | 2024-10-02 05:33:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 15f6dffc-77ac-3115-8499-92e0b1d168de | -9.01654 | -67.38776 | 2024-10-02 05:33:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 384ee485-9ddc-3d24-94a8-ebc732faffb1 | -9.01363 | -67.38296 | 2024-10-02 05:33:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 367e1e45-f0d5-35a9-a048-2cc07c2dbd3d | -9.0063 | -67.36031 | 2024-10-02 05:33:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 34a02961-63f2-3c05-96fe-dae266028ca4 | -9.0027 | -67.3597 | 2024-10-02 05:33:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |


[Clique aqui para ver as próximas entradas](README167.md)
