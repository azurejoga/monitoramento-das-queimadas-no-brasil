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

## Dados Diários - Página 28

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9f29836c-2b8c-3fdd-8b35-d47874057b9a | -2.32729 | -51.28051 | 2024-11-14 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 90fd0466-7d94-33d2-9e97-3fdc1e600ee2 | -2.37525 | -48.5094 | 2024-11-14 04:40:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d0692235-a33f-369b-8347-228a7c4b1ef8 | -4.00704 | -46.41013 | 2024-11-14 04:40:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| bad88394-54cc-3e86-968d-61d72fcafb3f | -1.33481 | -51.41668 | 2024-11-14 04:40:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 964cbd35-6ab1-3c54-8027-55c52c56253b | -3.94328 | -48.99052 | 2024-11-14 04:40:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 13f4fd92-a811-380c-8705-4f8489534583 | -2.79485 | -48.28209 | 2024-11-14 04:40:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ed1bff9a-8710-3559-ac61-1901cb6b93dc | -2.11347 | -48.26765 | 2024-11-14 04:40:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a7093310-71e2-39bf-8021-ee6d4ad5f5b3 | -2.67085 | -46.82508 | 2024-11-14 04:40:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| bc4ba364-6655-3675-8462-7fdaa09b26b2 | -2.96048 | -48.70652 | 2024-11-14 04:40:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 71e4dd03-50f4-3ee6-83d6-55f24ccbd358 | -3.6415 | -50.59436 | 2024-11-14 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 41dd6b38-1284-33d6-8e47-0535b9b7e010 | -2.40221 | -48.51003 | 2024-11-14 04:40:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 25488660-9855-31eb-9ba7-35ea46fb909e | -3.26888 | -51.26892 | 2024-11-14 04:40:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 7be40f0a-86ad-335c-817a-c269e61ab611 | -2.3095 | -49.08252 | 2024-11-14 04:40:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 20493e53-3818-3f17-8d36-f41896c7156b | -3.0521 | -50.33313 | 2024-11-14 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 19f7f265-7579-3c04-86a7-b2264cc1dd37 | -3.99024 | -48.31561 | 2024-11-14 04:40:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b8ed70c7-9a50-3319-97c5-33abd32f36f2 | -4.05712 | -47.23287 | 2024-11-14 04:40:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fa99631a-7f55-3cd6-bb1a-b6bd1a87e16c | -2.37598 | -53.83956 | 2024-11-14 04:40:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ecfdc70a-7aa7-3a1a-8f0a-481a346fee76 | -2.88661 | -50.4181 | 2024-11-14 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f7049eed-0b31-37d8-861e-be25f3e72991 | -3.67487 | -50.16147 | 2024-11-14 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3d7ad056-3d8e-3faf-8eb0-ccc029c8dc5b | -1.6156 | -52.51678 | 2024-11-14 04:40:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8f42b6e1-cbe6-36da-b4f8-07f34304bfee | -3.20144 | -51.25505 | 2024-11-14 04:40:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cdcfa522-c719-31f5-9b24-ab3f54fd376e | -6.07077 | -44.88026 | 2024-11-14 04:40:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 342cfb1a-57b9-34d6-b9dc-384f11b0a191 | -2.07619 | -46.56465 | 2024-11-14 04:40:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| eb161bee-17eb-32da-8e9c-7e9048cb32b5 | -2.2223 | -48.39775 | 2024-11-14 04:40:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7f41d063-117d-37be-af31-b899068fa84f | -4.23053 | -46.87503 | 2024-11-14 04:40:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b3c5d5c3-fdd5-3b8f-935f-1b6cc0310d5b | -2.18714 | -46.57383 | 2024-11-14 04:40:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4d804d2a-3dea-33d5-8bb2-314e25ca1d39 | -2.40901 | -45.34214 | 2024-11-14 04:40:00 | NOAA-21 | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 0d191aca-070d-3e93-b0f2-33fce5a9feae | -2.85804 | -47.81108 | 2024-11-14 04:40:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1a9ca5be-fe68-3676-b46e-7ae84feef606 | -2.68184 | -56.92437 | 2024-11-14 04:40:00 | NOAA-21 | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7e8e06ca-6d08-30a1-8087-f38ac24b237a | -1.55868 | -51.86153 | 2024-11-14 04:40:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| f116c173-9308-387d-93e9-e18d5f69936a | -5.43302 | -47.38477 | 2024-11-14 04:40:00 | NOAA-21 | JOÃO LISBOA | MARANHÃO | Brasil | 2105500 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| dab3d05a-7090-3653-beba-173ce528b4ba | -2.64021 | -46.18125 | 2024-11-14 04:40:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 3.6 |
| c41698ab-7640-3b21-b9f5-46dbbf9b976f | -2.21301 | -50.81799 | 2024-11-14 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1205e691-e913-3512-b2b8-31e3aef2727e | -4.41198 | -48.60123 | 2024-11-14 04:40:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| edda12bb-a024-3560-926d-fc812b1ddc04 | -2.42417 | -46.26524 | 2024-11-14 04:40:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a68f131a-b286-3252-9daa-ef799a0dc914 | -2.18174 | -48.31056 | 2024-11-14 04:40:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 4972c797-f4a9-3946-89e4-e3ac580c288d | -1.79722 | -52.17915 | 2024-11-14 04:40:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| b9ce8d2e-8418-30b6-86f6-7cd06fccd13a | -2.14097 | -48.78916 | 2024-11-14 04:40:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f62f52fd-42e7-3912-a3c7-91ac3681888b | -2.17656 | -48.75601 | 2024-11-14 04:40:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 05b075b9-cbe0-3425-b8f8-c389216e33e1 | -4.25503 | -48.53809 | 2024-11-14 04:40:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4d762300-ebf8-36bd-825b-7c7814499496 | -1.13956 | -51.68985 | 2024-11-14 04:40:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 56a91f28-e804-3700-8e93-e44e0b228dc7 | -4.27305 | -48.20219 | 2024-11-14 04:40:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0d1bf87c-7586-3159-8553-def8e6960df1 | -2.9076 | -48.3001 | 2024-11-14 04:40:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 10b078cb-d20f-32a0-9671-92301d989430 | -2.2382 | -48.38261 | 2024-11-14 04:40:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 27daf3f1-ea93-3375-bf37-c13db349ce97 | -4.44736 | -45.3695 | 2024-11-14 04:40:00 | NOAA-21 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 144a6669-460e-3b96-a409-0d6874deff31 | -2.55884 | -51.23632 | 2024-11-14 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 649d4259-0a5e-387d-b957-873356d8fd42 | -2.3193 | -49.19326 | 2024-11-14 04:40:00 | NOAA-21 | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 50b7c252-bb07-350d-bd89-0b980de25506 | -4.73131 | -45.77769 | 2024-11-14 04:40:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f3145a89-ab54-3f4c-ad9f-268880f230a3 | -1.33935 | -46.56447 | 2024-11-14 04:40:00 | NOAA-21 | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| d702761f-4c4f-3b81-8b60-1cbeb5c116ec | -4.00746 | -45.56442 | 2024-11-14 04:40:00 | NOAA-21 | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f95f220d-5c83-3d9a-b14a-d76f3c3e7bab | -1.33559 | -51.40826 | 2024-11-14 04:40:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 31925c84-8bee-3c8b-aa1c-55a948b4f732 | -2.37472 | -48.51283 | 2024-11-14 04:40:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 23d9825c-145a-324d-8e7f-3a2bb721ff40 | -2.1534 | -50.90933 | 2024-11-14 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a30d36e4-24c1-389d-b1f9-0cef18542044 | -2.61969 | -48.07452 | 2024-11-14 04:40:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f97add9a-b30e-3606-90bc-2520086b28d1 | -4.07587 | -49.14128 | 2024-11-14 04:40:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e38f32f5-e8ff-3896-92b0-2aa24c255197 | -2.58639 | -47.48036 | 2024-11-14 04:40:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a151849b-17ab-33d4-84f8-169a10730b99 | -2.26059 | -48.32973 | 2024-11-14 04:40:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3860aa49-34f7-3299-b906-fc7cb0bb1fe2 | -1.245 | -47.79308 | 2024-11-14 04:40:00 | NOAA-21 | SÃO FRANCISCO DO PARÁ | PARÁ | Brasil | 1507409 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 960aa1c3-97f3-377d-935b-8ad8a7fa2aef | -2.72617 | -51.74115 | 2024-11-14 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 74380c05-d7c2-32f5-b30a-077448619ee7 | -1.80228 | -52.17106 | 2024-11-14 04:40:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 15.0 |
| 4b820e78-c876-3294-9590-c8fa5f257ee6 | -3.28889 | -45.36573 | 2024-11-14 04:40:00 | NOAA-21 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 32b6fe20-82aa-3e08-a881-ce376c1a87df | -3.03864 | -50.33104 | 2024-11-14 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 18e29eaa-14a1-3d9f-b683-a09494b54c9a | -2.89999 | -51.79203 | 2024-11-14 04:40:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 68241e25-9949-3c47-aa0e-3fdb76e1f101 | -3.4341 | -50.30857 | 2024-11-14 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c5739831-05ed-34b8-801b-9634427d2132 | -3.24696 | -46.52385 | 2024-11-14 04:40:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6751aa19-8984-33e3-af3b-8d4e674c8a91 | -3.93305 | -47.33478 | 2024-11-14 04:40:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| db75281f-af29-38e1-8b22-d9cbefdc83bc | -2.11706 | -50.69275 | 2024-11-14 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7c60543f-dba5-3995-a35e-06467121382c | -2.34895 | -53.87525 | 2024-11-14 04:40:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| fc6a80ae-3b19-3e3c-a01b-74b1380cd7bf | -3.03104 | -47.98856 | 2024-11-14 04:40:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8d0b720b-4d24-33bd-8abb-18dad100fb60 | -3.97005 | -46.7004 | 2024-11-14 04:40:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0b330b7f-8f39-34e0-a985-bcf217fcb13a | -1.21197 | -51.75548 | 2024-11-14 04:40:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7ac4c9d1-8fb6-3224-964b-8b87515107b5 | -2.94336 | -48.31263 | 2024-11-14 04:40:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 96b9c93a-4a0b-3891-9c94-122d483f068f | -5.35734 | -44.37054 | 2024-11-14 04:40:00 | NOAA-21 | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5eb17e74-82a5-3cdb-945b-d33e32475c74 | -1.55842 | -51.21373 | 2024-11-14 04:40:00 | NOAA-21 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9980223e-64a3-3bcc-9a38-84bc173d7836 | -2.31356 | -50.69241 | 2024-11-14 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 7c01179a-482f-3dac-9352-3bf591a32e89 | -3.77566 | -47.48576 | 2024-11-14 04:40:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| e7b62598-1970-38ac-83d1-057c8de76ce0 | -3.22594 | -50.54449 | 2024-11-14 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 44096be2-16bd-323b-8ef5-8f3dd18049d6 | -2.24829 | -53.74599 | 2024-11-14 04:40:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 94f8cb90-1083-3263-b7b3-7251f1ef6948 | -2.5605 | -51.23594 | 2024-11-14 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f9a71abc-653a-352e-91d3-c89f3c9a177d | -2.1122 | -50.85663 | 2024-11-14 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 68e356c1-1537-35d4-82c9-93d46ab8ac4d | -4.45783 | -44.93306 | 2024-11-14 04:40:00 | NOAA-21 | LAGO DO JUNCO | MARANHÃO | Brasil | 2105807 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d85c24dc-5f2a-32d0-8264-778eacb3ee1f | -2.79294 | -46.64818 | 2024-11-14 04:40:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| afcfbd18-c479-3d11-a21f-8343242342c6 | -1.93301 | -46.28344 | 2024-11-14 04:40:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| fbb5e242-8fe2-3950-8048-6fad8424c949 | -2.41363 | -48.48014 | 2024-11-14 04:40:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 05fa9f9e-9b6d-3ecd-843a-a26d68b86f9e | -2.36508 | -46.99023 | 2024-11-14 04:40:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| dd529d2c-a823-3700-90a7-c2710f1c7969 | -3.22581 | -50.58896 | 2024-11-14 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5581bb30-0cab-3d4d-96d5-e8ee80a6be57 | -4.52158 | -48.66132 | 2024-11-14 04:40:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 365adc86-0b02-32e6-abc3-46ce8fe2da3a | -3.16179 | -50.59047 | 2024-11-14 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 2f7e4b8e-c138-322b-af58-2a956b695b08 | -3.76778 | -47.49192 | 2024-11-14 04:40:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4bd49339-a60f-3629-b04d-ec42e5178f58 | -2.15543 | -48.9565 | 2024-11-14 04:40:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 017aca62-e9e3-3fbe-af78-9c983d8578c5 | -4.8181 | -45.79778 | 2024-11-14 04:40:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8bbe9a50-7e56-3dca-a4d3-152bd6b17b1f | -1.21427 | -51.76443 | 2024-11-14 04:40:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f24a4c8e-70bf-3490-a6b7-1b621ddd2b62 | -2.11657 | -46.52844 | 2024-11-14 04:40:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0eee3b90-124f-3b34-90e0-60b9f682effd | -2.23355 | -46.83912 | 2024-11-14 04:40:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 10287d95-d2ca-3686-824a-91cd9971acaa | -2.07932 | -46.47658 | 2024-11-14 04:40:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fab024c6-fec9-3d76-b5a8-424a10a8b0d5 | -1.55934 | -51.85731 | 2024-11-14 04:40:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 3be43d1d-250f-3a9f-993a-a259a3198463 | -2.11313 | -46.52791 | 2024-11-14 04:40:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2a8eb353-da03-3f31-9318-4238baf1a63d | -0.98692 | -51.77959 | 2024-11-14 04:40:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f23a3a42-537c-318d-bbd2-ca7a1d6c0b10 | -3.29738 | -51.59455 | 2024-11-14 04:40:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| b84c900f-be3f-3dae-8b4c-aa29a5fddd5a | -2.63971 | -46.16103 | 2024-11-14 04:40:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |


[Clique aqui para ver as próximas entradas](README29.md)
