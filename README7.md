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

## Dados Diários - Página 7

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9b99b8df-4072-3b8c-9b0d-55918f0c804c | 4.6568 | -60.91364 | 2025-03-25 06:08:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 3.0 |
| c2c97e9d-4666-3b78-a014-0c31bf17204f | 1.52849 | -60.71 | 2025-03-25 06:08:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| da1beda0-988a-3150-983a-4829a4b24e12 | 4.65753 | -60.91795 | 2025-03-25 06:08:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cb587e48-b354-38a2-8930-44808cce04a0 | 2.58238 | -60.27225 | 2025-03-25 06:08:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 968d12e1-8938-3a74-9fd6-918c52f0b11e | 4.66215 | -60.91327 | 2025-03-25 06:08:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 49e6abfa-0444-3ff6-9d9f-9e14a9c35e78 | 2.91219 | -60.43206 | 2025-03-25 06:08:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3dee6a16-e029-389d-804d-18f5dca29a6a | 4.657 | -60.91626 | 2025-03-25 06:08:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 514fbf02-5b56-3fa9-92e7-7bf355ccd197 | 2.89956 | -60.46418 | 2025-03-25 06:08:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a9209057-72bd-3249-9ee6-474527c18ca8 | 4.66289 | -60.9175 | 2025-03-25 06:08:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3e176088-fc53-3958-b2aa-803d71a9f802 | 2.9054 | -60.46321 | 2025-03-25 06:08:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 28ab7219-5933-31d5-95ab-decf85956514 | 4.65828 | -60.92244 | 2025-03-25 06:08:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d831b846-560c-3e98-b7c0-c51ed73c54ce | 2.90634 | -60.43304 | 2025-03-25 06:08:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 42d23d09-80e5-3ec9-9a09-1f6052e4b2ba | 4.65777 | -60.92064 | 2025-03-25 06:08:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 718dad16-51da-3cac-a33e-9d48c0b7687d | 2.90704 | -60.43722 | 2025-03-25 06:08:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6703a30f-4187-30ed-bc6e-a28f018b7246 | 4.66696 | -60.90833 | 2025-03-25 06:08:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f69e721a-7d82-31f9-9c2f-ee705dee8e79 | 4.65624 | -60.91194 | 2025-03-25 06:08:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 32217eca-c5f8-3d93-adfd-3a4c749dda61 | 1.52917 | -60.71416 | 2025-03-25 06:08:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 92f13f4d-546a-3946-b18d-4e371fb6885b | 1.10949 | -60.54443 | 2025-03-25 06:10:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 274f25e3-1985-3f26-a798-ee547f726cce | 2.90223 | -60.46767 | 2025-03-25 06:37:00 | AQUA_M-M | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 48a1db00-3f53-35b5-b5c6-23ff21a3b1b8 | 2.90091 | -60.45892 | 2025-03-25 06:37:00 | AQUA_M-M | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 04312685-b76a-3879-806f-fa8871f76a2c | 2.90971 | -60.45763 | 2025-03-25 06:37:00 | AQUA_M-M | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 13.9 |
| d6b67716-657c-3836-887d-1211bd9d0459 | 2.91102 | -60.46638 | 2025-03-25 06:37:00 | AQUA_M-M | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 4.5 |
| a2a0a5ef-5246-35f6-a37c-0cadd3420b0b | -17.8658 | -39.8648 | 2025-03-25 07:00:00 | GOES-16 | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 129.1 |
| 50a96d09-4923-3171-bcde-9e7e490beaeb | -17.8666 | -39.8386 | 2025-03-25 07:00:00 | GOES-16 | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 81.4 |
| 5ab4504f-62e5-3c97-a508-63dd61ce1858 | -17.8658 | -39.8648 | 2025-03-25 07:10:00 | GOES-16 | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 120.5 |
| 9e720b8b-9792-3857-80b2-139005976e07 | -17.8666 | -39.8386 | 2025-03-25 07:10:00 | GOES-16 | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 78.5 |
| c5f6021b-ef4f-34e3-bd09-db523e4e3c14 | -17.8658 | -39.8648 | 2025-03-25 07:20:00 | GOES-16 | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 125.4 |
| 4a0b4c07-52ee-3bbd-afa6-b731eece5ccd | -17.8666 | -39.8386 | 2025-03-25 07:20:00 | GOES-16 | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 78.5 |
| 56d477ef-be69-316b-b67d-25b181aa58b9 | -17.8666 | -39.8386 | 2025-03-25 07:30:00 | GOES-16 | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 86.6 |
| 8daf0592-4642-3c59-9eac-f31a8d6fc2c1 | -17.8658 | -39.8648 | 2025-03-25 07:30:00 | GOES-16 | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 126.4 |
| aede776f-5473-3657-9b76-c2f4ec99002e | -17.8666 | -39.8386 | 2025-03-25 07:40:00 | GOES-16 | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 84.9 |
| 61eb3b97-6d02-35f9-a4dc-96f7455cc57f | -17.8658 | -39.8648 | 2025-03-25 07:40:00 | GOES-16 | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 130.1 |
| 391d17df-9df3-39d2-b973-866c6ea862f1 | -17.8666 | -39.8386 | 2025-03-25 07:50:00 | GOES-16 | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 78.1 |
| 10965ef1-c744-302d-94d1-9399416a363b | -17.8658 | -39.8648 | 2025-03-25 07:50:00 | GOES-16 | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 109.6 |
| a8f0e05f-9670-37c4-afca-88f3cd1a970a | -17.8658 | -39.8648 | 2025-03-25 08:00:00 | GOES-16 | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 104.5 |


