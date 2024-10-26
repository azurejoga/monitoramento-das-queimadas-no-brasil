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

## Dados Diários - Página 38

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ec59be32-c079-3d60-9b80-9b3db9a14a3d | -5.41711 | -42.8264 | 2024-10-26 04:17:00 | NPP-375D | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| fbf6e4c7-bf1d-3c81-b0f0-f69457ff4c56 | -5.32335 | -42.97874 | 2024-10-26 04:17:00 | NPP-375D | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 3af8ca7a-64b9-3d6a-b055-6c1060c74b98 | -5.3228 | -42.98232 | 2024-10-26 04:17:00 | NPP-375D | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 0e613c39-5e37-3553-ad27-b0e2de91ff75 | -5.31997 | -42.97823 | 2024-10-26 04:17:00 | NPP-375D | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 925e14a6-da72-3c93-a98a-3c8cc5d51850 | -5.31942 | -42.98181 | 2024-10-26 04:17:00 | NPP-375D | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 5a6bf01f-e738-353e-b98e-7a77cd0609db | -3.48413 | -43.32694 | 2024-10-26 04:17:00 | NPP-375D | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 04ef1223-fe0e-3e74-a2a3-2d7913ae3025 | -3.48135 | -43.32295 | 2024-10-26 04:17:00 | NPP-375D | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 1b4afa26-53cb-3cf5-894d-ee7e3268235c | -3.4808 | -43.32642 | 2024-10-26 04:17:00 | NPP-375D | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| e8f15c8d-765e-3225-bf85-bcca57635a3f | -3.48025 | -43.3299 | 2024-10-26 04:17:00 | NPP-375D | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 7ec7f712-7637-3c53-aa38-396777ddc162 | -3.47971 | -43.33337 | 2024-10-26 04:17:00 | NPP-375D | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 364c8859-a9f0-3e96-a50a-d1254d08b1c0 | -3.47802 | -43.32243 | 2024-10-26 04:17:00 | NPP-375D | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 4732b41e-e93b-3b17-8c50-eedc19e17535 | -3.47747 | -43.3259 | 2024-10-26 04:17:00 | NPP-375D | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 13.1 |
| ddd755b9-85df-3c0a-b630-ddd7be799f9b | -3.47692 | -43.32938 | 2024-10-26 04:17:00 | NPP-375D | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 35.1 |
| c17678db-c4b9-30cc-acfa-39fb4a2083cd | -3.47638 | -43.33286 | 2024-10-26 04:17:00 | NPP-375D | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 35.1 |
| 8b673d20-8ee6-3ec6-8c46-918e92be34f5 | -3.47469 | -43.32191 | 2024-10-26 04:17:00 | NPP-375D | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 53f89511-6d78-36bf-93db-e51e5870818c | -3.47414 | -43.32539 | 2024-10-26 04:17:00 | NPP-375D | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 71c22e45-3274-3653-9877-ef4342f44dc0 | -3.47359 | -43.32886 | 2024-10-26 04:17:00 | NPP-375D | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 35.1 |
| 7551803a-eda4-3ffb-9faa-d0a709cc3174 | -3.47305 | -43.33234 | 2024-10-26 04:17:00 | NPP-375D | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 35.1 |
| f81dae16-e993-3b03-bc6e-8555033d3d13 | -3.47136 | -43.3214 | 2024-10-26 04:17:00 | NPP-375D | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 13.7 |
| b59832be-435d-364c-9f26-6070cdaefd98 | -3.47081 | -43.32487 | 2024-10-26 04:17:00 | NPP-375D | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 4566e5ea-8bfa-3a40-9fb0-bb029d849489 | -3.47026 | -43.32835 | 2024-10-26 04:17:00 | NPP-375D | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 1e5d4b50-69fb-36fe-a109-a1e52c473971 | -3.46972 | -43.33182 | 2024-10-26 04:17:00 | NPP-375D | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| ceea440e-8d65-33a8-93df-dc991cbecb09 | -3.29423 | -43.23696 | 2024-10-26 04:17:00 | NPP-375D | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fce0c356-17a5-3313-9b72-6be5c3632eb4 | -4.55935 | -43.56213 | 2024-10-26 04:17:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1de7e906-3774-3406-abd7-72698bddb8fe | -4.5335 | -43.42983 | 2024-10-26 04:17:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 36cea3e6-a0b5-33aa-ad3d-80744926d7ac | -4.52628 | -43.43229 | 2024-10-26 04:17:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7ecbdf73-fcb5-3493-8fa1-65e5963363fe | -4.92202 | -44.09836 | 2024-10-26 04:17:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d27e702c-47e0-3aa0-b010-e26f83b81fd2 | -4.92148 | -44.10182 | 2024-10-26 04:17:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4fe4e648-17b6-3ae9-b615-a1478f4d3dda | -4.9187 | -44.09784 | 2024-10-26 04:17:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| bc24ea7b-c1ce-3009-9fa3-210ae02d1d32 | -4.91816 | -44.1013 | 2024-10-26 04:17:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| c025ba1c-ad85-39b4-b163-dacc5285b406 | -4.91483 | -44.10078 | 2024-10-26 04:17:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 309cc168-776e-3944-b567-577e510e8d2e | -4.91151 | -44.10027 | 2024-10-26 04:17:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b75d9f42-b1dd-3e41-999f-48c264c781bb | -4.8178 | -44.3549 | 2024-10-26 04:17:00 | NPP-375D | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c3cc178c-ec4a-3058-9b67-6918b31fedd5 | -4.73045 | -44.39371 | 2024-10-26 04:17:00 | NPP-375D | CAPINZAL DO NORTE | MARANHÃO | Brasil | 2102754 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 82c20245-9e62-3ec2-b1f4-fd146f00355b | -4.7299 | -44.39717 | 2024-10-26 04:17:00 | NPP-375D | CAPINZAL DO NORTE | MARANHÃO | Brasil | 2102754 | 21 | 33 | nan | nan | nan | Cerrado | 14.3 |
| 51aae6ee-1116-3833-899d-2b9d93b83e63 | -4.72936 | -44.40063 | 2024-10-26 04:17:00 | NPP-375D | CAPINZAL DO NORTE | MARANHÃO | Brasil | 2102754 | 21 | 33 | nan | nan | nan | Cerrado | 14.3 |
| de40f9dd-dd0b-37f7-a925-52bf5c2367cf | -4.72658 | -44.39665 | 2024-10-26 04:17:00 | NPP-375D | CAPINZAL DO NORTE | MARANHÃO | Brasil | 2102754 | 21 | 33 | nan | nan | nan | Cerrado | 14.3 |
| c8e938e3-3c73-33ce-9277-5294f428e28c | -4.72604 | -44.40011 | 2024-10-26 04:17:00 | NPP-375D | CAPINZAL DO NORTE | MARANHÃO | Brasil | 2102754 | 21 | 33 | nan | nan | nan | Cerrado | 14.3 |
| 1244b0ed-44d5-3589-ad32-c858748e7c8d | -4.70355 | -44.4781 | 2024-10-26 04:17:00 | NPP-375D | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 55337915-5efd-33c3-8e3d-cb4fd02ab5c7 | -4.703 | -44.48155 | 2024-10-26 04:17:00 | NPP-375D | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a7678560-f2d6-3a77-bb13-4c71fb49f8e0 | -4.70246 | -44.48502 | 2024-10-26 04:17:00 | NPP-375D | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b08db21f-54f9-3643-b78d-8cd04df14063 | -4.69968 | -44.48103 | 2024-10-26 04:17:00 | NPP-375D | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 75622b5a-4b27-302e-853d-f2ebdeb0580a | -4.69914 | -44.48449 | 2024-10-26 04:17:00 | NPP-375D | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 84da57bb-cf92-39c3-8c7b-79ad0ea03396 | -4.2242 | -44.53399 | 2024-10-26 04:17:00 | NPP-375D | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 51929d7c-029d-323f-9a81-4c4a0ff20c9c | -4.20276 | -44.24363 | 2024-10-26 04:17:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 42b6e025-8dee-37e2-88f2-e6f2819a91b5 | -4.20222 | -44.24709 | 2024-10-26 04:17:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 167a1ed1-58db-30f6-8d56-9d99a5e6b776 | -4.19944 | -44.24311 | 2024-10-26 04:17:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| cd763367-8abf-341c-895a-4abd98f291fc | -4.1989 | -44.24657 | 2024-10-26 04:17:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d0500c34-31d5-375c-a6a7-88015f021811 | -4.19836 | -44.25002 | 2024-10-26 04:17:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3cb922f7-7d6c-3ef7-ad0b-de156b2681e7 | -4.19612 | -44.2426 | 2024-10-26 04:17:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 33ebee1e-e1fb-3148-9c57-21b9c3adca64 | -4.19558 | -44.24605 | 2024-10-26 04:17:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| fd242139-013e-3681-b014-e12c46965f33 | -4.1159 | -44.2336 | 2024-10-26 04:17:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d96bbc63-2314-34e1-a978-9a8739e5540c | -5.98299 | -44.43143 | 2024-10-26 04:17:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| bbe44479-2e5b-3fca-aec7-9b59f5437167 | -5.97967 | -44.43091 | 2024-10-26 04:17:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ad59eecb-6283-399a-8f6b-7967c7c92aef | -5.97029 | -44.23065 | 2024-10-26 04:17:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 9dfcd4ea-b194-360e-8563-c24743d58106 | -5.9315 | -44.65042 | 2024-10-26 04:17:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 94481f4a-fb46-335e-be50-dafb8d809d40 | -5.10242 | -43.85687 | 2024-10-26 04:17:00 | NPP-375D | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2ddee08c-9587-34d8-862c-ef8d5a1fd2ef | -3.61656 | -44.78106 | 2024-10-26 04:17:00 | NPP-375D | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 9e4a33f9-7f76-3952-8ee0-fabe1b5b4445 | -3.616 | -44.78456 | 2024-10-26 04:17:00 | NPP-375D | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9785b836-e18c-3b66-a67f-c0a8a9164a27 | -3.61322 | -44.78054 | 2024-10-26 04:17:00 | NPP-375D | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| af675bef-4456-3a60-8e66-6a2a7ae6e672 | -3.60988 | -44.78002 | 2024-10-26 04:17:00 | NPP-375D | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6e7a804b-fcff-35d6-ae03-58d91af3caf7 | -3.60712 | -44.97026 | 2024-10-26 04:17:00 | NPP-375D | VITÓRIA DO MEARIM | MARANHÃO | Brasil | 2112902 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 49c5bad6-04e7-33d8-af0e-73223bbe2aff | -3.60433 | -44.96621 | 2024-10-26 04:17:00 | NPP-375D | VITÓRIA DO MEARIM | MARANHÃO | Brasil | 2112902 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| efc1b108-0721-35e3-aeb0-74ff1453ea53 | -3.60377 | -44.96974 | 2024-10-26 04:17:00 | NPP-375D | VITÓRIA DO MEARIM | MARANHÃO | Brasil | 2112902 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1f8c6641-1731-3bfa-b935-4042bee09aae | -3.52638 | -44.96854 | 2024-10-26 04:17:00 | NPP-375D | VITÓRIA DO MEARIM | MARANHÃO | Brasil | 2112902 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 468e0798-4d2d-3ceb-a7d1-08e011259253 | -3.32021 | -45.47869 | 2024-10-26 04:17:00 | NPP-375D | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c36696c7-e69f-38d3-bd8a-2aef8ab687c9 | -3.31963 | -45.48231 | 2024-10-26 04:17:00 | NPP-375D | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 110d1d23-61bb-3467-9a53-c8df262c9cb1 | -3.28978 | -45.73657 | 2024-10-26 04:17:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 6.2 |
| edb0c539-836d-36a1-8803-fc39fcf772e2 | -3.28635 | -45.73603 | 2024-10-26 04:17:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 16.0 |
| eb53526b-e3b8-3db4-a637-e250489fb82b | -3.24651 | -45.80949 | 2024-10-26 04:17:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 058560e6-5339-383b-b0ab-655a2c361079 | -3.24592 | -45.81321 | 2024-10-26 04:17:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 5.7 |
| be5e1420-877f-3222-b647-5342958060d4 | -3.24308 | -45.80895 | 2024-10-26 04:17:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 3bdf19db-7f4a-33df-b2f8-2ad96276ae2b | -3.24248 | -45.81267 | 2024-10-26 04:17:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 5.7 |
| be400b87-bcb5-3d4d-abec-ed36b99a870a | -3.24237 | -45.28532 | 2024-10-26 04:17:00 | NPP-375D | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 00ec61d8-92d1-390a-b7fb-9dbf3c307c90 | -3.23053 | -45.55817 | 2024-10-26 04:17:00 | NPP-375D | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5e7cae40-3bf9-31fe-bb50-e14843ae4686 | -3.22909 | -45.15119 | 2024-10-26 04:17:00 | NPP-375D | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 72ea4e07-2b93-3000-84c4-0983abe4cf0e | -3.22572 | -45.15066 | 2024-10-26 04:17:00 | NPP-375D | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 92b27e22-a67e-3b0a-bd9a-fb4b4cb0beea | -3.10629 | -45.77259 | 2024-10-26 04:17:00 | NPP-375D | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6b713ae2-6915-38b5-8bc6-27ae9a9fcfe0 | -3.10518 | -45.77238 | 2024-10-26 04:17:00 | NPP-375D | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0ec53418-2d2e-365a-a2d2-5b804cf78415 | -3.08028 | -45.36298 | 2024-10-26 04:17:00 | NPP-375D | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0bc566ac-53b7-39c3-b0cd-fdceee20905b | -3.46064 | -45.97992 | 2024-10-26 04:17:00 | NPP-375D | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 84de9de8-acfd-3240-a71b-55b04d9ef326 | -3.46004 | -45.98368 | 2024-10-26 04:17:00 | NPP-375D | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 2abc6bbb-d42e-3a6c-9484-0c3f4ec231bb | -3.45719 | -45.97938 | 2024-10-26 04:17:00 | NPP-375D | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c6635881-09f0-3b77-a0db-4b5df3390bdf | -5.08239 | -45.24858 | 2024-10-26 04:17:00 | NPP-375D | SÃO RAIMUNDO DO DOCA BEZERRA | MARANHÃO | Brasil | 2111631 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 23cdcaec-6010-33e6-9ec9-2aa88271aca7 | -5.04303 | -45.45271 | 2024-10-26 04:17:00 | NPP-375D | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a55d0994-5714-333c-a61b-f0cde7f90af6 | -5.04246 | -45.45627 | 2024-10-26 04:17:00 | NPP-375D | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 17ed70fd-d43b-3159-8887-4b89f8bfa228 | -5.03967 | -45.45218 | 2024-10-26 04:17:00 | NPP-375D | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| dbc19328-c473-37b0-a371-09eb1dadd899 | -5.03166 | -45.12181 | 2024-10-26 04:17:00 | NPP-375D | SÃO RAIMUNDO DO DOCA BEZERRA | MARANHÃO | Brasil | 2111631 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8fc519a9-197c-3d44-bc26-1a3621b95db2 | -5.02832 | -45.12129 | 2024-10-26 04:17:00 | NPP-375D | SÃO RAIMUNDO DO DOCA BEZERRA | MARANHÃO | Brasil | 2111631 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 97a7d2bc-f9a9-3742-b0ef-173aa5720137 | -4.94975 | -45.61761 | 2024-10-26 04:17:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 572cd707-126c-30b0-869e-1ff6c3166968 | -4.94637 | -45.61708 | 2024-10-26 04:17:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 583a1566-b986-3d9f-afdd-f637645680c5 | -4.92272 | -45.85392 | 2024-10-26 04:17:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b2278118-a62a-38a9-a237-ee302d39b622 | -4.92214 | -45.85759 | 2024-10-26 04:17:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 95779795-fb1a-3120-86d7-17a895aad5ba | -4.92156 | -45.86126 | 2024-10-26 04:17:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a311e09b-7a87-3a06-bf6d-42ac4f0c78c9 | -4.91932 | -45.85338 | 2024-10-26 04:17:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a42397c9-e95d-36e1-a95e-9bd2790c5c12 | -4.91875 | -45.85705 | 2024-10-26 04:17:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 6de3bd02-9dc3-36f6-8743-6ed67c98199d | -4.91816 | -45.86071 | 2024-10-26 04:17:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 6c7d4951-5e44-31b8-92df-6243ebadb8ec | -4.91758 | -45.86438 | 2024-10-26 04:17:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 21e2dcf7-de72-352e-81a9-701ef73462c0 | -4.91535 | -45.85651 | 2024-10-26 04:17:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 4.5 |
| feebaecd-1f89-31a2-aa33-5ed3f53b649d | -4.91476 | -45.86018 | 2024-10-26 04:17:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 4.5 |


[Clique aqui para ver as próximas entradas](README39.md)
