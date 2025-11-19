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

## Dados Diários - Página 22

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 356605e4-f720-36e9-9b28-4926b71250a0 | -12.21866 | -60.94871 | 2025-11-19 12:59:00 | TERRA_M-T | CHUPINGUAIA | RONDÔNIA | Brasil | 1100924 | 11 | 33 | nan | nan | nan | Amazônia | 8.0 |
| f99e8750-9dc3-3682-aa48-590883d8deb2 | -15.12522 | -55.48365 | 2025-11-19 12:59:00 | TERRA_M-T | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 18.9 |
| dd9b0e80-7816-365c-b7c9-723e2e7b6ca6 | -11.59342 | -59.04896 | 2025-11-19 12:59:00 | TERRA_M-T | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 7.9 |
| e35debb4-2dc2-3388-8ca8-ee5fca58a2e5 | -12.87985 | -56.53464 | 2025-11-19 12:59:00 | TERRA_M-T | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 417ed77c-c527-3a48-bfc8-f4ed788d65a5 | -11.52893 | -59.0427 | 2025-11-19 12:59:00 | TERRA_M-T | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 9.0 |
| c7351a37-f808-312d-a1a3-21b1f4be7f74 | -12.11646 | -57.82068 | 2025-11-19 12:59:00 | TERRA_M-T | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 4624a809-75aa-3aec-b3de-5b0f89148cda | -12.79817 | -57.00533 | 2025-11-19 12:59:00 | TERRA_M-T | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 9.5 |
| dbf42201-e435-327d-ac75-c84f44cad0c2 | -15.94081 | -58.14793 | 2025-11-19 12:59:00 | TERRA_M-T | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 9.5 |
| 047cfd64-8ac0-32d7-8476-ea0a4502945f | -12.08993 | -57.21587 | 2025-11-19 12:59:00 | TERRA_M-T | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 7.3 |
| c0b7c371-e8ff-36cb-8648-69abd6379be6 | -15.71551 | -57.63452 | 2025-11-19 12:59:00 | TERRA_M-T | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 0edf9ec9-45e2-38f4-968b-2e916a0a3394 | -11.88031 | -58.71063 | 2025-11-19 12:59:00 | TERRA_M-T | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 6.7 |
| ee9952de-6354-3a76-8178-500ee564e9f5 | -12.86412 | -55.64199 | 2025-11-19 12:59:00 | TERRA_M-T | SORRISO | MATO GROSSO | Brasil | 5107925 | 51 | 33 | nan | nan | nan | Cerrado | 11.5 |
| a9171f07-8ee7-34dc-8bd3-8c9d71b79cb3 | -16.01476 | -57.64758 | 2025-11-19 12:59:00 | TERRA_M-T | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 9.0 |
| f1d60485-da13-31f3-a227-6346ac81abfd | -12.37492 | -55.08936 | 2025-11-19 12:59:00 | TERRA_M-T | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 12.3 |
| b03a2f55-e377-3c6f-b346-28f85ada0d63 | -13.00777 | -55.07923 | 2025-11-19 12:59:00 | TERRA_M-T | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 13.4 |
| 9c6773d7-7def-3caa-9214-f412eacf2972 | -11.52328 | -55.89397 | 2025-11-19 12:59:00 | TERRA_M-T | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 7666c90e-99e9-3a4d-a493-172dd0271a13 | -15.00512 | -53.62368 | 2025-11-19 12:59:00 | TERRA_M-T | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 17.2 |
| 6c0aea56-b28c-33e8-8b27-f85daa0f0b90 | -12.08857 | -57.22572 | 2025-11-19 12:59:00 | TERRA_M-T | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 332efbd0-1f48-3d12-8c9f-436f92b85bdc | -11.5947 | -59.04004 | 2025-11-19 12:59:00 | TERRA_M-T | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 491f87cc-1fe7-3fe2-9559-584d4a690ffe | -15.11192 | -58.28012 | 2025-11-19 12:59:00 | TERRA_M-T | RESERVA DO CABAÇAL | MATO GROSSO | Brasil | 5107156 | 51 | 33 | nan | nan | nan | Amazônia | 30.3 |
| 9d05e482-04af-3723-b0b5-57e82a23b521 | -13.32475 | -56.17524 | 2025-11-19 12:59:00 | TERRA_M-T | LUCAS DO RIO VERDE | MATO GROSSO | Brasil | 5105259 | 51 | 33 | nan | nan | nan | Cerrado | 9.8 |
| ca193a34-81ca-37ce-9a5c-534d4dae4df9 | -12.29757 | -56.51157 | 2025-11-19 12:59:00 | TERRA_M-T | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 8.9 |
| b217a29d-0e6a-37b4-bf2e-620bcf9b3274 | -12.11515 | -57.83002 | 2025-11-19 12:59:00 | TERRA_M-T | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 9.1 |
| b0f200ec-dd58-3550-8594-c9291f6bd4d9 | -15.69076 | -56.01514 | 2025-11-19 12:59:00 | TERRA_M-T | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Pantanal | 7.4 |
| dce6383a-089d-3545-9417-7ee2b07447d2 | -15.12354 | -55.49726 | 2025-11-19 12:59:00 | TERRA_M-T | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 16.4 |
| d9211f13-141c-3537-a3dd-69ce3adf7451 | -12.79953 | -56.99503 | 2025-11-19 12:59:00 | TERRA_M-T | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 6a8f0638-5d92-33af-97b5-da673bf45d3a | -16.00832 | -57.65133 | 2025-11-19 12:59:00 | TERRA_M-T | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 6480cbc4-fd9f-3a9d-8a2e-07d5a00d7a89 | -15.64507 | -57.54483 | 2025-11-19 12:59:00 | TERRA_M-T | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Amazônia | 10.4 |
| c4fab83c-d9ca-315f-8346-a81627cde278 | -9.3226 | -36.9775 | 2025-11-19 13:30:00 | GOES-19 | IATI | PERNAMBUCO | Brasil | 2606507 | 26 | 33 | nan | nan | nan | Caatinga | 97.0 |
| bce008f4-0795-3847-b845-8639be157697 | 0.8925 | -51.1043 | 2025-11-19 13:30:00 | GOES-19 | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 92.1 |
| 03db046f-04f2-3bca-aaf6-d6af81559086 | 0.9109 | -51.1042 | 2025-11-19 13:30:00 | GOES-19 | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 106.3 |


