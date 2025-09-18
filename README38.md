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
| a710aaf1-13d5-394b-8d4e-15eca81f205a | -6.9212 | -44.764 | 2025-09-18 14:10:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 105.2 |
| afaab452-7eb6-3850-bdf5-11189c0a9056 | -11.4482 | -43.5277 | 2025-09-18 14:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 97.3 |
| 5417de59-6e67-39af-9b2b-d3c74fe84e68 | -5.786 | -43.9147 | 2025-09-18 14:10:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 69.2 |
| 4e984a16-df85-3956-ba92-0742d1e8d3e6 | -15.8236 | -59.3816 | 2025-09-18 14:10:00 | GOES-19 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 64.3 |
| d8f55ee6-dba9-379a-ab57-0226ad16ef08 | -8.7866 | -46.0804 | 2025-09-18 14:10:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 147.0 |
| 72971551-d0b3-3085-b3ec-ce460749e75e | -8.3334 | -44.6507 | 2025-09-18 14:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 96.2 |
| 49178db4-383f-3c36-88b4-e4f71182821a | -7.5164 | -45.2796 | 2025-09-18 14:10:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 68.3 |
| ed0fdfa2-98a4-3416-8a9f-765c33d83dda | -11.1873 | -45.3347 | 2025-09-18 14:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 99.2 |
| 94b483d6-946c-3f0b-998e-df24298785ce | -9.2084 | -46.9974 | 2025-09-18 14:10:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 105.2 |
| 0dd7a5d6-b8d5-3e35-b198-da5e5f215a90 | -6.0786 | -44.6733 | 2025-09-18 14:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 76.6 |
| 3f6e9379-1ff7-31a9-802e-cae4484dd45a | -7.3551 | -44.5875 | 2025-09-18 14:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 56.7 |
| 5ba4b44e-2327-3963-b18e-db92a61257e7 | -8.3332 | -44.6737 | 2025-09-18 14:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 64.2 |
| 99968cf7-8153-3bb0-ae4a-36c09150b841 | -19.5872 | -57.7557 | 2025-09-18 14:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 150.3 |
| 4962de74-b9ad-3924-8566-aed999778320 | -6.0599 | -44.6747 | 2025-09-18 14:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 80.9 |
| 8c230adf-3461-3861-ae53-1f6c12432a6c | -8.8801 | -46.138 | 2025-09-18 14:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 104.0 |
| 36673b38-2b99-33ba-a9e1-864bb26101c3 | -7.5601 | -44.7514 | 2025-09-18 14:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 97.9 |
| 235d3f19-0be8-3114-b565-ac835ccf42d2 | -6.2055 | -45.1187 | 2025-09-18 14:10:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 66.3 |
| 25c43bee-05f2-36db-9c3f-93cb30a5a7dd | -8.0196 | -45.662 | 2025-09-18 14:10:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 76.4 |
| 4a98c245-6486-3263-a941-e4abfcbce1af | -6.0597 | -44.6976 | 2025-09-18 14:10:00 | GOES-19 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 62.9 |
| ef7a4375-c18c-306d-86b0-77c3b765f5bd | -5.7862 | -43.8915 | 2025-09-18 14:10:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 69.3 |
| c0d4ac91-bc20-3539-a0e1-4ce68d1e480f | -8.899 | -46.136 | 2025-09-18 14:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 108.3 |
| 56a6f601-ba60-35b3-83e8-768722adee5e | -3.2692 | -43.0441 | 2025-09-18 14:10:00 | GOES-19 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 88.0 |
| d8b4bc3e-0d0b-36f4-a54e-8cb53d88d3a5 | -15.8813 | -59.4161 | 2025-09-18 14:10:00 | GOES-19 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 77.6 |
| b45ef6a0-e2a5-3474-b577-21924291bf32 | -7.8509 | -45.6105 | 2025-09-18 14:10:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 87.2 |
| ad5a05cc-0099-36b0-b0b2-ab8ebe88fee5 | -9.0478 | -44.8936 | 2025-09-18 14:10:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 116.3 |
| bbe44b2e-ae3f-3ae8-9d0b-75144df9b650 | -8.7262 | -46.3784 | 2025-09-18 14:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 165.4 |
| 79ac33c2-6339-3397-bf5e-eefbb6a67683 | -6.5772 | -45.4064 | 2025-09-18 14:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 67.9 |
| cd7bbea0-8ef0-30aa-884e-2749f7289862 | -8.9911 | -46.3059 | 2025-09-18 14:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 114.2 |
| bb822437-3d53-3907-b809-0a2d28070e30 | -6.921 | -44.7869 | 2025-09-18 14:10:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 59.2 |
| 7faee4b6-8092-32a9-b62e-fab51ba1676a | -8.4137 | -45.7583 | 2025-09-18 14:10:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 65.7 |
| e5acf3b5-b3c9-3038-be5c-c6913b8d9e5b | -6.1878 | -41.2097 | 2025-09-18 14:10:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 113.4 |
| 66202a90-b2b1-3d4f-ba1c-3d8c35348229 | -11.4477 | -43.5514 | 2025-09-18 14:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 141.3 |
| 97d6b13d-116b-399b-9f87-a5a5519d0a34 | -6.0071 | -44.3124 | 2025-09-18 14:10:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 92.4 |
| 8444b335-e126-3594-89ea-671ae5485720 | -8.7868 | -46.0578 | 2025-09-18 14:10:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 89.2 |
| 5d6f173a-3ce4-390b-bdd6-0cf44c3c63ba | -6.9978 | -44.62 | 2025-09-18 14:10:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 275.6 |
| baa45f5e-c81d-392b-9599-f79c89b9f1d2 | -6.9981 | -44.5971 | 2025-09-18 14:10:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 69.6 |
| c989e1bf-340e-3f9c-9c39-4a71a9b49819 | -6.1688 | -41.2357 | 2025-09-18 14:10:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 115.5 |
| 28dbf0e9-b93f-3b8c-9a9c-fb2857ab0a2d | -9.8776 | -46.4317 | 2025-09-18 14:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 71.8 |
| fee88007-3a24-3bd8-86cc-453c4012f7a3 | -6.9981 | -44.5971 | 2025-09-18 14:20:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 70.0 |
| 05851915-249a-3d2e-9ba1-6b324f4209d4 | -5.786 | -43.9147 | 2025-09-18 14:20:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 70.1 |
| be4e3e34-3054-3852-89ee-6d7cef97310f | -10.6334 | -44.2324 | 2025-09-18 14:20:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 132.4 |
| 2f6b6a3d-ed7f-30a8-b2be-a1289dcddd2b | -9.1895 | -46.9994 | 2025-09-18 14:20:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 87.2 |
| 3014e089-1f86-3f62-9716-0faf50de02d3 | -19.5865 | -57.7973 | 2025-09-18 14:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 104.9 |
| ff2e22ff-7888-3886-b8dc-81ffb264b87b | -11.3342 | -43.4742 | 2025-09-18 14:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 113.1 |
| 7583ee55-4cc1-36e7-bb8a-0ffc0c139897 | -11.4477 | -43.5514 | 2025-09-18 14:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 145.2 |
| b5e20e68-2bca-3539-b1b7-907d1f676554 | -8.9449 | -45.521 | 2025-09-18 14:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 75.9 |
| 13dc8aff-a2a3-3890-8cfc-269d02911e55 | -9.2084 | -46.9974 | 2025-09-18 14:20:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 115.8 |
| b6542351-93a0-3dad-8169-0f562428f734 | -6.2133 | -44.2962 | 2025-09-18 14:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 61.2 |
| 38ca2e1f-443e-38aa-ae14-b26a2ee7ae85 | -8.8801 | -46.138 | 2025-09-18 14:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 93.1 |
| b74ac6cd-9b52-3f57-a7db-97a93bfbc830 | -8.8054 | -46.0784 | 2025-09-18 14:20:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 94.4 |
| 94885c43-a52e-3db2-bae4-234d7e6a98f9 | -6.9022 | -44.7885 | 2025-09-18 14:20:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 58.2 |
| b14ec0bd-1138-35ba-bfbb-fc93bce4c7c3 | -3.8658 | -43.1787 | 2025-09-18 14:20:00 | GOES-19 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 140.3 |
| 660f75e0-197d-317b-8724-fc8bbe960985 | -19.5869 | -57.7765 | 2025-09-18 14:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 143.0 |
| 3297d1e3-2f3d-36d1-bac0-06a502b720a9 | -7.4503 | -46.1647 | 2025-09-18 14:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 44.1 |
| 74aac3ec-7a16-3c12-81db-823fe7b1c872 | -6.5772 | -45.4064 | 2025-09-18 14:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 72.4 |
| eaeff12d-f6d7-3fb7-a236-6d60f7cf53c9 | -8.3334 | -44.6507 | 2025-09-18 14:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 111.0 |
| 8f9382ff-0d72-3432-8363-590b108a3bca | -6.0599 | -44.6747 | 2025-09-18 14:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 71.8 |
| 6f69179a-8915-37e1-a0e3-159736d41258 | -8.5609 | -47.5712 | 2025-09-18 14:20:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 58.7 |
| f51d4a8a-80dd-38f3-84a3-018c785c3542 | -7.5412 | -44.7532 | 2025-09-18 14:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 78.5 |
| 013df215-9515-3647-aa56-181b72f10629 | -19.5872 | -57.7557 | 2025-09-18 14:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 173.3 |
| 2a86b9aa-5936-39ee-a31b-a0822d050dd1 | -10.8609 | -45.4707 | 2025-09-18 14:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 111.7 |
| 49547832-b702-3164-9806-796e40a75ed4 | -3.2692 | -43.0441 | 2025-09-18 14:20:00 | GOES-19 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 92.8 |
| 73fda08e-eeee-3025-800c-df645c75d274 | -8.4645 | -44.7286 | 2025-09-18 14:20:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 51.6 |
| 5ca21bbb-1286-38b1-80e7-52677f0ddb02 | -6.1878 | -41.2097 | 2025-09-18 14:20:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 124.9 |
| 1d3a7d25-1224-3497-922b-df877dcc1b7a | -8.7866 | -46.0804 | 2025-09-18 14:20:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 78.1 |
| ce7a37de-950c-38c4-8c5a-774784224589 | -7.8512 | -45.5879 | 2025-09-18 14:20:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 75.5 |
| ad5b96b7-ad72-3090-8d4e-5b7bcf297cf4 | -8.0092 | -44.9589 | 2025-09-18 14:20:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 64.2 |
| 10529099-9958-3338-ad22-3af4bc4d649f | -8.352 | -44.6717 | 2025-09-18 14:20:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 254.2 |
| 46e49ed8-c48b-3296-b71f-8b299b786c73 | -8.0196 | -45.662 | 2025-09-18 14:20:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 75.7 |
| 5d7e810d-9bae-3332-b2f1-44d83a276086 | -6.9212 | -44.764 | 2025-09-18 14:20:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 88.7 |
| e7fb99f5-de28-34ab-849c-44aa540b9f7d | -5.7875 | -43.7526 | 2025-09-18 14:20:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 75.3 |
| 37c47f1f-86cd-3cea-93b5-1172ceffad54 | -7.5164 | -45.2796 | 2025-09-18 14:20:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 62.2 |
| 6c6b9f0b-123d-338c-a78f-da27a5099331 | -6.1196 | -46.3385 | 2025-09-18 14:20:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 61.8 |
| f540f55c-fc7c-3dc5-a1b0-c5658c5be891 | -7.8698 | -45.6087 | 2025-09-18 14:20:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 101.7 |
| d4a07a7c-0b67-3cb6-80fb-4d675b006782 | -3.8756 | -41.6188 | 2025-09-18 14:20:00 | GOES-19 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 89.1 |
| 0966a187-b76a-3d57-a1d4-42a14178c48e | -6.0786 | -44.6733 | 2025-09-18 14:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 75.6 |
| 429f9fda-f7b7-370a-82c6-03eba9d92f27 | -5.8397 | -44.1872 | 2025-09-18 14:20:00 | GOES-19 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 59.3 |
| 757e3360-aea0-3797-b060-69aeca2154fa | -7.8509 | -45.6105 | 2025-09-18 14:20:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 68.7 |
| ef68d554-3213-3a12-83b9-1f6e14832368 | -8.3332 | -44.6737 | 2025-09-18 14:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 65.9 |
| 94fba929-1103-3b54-9a97-099d7ee8fa8b | -6.9978 | -44.62 | 2025-09-18 14:20:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 165.0 |
| a520cfa8-12d1-3067-bc4d-6a714cedb54e | -15.843 | -59.3798 | 2025-09-18 14:20:00 | GOES-19 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 64.1 |
| 2b902d81-6710-3a74-baa8-58540f41c2f2 | -8.9728 | -46.263 | 2025-09-18 14:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 77.4 |
| b36d4a37-2c93-3b21-a8a4-a1ed33437542 | -8.9722 | -46.3079 | 2025-09-18 14:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 77.6 |
| a494e254-2c20-3fa0-a2f4-b6c94ec82651 | -7.6386 | -44.4686 | 2025-09-18 14:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 78.5 |
| eb94cfb2-527f-3b45-b8a7-dbd5648564dc | -15.8236 | -59.3816 | 2025-09-18 14:20:00 | GOES-19 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 103.7 |
| 260f7f8d-f5af-3c35-8931-4ecb1198bf95 | -8.899 | -46.136 | 2025-09-18 14:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 95.1 |
| d176b14b-42c3-3ccc-8ae3-dd7153107834 | -6.9024 | -44.7656 | 2025-09-18 14:20:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 112.6 |
| c34ebd71-3581-3217-baf6-6f0b57c8707f | -3.8659 | -43.1554 | 2025-09-18 14:20:00 | GOES-19 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 184.6 |
| afec5e46-9f9e-32ca-8184-dfe6e04a430d | -5.806 | -45.8918 | 2025-09-18 14:20:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 64.2 |
| abeed8cc-3fdd-39c4-ab81-e9602ae1dfd6 | -8.0281 | -44.957 | 2025-09-18 14:20:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 141.1 |
| e53a9d59-a80e-3324-9ac6-da803d5dec85 | -5.8058 | -45.9142 | 2025-09-18 14:20:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 83.5 |
| 2663174f-886f-3fe0-a100-da89373ba50a | -7.0255 | -45.5498 | 2025-09-18 14:20:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 60.3 |
| d48ddb07-032a-355b-abe1-fb405b5b2bcd | -8.3523 | -44.6487 | 2025-09-18 14:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 256.2 |
| 7f641def-6b40-382f-b856-af06a9d8d179 | -5.7862 | -43.8915 | 2025-09-18 14:20:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 72.1 |
| b8da29c7-aee8-3219-91a9-dbe69299024f | -8.935 | -46.267 | 2025-09-18 14:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 114.8 |
| b18b1c5c-3607-3029-bade-36728147f00b | -8.4137 | -45.7583 | 2025-09-18 14:20:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 54.0 |
| 3204ea2a-1abe-3661-b766-a0e840f98040 | -10.6525 | -44.2298 | 2025-09-18 14:20:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 205.0 |
| f58a6673-9cd2-30e5-861f-8e3838086a8f | -11.467 | -43.5485 | 2025-09-18 14:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 110.0 |
| 913cd334-cda3-3c91-86ea-7b9b3f23cdea | -3.8754 | -41.6427 | 2025-09-18 14:20:00 | GOES-19 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 78.6 |
| 800bd01a-aa6d-37f6-93f3-e087e2cadf1f | -3.1562 | -43.2587 | 2025-09-18 14:20:00 | GOES-19 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 88.0 |


[Clique aqui para ver as próximas entradas](README39.md)
