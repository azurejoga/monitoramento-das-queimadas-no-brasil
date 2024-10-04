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

## Dados Diários - Página 171

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4e6ae332-6de5-3d80-9116-e04e30786a8c | -21.84508 | -48.43079 | 2024-10-04 04:59:00 | NOAA-20 | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6da489da-9aa1-3c7b-b14f-b6649df434bd | -21.84475 | -48.43417 | 2024-10-04 04:59:00 | NOAA-20 | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 18affa0c-afbf-3a11-a250-60fc565a634e | -21.84442 | -48.43757 | 2024-10-04 04:59:00 | NOAA-20 | GAVIÃO PEIXOTO | SÃO PAULO | Brasil | 3516853 | 35 | 33 | nan | nan | nan | Cerrado | 1.7 |
| bb605cf9-2e74-33cc-a0f8-8439a6b67fb5 | -21.84376 | -48.44432 | 2024-10-04 04:59:00 | NOAA-20 | GAVIÃO PEIXOTO | SÃO PAULO | Brasil | 3516853 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 78ea9684-b858-3b62-8185-205bccd65aef | -21.84343 | -48.44766 | 2024-10-04 04:59:00 | NOAA-20 | GAVIÃO PEIXOTO | SÃO PAULO | Brasil | 3516853 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7b5398b5-101f-315f-b5e8-9cc57588a0f7 | -21.84019 | -48.42682 | 2024-10-04 04:59:00 | NOAA-20 | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4ed16427-77a0-3341-b936-2c477264fc39 | -21.83986 | -48.43024 | 2024-10-04 04:59:00 | NOAA-20 | GAVIÃO PEIXOTO | SÃO PAULO | Brasil | 3516853 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6884950e-20f0-3002-8db9-05ecd807d162 | -21.83687 | -48.45378 | 2024-10-04 04:59:00 | NOAA-20 | GAVIÃO PEIXOTO | SÃO PAULO | Brasil | 3516853 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1b77992a-4d6f-3a98-8268-943f9b1098c3 | -21.83233 | -48.45348 | 2024-10-04 04:59:00 | NOAA-20 | GAVIÃO PEIXOTO | SÃO PAULO | Brasil | 3516853 | 35 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ab4562ef-b359-3f87-8ba9-7b0b981d0ac6 | -21.83201 | -48.4568 | 2024-10-04 04:59:00 | NOAA-20 | GAVIÃO PEIXOTO | SÃO PAULO | Brasil | 3516853 | 35 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 32178877-628f-3a29-b2dc-e64fdacb7311 | -21.83165 | -48.45338 | 2024-10-04 04:59:00 | NOAA-20 | GAVIÃO PEIXOTO | SÃO PAULO | Brasil | 3516853 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b5534130-3fc0-36cc-804e-06a4f0b9153f | -21.8313 | -48.45669 | 2024-10-04 04:59:00 | NOAA-20 | GAVIÃO PEIXOTO | SÃO PAULO | Brasil | 3516853 | 35 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0b77ea77-89d7-3cb1-9157-82c58a497a2f | -21.82646 | -48.45977 | 2024-10-04 04:59:00 | NOAA-20 | GAVIÃO PEIXOTO | SÃO PAULO | Brasil | 3516853 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f6fdf03c-c971-3af7-8e11-6284b9ba2cf6 | -21.82573 | -48.45967 | 2024-10-04 04:59:00 | NOAA-20 | GAVIÃO PEIXOTO | SÃO PAULO | Brasil | 3516853 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0f9a46b2-690f-32e6-9bfb-3e1fd569f7b7 | -21.80069 | -48.44701 | 2024-10-04 04:59:00 | NOAA-20 | GAVIÃO PEIXOTO | SÃO PAULO | Brasil | 3516853 | 35 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 567d3140-6178-3d6b-8a57-a902918de048 | -21.79513 | -48.44992 | 2024-10-04 04:59:00 | NOAA-20 | GAVIÃO PEIXOTO | SÃO PAULO | Brasil | 3516853 | 35 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4bddd9af-4862-3594-8e3c-94db54bf178e | -21.79478 | -48.45338 | 2024-10-04 04:59:00 | NOAA-20 | GAVIÃO PEIXOTO | SÃO PAULO | Brasil | 3516853 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4affd1f7-90e4-319e-bd15-aee9a3324868 | -21.78957 | -48.45279 | 2024-10-04 04:59:00 | NOAA-20 | GAVIÃO PEIXOTO | SÃO PAULO | Brasil | 3516853 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4542c93f-9bed-3407-8142-9925073b6544 | -21.85129 | -48.36692 | 2024-10-04 04:59:00 | NOAA-20 | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ed761c04-ad94-3c9b-8ddc-29d0abd7d9e5 | -21.85097 | -48.3703 | 2024-10-04 04:59:00 | NOAA-20 | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e54bc205-68ad-3424-956f-cd894eda97af | -21.84933 | -48.3871 | 2024-10-04 04:59:00 | NOAA-20 | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d5ff43bc-edf2-32c5-b96a-423dd735ca8b | -21.846 | -48.36689 | 2024-10-04 04:59:00 | NOAA-20 | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 5ba3dff9-a242-327c-a336-041b5efcb979 | -21.84592 | -48.36692 | 2024-10-04 04:59:00 | NOAA-20 | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 28105377-9ae1-3f06-8f03-623c49393e10 | -21.84568 | -48.37019 | 2024-10-04 04:59:00 | NOAA-20 | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0acc319b-bb39-323d-9c42-f1ea21d7b0ff | -21.84558 | -48.37022 | 2024-10-04 04:59:00 | NOAA-20 | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5cfffa48-c242-3a02-b20f-e081e6edce29 | -21.84536 | -48.37349 | 2024-10-04 04:59:00 | NOAA-20 | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1640a498-885a-3eaf-bfc8-02bb4d26bf03 | -21.84524 | -48.37351 | 2024-10-04 04:59:00 | NOAA-20 | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 25576e7e-aa42-3580-a076-fa749f57ee45 | -21.84375 | -48.39008 | 2024-10-04 04:59:00 | NOAA-20 | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | 5.5 |
| dbb9b290-b9dc-3c29-9d74-85756dca1caf | -21.84352 | -48.39008 | 2024-10-04 04:59:00 | NOAA-20 | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 67701cfb-7d21-3700-80c0-ea56eea0c33b | -21.84341 | -48.39362 | 2024-10-04 04:59:00 | NOAA-20 | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 253e2102-3976-3bba-9f7b-b443ef55686b | -21.84315 | -48.39361 | 2024-10-04 04:59:00 | NOAA-20 | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | 7.5 |
| f71723a6-b2d6-3cb2-9ab7-8e10cf72812f | -21.83851 | -48.38962 | 2024-10-04 04:59:00 | NOAA-20 | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 4d507815-36f6-3b07-b6f4-c95d5b37b3c6 | -21.83827 | -48.38963 | 2024-10-04 04:59:00 | NOAA-20 | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 5a0060ed-ef90-33c9-b30e-ca0c5b36215d | -21.83817 | -48.3932 | 2024-10-04 04:59:00 | NOAA-20 | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | 5.5 |
| cf22d1a9-6d8d-3d85-88f2-800872f19ed2 | -21.8379 | -48.3932 | 2024-10-04 04:59:00 | NOAA-20 | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 7cd80867-7d5c-355b-925b-85089d6a1132 | -21.83783 | -48.39672 | 2024-10-04 04:59:00 | NOAA-20 | GAVIÃO PEIXOTO | SÃO PAULO | Brasil | 3516853 | 35 | 33 | nan | nan | nan | Cerrado | 3.8 |
| c9289ec3-acb9-3beb-b35f-87a08950dae2 | -21.83754 | -48.39671 | 2024-10-04 04:59:00 | NOAA-20 | GAVIÃO PEIXOTO | SÃO PAULO | Brasil | 3516853 | 35 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 0c043df7-42ac-33af-8234-0a234eeadaa8 | -21.8375 | -48.40013 | 2024-10-04 04:59:00 | NOAA-20 | GAVIÃO PEIXOTO | SÃO PAULO | Brasil | 3516853 | 35 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 5c9be80c-a20f-3b7b-9a76-e6e66a65d297 | -21.83718 | -48.40012 | 2024-10-04 04:59:00 | NOAA-20 | GAVIÃO PEIXOTO | SÃO PAULO | Brasil | 3516853 | 35 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 7baf3fa2-6cc4-33f4-b869-5eba777e028c | -21.83455 | -48.37579 | 2024-10-04 04:59:00 | NOAA-20 | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 28097e89-33e6-3500-9f30-2af264480352 | -21.83441 | -48.37582 | 2024-10-04 04:59:00 | NOAA-20 | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 42b918d5-7a4d-3961-8afa-807df3659bd2 | -21.83424 | -48.37909 | 2024-10-04 04:59:00 | NOAA-20 | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 410a4066-d0a2-3177-88d4-f7f194f7a1f8 | -21.83407 | -48.37912 | 2024-10-04 04:59:00 | NOAA-20 | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 40b2ac8d-668e-389b-b208-6cb9d03693cf | -21.83392 | -48.38243 | 2024-10-04 04:59:00 | NOAA-20 | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3f9fa787-2def-30f9-8ae5-ed30f0e5ca25 | -21.83372 | -48.38247 | 2024-10-04 04:59:00 | NOAA-20 | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6f8a518a-eac5-38bd-b89e-b49b4457c8af | -21.83359 | -48.38582 | 2024-10-04 04:59:00 | NOAA-20 | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c180e421-7149-3911-81bd-5b870f806ce2 | -21.83337 | -48.38585 | 2024-10-04 04:59:00 | NOAA-20 | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d7848a70-7e85-3f94-a8ee-9ff289efcf94 | -21.83326 | -48.38926 | 2024-10-04 04:59:00 | NOAA-20 | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 4895e53e-e1de-3185-8e6e-7749277e7146 | -21.83302 | -48.38928 | 2024-10-04 04:59:00 | NOAA-20 | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 604aac38-51a9-3201-a736-13742f608c06 | -21.83292 | -48.39275 | 2024-10-04 04:59:00 | NOAA-20 | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 0e760af2-362b-3e79-9928-83e0b86b6afe | -21.83266 | -48.39277 | 2024-10-04 04:59:00 | NOAA-20 | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | 9.7 |
| c332b42c-eb9b-3164-8505-a4a79272bf5f | -21.83259 | -48.3962 | 2024-10-04 04:59:00 | NOAA-20 | GAVIÃO PEIXOTO | SÃO PAULO | Brasil | 3516853 | 35 | 33 | nan | nan | nan | Cerrado | 20.2 |
| 98add0db-770d-3784-8de9-bc3c156e1223 | -21.8323 | -48.3962 | 2024-10-04 04:59:00 | NOAA-20 | GAVIÃO PEIXOTO | SÃO PAULO | Brasil | 3516853 | 35 | 33 | nan | nan | nan | Cerrado | 18.5 |
| c0c25827-3351-31a9-84ee-ec81cdacfff2 | -21.83227 | -48.39953 | 2024-10-04 04:59:00 | NOAA-20 | GAVIÃO PEIXOTO | SÃO PAULO | Brasil | 3516853 | 35 | 33 | nan | nan | nan | Cerrado | 20.2 |
| 5f98f304-b59a-32b5-98b5-c9bc0bfd5916 | -21.83196 | -48.39952 | 2024-10-04 04:59:00 | NOAA-20 | GAVIÃO PEIXOTO | SÃO PAULO | Brasil | 3516853 | 35 | 33 | nan | nan | nan | Cerrado | 18.5 |
| a6e22c83-a640-383b-be7d-941bb4f7f8b1 | -21.83195 | -48.40282 | 2024-10-04 04:59:00 | NOAA-20 | GAVIÃO PEIXOTO | SÃO PAULO | Brasil | 3516853 | 35 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 20b439f7-9f84-3a3d-8858-22f80970dd3e | -21.83162 | -48.40279 | 2024-10-04 04:59:00 | NOAA-20 | GAVIÃO PEIXOTO | SÃO PAULO | Brasil | 3516853 | 35 | 33 | nan | nan | nan | Cerrado | 14.5 |
| c3e323c1-930d-3838-9147-37aea8a2ae40 | -21.82965 | -48.37175 | 2024-10-04 04:59:00 | NOAA-20 | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | 4.2 |
| e3caf30e-c7a5-3e39-a823-a60433998375 | -21.82953 | -48.37181 | 2024-10-04 04:59:00 | NOAA-20 | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 057da04e-9ad5-3ed6-a7e9-c92659458c6d | -21.82932 | -48.37513 | 2024-10-04 04:59:00 | NOAA-20 | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | 1.9 |
| cd7e111e-5ca4-3b9a-8490-ecac05caecac | -21.82918 | -48.37519 | 2024-10-04 04:59:00 | NOAA-20 | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | 1.9 |
| acbb285b-15cd-30f4-9533-603ca6c240c9 | -21.82899 | -48.37857 | 2024-10-04 04:59:00 | NOAA-20 | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 388d1b68-ee8f-3cd0-895f-b054ef76f563 | -21.82883 | -48.37862 | 2024-10-04 04:59:00 | NOAA-20 | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 175b5317-2624-3fa7-9cab-f4f42b34e4ec | -21.82768 | -48.39231 | 2024-10-04 04:59:00 | NOAA-20 | GAVIÃO PEIXOTO | SÃO PAULO | Brasil | 3516853 | 35 | 33 | nan | nan | nan | Cerrado | 10.0 |
| e50754c9-eb99-334a-b9e1-3da317a85c78 | -21.82735 | -48.39568 | 2024-10-04 04:59:00 | NOAA-20 | GAVIÃO PEIXOTO | SÃO PAULO | Brasil | 3516853 | 35 | 33 | nan | nan | nan | Cerrado | 20.2 |
| d5a397e7-83ea-3a7e-bd13-f10888550dcc | -21.82706 | -48.39569 | 2024-10-04 04:59:00 | NOAA-20 | GAVIÃO PEIXOTO | SÃO PAULO | Brasil | 3516853 | 35 | 33 | nan | nan | nan | Cerrado | 18.5 |
| a2a7cb8e-4e49-3f31-81ba-919856774b39 | -21.82704 | -48.39894 | 2024-10-04 04:59:00 | NOAA-20 | GAVIÃO PEIXOTO | SÃO PAULO | Brasil | 3516853 | 35 | 33 | nan | nan | nan | Cerrado | 20.2 |
| 1bf17f48-11c8-309b-896c-ddcd1ba3f78b | -21.82673 | -48.40217 | 2024-10-04 04:59:00 | NOAA-20 | GAVIÃO PEIXOTO | SÃO PAULO | Brasil | 3516853 | 35 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 4348a233-99e8-3de7-9933-b5c19759d00b | -21.82673 | -48.39895 | 2024-10-04 04:59:00 | NOAA-20 | GAVIÃO PEIXOTO | SÃO PAULO | Brasil | 3516853 | 35 | 33 | nan | nan | nan | Cerrado | 18.5 |
| 3d22e470-d7a6-37e6-8a6c-38c9a21211da | -21.8264 | -48.40216 | 2024-10-04 04:59:00 | NOAA-20 | GAVIÃO PEIXOTO | SÃO PAULO | Brasil | 3516853 | 35 | 33 | nan | nan | nan | Cerrado | 14.5 |
| 7226beb2-0518-3c6a-86aa-5fcdf17701cd | -21.82393 | -48.37471 | 2024-10-04 04:59:00 | NOAA-20 | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 99c088b1-3025-3af0-8689-1f68c9652518 | -21.80855 | -48.36983 | 2024-10-04 04:59:00 | NOAA-20 | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| af88c75c-5ec6-3f16-99cb-4eb25d3e4106 | -21.80683 | -48.38678 | 2024-10-04 04:59:00 | NOAA-20 | GAVIÃO PEIXOTO | SÃO PAULO | Brasil | 3516853 | 35 | 33 | nan | nan | nan | Cerrado | 4.3 |
| ec842517-69e8-32f6-b11b-e1e52c51a88c | -21.8065 | -48.39002 | 2024-10-04 04:59:00 | NOAA-20 | GAVIÃO PEIXOTO | SÃO PAULO | Brasil | 3516853 | 35 | 33 | nan | nan | nan | Cerrado | 4.3 |
| a54f0541-df35-3015-9ade-abd119fb9cee | -21.80366 | -48.36582 | 2024-10-04 04:59:00 | NOAA-20 | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f9127ee3-8ae2-3bb2-93fe-797201db9c13 | -21.8033 | -48.36934 | 2024-10-04 04:59:00 | NOAA-20 | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8f5df2af-9f6a-3536-b483-8f41dcdd20db | -21.80295 | -48.37281 | 2024-10-04 04:59:00 | NOAA-20 | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6201ee23-5a25-35a2-9e24-ac95b3721d70 | -21.80127 | -48.3894 | 2024-10-04 04:59:00 | NOAA-20 | GAVIÃO PEIXOTO | SÃO PAULO | Brasil | 3516853 | 35 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5826a641-b337-3837-973f-831fd40805f5 | -21.80094 | -48.39268 | 2024-10-04 04:59:00 | NOAA-20 | GAVIÃO PEIXOTO | SÃO PAULO | Brasil | 3516853 | 35 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5ee88255-17ae-3804-a9d3-c49a752656d7 | -21.79705 | -48.37885 | 2024-10-04 04:59:00 | NOAA-20 | GAVIÃO PEIXOTO | SÃO PAULO | Brasil | 3516853 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e28ab367-2b7d-3218-84fa-85c84e810a67 | -21.79672 | -48.38213 | 2024-10-04 04:59:00 | NOAA-20 | GAVIÃO PEIXOTO | SÃO PAULO | Brasil | 3516853 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3e517e1b-dbea-3cce-895c-e00d22c5bf62 | -21.79639 | -48.38539 | 2024-10-04 04:59:00 | NOAA-20 | GAVIÃO PEIXOTO | SÃO PAULO | Brasil | 3516853 | 35 | 33 | nan | nan | nan | Cerrado | 1.6 |
| eb2a1ff1-bdc9-3b92-856c-d3d0655b9690 | -21.79181 | -48.37831 | 2024-10-04 04:59:00 | NOAA-20 | GAVIÃO PEIXOTO | SÃO PAULO | Brasil | 3516853 | 35 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 489e9f55-03ba-3d16-8ef6-871add04f46b | -21.79148 | -48.38158 | 2024-10-04 04:59:00 | NOAA-20 | GAVIÃO PEIXOTO | SÃO PAULO | Brasil | 3516853 | 35 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b65d1df9-628c-361a-910f-23db67eff734 | -21.79116 | -48.38483 | 2024-10-04 04:59:00 | NOAA-20 | GAVIÃO PEIXOTO | SÃO PAULO | Brasil | 3516853 | 35 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 0bdcfb9c-f826-3f43-bd2d-1864fa2e1112 | -21.79082 | -48.38813 | 2024-10-04 04:59:00 | NOAA-20 | GAVIÃO PEIXOTO | SÃO PAULO | Brasil | 3516853 | 35 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 4890d3c0-9ca3-3e3d-b563-d6f7c87d7368 | -21.78624 | -48.38109 | 2024-10-04 04:59:00 | NOAA-20 | GAVIÃO PEIXOTO | SÃO PAULO | Brasil | 3516853 | 35 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 02a7a530-b254-34eb-8e60-cad89b44c2e9 | -21.78592 | -48.38433 | 2024-10-04 04:59:00 | NOAA-20 | GAVIÃO PEIXOTO | SÃO PAULO | Brasil | 3516853 | 35 | 33 | nan | nan | nan | Cerrado | 4.5 |
| ec35d607-0d88-3a4e-90cf-9e36483800a1 | -21.78559 | -48.38763 | 2024-10-04 04:59:00 | NOAA-20 | GAVIÃO PEIXOTO | SÃO PAULO | Brasil | 3516853 | 35 | 33 | nan | nan | nan | Cerrado | 4.5 |
| beeac34d-441a-36f4-9065-75410a9c5cd1 | -21.78525 | -48.39098 | 2024-10-04 04:59:00 | NOAA-20 | GAVIÃO PEIXOTO | SÃO PAULO | Brasil | 3516853 | 35 | 33 | nan | nan | nan | Cerrado | 11.4 |
| ae3bad08-ff03-303d-9dec-749b85dfcc31 | -21.78491 | -48.39435 | 2024-10-04 04:59:00 | NOAA-20 | GAVIÃO PEIXOTO | SÃO PAULO | Brasil | 3516853 | 35 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 5db0f822-2c9f-3765-acff-95a22d362990 | -21.78035 | -48.38717 | 2024-10-04 04:59:00 | NOAA-20 | GAVIÃO PEIXOTO | SÃO PAULO | Brasil | 3516853 | 35 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 85d1cf24-eac1-3355-864d-809897131f1d | -21.78002 | -48.39046 | 2024-10-04 04:59:00 | NOAA-20 | GAVIÃO PEIXOTO | SÃO PAULO | Brasil | 3516853 | 35 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 80eb189f-a950-3449-ad58-ef8f9ddaaff5 | -21.77969 | -48.39376 | 2024-10-04 04:59:00 | NOAA-20 | GAVIÃO PEIXOTO | SÃO PAULO | Brasil | 3516853 | 35 | 33 | nan | nan | nan | Cerrado | 3.8 |
| ca0d7434-55b6-3fc0-972c-db33d6c40274 | -21.77479 | -48.38987 | 2024-10-04 04:59:00 | NOAA-20 | GAVIÃO PEIXOTO | SÃO PAULO | Brasil | 3516853 | 35 | 33 | nan | nan | nan | Cerrado | 3.8 |
| a68fa577-237f-3088-ba93-1059ec0ef2d1 | -21.77446 | -48.3932 | 2024-10-04 04:59:00 | NOAA-20 | GAVIÃO PEIXOTO | SÃO PAULO | Brasil | 3516853 | 35 | 33 | nan | nan | nan | Cerrado | 3.8 |
| c6db442b-a225-3ee9-a460-3e5cf728c81e | -21.77412 | -48.39659 | 2024-10-04 04:59:00 | NOAA-20 | GAVIÃO PEIXOTO | SÃO PAULO | Brasil | 3516853 | 35 | 33 | nan | nan | nan | Cerrado | 3.2 |
| aa552cfc-ea7f-36a7-b8a7-cf81fdcac971 | -21.76923 | -48.39265 | 2024-10-04 04:59:00 | NOAA-20 | GAVIÃO PEIXOTO | SÃO PAULO | Brasil | 3516853 | 35 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 58f7f3ea-824c-3f7c-9260-d008252f1acf | -21.31033 | -47.60508 | 2024-10-04 04:59:00 | NOAA-20 | SERRA AZUL | SÃO PAULO | Brasil | 3551405 | 35 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 53986591-0e0b-3a6f-a81b-3c10c8b3ab1d | -21.31004 | -47.60819 | 2024-10-04 04:59:00 | NOAA-20 | SERRA AZUL | SÃO PAULO | Brasil | 3551405 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |


[Clique aqui para ver as próximas entradas](README172.md)
