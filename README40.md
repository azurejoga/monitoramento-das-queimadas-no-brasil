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

## Dados Diários - Página 40

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 999e389a-7b83-3c9b-9932-64daf6e67543 | -9.8075 | -43.5011 | 2026-09-11 14:10:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 251.6 |
| 9dd39b61-9b12-35c6-ab36-7f609f6930ca | -9.6951 | -43.3981 | 2026-09-11 14:10:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 106.1 |
| 754ed467-5854-3415-933c-d5f53f16855f | -6.5004 | -47.5909 | 2026-09-11 14:10:00 | GOES-19 | PALMEIRAS DO TOCANTINS | TOCANTINS | Brasil | 1713809 | 17 | 33 | nan | nan | nan | Cerrado | 60.7 |
| 191660b8-2f7b-390a-84e6-9e1f2482f0f4 | -11.3326 | -45.772 | 2026-09-11 14:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 162.4 |
| b6da44b6-eadb-31d5-a55d-5348c4bf71d3 | -22.2649 | -55.8315 | 2026-09-11 14:10:00 | GOES-19 | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 83.9 |
| cdb4bc74-42ad-3323-b6a0-2da1ff5d949f | -7.4595 | -42.1199 | 2026-09-11 14:10:00 | GOES-19 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 92.0 |
| acab27e3-9b41-3978-a6eb-143e92f37c88 | -10.5478 | -51.3367 | 2026-09-11 14:10:00 | GOES-19 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 229.3 |
| bc75cf55-6ab1-322f-8a25-7de797689e64 | -9.1799 | -68.2194 | 2026-09-11 14:10:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 56.1 |
| 858fcd6a-e338-33f3-876e-f3dd9ea5f818 | -9.0431 | -65.3988 | 2026-09-11 14:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 89.3 |
| 698b75bb-8f56-3b33-b464-7cc3ec90bc8a | -9.0245 | -65.3994 | 2026-09-11 14:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 64.1 |
| 6d07a744-8657-3d98-968a-5711478135fa | -7.5553 | -45.1624 | 2026-09-11 14:10:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 78.2 |
| 935f0469-adf0-3465-a7bf-bc17a304c005 | -13.2682 | -61.5775 | 2026-09-11 14:10:00 | GOES-19 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 82.7 |
| 0d2f62fd-ed50-3ad7-9d53-56fcefac8093 | -8.0934 | -54.8488 | 2026-09-11 14:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 59.9 |
| e8267fc4-d232-3a88-a064-641816dc4e79 | -8.0229 | -43.8517 | 2026-09-11 14:10:00 | GOES-19 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Caatinga | 80.7 |
| 73abe82f-359d-3401-aa39-5a143b64e6a4 | -13.249 | -61.5983 | 2026-09-11 14:10:00 | GOES-19 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 62.5 |
| a5bc169a-ee98-381f-8f21-d45fa5cf06ed | -7.9833 | -45.5525 | 2026-09-11 14:10:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 90.6 |
| 71eab237-9967-342d-b54a-ec8e158456b2 | -10.5475 | -51.3578 | 2026-09-11 14:10:00 | GOES-19 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 192.7 |
| 2dca397a-02a1-3f87-b642-c6583cc79e1f | -13.3243 | -61.6709 | 2026-09-11 14:10:00 | GOES-19 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 84.8 |
| 9f4d9a8f-79ab-34ff-a304-5812335a8bbc | -9.0244 | -65.4181 | 2026-09-11 14:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 68.5 |
| 04648046-bc85-3d22-9c64-a0b38880868f | -14.6026 | -48.8601 | 2026-09-11 14:10:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 104.1 |
| 051d9501-cd5d-35f2-a0d9-e042534648e1 | -13.268 | -61.597 | 2026-09-11 14:10:00 | GOES-19 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 142.2 |
| fa3fd913-3134-3cc1-8e39-f34f5fd64c20 | -9.0059 | -65.4186 | 2026-09-11 14:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 51.3 |
| 53f1f50c-7d74-3c07-b797-5b5269722c1e | -8.0021 | -45.5507 | 2026-09-11 14:10:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 99.7 |
| fa0313ef-a691-32ad-ac5a-3d68d6e38c15 | -9.9041 | -45.91 | 2026-09-11 14:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 286.8 |
| 7e65e09b-5048-3ea1-a848-d40fbdec32ff | -11.3513 | -45.7922 | 2026-09-11 14:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 613.6 |
| 9c4eb480-cbe7-392c-b644-ea474f8d14bd | -7.17 | -45.91 | 2026-09-11 14:15:00 | MSG-03 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ff8c120a-1ed8-3d21-b82d-30e897654d7a | -11.9547 | -49.7512 | 2026-09-11 14:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 108.9 |
| 1e7df734-f30e-31fa-bb09-35f8019925f2 | -6.7648 | -59.4408 | 2026-09-11 14:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 61.8 |
| 2a2d142f-1a38-3334-9178-abae436ace25 | -15.038 | -48.4573 | 2026-09-11 14:20:00 | GOES-19 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 151.7 |
| d6cc2c54-37a3-35e3-9c15-6561a4654f05 | -4.8676 | -56.0039 | 2026-09-11 14:20:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 387.4 |
| 065c7672-4fca-3f1a-a04e-d3fa01ad429f | -9.0245 | -65.3994 | 2026-09-11 14:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 72.9 |
| 36efef79-dbcb-3cb9-9f30-c523c92be820 | -13.2278 | -61.8325 | 2026-09-11 14:20:00 | GOES-19 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 58.2 |
| 92a398aa-e966-3fea-affc-da5eeeb392d5 | -9.8075 | -43.5011 | 2026-09-11 14:20:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 158.4 |
| 3d6fdcea-0f0d-320b-9fcc-cdfaca2540d2 | -9.0982 | -65.4904 | 2026-09-11 14:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 50.8 |
| 02b90d42-50e1-38c8-bb3c-7937ae8dc4a9 | -7.9645 | -43.9971 | 2026-09-11 14:20:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 128.5 |
| 8eda3b9c-57c2-3e0c-bc86-df2de3d69798 | -6.2429 | -51.6939 | 2026-09-11 14:20:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 92.9 |
| 5be48c86-a7dd-32e0-b614-b9dd5f5f7479 | -8.0023 | -43.9931 | 2026-09-11 14:20:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 111.7 |
| e14589c6-1a89-3a63-9ed9-14973a9739f0 | -13.2088 | -61.8338 | 2026-09-11 14:20:00 | GOES-19 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 65.2 |
| daff9440-b527-3252-b52d-185fc2dada1f | -8.7252 | -62.4367 | 2026-09-11 14:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 58.3 |
| ce94b7a3-5b8e-3f5e-9bf9-13a9f1c8c79c | -4.8675 | -56.0237 | 2026-09-11 14:20:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 143.0 |
| e43b7846-fb4a-3b32-9c22-0d4017682008 | -9.6951 | -43.3981 | 2026-09-11 14:20:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 99.4 |
| dc4ac278-79f5-3c46-b0b7-06a54b3c8740 | -11.417 | -51.416 | 2026-09-11 14:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 95.1 |
| e1193274-c63a-3f1e-8cab-e1bd127c7f2b | -7.0242 | -59.2374 | 2026-09-11 14:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 61.0 |
| 8a89f4c4-2d09-3e04-9454-99d4e0933859 | -11.4021 | -43.9585 | 2026-09-11 14:20:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 137.2 |
| c175e277-6260-3d65-ac4e-c82bee6ad0e8 | -8.0936 | -54.8286 | 2026-09-11 14:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 59.6 |
| 08dca230-b294-3db5-8952-d66a2b6d22f3 | -9.1799 | -68.2194 | 2026-09-11 14:20:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 50.3 |
| 593c7c15-a641-361c-8910-846802742572 | -9.2276 | -65.5797 | 2026-09-11 14:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 56.8 |
| f0c8a32e-05b8-31b6-a59d-476a8163eb79 | -6.2427 | -51.7146 | 2026-09-11 14:20:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 63.6 |
| c5fff668-4f15-3ced-b85f-b311b6f99e15 | -8.7254 | -62.3987 | 2026-09-11 14:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 57.2 |
| 4fe11010-ea49-309c-9aab-c301273c2cc7 | -13.2682 | -61.5775 | 2026-09-11 14:20:00 | GOES-19 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 103.5 |
| 80461a5a-12a4-3f63-bcd3-9aa1198730d5 | -14.6026 | -48.8601 | 2026-09-11 14:20:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 121.3 |
| f74ff1da-1ab3-3751-b998-dca33fd6222d | -10.5286 | -51.3597 | 2026-09-11 14:20:00 | GOES-19 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 96.0 |
| a217ea0a-feda-3627-b2b7-e9007e593a83 | -13.268 | -61.597 | 2026-09-11 14:20:00 | GOES-19 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 134.1 |
| 613f369e-5d43-398b-962e-e8c222362b53 | -13.249 | -61.5983 | 2026-09-11 14:20:00 | GOES-19 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 65.9 |
| 57f1c7da-0b7d-3c56-9c3d-6d31b660d4c7 | -9.043 | -65.4175 | 2026-09-11 14:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 83.9 |
| 55a1c804-e3cc-3fa1-9425-3c11dc2d41f4 | -7.9831 | -44.0183 | 2026-09-11 14:20:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 86.6 |
| 9fca4ad0-3a84-38ad-b429-8534ed09f481 | -8.6496 | -66.5096 | 2026-09-11 14:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 57.7 |
| 8b870948-2b7e-3a5f-8be3-30cf3975b5ba | -10.5478 | -51.3367 | 2026-09-11 14:20:00 | GOES-19 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 609.8 |
| 270e05ab-c73c-341b-9793-356f67a6675a | -10.2182 | -45.2111 | 2026-09-11 14:20:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 81.4 |
| a7de3f34-b59f-3453-a3a2-5d332ee65c6d | -11.3513 | -45.7922 | 2026-09-11 14:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 371.1 |
| 77416a2b-3f65-3e4e-a032-04be4b33f7fb | -9.0244 | -65.4181 | 2026-09-11 14:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 72.4 |
| 1cf23727-443d-38ad-9bac-ff9503c10fd7 | -11.4026 | -43.935 | 2026-09-11 14:20:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 128.1 |
| 3b5ddb33-e13a-34a8-8789-9d42bc19433b | -9.0059 | -65.4186 | 2026-09-11 14:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 53.2 |
| 9904bb8b-e2af-3e4b-92db-68fa1f9a36e3 | -7.9834 | -43.9951 | 2026-09-11 14:20:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 133.3 |
| aec9447d-2070-3db7-be9d-1418b4e4c4b0 | -9.0431 | -65.3988 | 2026-09-11 14:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 79.4 |
| 37291443-d2b6-3744-9fa6-d683a3c1d9ee | -10.5289 | -51.3386 | 2026-09-11 14:20:00 | GOES-19 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 113.9 |
| 0e1d6e9a-6197-3bff-9f84-f5412ce22b66 | -8.0418 | -43.8497 | 2026-09-11 14:20:00 | GOES-19 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Caatinga | 267.1 |
| 7390516d-b391-3580-a4c6-865e29779243 | -10.5475 | -51.3578 | 2026-09-11 14:20:00 | GOES-19 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 492.7 |
| c64b748f-0da8-3883-b68e-1a9af031eee9 | -6.1993 | -55.2739 | 2026-09-11 14:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 66.4 |
| 2259f9d9-a621-39b6-99fd-6939c226a2e6 | -13.249 | -61.5983 | 2026-09-11 14:30:00 | GOES-19 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 52.3 |
| 949bea7f-ed89-3f99-ab1d-39674757f2af | -10.5289 | -51.3386 | 2026-09-11 14:30:00 | GOES-19 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 118.8 |
| a0633092-ce28-3951-a327-1dc9c334ee72 | -13.3241 | -61.6903 | 2026-09-11 14:30:00 | GOES-19 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 60.9 |
| c901c1b3-3aa3-33f5-9fa5-5e010db1aa5f | -8.688 | -62.4572 | 2026-09-11 14:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 52.7 |
| e8c63af4-09b6-3d21-ac19-f29e2ea78250 | -11.9547 | -49.7512 | 2026-09-11 14:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 156.9 |
| e5f1e17c-a91d-37e6-8372-c90523900bfd | -11.3513 | -45.7922 | 2026-09-11 14:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 310.8 |
| ec4cf4ff-53ea-3fbb-95f8-e06421c6fd18 | -6.2427 | -51.7146 | 2026-09-11 14:30:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 68.0 |
| 31197f53-9e05-36a1-b10c-46da8bae57d3 | -6.2429 | -51.6939 | 2026-09-11 14:30:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 111.6 |
| b6e4eeec-4210-3ffc-b083-cc651d0698be | -13.3243 | -61.6709 | 2026-09-11 14:30:00 | GOES-19 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 88.1 |
| 3935d45d-6341-3c8f-8925-35c1ba720ae7 | -6.1993 | -55.2739 | 2026-09-11 14:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 79.5 |
| de1339fc-288d-37a7-bcb3-f384825a37a6 | -7.1009 | -42.1327 | 2026-09-11 14:30:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 130.8 |
| 1db273ae-07f3-347c-a0be-f70ca1eb85dd | -8.6496 | -66.5096 | 2026-09-11 14:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 73.4 |
| 7a765269-c3d4-315f-9154-5e32762cd434 | -6.7648 | -59.4408 | 2026-09-11 14:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 68.2 |
| 4204a895-0036-3e59-8457-c92f0daba0b6 | -6.7263 | -45.4846 | 2026-09-11 14:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 97.0 |
| d36d86a6-6466-3b85-83e8-3ea9ce7ff528 | -13.268 | -61.597 | 2026-09-11 14:30:00 | GOES-19 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 84.9 |
| 1e43b90a-e733-306a-8201-9b21eb9f4ec4 | -9.2276 | -65.5797 | 2026-09-11 14:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 51.3 |
| 034d72c3-59c8-3b5e-bfee-1ef71a50ef01 | -7.0242 | -59.2374 | 2026-09-11 14:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 62.9 |
| 74be0a1e-75bc-35b3-a2a7-cb2f5241a067 | -4.8491 | -56.0046 | 2026-09-11 14:30:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 82.6 |
| d758829b-63b0-3842-8c15-849a4fbe8ccc | -13.3055 | -61.6527 | 2026-09-11 14:30:00 | GOES-19 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 52.2 |
| 99c5184a-c17b-3f1c-bb0e-351de32d2b91 | -11.0434 | -49.6851 | 2026-09-11 14:30:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 109.8 |
| 09470cc0-2356-3e05-bce1-09fdafaa7ffd | -9.1799 | -68.2194 | 2026-09-11 14:30:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 48.4 |
| 1c56ca0e-7f0b-38e6-9715-a0a624c76eee | -13.3435 | -61.6501 | 2026-09-11 14:30:00 | GOES-19 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 52.3 |
| 2c7f95dc-e588-3a97-94f8-66a50a3e8799 | -4.8676 | -56.0039 | 2026-09-11 14:30:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 290.7 |
| f72fc27c-7e56-3b31-900d-127bf9a6d38d | -10.2743 | -45.2726 | 2026-09-11 14:30:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 117.1 |
| 61072971-4de4-39de-8717-7758cfba9c70 | -7.9834 | -43.9951 | 2026-09-11 14:30:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 115.1 |
| 73776812-e892-3e60-9524-09aae68e6099 | -10.7359 | -46.1465 | 2026-09-11 14:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 141.4 |
| bd3a2239-512a-3322-82dc-71715e5fc5e1 | -7.9645 | -43.9971 | 2026-09-11 14:30:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 127.9 |
| 13595b59-93bc-38eb-8d19-d6d4d5b4e750 | -12.1501 | -64.1414 | 2026-09-11 14:30:00 | GOES-19 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 51.1 |
| 3aa0147e-2903-30ec-b5c3-1a94a9edd178 | -6.5002 | -47.6128 | 2026-09-11 14:30:00 | GOES-19 | PALMEIRAS DO TOCANTINS | TOCANTINS | Brasil | 1713809 | 17 | 33 | nan | nan | nan | Cerrado | 129.0 |
| 132e1a0c-71b2-3da8-a2d5-be88fcfd7a5f | -13.3245 | -61.6514 | 2026-09-11 14:30:00 | GOES-19 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 49.1 |
| 1044c0c0-3a03-372f-82a1-ef24e7b53005 | -9.9045 | -45.8873 | 2026-09-11 14:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 256.2 |


[Clique aqui para ver as próximas entradas](README41.md)
