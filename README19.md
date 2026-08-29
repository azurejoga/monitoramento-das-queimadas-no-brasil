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

## Dados Diários - Página 19

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 88e34794-d851-3c0a-99d9-4c54e64b1a92 | -5.8894 | -57.7708 | 2026-08-29 02:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 88.6 |
| 1281ab8d-a50a-3b0e-a441-a277e110b108 | -7.5137 | -55.3051 | 2026-08-29 02:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 127.1 |
| a8448d67-cc68-3501-836e-bdc5124df341 | -6.7514 | -55.6654 | 2026-08-29 02:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 42.8 |
| 20470c72-441b-33a0-97b2-8115c3c51b63 | -5.9819 | -57.6892 | 2026-08-29 02:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 49.5 |
| 080ea715-80b5-36a3-9892-fff423cc90cd | -10.4794 | -64.5012 | 2026-08-29 02:20:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 99.1 |
| 7c2014b3-0346-3685-ab6b-68658f78854f | -6.6315 | -43.7533 | 2026-08-29 02:20:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 41.1 |
| 082dff6a-c745-3d4f-b91d-d02008ae68b8 | -5.4179 | -43.1752 | 2026-08-29 02:20:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 60.0 |
| 57ecc802-b8c3-3847-b252-973df0f17ae9 | -6.6127 | -43.7549 | 2026-08-29 02:20:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 33.1 |
| 6f0faf87-77be-34a6-be1c-bb0d78e91b28 | -5.9079 | -57.7506 | 2026-08-29 02:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 79.7 |
| 06443b60-af8e-30e4-aae1-d13408d5c9f7 | -6.7884 | -55.6635 | 2026-08-29 02:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 84.1 |
| 5fa1759d-c512-3f33-a737-081b10be9675 | -6.7699 | -55.6644 | 2026-08-29 02:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 166.2 |
| 165d4b4e-cbec-3f82-8127-b78b3889afc2 | -10.4795 | -64.4824 | 2026-08-29 02:20:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 60.2 |
| 7e052598-d4f1-3f71-a520-2baa7afba08b | -11.0254 | -57.2237 | 2026-08-29 02:20:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 50.0 |
| 2dbe60cc-6cdd-36e9-9582-f9a103770ab1 | -11.0443 | -57.2222 | 2026-08-29 02:20:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 64.1 |
| df66e996-02b0-3545-ab02-063e2b414aac | -8.9613 | -63.279 | 2026-08-29 02:20:00 | GOES-19 | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 96.3 |
| 92c19ad8-b567-3e28-840b-21ebea1d6d71 | -6.77 | -55.6445 | 2026-08-29 02:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 46.5 |
| 9384bbc4-606c-3726-a640-2488120e7423 | -14.9386 | -56.3216 | 2026-08-29 02:20:00 | GOES-19 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 170.4 |
| 87e2606b-b453-3b98-a903-3ca34d27f953 | -14.9193 | -56.3237 | 2026-08-29 02:20:00 | GOES-19 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 57.9 |
| c481fc41-5ae9-3c1d-a9d2-a9f9552a0ba7 | 3.1095 | -60.7081 | 2026-08-29 02:20:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 82.9 |
| c05edf85-4cea-3ffa-8aeb-921bf9baf08d | -10.4609 | -64.4831 | 2026-08-29 02:20:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 43.1 |
| 1412efe1-cc95-39a2-91b5-35067188a35a | -6.7698 | -55.6844 | 2026-08-29 02:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 53.2 |
| f8cbd35c-82b9-352e-932d-401fd96cb5f7 | -5.8895 | -57.7513 | 2026-08-29 02:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 141.5 |
| 304c9e20-fbc0-3c4d-a781-7eca6d41646c | -10.4981 | -64.5005 | 2026-08-29 02:20:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 72.3 |
| 36fc23eb-897d-3cf9-a16c-baaf492fe4fd | -5.4177 | -43.1986 | 2026-08-29 02:20:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 56.7 |
| 9654b2c7-7283-3fd0-9bf5-ff28180bd314 | -10.4608 | -64.502 | 2026-08-29 02:20:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 40.0 |
| 663ae5af-bdbd-348d-a542-4a69323df3ab | -8.9428 | -63.2797 | 2026-08-29 02:20:00 | GOES-19 | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 89.8 |
| 057a1934-249c-3dd1-b2e1-e0a6f1d5e26c | -6.6129 | -43.7317 | 2026-08-29 02:20:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 42.2 |
| faa75065-07af-33ab-835f-a69d16dc62ea | -10.4981 | -64.5005 | 2026-08-29 02:30:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 72.1 |
| cbae18aa-442e-3a0b-8e1c-9e113c6da228 | -10.4795 | -64.4824 | 2026-08-29 02:30:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 53.7 |
| 48c2db58-fa5b-327a-8c0f-81942516bb8f | -8.9613 | -63.279 | 2026-08-29 02:30:00 | GOES-19 | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 69.4 |
| db91c6da-b636-3bb3-894b-450b8bdd216c | -5.8894 | -57.7708 | 2026-08-29 02:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 106.8 |
| 4e8ba4fa-53cc-3168-8bf2-cc0c70417ce4 | -7.4952 | -55.3062 | 2026-08-29 02:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 65.8 |
| afbc1fff-169e-361c-8c82-c777b9fd0156 | -6.6315 | -43.7533 | 2026-08-29 02:30:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 51.0 |
| bc19e576-a704-313f-aef0-49c43d00b9c2 | 3.1095 | -60.7081 | 2026-08-29 02:30:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 70.6 |
| bb7bbabf-76b0-39fb-9e16-93da33da141f | -10.4794 | -64.5012 | 2026-08-29 02:30:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 107.8 |
| 0c80765e-6e91-3ecc-9261-0abc588af878 | -6.7699 | -55.6644 | 2026-08-29 02:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 125.7 |
| aeb9ea0a-d837-3a93-9cae-b98dfd5caa03 | -5.9079 | -57.7506 | 2026-08-29 02:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 42.2 |
| d62bda85-7545-3e37-8727-9e0278aa9f46 | -5.9819 | -57.6892 | 2026-08-29 02:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 43.9 |
| 141a51d0-2e15-382a-9274-deac033c5b27 | -11.0443 | -57.2222 | 2026-08-29 02:30:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 67.6 |
| 29dbded7-33ec-3328-8770-8d0bb4780ddf | -7.5139 | -55.2851 | 2026-08-29 02:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 52.6 |
| b36430dd-82ef-335b-a12f-e82b8bb5fd40 | -5.8895 | -57.7513 | 2026-08-29 02:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 136.6 |
| 9851f629-907e-34e6-b9f8-20033dbca1fd | -8.9428 | -63.2797 | 2026-08-29 02:30:00 | GOES-19 | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 59.6 |
| a082b47c-b69d-3ded-9031-5ef8a09a4edd | -7.5137 | -55.3051 | 2026-08-29 02:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 125.5 |
| 52047b7b-031d-3f9a-b9de-805b50949ea1 | -6.7698 | -55.6844 | 2026-08-29 02:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 58.1 |
| df25655a-abb4-328e-b32b-de557bb1d52c | -6.7884 | -55.6635 | 2026-08-29 02:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 76.5 |
| 446afa6b-f717-35d8-ab9e-a5df3d1a95c2 | -6.6317 | -43.73 | 2026-08-29 02:30:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 68.2 |
| 4b9f820a-c63f-3bd3-9572-0bd140bed852 | -7.5137 | -55.3051 | 2026-08-29 02:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 151.2 |
| 8b7a69fd-178b-343e-a8f4-9eaa6e88de93 | -6.6317 | -43.73 | 2026-08-29 02:40:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 70.8 |
| 119815c4-426b-31bb-8eb6-661bd92fe5c9 | -5.8894 | -57.7708 | 2026-08-29 02:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 86.5 |
| 0555c173-3398-3129-9367-9960c1bfe01f | -6.7884 | -55.6635 | 2026-08-29 02:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 132.1 |
| 5b6e47f9-7275-3829-aee9-3ab1f6a492f3 | -5.4179 | -43.1752 | 2026-08-29 02:40:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 71.4 |
| 4cf8ab6f-2f1f-3729-85aa-c8e547ebc561 | -10.4795 | -64.4824 | 2026-08-29 02:40:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 60.4 |
| fc9315f6-4eaf-3b6c-92e8-67157e1d6d7d | -10.4981 | -64.5005 | 2026-08-29 02:40:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 57.7 |
| f56ee396-cc13-3854-8af2-42af5b12cd89 | -11.0443 | -57.2222 | 2026-08-29 02:40:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 59.5 |
| 6674f4bd-b794-372c-9de1-710fda51a852 | -6.6315 | -43.7533 | 2026-08-29 02:40:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 60.1 |
| 78436c31-529c-3dc6-8026-5b29ff6d178d | -6.7883 | -55.6834 | 2026-08-29 02:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 51.9 |
| b1dc2684-ae0f-39e6-bfde-580207d1d526 | -5.9079 | -57.7506 | 2026-08-29 02:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 51.4 |
| 684fd3a2-4855-3302-9488-e9398808315e | -7.5139 | -55.2851 | 2026-08-29 02:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 54.8 |
| 64fe2dc5-d41d-321b-bb1e-4079cd3bf09d | -6.6127 | -43.7549 | 2026-08-29 02:40:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 52.6 |
| 68950483-5f1f-370b-a76f-d613238f5790 | -6.6129 | -43.7317 | 2026-08-29 02:40:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 69.3 |
| 37f6b8a2-901a-3dd8-9262-1687b4fa7d10 | -5.8895 | -57.7513 | 2026-08-29 02:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 130.3 |
| 6154b049-ba5b-331a-9457-c49cb340fdce | -10.4794 | -64.5012 | 2026-08-29 02:40:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 103.6 |
| 4fd7854d-f850-3a38-be8c-32a81e3b4ff6 | -6.77 | -55.6445 | 2026-08-29 02:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 56.2 |
| 7f464297-ebea-3d87-9f20-0b305f77285a | -6.7698 | -55.6844 | 2026-08-29 02:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 53.5 |
| c24c4d81-c54b-3766-ab02-2e1c918df691 | -5.9819 | -57.6892 | 2026-08-29 02:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 40.0 |
| fa8ab64d-f016-342a-aa7c-fc6643609f7c | -7.4952 | -55.3062 | 2026-08-29 02:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 72.2 |
| c24a6960-962b-3083-adb5-2e5de8247429 | -8.9613 | -63.279 | 2026-08-29 02:40:00 | GOES-19 | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 50.4 |
| 3fa0d8cf-4796-342c-b37b-211abfad78bc | -5.4177 | -43.1986 | 2026-08-29 02:40:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 72.9 |
| 1671cbf5-16d8-3528-9de3-6e9f3ec41f26 | -6.7699 | -55.6644 | 2026-08-29 02:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 150.8 |
| d8e79eea-17d1-39e6-83a0-e72c471afb5a | -6.6317 | -43.73 | 2026-08-29 02:50:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 76.0 |
| 9fc38731-9221-32cc-9ffb-a33986467643 | -11.0443 | -57.2222 | 2026-08-29 02:50:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 52.4 |
| 19c2b6e0-2ebc-3b3b-9380-f44a7886c4d4 | -7.5137 | -55.3051 | 2026-08-29 02:50:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 149.7 |
| 0b61ba39-2756-30db-bed1-4876fedd595d | -5.8894 | -57.7708 | 2026-08-29 02:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 79.7 |
| a83118b2-e14c-345f-9d5c-c9cd8d2ad545 | -10.4981 | -64.5005 | 2026-08-29 02:50:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 54.7 |
| 1b779245-37a3-32e2-92c3-33c3e7b72d20 | -7.5139 | -55.2851 | 2026-08-29 02:50:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 57.1 |
| 18dfa6f1-e2c3-39fa-bdae-18e2a1402195 | -5.8895 | -57.7513 | 2026-08-29 02:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 119.7 |
| 15e8a450-6d89-3dc2-9a5c-e667a80d56d1 | -10.4794 | -64.5012 | 2026-08-29 02:50:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 113.5 |
| 69fbb946-b41e-3f2c-9d70-ad7fa3af791a | -6.77 | -55.6445 | 2026-08-29 02:50:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 55.9 |
| 8e87a10d-5da3-3ada-9a8b-89e41b32a72a | -10.4795 | -64.4824 | 2026-08-29 02:50:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 59.9 |
| b0dafbbb-bc60-3ce1-b5cc-44923c4baab1 | -6.6315 | -43.7533 | 2026-08-29 02:50:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 66.6 |
| bd97bf6e-cd3e-31c0-9be8-53d5548c6c5b | -5.4179 | -43.1752 | 2026-08-29 02:50:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 61.9 |
| b0ef88cb-dada-34ae-b589-86cd5f973159 | -5.9079 | -57.7506 | 2026-08-29 02:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 64.5 |
| ae132c8b-7f0c-3214-a345-9fb036332b9b | -6.7699 | -55.6644 | 2026-08-29 02:50:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 159.6 |
| a82c82e9-12d4-3784-a8a5-05e930547252 | -5.9819 | -57.6892 | 2026-08-29 02:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 55.2 |
| 3cfca619-4599-32fe-8732-26b00eb1cef6 | -10.4608 | -64.502 | 2026-08-29 02:50:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 39.7 |
| 5afbfdcd-032c-3e97-9160-02cb30102253 | -6.7698 | -55.6844 | 2026-08-29 02:50:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 55.9 |
| a98286e5-b259-387c-b27a-06b7e907b141 | -7.4952 | -55.3062 | 2026-08-29 02:50:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 51.3 |
| 4e65024e-b343-3fd5-a557-2955754089b5 | 3.1095 | -60.7081 | 2026-08-29 02:50:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 37.7 |
| ada8c51b-0671-3b3c-84c2-c39eefa0970e | -6.6129 | -43.7317 | 2026-08-29 02:50:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 60.9 |
| be264fa6-be2a-3e7c-b81c-4883d1b90dbc | -6.7884 | -55.6635 | 2026-08-29 02:50:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 101.7 |
| 877c7d23-e4e9-333f-92df-b0288edb5b53 | -5.4177 | -43.1986 | 2026-08-29 02:50:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 65.5 |
| 0b8f299f-700f-3ae0-927a-a86f432df6df | -7.4952 | -55.3062 | 2026-08-29 03:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 72.3 |
| c4732fe5-079c-37a3-895b-d893bf85e497 | -8.9428 | -63.2797 | 2026-08-29 03:00:00 | GOES-19 | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 55.1 |
| d09c5c14-0502-3e06-9ebc-9d3f34650a5f | -7.5137 | -55.3051 | 2026-08-29 03:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 154.3 |
| c71a6cee-b79b-3e44-abc6-538d603c9e49 | -10.4795 | -64.4824 | 2026-08-29 03:00:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 62.2 |
| 0043051a-9526-3f58-bef6-0168089c5cfe | -5.982 | -57.6697 | 2026-08-29 03:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 53.1 |
| 415a54ef-ba35-3105-bfc2-b75d4fa8bc23 | -7.5139 | -55.2851 | 2026-08-29 03:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 56.3 |
| eb3d8008-e4ca-386d-a4e4-fa955f639b2e | -6.6315 | -43.7533 | 2026-08-29 03:00:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 57.7 |
| e51aaa27-8db7-3f6d-aece-6525fbf44f4a | -5.8894 | -57.7708 | 2026-08-29 03:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 90.1 |
| 2a74c7de-1f08-3cf4-9a22-ef00fabec79a | -6.7699 | -55.6644 | 2026-08-29 03:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 164.8 |


[Clique aqui para ver as próximas entradas](README20.md)
