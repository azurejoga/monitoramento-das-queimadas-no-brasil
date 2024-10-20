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

## Dados Diários - Página 41

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e610b3c4-f0c8-3e5b-adcc-03889f729810 | -1.05759 | -48.26217 | 2024-10-20 04:53:00 | NOAA-20 | SANTO ANTÔNIO DO TAUÁ | PARÁ | Brasil | 1507003 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 707af6a4-bd8f-323d-b496-a531cdc5065f | -1.47054 | -48.97213 | 2024-10-20 04:53:00 | NOAA-20 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c7cc9aec-1377-3788-aa7d-e25923d2e6ae | -1.46673 | -48.97155 | 2024-10-20 04:53:00 | NOAA-20 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 21bcd251-b611-320d-ab26-cc1992cf5371 | -1.46403 | -48.96878 | 2024-10-20 04:53:00 | NOAA-20 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| cd151b3b-80ae-3a7d-bbce-56e9c7f662a9 | -1.46292 | -48.97097 | 2024-10-20 04:53:00 | NOAA-20 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1af4cbcc-db94-37f8-8864-c668fdcdd439 | -1.01415 | -48.8474 | 2024-10-20 04:53:00 | NOAA-20 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b925243b-d1d7-3190-8ffa-925703201e8b | -1.01341 | -48.85207 | 2024-10-20 04:53:00 | NOAA-20 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d1f0e613-2c0e-3974-b08d-114e9ed9c478 | -1.01107 | -48.84214 | 2024-10-20 04:53:00 | NOAA-20 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0c185039-b289-3f3c-a930-46e1e5894e05 | -1.01034 | -48.84681 | 2024-10-20 04:53:00 | NOAA-20 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ee64967e-9dc9-3fa3-ac00-225134361c5c | 2.1113 | -50.85286 | 2024-10-20 04:53:00 | NOAA-20 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 9bd9ea41-1729-3c75-b72a-882915afab63 | 1.12279 | -51.04203 | 2024-10-20 04:53:00 | NOAA-20 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 091118ed-af78-3645-8da5-a4b3857e5d96 | 2.26844 | -51.62943 | 2024-10-20 04:53:00 | NOAA-20 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b23b9a8c-6325-376f-af54-2b509dd0751a | 1.11592 | -52.57711 | 2024-10-20 04:53:00 | NOAA-20 | PEDRA BRANCA DO AMAPARI | AMAPÁ | Brasil | 1600154 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 81fb93aa-3f50-3c20-8134-754e3c3f13d7 | 1.00876 | -52.21813 | 2024-10-20 04:53:00 | NOAA-20 | PEDRA BRANCA DO AMAPARI | AMAPÁ | Brasil | 1600154 | 16 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 7a37ecae-59d6-3fdb-b935-54b6648610d2 | 0.91611 | -52.12645 | 2024-10-20 04:53:00 | NOAA-20 | PEDRA BRANCA DO AMAPARI | AMAPÁ | Brasil | 1600154 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 609039fd-038b-3471-9602-fb4fa4056158 | 0.7393 | -51.91061 | 2024-10-20 04:53:00 | NOAA-20 | PEDRA BRANCA DO AMAPARI | AMAPÁ | Brasil | 1600154 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ce328e5f-1f68-37ce-bbab-91f87abd5c50 | 0.73876 | -51.90715 | 2024-10-20 04:53:00 | NOAA-20 | PEDRA BRANCA DO AMAPARI | AMAPÁ | Brasil | 1600154 | 16 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ad334113-3aa4-3052-aa56-58d1f824bea3 | 0.65544 | -51.874 | 2024-10-20 04:53:00 | NOAA-20 | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| dc1536c2-06ae-3036-af47-ce34cf47b31a | 0.6549 | -51.87053 | 2024-10-20 04:53:00 | NOAA-20 | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5ddcc160-7495-39a5-a2eb-caf67c0b6789 | 0.65435 | -51.86707 | 2024-10-20 04:53:00 | NOAA-20 | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 202bd971-c863-3a20-9590-86791f6b875e | 0.65213 | -51.87452 | 2024-10-20 04:53:00 | NOAA-20 | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8bf29658-b917-35e3-b7d3-40cabf348445 | 0.65158 | -51.87105 | 2024-10-20 04:53:00 | NOAA-20 | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 0.6 |
| fc194755-aeed-3b0d-b3a2-a1065e8bceae | 0.65103 | -51.86758 | 2024-10-20 04:53:00 | NOAA-20 | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 18f7a5db-ffa3-3ddf-85bd-fb2640874dfb | 0.64881 | -51.87503 | 2024-10-20 04:53:00 | NOAA-20 | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b99c3f4a-4549-3af7-82fc-4135f13a65e6 | 0.64771 | -51.86809 | 2024-10-20 04:53:00 | NOAA-20 | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 99a8d165-e2b0-3be1-9c5f-c9850d35412c | -0.36168 | -52.01813 | 2024-10-20 04:53:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7fb8d855-1ce9-39d6-aa8c-d631b4e8313b | -0.23478 | -51.52774 | 2024-10-20 04:53:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 97e5b034-0d1c-3fe2-aa2e-fecef924b794 | -0.23143 | -51.52721 | 2024-10-20 04:53:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0cef774d-5275-34bb-825e-f506b5e0658d | -1.44762 | -52.26496 | 2024-10-20 04:53:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ba31e91c-6a17-340a-b816-302db513a38f | -1.41318 | -52.4194 | 2024-10-20 04:53:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2389c43b-bd7f-37f0-bb5e-a6a00eaea766 | -1.41264 | -52.42285 | 2024-10-20 04:53:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ce17cc0d-8f79-3542-95dc-cd18b723de26 | -1.40028 | -52.35004 | 2024-10-20 04:53:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 145f3a8e-ac69-364a-a6d8-6904ac41eda6 | -1.35767 | -52.27593 | 2024-10-20 04:53:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9dc63f3e-f851-3d28-b2a1-d8a93a1017d2 | -1.35217 | -52.2893 | 2024-10-20 04:53:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 95d88ecc-9258-3b4b-b427-6e0f58507af8 | -1.35162 | -52.29277 | 2024-10-20 04:53:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4947cab2-42c9-3cac-bcf8-202a6e6db9f0 | -1.35107 | -52.29624 | 2024-10-20 04:53:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8d68b126-8229-394c-937e-9d4e4f984145 | -1.22025 | -51.93618 | 2024-10-20 04:53:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8f81a692-30f2-35b8-919b-a07261792f7f | -1.12918 | -52.15124 | 2024-10-20 04:53:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b5cfd2a5-84d6-395f-bfae-7105014df9e9 | -1.12586 | -52.15072 | 2024-10-20 04:53:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 87296c61-c2bb-3918-9f56-3897d27340d8 | -1.12253 | -52.15021 | 2024-10-20 04:53:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8624ed56-e0e7-3507-bdf1-74751d5987d0 | -0.95061 | -52.37945 | 2024-10-20 04:53:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b4a6d82c-4f38-3b32-8dff-99bc97e3cede | -1.05488 | -53.01469 | 2024-10-20 04:53:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| dcce0b06-1ddd-3a2f-88d0-3f37b60b7fe4 | -1.20594 | -53.37235 | 2024-10-20 04:53:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 11fdb648-0abc-30ad-8894-0528dd87b12c | -1.2054 | -53.37577 | 2024-10-20 04:53:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fb8bc349-3275-3288-a29b-9e9fc485fc4e | -1.1708 | -53.65951 | 2024-10-20 04:53:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 14.0 |
| d56d03bd-0f40-3782-a916-1957a25d7288 | -1.17026 | -53.66296 | 2024-10-20 04:53:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 14.0 |
| 339c58bd-4fc8-3790-9775-6c54fa71fbe3 | -1.16804 | -53.65553 | 2024-10-20 04:53:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 16.8 |
| 731566e6-4205-3911-8e5c-5a86d401e81e | -1.16749 | -53.65898 | 2024-10-20 04:53:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 14.0 |
| 16965efd-b558-3275-a26b-b26253480694 | -1.16695 | -53.66243 | 2024-10-20 04:53:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 14.0 |
| d83adfd4-916f-30b1-8634-35bb8b806976 | -1.16473 | -53.65499 | 2024-10-20 04:53:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 48eca6cd-160f-3165-98ae-28c98fa1e2cb | -1.16418 | -53.65844 | 2024-10-20 04:53:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| e4c0d6b9-17e7-3f5e-829e-ab9baf2c65bb | -1.10367 | -54.21377 | 2024-10-20 04:53:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0bfac225-9a07-3a86-82b6-4d67a852d590 | -1.08197 | -54.15612 | 2024-10-20 04:53:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0620b8ff-a282-3cf3-8d5d-d04a3469ca74 | -1.0795 | -54.15584 | 2024-10-20 04:53:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f0d38940-9e4e-347d-99aa-ec0e4c081ed1 | -1.0428 | -53.37112 | 2024-10-20 04:53:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 231bb0ac-994d-3fa3-9d67-9471cd83f7cd | -1.03949 | -53.37061 | 2024-10-20 04:53:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1f86b134-9468-31ab-afdd-dfce3fadd641 | 1.10802 | -59.61966 | 2024-10-20 04:53:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 500f9315-3a36-3cdd-aa93-b6b83dfa46a5 | 0.99746 | -59.44827 | 2024-10-20 04:53:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1818a1f6-2b71-3e6b-85c6-d8c8adb01a32 | 0.99674 | -59.44361 | 2024-10-20 04:53:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 116346a3-310f-3021-bb08-b6cf9bb9544d | 0.87912 | -59.70786 | 2024-10-20 04:53:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2d2ea2d2-9173-3109-a206-82f78e3c8958 | 0.87693 | -59.70628 | 2024-10-20 04:53:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 51f95fe3-6dc6-30dc-9b89-d187ae78f12a | -4.86036 | -43.23893 | 2024-10-20 04:55:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 00420ad6-be45-3485-b6e1-0d2080d002a3 | -4.74905 | -42.97203 | 2024-10-20 04:55:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| e8a9cdd6-0084-36ea-a4eb-54265c9fa9bf | -4.74306 | -42.97128 | 2024-10-20 04:55:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 7f236eef-7e9f-3df4-8f16-42910ec59a98 | -5.9511 | -43.38877 | 2024-10-20 04:55:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 15ab9c4a-8eb0-3dca-a84e-d63f8987b0eb | -5.94721 | -43.39018 | 2024-10-20 04:55:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Caatinga | 2.4 |
| e5341fdc-57dc-3fcb-b2c1-82dceeb1c530 | -5.94661 | -43.39438 | 2024-10-20 04:55:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Caatinga | 2.4 |
| fc3b50f5-e457-3849-ad2f-4f5b90c9e880 | -5.94518 | -43.38789 | 2024-10-20 04:55:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Caatinga | 1.2 |
| a83b485e-a80f-31c8-ae4a-50f1579b426b | -5.94461 | -43.39214 | 2024-10-20 04:55:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 9ef532bc-57c9-3a30-a46b-783a624b383d | -5.93252 | -43.36592 | 2024-10-20 04:55:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 07adfcb0-cfd3-37a2-895e-c45e775868b9 | -5.93191 | -43.37024 | 2024-10-20 04:55:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Caatinga | 1.3 |
| f77155de-3877-3498-8fda-47f2e6365970 | -5.93033 | -43.36353 | 2024-10-20 04:55:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 064380bc-e00e-3a2f-ad6c-7361956f96ad | -5.92976 | -43.36781 | 2024-10-20 04:55:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Caatinga | 2.5 |
| c978eb5a-cd1f-3613-a551-febbad844133 | -6.60189 | -43.43273 | 2024-10-20 04:55:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4f2425fa-81df-341c-b5aa-ffe67e6a0eba | -6.60133 | -43.43697 | 2024-10-20 04:55:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 651c0435-e4f4-3969-a4d1-3707773f9acc | -3.51772 | -43.61609 | 2024-10-20 04:55:00 | NOAA-20 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7f743f1f-73f8-3cd0-928c-0d075f0d8402 | -3.51717 | -43.61983 | 2024-10-20 04:55:00 | NOAA-20 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 67d4301e-548c-3a8c-851b-9dd2e99bbc98 | -4.58442 | -43.98696 | 2024-10-20 04:55:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 311d30d9-1f39-36bf-a603-cf2fd9e49dcd | -4.58293 | -43.98613 | 2024-10-20 04:55:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| cfbced10-7d32-3411-8815-e6cc8a306594 | -4.58242 | -43.98981 | 2024-10-20 04:55:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 167538ab-c9e7-3159-9e0b-98e2af0841e4 | -4.57829 | -43.98981 | 2024-10-20 04:55:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5b5a25de-b0b4-325d-93b0-afd564cd870f | -4.29043 | -44.52195 | 2024-10-20 04:55:00 | NOAA-20 | SÃO LUÍS GONZAGA DO MARANHÃO | MARANHÃO | Brasil | 2111409 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 47ac23c9-b48d-3c34-8c9a-9f4ccc285149 | -2.29588 | -48.58313 | 2024-10-20 04:55:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 518d8fad-f587-3b47-8c0a-4376ca713ba5 | -4.28992 | -44.52533 | 2024-10-20 04:55:00 | NOAA-20 | SÃO LUÍS GONZAGA DO MARANHÃO | MARANHÃO | Brasil | 2111409 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 08f98ee0-35e8-310d-93df-04a87f2357cf | -4.28782 | -44.52176 | 2024-10-20 04:55:00 | NOAA-20 | SÃO LUÍS GONZAGA DO MARANHÃO | MARANHÃO | Brasil | 2111409 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 46566ddd-ae09-33e9-ab4a-3f0666ff937a | -4.85976 | -43.24311 | 2024-10-20 04:55:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cac6df04-f7b5-30e3-88f3-20f3095507cb | -4.90087 | -44.63185 | 2024-10-20 04:55:00 | NOAA-20 | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 688b1d80-8506-31a0-bf69-7731655833b4 | -4.90033 | -44.63549 | 2024-10-20 04:55:00 | NOAA-20 | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b885e0aa-d4b1-3879-bd7d-60aef591ac82 | -5.85564 | -43.74199 | 2024-10-20 04:55:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a7aa41ec-cfaf-398c-9468-b5f6d0e8d1af | -5.85506 | -43.74617 | 2024-10-20 04:55:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0508b827-30af-3c4a-8b10-f932ccb804bc | -5.72082 | -43.77376 | 2024-10-20 04:55:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ce9bf706-54bb-3bd8-b5bf-42275402cc33 | -5.72028 | -43.77761 | 2024-10-20 04:55:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5e63d13f-e326-327f-bd38-0f586c9b3ced | -5.71506 | -43.77294 | 2024-10-20 04:55:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 578a37dd-93a6-3734-8e31-4723a71f15e2 | -5.54396 | -43.90265 | 2024-10-20 04:55:00 | NOAA-20 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| dfc2ca7a-bc71-30f3-b83e-756e4133cbab | -5.54342 | -43.9066 | 2024-10-20 04:55:00 | NOAA-20 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 95f7f5b6-49a7-39b0-987f-ba9b31901ad1 | -5.54288 | -43.91058 | 2024-10-20 04:55:00 | NOAA-20 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6a76fa78-8df7-32da-837b-11cdb5609a64 | -5.54139 | -43.90424 | 2024-10-20 04:55:00 | NOAA-20 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 26aff613-c966-3520-9600-edda9f533d17 | -5.54082 | -43.9082 | 2024-10-20 04:55:00 | NOAA-20 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| e898cde6-050d-3c79-8f14-68d013039638 | -5.54026 | -43.91213 | 2024-10-20 04:55:00 | NOAA-20 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 896e7fea-7e70-3d1c-926b-897a93a816a7 | -5.53774 | -43.90571 | 2024-10-20 04:55:00 | NOAA-20 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |


[Clique aqui para ver as próximas entradas](README42.md)
