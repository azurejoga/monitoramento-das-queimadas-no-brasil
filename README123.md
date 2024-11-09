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

## Dados Diários - Página 123

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b9d30552-6417-35cc-9093-a330d6d475fc | -2.3605 | -46.8557 | 2024-11-09 14:10:00 | GOES-16 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 143.5 |
| 6201cb7a-1ba4-3686-b74e-43e7e4f6e93a | -3.3694 | -45.2865 | 2024-11-09 14:10:00 | GOES-16 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 71.8 |
| 50058887-b758-3af8-85e1-46db1c7b94d1 | -3.9625 | -48.9883 | 2024-11-09 14:10:00 | GOES-16 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 76.8 |
| ce97c1b3-b688-3890-9673-e71225b195a5 | -2.6276 | -49.8824 | 2024-11-09 14:10:00 | GOES-16 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 56.9 |
| 3a8b4e3e-e485-35e2-85a8-807262170984 | -0.2299 | -51.6249 | 2024-11-09 14:10:00 | GOES-16 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 85.5 |
| cd0345da-9059-3e1d-9ec7-ad5f0ffd77a8 | -17.6083 | -57.4482 | 2024-11-09 14:10:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 135.6 |
| c5443fe8-5ff7-3d45-aee2-dfd90ae052c5 | -0.3034 | -51.7071 | 2024-11-09 14:10:00 | GOES-16 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 73.7 |
| f40d6181-6391-3ce4-b3b4-824e14030107 | -4.1244 | -43.6064 | 2024-11-09 14:10:00 | GOES-16 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 80.1 |
| 5b3cc02b-83ed-3da2-bc3c-4c71e5d6489d | -2.4104 | -48.5265 | 2024-11-09 14:10:00 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 85.5 |
| 9c143288-f0c0-3472-b69c-129960e012c6 | -3.9485 | -48.1508 | 2024-11-09 14:10:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 61.1 |
| a895f596-8b19-3ffa-ac0e-17147e099c5c | -4.5713 | -43.789 | 2024-11-09 14:10:00 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 89.0 |
| 5c0be066-a512-368a-b69d-1f3b92910a13 | -3.5355 | -49.2608 | 2024-11-09 14:10:00 | GOES-16 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 60.4 |
| 3e842bb7-91fb-3860-a12a-9be2b8bccadc | -3.032 | -50.3338 | 2024-11-09 14:10:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 67.8 |
| ec95db0a-ef5d-3d11-ae21-1e7155b91ee9 | -2.8921 | -48.2977 | 2024-11-09 14:10:00 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 68.3 |
| 5aeb7239-0eed-3e40-847d-3fff7d139285 | -11.0877 | -43.3456 | 2024-11-09 14:10:00 | GOES-16 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 191.7 |
| 87c92f3d-3ac4-3bf8-bcb2-0aa30102e61d | -2.2137 | -46.4187 | 2024-11-09 14:10:00 | GOES-16 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 71.2 |
| 99bc6b60-15bd-337d-9d56-f9dd4415c7d5 | -2.6758 | -46.7806 | 2024-11-09 14:10:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 176.5 |
| a2ab9069-89dd-3a7f-9593-469541703524 | -3.9624 | -49.0096 | 2024-11-09 14:10:00 | GOES-16 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 69.5 |
| 0fd1b664-2a00-3acd-b8a2-fe225b224bed | -2.2479 | -53.7627 | 2024-11-09 14:10:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 73.1 |
| 9f8435d1-695e-3f44-92b0-2c172192b7bf | -2.0293 | -46.0908 | 2024-11-09 14:10:00 | GOES-16 | JUNCO DO MARANHÃO | MARANHÃO | Brasil | 2105658 | 21 | 33 | nan | nan | nan | Amazônia | 80.0 |
| 5379fda7-c096-3bcf-bbf2-027541e0fa10 | -5.4359 | -43.2673 | 2024-11-09 14:20:00 | GOES-16 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 104.3 |
| bfb66224-f23c-3ba5-89c6-25046d39e583 | -2.2803 | -48.744 | 2024-11-09 14:20:00 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 101.3 |
| a071c82d-0ccf-311a-832a-54b8d146e72c | -0.5992 | -49.5352 | 2024-11-09 14:20:00 | GOES-16 | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 78.8 |
| 82e7d5e3-30e9-3cce-87f3-7d2985c32346 | -1.4144 | -47.6187 | 2024-11-09 14:20:00 | GOES-16 | SANTA MARIA DO PARÁ | PARÁ | Brasil | 1506609 | 15 | 33 | nan | nan | nan | Amazônia | 129.9 |
| 7249ab96-1576-3831-9a71-8e5a1e96c70f | -2.2479 | -53.7627 | 2024-11-09 14:20:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 54.3 |
| 02f9d9bd-0380-3c99-b7ed-2f3d0b3c64a1 | -1.7182 | -52.3714 | 2024-11-09 14:20:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 67.0 |
| 4cbe7899-be12-346e-8f73-df6c39f1895b | -0.6177 | -49.5351 | 2024-11-09 14:20:00 | GOES-16 | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 93.2 |
| b02cc9f0-ea2a-3eea-b3c4-c805d677309f | -2.3733 | -48.5703 | 2024-11-09 14:20:00 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 104.4 |
| 34ca7f5f-2923-3f9d-9826-e5ab0059831a | -2.3555 | -54.7627 | 2024-11-09 14:20:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 72.8 |
| ce42868d-1b7e-36b7-a1d8-c3db237bbc0c | -7.1778 | -42.0055 | 2024-11-09 14:20:00 | GOES-16 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 64.9 |
| 0b8e2dd2-6b62-36eb-9715-cf1fba24b217 | -2.6758 | -46.7806 | 2024-11-09 14:20:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 152.7 |
| 709f6d0e-b645-3be3-8181-d27cd2996e2f | -2.2479 | -53.7829 | 2024-11-09 14:20:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 81.1 |
| b160cca0-b09d-3052-b37c-567836ae8ac9 | -2.5781 | -48.1777 | 2024-11-09 14:20:00 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 68.7 |
| 141be51e-46ba-3b78-89cb-5a73036998a3 | -0.6177 | -49.5562 | 2024-11-09 14:20:00 | GOES-16 | ANAJÁS | PARÁ | Brasil | 1500701 | 15 | 33 | nan | nan | nan | Amazônia | 63.6 |
| 699a8343-ae72-3607-af92-198953d89b12 | -3.9483 | -48.1724 | 2024-11-09 14:20:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 89.2 |
| 546f513f-c2e8-32a2-9295-6a54baf33cb1 | -1.4806 | -51.5737 | 2024-11-09 14:20:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 183.2 |
| b53d57e1-ead6-3456-ae9e-3d8d73e0ec1e | -2.3556 | -54.7427 | 2024-11-09 14:20:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 57.7 |
| 8922b7a7-8e3a-35c0-a4a7-a214be4e0a65 | -0.2115 | -51.6455 | 2024-11-09 14:20:00 | GOES-16 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 70.0 |
| b7105be3-b6a1-391d-80a3-d0fa16a9ac4c | -6.1366 | -42.5544 | 2024-11-09 14:20:00 | GOES-16 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 70.1 |
| 0afe6535-bef3-3bb6-9374-5e0f7960af4d | -1.5164 | -52.1491 | 2024-11-09 14:20:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 106.9 |
| 0215094c-2f58-332c-bf0d-9bc287b11108 | -6.9974 | -41.3016 | 2024-11-09 14:20:00 | GOES-16 | SANTO ANTÔNIO DE LISBOA | PIAUÍ | Brasil | 2209401 | 22 | 33 | nan | nan | nan | Caatinga | 76.3 |
| e87ad09e-ce6e-31a6-b6a7-ed4aea53f59f | -2.379 | -46.8552 | 2024-11-09 14:20:00 | GOES-16 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 160.0 |
| 5cc145d4-fafb-30dc-97db-5bd6838ea569 | -3.2538 | -50.2639 | 2024-11-09 14:20:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 80.7 |
| fc3815fb-4fbd-3c50-b7e8-e530fcb0832e | -3.5649 | -43.5654 | 2024-11-09 14:20:00 | GOES-16 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 75.4 |
| 1f870815-3afb-34e1-9188-d43226df56fe | -0.3769 | -51.892 | 2024-11-09 14:20:00 | GOES-16 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 100.4 |
| 79a472b3-08ae-378d-9840-6eb1ef8b8498 | -3.9624 | -49.0096 | 2024-11-09 14:20:00 | GOES-16 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 69.3 |
| 4b81f676-0d4e-3789-99d1-6a2cf7f0776d | -1.6707 | -48.7354 | 2024-11-09 14:20:00 | GOES-16 | ABAETETUBA | PARÁ | Brasil | 1500107 | 15 | 33 | nan | nan | nan | Amazônia | 97.6 |
| 82438ddc-8ec2-3706-b67d-21fd073ce983 | -5.7475 | -41.9927 | 2024-11-09 14:20:00 | GOES-16 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 101.7 |
| f2307779-f7b8-3fb6-885a-2532c4fefcae | -3.125 | -50.1419 | 2024-11-09 14:20:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 101.3 |
| 643f4a64-f1c4-3e35-a50c-bd6630e238d3 | -2.2315 | -46.6169 | 2024-11-09 14:20:00 | GOES-16 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 77.9 |
| 524e484b-2007-38d4-a84e-6e31a0f5cb3a | -2.2318 | -46.5508 | 2024-11-09 14:20:00 | GOES-16 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 78.2 |
| eb43e1e5-c009-34a6-874a-f40d60c26535 | -1.1306 | -51.9485 | 2024-11-09 14:20:00 | GOES-16 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 58.4 |
| a7babd97-9485-36b6-8aff-86c3cbcc3448 | -2.3605 | -46.8557 | 2024-11-09 14:20:00 | GOES-16 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 160.9 |
| 2422ef39-84cf-3af7-be68-5c49671a65cc | -3.9625 | -48.9883 | 2024-11-09 14:20:00 | GOES-16 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 76.7 |
| 5124e686-c1b3-3700-9458-2cd08b639019 | -2.2322 | -46.4182 | 2024-11-09 14:20:00 | GOES-16 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 93.1 |
| ec5415a2-46ea-33ad-94ec-3415ac0e8f8f | -3.5462 | -43.5663 | 2024-11-09 14:20:00 | GOES-16 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 130.4 |
| 6a4d3a9c-0612-3d25-81ca-1a9f7a80a078 | -7.1592 | -41.9834 | 2024-11-09 14:20:00 | GOES-16 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 58.5 |
| cc0ff631-0dad-3955-8701-3f993ffa0d3e | -0.3034 | -51.7277 | 2024-11-09 14:20:00 | GOES-16 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 69.7 |
| c160a511-f461-3260-a40b-7b2f455289e3 | -3.197 | -50.6219 | 2024-11-09 14:20:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 57.7 |
| 9f1071a0-3566-3960-a2f1-155c97ff0fd0 | -6.1363 | -42.578 | 2024-11-09 14:20:00 | GOES-16 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 66.4 |
| 66b8f380-d36e-3f73-a421-323f1f532bdc | -3.6111 | -48.9167 | 2024-11-09 14:20:00 | GOES-16 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 177.7 |
| 922c4027-ed2b-30c5-b765-e78d8f2b28aa | -2.8921 | -48.2977 | 2024-11-09 14:20:00 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 68.4 |
| 964a75e0-b3d3-3041-aecc-e51681f41e7a | -3.0319 | -50.3547 | 2024-11-09 14:20:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 144.6 |
| 9ebc1a97-50b6-3e68-88fc-2505670ab9d1 | -6.3717 | -45.3549 | 2024-11-09 14:20:00 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 53.3 |
| 1f13e75a-0e96-3f6e-b50c-e5383dbdceed | -2.646 | -49.8819 | 2024-11-09 14:20:00 | GOES-16 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 63.2 |
| e17f8161-5c01-39b6-874f-101d56e17db7 | -4.807 | -44.7606 | 2024-11-09 14:20:00 | GOES-16 | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 83.8 |
| 2848358c-91e5-39bb-9d85-0396b1061a56 | -4.1246 | -43.5833 | 2024-11-09 14:20:00 | GOES-16 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 91.5 |
| 8b9a6d5b-5eda-331a-93f3-3bc18fcc4d01 | -1.6892 | -48.735 | 2024-11-09 14:20:00 | GOES-16 | ABAETETUBA | PARÁ | Brasil | 1500107 | 15 | 33 | nan | nan | nan | Amazônia | 103.6 |
| fd1efe76-51c8-31fe-9df7-62d5c21cc3c6 | -1.5347 | -52.1694 | 2024-11-09 14:20:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 78.1 |
| d2d8fc37-6d8d-3ed0-9574-6f5079b63c02 | -3.2346 | -50.4533 | 2024-11-09 14:20:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 65.5 |
| 2057e36e-dab3-3911-b0b6-bc853eb04217 | -2.2804 | -48.7226 | 2024-11-09 14:20:00 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 110.1 |
| 4f2adbc9-ac04-3d93-b9f2-4f36f84254eb | -2.0841 | -46.3556 | 2024-11-09 14:20:00 | GOES-16 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 68.7 |
| 9ed2c52a-abdc-3d21-98bf-36e8f9212b9b | -6.3689 | -45.6483 | 2024-11-09 14:20:00 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 62.9 |
| 008240ef-5a27-389d-854e-5473292566a5 | -3.9485 | -48.1508 | 2024-11-09 14:20:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 63.3 |
| 24b33087-48c6-390e-8284-f69fcdd505ab | -2.455 | -46.3235 | 2024-11-09 14:20:00 | GOES-16 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 287.9 |
| f86783bd-6822-3be7-92fc-54cfd7cceb9d | -1.3959 | -47.619 | 2024-11-09 14:20:00 | GOES-16 | SANTA MARIA DO PARÁ | PARÁ | Brasil | 1506609 | 15 | 33 | nan | nan | nan | Amazônia | 93.4 |
| 0ac02971-cce3-377d-8905-e56873a87911 | -2.2642 | -47.9916 | 2024-11-09 14:20:00 | GOES-16 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 97.8 |
| f01d2e4a-da2d-3c23-86b4-3e83af8502d8 | -3.967 | -48.15 | 2024-11-09 14:20:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 60.5 |
| 3164f44e-c9f7-39d5-8028-15865ed65a7c | -2.9541 | -46.7495 | 2024-11-09 14:20:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 74.8 |
| 0210273a-c5d5-3869-bf2f-4339441bc98e | -4.5713 | -43.789 | 2024-11-09 14:20:00 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 83.6 |
| 52237dff-858e-3afe-9645-37a141268e07 | -5.4734 | -43.2646 | 2024-11-09 14:20:00 | GOES-16 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 93.9 |
| 664cd6ef-c370-35b1-87eb-4a25300e8cf5 | -3.3694 | -45.2865 | 2024-11-09 14:20:00 | GOES-16 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 97.7 |
| b06d6032-ee21-3398-9747-26e2d13cf14a | -2.4104 | -48.5265 | 2024-11-09 14:20:00 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 82.6 |
| 988a565d-c712-3c54-82cb-984c42f3e644 | -7.1781 | -41.9815 | 2024-11-09 14:20:00 | GOES-16 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 58.8 |
| 59ce0326-4b7c-338b-b27f-b1e9712cfc4f | -4.1565 | -44.4099 | 2024-11-09 14:20:00 | GOES-16 | ALTO ALEGRE DO MARANHÃO | MARANHÃO | Brasil | 2100436 | 21 | 33 | nan | nan | nan | Cerrado | 85.0 |
| 6347da69-0777-33eb-88ad-6794e8aa609c | -2.4551 | -46.3014 | 2024-11-09 14:20:00 | GOES-16 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 87.6 |
| 94305bd0-a08c-38fb-8a62-e1e8e9d28b54 | -0.2299 | -51.6249 | 2024-11-09 14:20:00 | GOES-16 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 74.6 |
| cd18bcee-1cf8-3441-96cd-8fef7591d3b6 | -3.032 | -50.3338 | 2024-11-09 14:20:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 60.4 |
| 2b082063-e6df-3511-994c-8933bd0bf258 | -0.3769 | -51.8715 | 2024-11-09 14:20:00 | GOES-16 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 94.4 |
| a9239706-8a99-3d32-b34a-08df4e6ad026 | -0.2299 | -51.6455 | 2024-11-09 14:20:00 | GOES-16 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 134.5 |
| 7ad22ce2-f96f-3d96-82f0-e32a86044692 | -5.2483 | -48.0857 | 2024-11-09 14:20:00 | GOES-16 | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 67.4 |
| f184b245-9385-3831-9b6d-e0a3e6e6b96e | -5.7336 | -43.5014 | 2024-11-09 14:20:00 | GOES-16 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 70.7 |
| a38fe652-bffc-39c2-8d05-68df80325069 | -3.0292 | -42.5385 | 2024-11-09 14:20:00 | GOES-16 | TUTÓIA | MARANHÃO | Brasil | 2112506 | 21 | 33 | nan | nan | nan | Cerrado | 133.9 |
| abf154ea-5376-3fee-a850-549c36b67c71 | -1.6892 | -48.735 | 2024-11-09 14:30:00 | GOES-16 | ABAETETUBA | PARÁ | Brasil | 1500107 | 15 | 33 | nan | nan | nan | Amazônia | 87.4 |
| b5a61ec0-9f27-3d2d-a057-b9240531233c | -2.6694 | -48.498 | 2024-11-09 14:30:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 79.8 |
| cb9debe8-78c2-32a7-bfe1-c2609b1be8ec | -5.4544 | -43.2893 | 2024-11-09 14:30:00 | GOES-16 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 103.5 |
| 41174b6f-e3bc-3f89-a9bc-9e8029f5d67f | -3.967 | -48.15 | 2024-11-09 14:30:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 58.6 |
| bca329c5-aa6a-3d1d-81e9-db052c357f11 | -2.2318 | -46.5508 | 2024-11-09 14:30:00 | GOES-16 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 72.7 |
| 65e47862-8118-3c54-b7a9-9f68c21fb628 | -5.7146 | -43.5261 | 2024-11-09 14:30:00 | GOES-16 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 75.3 |
| e39e75d7-bffc-3cad-a64c-280135ca20f6 | -2.4104 | -48.5265 | 2024-11-09 14:30:00 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 86.2 |


[Clique aqui para ver as próximas entradas](README124.md)
