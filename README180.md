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

## Dados Diários - Página 180

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| fdcb073a-63ce-3abb-8e0b-1f7f191d663a | -2.9157 | -57.7983 | 2026-09-21 17:20:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 153.1 |
| ed5c7f1b-f0fe-3cb7-86bb-e195da241fad | -10.0714 | -50.2387 | 2026-09-21 17:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 87.7 |
| 931de19b-c1c6-33f4-8ff1-2e6b5dc01b87 | -10.09 | -50.2581 | 2026-09-21 17:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 70.9 |
| 767ba659-cc7e-3e80-a6ef-001571f75574 | -2.9526 | -57.7006 | 2026-09-21 17:20:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 48.1 |
| 34b9577b-9cbf-3c0d-a152-c59552a5d5c4 | -10.4099 | -50.3324 | 2026-09-21 17:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 64.6 |
| 368e3e67-b75b-39be-9748-bfcd216f38f0 | -2.9528 | -57.623 | 2026-09-21 17:20:00 | GOES-19 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 42.6 |
| 8918f58e-f380-3c50-b675-366d0be15328 | -10.4105 | -50.2897 | 2026-09-21 17:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 107.8 |
| b864a0d2-303e-3bcd-b50b-b29d226562c8 | -6.5569 | -45.566 | 2026-09-21 17:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 113.5 |
| 8c5fc632-473f-349e-8f32-f1c9c75fef85 | -2.9157 | -57.8177 | 2026-09-21 17:20:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 156.9 |
| 7f9aab49-08b6-3ee7-a203-d7503571b8c9 | -2.4977 | -56.5978 | 2026-09-21 17:20:00 | GOES-19 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 37.1 |
| ab4cf719-9a58-39f8-bcfa-5d14e2c6e3d4 | -10.0898 | -50.2795 | 2026-09-21 17:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 108.2 |
| 8c5ac999-a606-3779-9fd8-e6aeecda89ba | -1.4302 | -48.9529 | 2026-09-21 17:20:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 77.4 |
| fe4581e6-dbd9-3d28-89b6-e32e7af8ff2e | -6.5829 | -58.9851 | 2026-09-21 17:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 81.4 |
| aee48ab7-cb50-3acd-aaae-fc5e7af09b85 | -7.9152 | -72.9324 | 2026-09-21 17:20:00 | GOES-19 | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 56.3 |
| a97a44c6-0ee6-3c65-a166-c051e21edfd8 | -0.803 | -48.6825 | 2026-09-21 17:20:00 | GOES-19 | SALVATERRA | PARÁ | Brasil | 1506302 | 15 | 33 | nan | nan | nan | Amazônia | 66.5 |
| 986e742c-e75c-32f2-9595-bb613c3a169f | -1.4671 | -48.995 | 2026-09-21 17:20:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 77.1 |
| 67e63fbd-a8b5-353e-85dd-432d29ba99f2 | -10.3729 | -50.2722 | 2026-09-21 17:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 89.7 |
| 424dbf91-0fec-3ef7-a53b-9f369960c3ad | -8.8644 | -68.5034 | 2026-09-21 17:20:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 52.6 |
| 599803ba-cb70-33e2-ad6b-ecba9f31e138 | -1.1345 | -49.2123 | 2026-09-21 17:20:00 | GOES-19 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 66.5 |
| c1fd5c3f-f82d-3fa0-99b5-c5d88cddd703 | -1.4487 | -48.9526 | 2026-09-21 17:20:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 84.2 |
| dc7f99bd-e46d-3848-9e8f-95c449d7c8ba | -10.2982 | -50.2158 | 2026-09-21 17:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 92.8 |
| a9f629c8-6259-355a-ba2c-e4d1d3b5dbb3 | -6.5451 | -44.8643 | 2026-09-21 17:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 95.9 |
| ec5b4e79-7121-30b4-ac31-f406a15671a5 | -6.513 | -58.3099 | 2026-09-21 17:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 44.2 |
| 281dc0f4-1dec-3b1a-9e17-0a6edce4354c | -1.4855 | -48.9947 | 2026-09-21 17:20:00 | GOES-19 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 70.0 |
| 89c913e3-ba05-3b46-9af8-bc09ec747b9d | -10.67 | -50.6678 | 2026-09-21 17:30:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 144.1 |
| 8474106c-47f4-378d-93e6-6e4f44819e63 | -10.279 | -50.2391 | 2026-09-21 17:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 74.8 |
| d2618ff3-09d2-3f35-ad05-14a58a9f651d | -2.9157 | -57.7983 | 2026-09-21 17:30:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 148.4 |
| 47016ce6-de89-3a0e-bcbf-977d0fb886bf | -6.5569 | -45.566 | 2026-09-21 17:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 110.2 |
| a790a344-7a3d-31fa-8599-20c3a173dae3 | -10.7994 | -50.8881 | 2026-09-21 17:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 89.3 |
| 604bacca-f91c-3f90-afe4-8dfca5b6bedb | -10.6875 | -50.7722 | 2026-09-21 17:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 84.6 |
| 6901d2d6-20c0-35c3-94bb-f400e45138a9 | -6.0744 | -57.6269 | 2026-09-21 17:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 102.7 |
| 2550d3d8-bb11-3681-a174-4ca82fe5edab | -10.7061 | -50.7915 | 2026-09-21 17:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 122.5 |
| 1d8cb046-9e65-3117-8b8c-300b9f61b134 | -2.9528 | -57.623 | 2026-09-21 17:30:00 | GOES-19 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 61.5 |
| e178da87-166f-3463-abf5-d22677ea274c | -6.7517 | -55.6256 | 2026-09-21 17:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 181.0 |
| 157fd217-deaf-352b-8e0e-1f249ad07e8a | -10.2793 | -50.2177 | 2026-09-21 17:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 76.5 |
| 7a7f1744-4bf8-34f7-8cda-d9df5abac3b3 | -1.1345 | -49.2123 | 2026-09-21 17:30:00 | GOES-19 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 62.9 |
| 758d7e91-af70-3c13-9d1f-aa247fb8f338 | -6.5571 | -45.5434 | 2026-09-21 17:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 224.2 |
| 3642ec01-b908-3c1f-b1db-8244329d2238 | -0.803 | -48.6825 | 2026-09-21 17:30:00 | GOES-19 | SALVATERRA | PARÁ | Brasil | 1506302 | 15 | 33 | nan | nan | nan | Amazônia | 61.0 |
| d98387be-78ec-3130-80c8-eca7d1983f42 | -11.4001 | -44.076 | 2026-09-21 17:30:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 249.4 |
| 8c89d480-ec8c-30db-8111-d661edc4ade5 | -8.5989 | -44.5531 | 2026-09-21 17:30:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 117.2 |
| 3ab4bdd0-9159-3423-acf6-7780ab9fed33 | -2.9525 | -57.7394 | 2026-09-21 17:30:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 76.5 |
| ae1cbe0d-59fd-3edc-9d78-af4e229d613f | -7.9152 | -72.9324 | 2026-09-21 17:30:00 | GOES-19 | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 58.8 |
| 3329a300-3f98-3712-8f8a-89a22f25b7a5 | -6.183 | -47.6133 | 2026-09-21 17:30:00 | GOES-19 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 84.4 |
| 333bbdac-50b6-39c4-a76c-5cc1028bda65 | -10.0898 | -50.2795 | 2026-09-21 17:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 111.5 |
| e50de6d0-bae3-3fd7-b5e4-bfc667760353 | -6.513 | -58.3099 | 2026-09-21 17:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 44.0 |
| 9593f167-ba73-3a58-aef9-e6342667320f | -6.0927 | -57.6457 | 2026-09-21 17:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 36.9 |
| bf65061f-188b-38af-a1ba-a3bcae1a8a40 | -5.6406 | -43.4153 | 2026-09-21 17:30:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 91.0 |
| 4f5b4446-5cb9-3535-ab73-2ecf09f4959b | -10.3549 | -50.2099 | 2026-09-21 17:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 86.4 |
| 11e671eb-de48-3f2d-b8f2-f3edc7348254 | -6.5451 | -44.8643 | 2026-09-21 17:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 145.4 |
| 335f59d5-7c13-3fa6-b7ca-4f3d816b98b8 | -11.8559 | -49.979 | 2026-09-21 17:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 67.5 |
| 110669f7-6b1a-366d-9cc6-81b5f2fe1c68 | -8.7729 | -44.2568 | 2026-09-21 17:30:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 333.8 |
| 1f7d34cb-ecc4-3541-9fee-57e3b61a5436 | -2.9157 | -57.8177 | 2026-09-21 17:30:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 145.2 |
| 51f4c269-294a-3e86-9ac1-60fcb7ced8ec | -8.8644 | -68.5034 | 2026-09-21 17:30:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 53.2 |
| 24d5d5c2-f081-30c9-b364-4cb3e55fe29a | -6.3434 | -55.8442 | 2026-09-21 17:30:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 68.6 |
| 203b08a2-79f4-39c7-8b28-a8760f80d444 | -10.2748 | -50.5592 | 2026-09-21 17:30:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 75.2 |
| 5442eaf6-79eb-3187-a16c-4834c909b32c | -9.7693 | -46.0615 | 2026-09-21 17:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 81.6 |
| feb22844-d2e7-3cf4-b07c-aac543ec2cd5 | -11.3996 | -44.0995 | 2026-09-21 17:30:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 128.1 |
| 1be18695-d2c1-32b2-80a2-5b880b59bc98 | -2.8974 | -57.7987 | 2026-09-21 17:30:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 84.6 |
| f7764304-d9c0-3e84-bc98-630afc6e291f | -8.7706 | -45.8567 | 2026-09-21 17:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 144.2 |
| fc018fb2-87d8-33b6-b799-89cb64181d0f | -6.2766 | -57.7358 | 2026-09-21 17:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 40.8 |
| 39f986eb-3525-35b5-8554-9ce78503c8fa | -0.803 | -48.6611 | 2026-09-21 17:40:00 | GOES-19 | SALVATERRA | PARÁ | Brasil | 1506302 | 15 | 33 | nan | nan | nan | Amazônia | 66.4 |
| 884e285e-6bc9-3b21-97cd-bbd3ef424261 | -9.1708 | -50.0049 | 2026-09-21 17:40:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 82.6 |
| c8076206-48a8-3330-b9dd-ceb7719dcac3 | -2.9326 | -58.3397 | 2026-09-21 17:40:00 | GOES-19 | SILVES | AMAZONAS | Brasil | 1304005 | 13 | 33 | nan | nan | nan | Amazônia | 62.1 |
| 88400616-9f29-37fc-b31c-4a5b478d7992 | -3.8264 | -59.3407 | 2026-09-21 17:40:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 35.0 |
| ee41d430-979d-3cef-99b4-befe037f23df | -6.2949 | -57.7545 | 2026-09-21 17:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 103.9 |
| 29b177c0-ff5f-344f-a4d5-8abda8dc153f | -7.822 | -61.8084 | 2026-09-21 17:40:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 128.6 |
| 4cbe7264-1afa-3ae9-bfd7-f72ae2dc94dd | -8.7706 | -45.8567 | 2026-09-21 17:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 151.4 |
| 88bf1163-492a-3f00-8497-58b652c752a5 | -10.7064 | -50.7703 | 2026-09-21 17:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 114.8 |
| 5d6ab75a-a547-309c-bd4c-95150dcba2f0 | -10.6883 | -50.7084 | 2026-09-21 17:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 77.8 |
| 85fb8cb2-bd7a-3a92-b722-be500c1b3628 | -11.8014 | -49.8129 | 2026-09-21 17:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 94.6 |
| e3160993-851b-38ff-b0cc-93ae044b24d2 | -5.7504 | -43.7091 | 2026-09-21 17:40:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 145.0 |
| 9b79a8f0-cd58-302c-9e96-acb6ed6e7872 | -6.5569 | -45.566 | 2026-09-21 17:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 143.5 |
| 6821a794-7309-3535-9a7e-276a4b394403 | -11.8362 | -50.0244 | 2026-09-21 17:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 74.0 |
| e0152835-9bc1-3d98-a992-bff5bf1e3000 | -2.9157 | -57.7983 | 2026-09-21 17:40:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 130.6 |
| 7cb167a9-0d91-3599-9c73-1f1cb7004d2f | -9.0286 | -44.9187 | 2026-09-21 17:40:00 | GOES-19 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 139.8 |
| 86de1010-2dc9-3ecb-ad4e-8b3b4b4f0759 | -6.3436 | -55.8243 | 2026-09-21 17:40:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 86.4 |
| 0ebb4f60-65bd-3f9c-b3a4-b9b7ca22f5e2 | -11.3996 | -44.0995 | 2026-09-21 17:40:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 90.0 |
| 7c77e8bc-406e-3d7a-be6f-5abf86227f53 | -3.1698 | -58.5859 | 2026-09-21 17:40:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 63.5 |
| 386558c3-9170-3580-b827-b9c358693206 | -6.8985 | -41.6976 | 2026-09-21 17:40:00 | GOES-19 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 120.6 |
| 3c7f610c-e887-3dae-a893-29bd09aca61a | -3.3367 | -57.8673 | 2026-09-21 17:40:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 51.7 |
| 518001bd-2c5f-3440-bed0-e8288c6ac911 | -6.5257 | -44.9342 | 2026-09-21 17:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 50.4 |
| abe4378f-5ef2-3a77-bc6d-9d800b626f91 | -6.513 | -58.3099 | 2026-09-21 17:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 43.2 |
| bb5cf64b-a33d-32f1-80b4-4542ddbaea19 | -6.7094 | -59.443 | 2026-09-21 17:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 56.3 |
| 4621bc6b-5f31-3584-930a-813fc80df12f | -5.6406 | -43.4153 | 2026-09-21 17:40:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 105.9 |
| 9d809f69-edcf-3d33-9002-d361e34dd329 | -2.9528 | -57.623 | 2026-09-21 17:40:00 | GOES-19 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 45.2 |
| 6cb850f0-9540-3697-a20e-ddfca4f19f66 | -2.9525 | -57.7394 | 2026-09-21 17:40:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 68.6 |
| f9bc1357-b530-31cb-8854-ec21a5ba30f1 | -9.3577 | -50.0943 | 2026-09-21 17:40:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 83.7 |
| 6d1aff70-01f0-3bd2-a266-112bda43f15f | -3.5893 | -59.0773 | 2026-09-21 17:40:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 69.5 |
| eb6439db-0361-3292-8eb0-6f119ff95e0a | -5.9152 | -59.933 | 2026-09-21 17:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 57.0 |
| 45aa0356-7f7e-301d-ba1b-583702a001ae | -6.7649 | -59.4216 | 2026-09-21 17:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 41.9 |
| 4af480cf-2c88-396e-8586-f83a5983d1b4 | -2.8791 | -57.799 | 2026-09-21 17:40:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 189.7 |
| f711c4cb-9b3b-3f40-9256-2ddbcd5950d4 | -10.2545 | -68.7679 | 2026-09-21 17:40:00 | GOES-19 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 49.9 |
| 88dc91df-40eb-3932-9e32-637f051a251f | -6.3434 | -55.8442 | 2026-09-21 17:40:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 78.1 |
| fbf7c481-4387-3f0f-a2ff-8481ee51b767 | -2.9157 | -57.8177 | 2026-09-21 17:40:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 105.4 |
| 48d1755a-6df0-39db-a7a0-bdff8a51055b | -6.5759 | -45.5419 | 2026-09-21 17:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 135.5 |
| 70d8de8f-0cf4-374c-b756-68b8cfc8d028 | -11.0048 | -49.7325 | 2026-09-21 17:40:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 121.8 |
| 05c27e2c-3636-38d9-befb-142c19508f68 | -3.4828 | -57.9803 | 2026-09-21 17:40:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 42.2 |
| e070ebb8-17d0-3586-b2f7-c1f72ddfe225 | -6.0196 | -51.7893 | 2026-09-21 17:40:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 61.9 |
| 2c1ce102-4f03-389a-a2df-8c15f75978da | -10.6875 | -50.7722 | 2026-09-21 17:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 78.3 |
| 4d3f9eb1-920f-3657-9216-698731b013a7 | -11.4001 | -44.076 | 2026-09-21 17:40:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 117.0 |


[Clique aqui para ver as próximas entradas](README181.md)
