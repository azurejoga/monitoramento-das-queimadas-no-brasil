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

## Dados Diários - Página 54

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7560247e-2c43-3b66-8816-99327ba7a454 | -12.46748 | -50.82629 | 2026-09-17 04:42:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3278ce2c-efe8-39fb-b34d-65e33d6745ca | -18.88551 | -46.84383 | 2026-09-17 04:44:00 | NOAA-21 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3fc2349b-48ef-3be0-b890-3a812ac9c5ca | -18.88964 | -46.84452 | 2026-09-17 04:44:00 | NOAA-21 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2ece75bf-ca50-3136-af6b-8f02dd200394 | -21.46244 | -48.68462 | 2026-09-17 04:44:00 | NOAA-21 | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 14.6 |
| ebded533-4b47-3c4e-b935-e48bcc0d1b8f | -21.4584 | -48.67512 | 2026-09-17 04:44:00 | NOAA-21 | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 76254e16-31ca-3b16-a254-fc5cf659e7c2 | -21.4616 | -48.68076 | 2026-09-17 04:44:00 | NOAA-21 | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 5bd0266d-4f72-3855-9830-20e1c9dd8175 | -21.44549 | -57.00126 | 2026-09-17 04:44:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f19cafb6-0e32-3fb2-bc99-c4af904b1d6e | -20.22665 | -50.91627 | 2026-09-17 04:44:00 | NOAA-21 | SANTA FÉ DO SUL | SÃO PAULO | Brasil | 3546603 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| e9598aa2-e7ce-3d60-a734-bf6b2b396e71 | -21.46224 | -48.6757 | 2026-09-17 04:44:00 | NOAA-21 | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 11.0 |
| d8cb9a96-86e2-3aa8-9098-91d6da8b1e00 | -21.46309 | -48.67966 | 2026-09-17 04:44:00 | NOAA-21 | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 14.6 |
| 68613732-1555-31ee-91b7-9921c15ec2ee | -18.11902 | -51.69369 | 2026-09-17 04:44:00 | NOAA-21 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a461c898-1091-35b1-af26-8d56ef14335c | -18.88734 | -49.76464 | 2026-09-17 04:44:00 | NOAA-21 | ITUIUTABA | MINAS GERAIS | Brasil | 3134202 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| e988a200-2248-3199-8e7d-d1f3d373f611 | -21.45927 | -48.67907 | 2026-09-17 04:44:00 | NOAA-21 | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 14.6 |
| 534396ff-8e65-3450-90ff-787360d4ca96 | -18.12454 | -51.72448 | 2026-09-17 04:44:00 | NOAA-21 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| cd94d75e-4c68-35df-80e9-4f247214e0ce | -21.45778 | -48.68017 | 2026-09-17 04:44:00 | NOAA-21 | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 17c3a260-f34c-34cf-8e0e-b62fa3c9a299 | -23.02942 | -52.66517 | 2026-09-17 04:44:00 | NOAA-21 | PARANAVAÍ | PARANÁ | Brasil | 4118402 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| 1fa9e8ff-222e-32fd-81eb-b5d18e3dfc28 | -21.45993 | -48.67401 | 2026-09-17 04:44:00 | NOAA-21 | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 146e461a-9772-3c65-8c93-4cfbe6bf80e5 | -18.11199 | -51.69664 | 2026-09-17 04:44:00 | NOAA-21 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b0062ee6-9305-3284-a977-88e801737c93 | -27.01841 | -50.48565 | 2026-09-17 04:46:00 | NOAA-21 | SANTA CECÍLIA | SANTA CATARINA | Brasil | 4215505 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 59458e44-9bf5-396c-bffc-097fb00f6e5a | -27.56374 | -48.66177 | 2026-09-17 04:46:00 | NOAA-21 | SÃO JOSÉ | SANTA CATARINA | Brasil | 4216602 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| e6a62f0e-f52a-32a4-af08-f486d80050cc | -29.89109 | -51.23267 | 2026-09-17 04:46:00 | NOAA-21 | CANOAS | RIO GRANDE DO SUL | Brasil | 4304606 | 43 | 33 | nan | nan | nan | Pampa | 0.9 |
| d3450f80-db64-3e79-841e-6de549389114 | -27.34026 | -50.73652 | 2026-09-17 04:46:00 | NOAA-21 | CURITIBANOS | SANTA CATARINA | Brasil | 4204806 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| be9e037a-10f9-3438-9eea-9e5872f32c17 | 0.91189 | -59.62956 | 2026-09-17 05:14:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f9986b52-a753-3efe-825d-e1594d83eae0 | -1.03662 | -53.73472 | 2026-09-17 05:14:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 439d567e-55b6-3bb0-bdf1-35fbd352acd3 | -1.79501 | -52.17994 | 2026-09-17 05:14:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 72e3c54e-5efd-308b-8c64-9f96d5395a4f | -1.50077 | -54.96972 | 2026-09-17 05:14:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d5c08ab4-f69c-3032-bea4-807ed827d78b | -2.29941 | -48.58198 | 2026-09-17 05:14:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e40f2a34-4dab-3f82-8a63-3471db0dc6f7 | -1.79149 | -52.17935 | 2026-09-17 05:14:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 6da77cc3-cc3e-3250-ab6f-2d69291bf987 | -1.22794 | -54.12405 | 2026-09-17 05:14:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6d0882c0-16b2-3dc5-9a3c-55c5a4b08f72 | 2.72116 | -60.30045 | 2026-09-17 05:14:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 9c6861ac-7c62-31a0-bfc6-8930d65b6d8b | -2.7235 | -47.55686 | 2026-09-17 05:14:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| af23767c-5992-374b-bb88-007d810457d7 | -1.02215 | -53.73959 | 2026-09-17 05:14:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c1abbf7c-3c25-3081-8d72-da0cfac77fa5 | -1.22559 | -54.12377 | 2026-09-17 05:14:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 27223933-df1b-3a65-b9c1-284cc80d12b2 | -1.18633 | -53.38534 | 2026-09-17 05:14:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5bb4faa1-6c23-3f9e-bb09-3d186913715f | -2.10292 | -52.05381 | 2026-09-17 05:14:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 96aa3a83-0e63-3ae3-bec7-841dfda200a7 | -1.50355 | -54.9737 | 2026-09-17 05:14:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fa019841-07a2-3d6c-afdb-e98d005365c2 | -2.09669 | -52.05397 | 2026-09-17 05:14:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 244e400f-8bd4-3886-a88f-0d3dfbeb2f2a | -0.9185 | -47.20525 | 2026-09-17 05:14:00 | NPP-375D | PRIMAVERA | PARÁ | Brasil | 1506104 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| fdb1427c-d255-332b-8284-fdf0411f630a | -2.09936 | -52.05326 | 2026-09-17 05:14:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| eaf79c04-1d06-309e-94fa-69b0d401fcdf | 2.71599 | -60.29673 | 2026-09-17 05:14:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 3.1 |
| db9f862f-fa09-3066-a53e-fe1d98e9a317 | -1.50022 | -54.97318 | 2026-09-17 05:14:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2d5082f7-b259-31bc-9cb3-259c45e5b132 | 1.96195 | -50.98021 | 2026-09-17 05:14:00 | NPP-375D | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d8d8c439-e745-3e8e-9190-7bfb8bcc799a | -1.67802 | -53.67896 | 2026-09-17 05:14:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5a5ef45b-18a0-36a3-8e5b-459942d447a4 | 2.20602 | -50.87733 | 2026-09-17 05:14:00 | NPP-375D | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2571bc0d-8bd8-30bb-a67f-2e39a810a953 | 2.20243 | -50.8779 | 2026-09-17 05:14:00 | NPP-375D | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bcd26c88-fe08-342e-97bb-6d8f98abe76e | 1.17009 | -52.76142 | 2026-09-17 05:14:00 | NPP-375D | PEDRA BRANCA DO AMAPARI | AMAPÁ | Brasil | 1600154 | 16 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 0a9c0a5f-13f3-3c36-bf2c-de28ad626fb7 | 1.2873 | -50.89395 | 2026-09-17 05:14:00 | NPP-375D | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7c2c3aea-0790-3a56-896e-386f5239e07b | 0.78566 | -59.20002 | 2026-09-17 05:14:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4dd1f1e2-018b-3996-b6fa-521ef17be1c1 | -1.14751 | -54.16467 | 2026-09-17 05:14:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4e96a924-b4d6-3fdf-89c4-46897781a67d | -1.60902 | -55.56637 | 2026-09-17 05:14:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 932749aa-2137-3ac5-924f-485153b232c6 | -1.61236 | -55.56689 | 2026-09-17 05:14:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 18c9ca6f-24ca-3f99-b93d-122f0bc7b75e | -1.78456 | -47.83364 | 2026-09-17 05:14:00 | NPP-375D | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 4480bfe7-32be-3fa8-9461-673897bd0423 | 2.20667 | -50.88141 | 2026-09-17 05:14:00 | NPP-375D | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 736d1abc-d6bb-31a1-8dc5-385529f5563b | 2.71082 | -60.29298 | 2026-09-17 05:14:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| af696994-deec-3edd-8e57-787ac7f45f31 | -1.78629 | -47.83204 | 2026-09-17 05:14:00 | NPP-375D | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d3660bf0-d8e5-38e5-b1b6-599676abec73 | -1.20024 | -54.21898 | 2026-09-17 05:14:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0b42d455-1578-34d6-89b5-ecc2c442afd6 | -1.03218 | -53.74116 | 2026-09-17 05:14:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 376af121-0717-325a-8eec-af594b3fdaa8 | -1.02549 | -53.74012 | 2026-09-17 05:14:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7a4f292a-7127-362c-b8d9-babeecb16bd0 | -1.78168 | -47.83132 | 2026-09-17 05:14:00 | NPP-375D | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 07e4538a-1899-3678-8b1d-c4aad2327eb0 | -1.60567 | -55.56586 | 2026-09-17 05:14:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8e1fdb9b-4eb6-36b3-88b1-47f0504fe7a2 | -2.62509 | -49.1118 | 2026-09-17 05:14:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6bcdfb2b-2178-374a-a567-85c0d79e4259 | -1.14641 | -54.17159 | 2026-09-17 05:14:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 9ff370f1-ce84-3db0-ac8a-71e21611768a | 2.71667 | -60.30119 | 2026-09-17 05:14:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d57378de-500b-312e-a7a0-566266d9a17a | -1.25107 | -55.70857 | 2026-09-17 05:14:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| faa2904e-ec9b-3697-8aa6-41e2853fa1b2 | -1.50409 | -54.97025 | 2026-09-17 05:14:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e6f44f01-4122-3329-bc57-e5c003a2fcb3 | -1.01824 | -53.72105 | 2026-09-17 05:14:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d92953c3-aad3-3de1-b581-8e5fefd0923b | -1.60846 | -55.56988 | 2026-09-17 05:14:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 17969c45-0bc8-37d0-b5bc-e4b61bd37e68 | -1.14974 | -54.17211 | 2026-09-17 05:14:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 1b292bb1-6b82-3f62-8652-28cc2eb52249 | -2.09998 | -52.04926 | 2026-09-17 05:14:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5faa883d-64a1-3731-9716-747d3c849b08 | -0.91769 | -47.21027 | 2026-09-17 05:14:00 | NPP-375D | PRIMAVERA | PARÁ | Brasil | 1506104 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6496429e-e68b-35c3-a98a-150fa00b8f5d | 2.20308 | -50.88198 | 2026-09-17 05:14:00 | NPP-375D | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8d875b97-a511-36cc-8610-08617d0b8fee | 1.91854 | -50.83073 | 2026-09-17 05:14:00 | NPP-375D | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 91b29bca-6d48-386e-aa35-f76b782f0b2b | -2.09733 | -52.04997 | 2026-09-17 05:14:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2109dfcc-1591-3080-8047-a33b8ca2b084 | 2.51522 | -50.84832 | 2026-09-17 05:14:00 | NPP-375D | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ce7b0320-6503-35a4-a1a4-389218fec973 | -1.03996 | -53.73524 | 2026-09-17 05:14:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 39a3e115-185b-3e96-b0fa-44efccbc253d | -1.03941 | -53.73874 | 2026-09-17 05:14:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 42225879-9a83-3cf2-8d2a-6da25d50c866 | -1.19747 | -54.215 | 2026-09-17 05:14:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d22e7a13-23dd-339f-810d-bd2a2f67cef4 | 1.95306 | -50.94824 | 2026-09-17 05:14:00 | NPP-375D | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 379a5ae4-8a95-35f2-ad83-21638b0bbee6 | -2.62447 | -49.11578 | 2026-09-17 05:14:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8519a4b1-3455-3871-8774-ebef8a1ed98d | -1.34456 | -55.84657 | 2026-09-17 05:14:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 022c4230-cda9-3329-988f-56e9fd4235cd | -1.61181 | -55.5704 | 2026-09-17 05:14:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 35cca892-7cac-3166-8e9b-ac64de0f07bf | -2.10416 | -52.04581 | 2026-09-17 05:14:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fa641bd6-ebb3-31cf-a2e1-91d3112b333f | -1.03607 | -53.73823 | 2026-09-17 05:14:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 04a7bcfa-6914-3a8f-b99f-19b1a4f51c35 | 2.72048 | -60.296 | 2026-09-17 05:14:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 27fbf705-aa92-32fe-b746-52484da1b791 | -1.15028 | -54.16865 | 2026-09-17 05:14:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 12257edc-81ef-31ac-9c44-a32fe994df63 | -1.60957 | -55.56287 | 2026-09-17 05:14:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| fcf40888-32a4-30b3-a753-50d1630c2cff | -1.14696 | -54.16813 | 2026-09-17 05:14:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 8cef7bc5-0a91-3ffe-a8b5-c0ac32081901 | -1.21701 | -55.64172 | 2026-09-17 05:14:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 05ac7931-e3f8-3f0c-9e79-c879f7073e74 | 2.21092 | -50.88491 | 2026-09-17 05:14:00 | NPP-375D | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 78b9847e-58e7-3abf-8d75-4689542fe834 | -1.22036 | -55.64224 | 2026-09-17 05:14:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5c165daf-1c76-33d0-b4b9-3b98d0102da3 | 2.21026 | -50.88084 | 2026-09-17 05:14:00 | NPP-375D | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d600f2d8-f815-3798-8fee-98b196658f3b | 0.91547 | -59.62516 | 2026-09-17 05:14:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c051b305-6486-3882-a91f-4161d7f94358 | 1.96129 | -50.97614 | 2026-09-17 05:14:00 | NPP-375D | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b61f9174-6d05-3462-876b-8e55725937bf | -1.65255 | -55.18468 | 2026-09-17 05:14:00 | NPP-375D | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 1175aad4-3e5c-3730-8242-e26a4ab76b06 | -1.20079 | -54.21552 | 2026-09-17 05:14:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c08cb31a-04a2-3844-bc9c-6e24fc2fcc49 | 0.9113 | -59.62584 | 2026-09-17 05:14:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 91da7466-6c93-31bd-b368-c9e0a251ae08 | 1.95704 | -50.97264 | 2026-09-17 05:14:00 | NPP-375D | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b82bba01-af62-389e-abc0-2cc837eda655 | -0.91886 | -47.20692 | 2026-09-17 05:14:00 | NPP-375D | PRIMAVERA | PARÁ | Brasil | 1506104 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| e39e3e35-9753-35d5-beb2-722a1ba483dd | -2.05187 | -52.08381 | 2026-09-17 05:14:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6cb4bce3-804c-3860-b6fc-702c5db23527 | 1.95622 | -50.97613 | 2026-09-17 05:14:00 | NPP-375D | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |


[Clique aqui para ver as próximas entradas](README55.md)
