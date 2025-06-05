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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e997af09-f32d-3e10-9fcf-297e3f0fc8a6 | -6.63407 | -47.35234 | 2025-06-05 03:40:00 | NOAA-20 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e5c7d9c0-99a5-3f0d-ae2a-0b4dfd2c1c64 | -6.20297 | -43.33847 | 2025-06-05 03:40:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e7ae2cbd-fda1-303b-bf15-6422e3ccb46a | -3.94313 | -41.51335 | 2025-06-05 03:40:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 9cfe4d1d-186c-3455-b55b-11a54577deb8 | -6.21909 | -44.51019 | 2025-06-05 03:40:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a735f015-de04-3caa-bcaf-32af09c28b04 | -6.20798 | -43.33925 | 2025-06-05 03:40:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1530268d-9f06-371c-9ccc-7f451d42e0a3 | -6.21974 | -44.50661 | 2025-06-05 03:40:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 05e08219-c36f-39c9-a154-8fdbd7e21037 | -6.96389 | -42.90703 | 2025-06-05 03:40:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 9.6 |
| d28fb02b-d0ed-32a6-a0aa-98afffeaba9a | -7.61299 | -45.75176 | 2025-06-05 03:40:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| fd699cf5-877f-3ceb-a755-dba3e248b3d8 | -6.22266 | -44.51127 | 2025-06-05 03:40:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 18142d95-fce5-3f8a-b48d-8e39dd64d5f1 | -5.19331 | -43.31874 | 2025-06-05 03:40:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f98256f3-d982-33af-b666-28f235077e24 | -4.80947 | -45.26163 | 2025-06-05 03:40:00 | NOAA-20 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f8e140e8-942a-35c0-a819-4053c7e0e686 | -6.22038 | -44.50307 | 2025-06-05 03:40:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c3e1bc59-3d4b-37d4-92cf-611f3f01ef73 | -7.61372 | -45.7477 | 2025-06-05 03:40:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| ceaf7f31-9e3a-369d-9413-a9bcde2caebf | -4.11521 | -38.33463 | 2025-06-05 03:40:00 | NOAA-20 | CASCAVEL | CEARÁ | Brasil | 2303501 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 3a1ed9b2-1f9f-3a28-abfc-67414534d579 | -4.80872 | -45.26582 | 2025-06-05 03:40:00 | NOAA-20 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2b30e7ba-8104-3565-b2d1-54ed16db4060 | -7.61431 | -45.75185 | 2025-06-05 03:40:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 356ec6da-6bfb-3b29-b815-420c8ca613e3 | -6.29717 | -47.0104 | 2025-06-05 03:40:00 | NOAA-20 | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| bdeb6d4a-f75a-3955-829c-18a2414f8794 | -7.61873 | -45.75274 | 2025-06-05 03:40:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 15c52556-5e16-341e-a69e-0d10adfcb1df | -5.18824 | -43.31785 | 2025-06-05 03:40:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7f103cd8-b6fa-3bf0-b3cd-32262208e442 | -6.96297 | -42.91222 | 2025-06-05 03:40:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 9.6 |
| 05dc68e9-8d02-32e6-8019-05632a2c65d1 | -4.82168 | -44.35723 | 2025-06-05 03:40:00 | NOAA-20 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d23fe812-782c-35f4-b5e7-b56fc2c95914 | -6.95909 | -42.90626 | 2025-06-05 03:40:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 9.6 |
| feb9389f-4522-39e4-9446-60aba37ef9a0 | -7.58744 | -45.86355 | 2025-06-05 03:40:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| b5ee5ab8-c2ad-39ba-ae4e-dcb584166978 | -6.95817 | -42.91146 | 2025-06-05 03:40:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 9.6 |
| dfb728b8-9fe2-35e3-8db6-718a2e78e5bb | -6.59429 | -43.89244 | 2025-06-05 03:40:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 147dd649-38a5-38d1-8e16-7fc364bfc313 | -7.53944 | -45.83016 | 2025-06-05 03:40:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 8.8 |
| a58c54b2-62fa-3679-bb1c-5754ba9bc39b | -4.94006 | -37.99907 | 2025-06-05 03:40:00 | NOAA-20 | RUSSAS | CEARÁ | Brasil | 2311801 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| a679023c-b0c5-32a0-9a18-14ea8dc6633f | -7.61507 | -45.74778 | 2025-06-05 03:40:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 78849f8d-1319-37a7-86b2-47a93b500d50 | -7.54444 | -45.83533 | 2025-06-05 03:40:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ae3f2ffb-3be5-3144-b65c-92abc32afe53 | -6.96958 | -42.90272 | 2025-06-05 03:40:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 2a1b6d7c-4c04-3fc3-80b8-e159bd87deca | -4.55392 | -38.46016 | 2025-06-05 03:40:00 | NOAA-20 | OCARA | CEARÁ | Brasil | 2309458 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 6199cb7d-6d82-3136-9860-2f89a4461806 | -7.62005 | -45.75281 | 2025-06-05 03:40:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 3ead96a0-4c65-380f-9a37-b0cbbe5d0fe1 | -6.5989 | -43.89643 | 2025-06-05 03:40:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| db401ed8-ea78-38d4-9c95-d7a38aef7727 | -6.21849 | -44.50316 | 2025-06-05 03:40:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a08573fe-671f-3768-9142-460e73fc50f2 | -6.97851 | -47.08685 | 2025-06-05 03:40:00 | NOAA-20 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 812a5cc6-af69-3bbd-a4a1-4fd39551bf14 | -6.20347 | -43.33555 | 2025-06-05 03:40:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0bccb4f3-ea60-36b1-b966-1bc3dd020c8b | -6.22449 | -44.5112 | 2025-06-05 03:40:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 23bbabfc-8375-3a9c-9c97-12943862fa41 | -4.3941 | -38.0649 | 2025-06-05 03:40:00 | NOAA-20 | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 22a025be-8d5f-3037-b402-3be4a3fb15eb | -7.59863 | -46.44035 | 2025-06-05 03:40:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ed2e8061-1bea-3ba9-b5ec-6d87ea704ab4 | -7.69881 | -45.7748 | 2025-06-05 03:40:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 30db75c1-a64e-3bdf-8acc-5e86421322c3 | -7.62082 | -45.74868 | 2025-06-05 03:40:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 48b6cdca-f468-33b6-8b9f-5c8d9c5f0431 | -6.59375 | -43.89549 | 2025-06-05 03:40:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e9fbbb25-edc1-3698-946a-782e8fb85882 | -6.64146 | -47.34828 | 2025-06-05 03:40:00 | NOAA-20 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b2fe875c-e8e5-3b14-9541-d8ac3843ae2a | -7.69735 | -45.78283 | 2025-06-05 03:40:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c9090e84-6098-33b0-98c7-a4e5c504404f | -7.61946 | -45.74862 | 2025-06-05 03:40:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| af1472b5-6db5-3303-bbc9-6693e7642187 | -4.88217 | -37.49842 | 2025-06-05 03:40:00 | NOAA-20 | ARACATI | CEARÁ | Brasil | 2301109 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 53684048-fc07-33a5-bebf-7f0391d93274 | -5.19627 | -43.06172 | 2025-06-05 03:40:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 33bd74d8-06b9-3471-aeaf-3091d25d0e47 | -7.67604 | -46.0932 | 2025-06-05 03:40:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2ff828bd-c304-37d9-8439-52d08982765b | -7.55022 | -45.83627 | 2025-06-05 03:40:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 68fb4249-e846-3263-bbd0-34dc8f8d5b55 | -6.21788 | -44.50671 | 2025-06-05 03:40:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9c1a4c34-70b3-3b15-96fb-c13a9648937d | -7.58691 | -45.86377 | 2025-06-05 03:40:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| cf189291-6c2c-390e-902f-228ccf21c597 | -5.92128 | -45.52486 | 2025-06-05 03:40:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b545973e-a7ce-3a5e-82b1-4d317a034f87 | -6.98478 | -47.08804 | 2025-06-05 03:40:00 | NOAA-20 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| aa42be06-6380-367e-b547-ec996327b7dd | -10.87783 | -46.86104 | 2025-06-05 03:42:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2ac17e9f-8866-3bd2-a484-83a5083bf0d5 | -8.44638 | -46.47943 | 2025-06-05 03:42:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 775278c8-52c2-3e3a-a61c-720475f0c0e8 | -9.38027 | -48.40603 | 2025-06-05 03:42:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4eff4311-bc0e-332d-9b18-81a3c47f2fbd | -11.9004 | -47.45544 | 2025-06-05 03:42:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7c2f3ef9-4d9b-3acc-9cef-4d2feb97d405 | -8.72428 | -47.98878 | 2025-06-05 03:42:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 4e8aca6a-8b2f-3407-af30-0a70b277a79c | -10.66826 | -44.38087 | 2025-06-05 03:42:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 9b565ec7-a247-3b3f-a974-fa8faa759925 | -10.5501 | -42.43395 | 2025-06-05 03:42:00 | NOAA-20 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| b43e2237-8027-3f77-bcbb-a832f8552929 | -8.45434 | -46.48332 | 2025-06-05 03:42:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| cbc14638-d6e8-3741-8196-8d23b54f9a07 | -10.64584 | -49.43425 | 2025-06-05 03:42:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| b105c37f-7248-3435-8207-6029d29e9751 | -12.154 | -46.59312 | 2025-06-05 03:42:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 17ef0348-f03d-3e65-9b55-52c56e93f3fd | -10.67428 | -44.37623 | 2025-06-05 03:42:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 95e3f3b6-4328-3309-8912-ba139d8d0be4 | -9.22481 | -48.85778 | 2025-06-05 03:42:00 | NOAA-20 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b9f531ac-20f3-3c23-97fc-b2af6156a025 | -11.42987 | -45.10044 | 2025-06-05 03:42:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 60181277-976c-3dc9-afa2-7fd4ce9a152b | -10.67393 | -44.37415 | 2025-06-05 03:42:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 72f3e364-b17d-3f81-8c20-2859bb7ae2fc | -10.64711 | -49.42818 | 2025-06-05 03:42:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 64769c22-09ed-38e6-90b2-eae486c166de | -10.86893 | -46.8733 | 2025-06-05 03:42:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4c65f467-12e4-3c9e-93a2-b9e8074250d1 | -8.73071 | -47.99009 | 2025-06-05 03:42:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 898ea1bc-0c88-375e-b946-5aafde8290de | -9.3868 | -48.40735 | 2025-06-05 03:42:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 891abdc6-9dda-348b-8abb-efaa0cf425d0 | -10.65035 | -49.44157 | 2025-06-05 03:42:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| daa8231d-5651-3c4d-8bbc-72bce5781239 | -10.86897 | -46.876 | 2025-06-05 03:42:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a34bacc8-654c-31e8-9b36-9543a733a754 | -10.84735 | -46.86044 | 2025-06-05 03:42:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 1c8d80f8-1fcf-3a41-b73e-193b67d73149 | -10.84654 | -46.86456 | 2025-06-05 03:42:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4fe288c1-3514-3df7-ad87-4db39bd66b9a | -10.669 | -44.3731 | 2025-06-05 03:42:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| fc2006f9-7ec7-3a7a-aee4-fc11be86fb4c | -11.42928 | -45.10356 | 2025-06-05 03:42:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 3902077e-928d-316c-8aca-e4f382a854b7 | -8.44846 | -46.48207 | 2025-06-05 03:42:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 75ea95ac-837e-3e87-abe7-7220a2ccc186 | -9.13801 | -41.00121 | 2025-06-05 03:42:00 | NOAA-20 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 65b3ebbf-6a97-3573-ae17-9b34bbafdf8a | -7.87523 | -45.9885 | 2025-06-05 03:42:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 7fec6374-c838-3a84-bbc0-1d9e60e5409c | -9.35225 | -47.69139 | 2025-06-05 03:42:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 25210306-7fba-383b-b37d-bbcddda8952e | -10.66692 | -44.38451 | 2025-06-05 03:42:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 70b4f5df-9887-3329-aca8-611d09a3d967 | -12.37584 | -45.92528 | 2025-06-05 03:42:00 | NOAA-20 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 48e2960c-9593-370d-a628-fa4342423e80 | -10.64355 | -49.44025 | 2025-06-05 03:42:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 61661205-44cc-3ca4-a143-c09f874b3905 | -8.96187 | -47.97598 | 2025-06-05 03:42:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 0f5e4cd6-c28f-30f7-bbd0-6f22e3f75057 | -8.72523 | -47.98598 | 2025-06-05 03:42:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e1417d5b-4f3d-35d9-b6b5-dd721f943049 | -10.34656 | -43.30343 | 2025-06-05 03:42:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| b3394ce8-9f45-39c9-ac0f-1e3fb8c61392 | -8.72415 | -47.99154 | 2025-06-05 03:42:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| ddbcf903-0e5e-32f1-a197-1d8e804602e6 | -14.15105 | -45.4852 | 2025-06-05 03:42:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 467e9668-194a-3ab9-8ecb-5dda79961077 | -9.38831 | -48.40689 | 2025-06-05 03:42:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a1a9f54e-70a2-3f98-8d7b-227ee3bba744 | -9.21809 | -48.85643 | 2025-06-05 03:42:00 | NOAA-20 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| c6e864b4-b621-384d-b0a4-177ca7478d22 | -7.87449 | -45.99257 | 2025-06-05 03:42:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d6bf2fb4-8102-33f8-b52c-03273f176dff | -10.65163 | -49.43522 | 2025-06-05 03:42:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 540de4cf-e7c3-3a42-87cd-827f0d3ea5c6 | -12.15327 | -46.59684 | 2025-06-05 03:42:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| dca52c81-6cd1-3d32-8daa-88da42431393 | -11.9063 | -47.45669 | 2025-06-05 03:42:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| dd585680-c28f-3646-9dbe-0bfe3ec5d155 | -10.85054 | -46.8463 | 2025-06-05 03:42:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0d97ea21-71e8-3878-8c64-e58c1bee97f0 | -13.56796 | -44.26405 | 2025-06-05 03:42:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 271fa02f-a3a7-337d-9439-2140884f2d79 | -13.34441 | -40.30672 | 2025-06-05 03:42:00 | NOAA-20 | MARACÁS | BAHIA | Brasil | 2920502 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| c47daf08-7375-34e6-92a8-444318ebca81 | -10.84655 | -46.86715 | 2025-06-05 03:42:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 9335619a-c681-3c10-8dd2-1ce5fe0af463 | -10.87554 | -46.87314 | 2025-06-05 03:42:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |


[Clique aqui para ver as próximas entradas](README5.md)
