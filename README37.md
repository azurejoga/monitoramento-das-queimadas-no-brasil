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

## Dados Diários - Página 37

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e56a6652-c4ed-3f86-80ce-4ddafefd385c | -6.9963 | -44.7574 | 2025-09-18 13:50:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 83.2 |
| 7d15412c-0d52-3144-880e-e69b2c9d5b22 | -6.0599 | -44.6747 | 2025-09-18 13:50:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 79.3 |
| ded42462-7c27-3089-a30a-10c4d87e39ec | -7.5412 | -44.7532 | 2025-09-18 13:50:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 96.0 |
| 43d6aac6-2695-3d88-9193-90f31600732d | -11.1677 | -45.3603 | 2025-09-18 13:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 80.1 |
| c0f4e568-9339-33ae-b651-9ce11411b530 | -9.8776 | -46.4317 | 2025-09-18 13:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 70.3 |
| c124884a-f88b-3f40-a0ed-75c03e8e5605 | -7.5598 | -44.7743 | 2025-09-18 14:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 160.7 |
| 553c07ef-30ff-3e11-af91-15015d253451 | -7.5601 | -44.7514 | 2025-09-18 14:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 153.7 |
| 5e15ae97-3af1-3d85-b86d-5d0e03baec52 | -8.7073 | -46.3804 | 2025-09-18 14:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 138.8 |
| 1e1cc0c9-8a36-30f0-be12-fa3eca17c255 | -8.0196 | -45.662 | 2025-09-18 14:00:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 79.6 |
| 860f2f39-c17b-3afe-b54a-235bf0cdd7f7 | -6.9024 | -44.7656 | 2025-09-18 14:00:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 68.8 |
| efbd04b3-9ecb-3eab-a3f1-0fb64a2a00b2 | -8.9722 | -46.3079 | 2025-09-18 14:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 73.8 |
| 75241d42-1da2-3afb-b565-328368a1248f | -19.5869 | -57.7765 | 2025-09-18 14:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 139.7 |
| ac75fb9f-86a0-3ef6-9b44-eae73ddd0931 | -11.5041 | -43.6136 | 2025-09-18 14:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 132.3 |
| caea992a-01ab-3832-ac2a-1a5429e65a6a | -11.4477 | -43.5514 | 2025-09-18 14:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 130.5 |
| 07965a63-e4b7-3b73-b7d2-cd8e8f2115b9 | -7.5162 | -45.3024 | 2025-09-18 14:00:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 97.0 |
| 8e955490-39a1-3bb0-8ee0-cc38f96c6be1 | -8.6268 | -45.3054 | 2025-09-18 14:00:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 105.6 |
| aa67026e-a20b-3138-bcca-f9387b545815 | -15.8034 | -59.4435 | 2025-09-18 14:00:00 | GOES-19 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 72.8 |
| d11e6887-8936-37d6-bc81-68d6436b2ead | -6.1876 | -41.234 | 2025-09-18 14:00:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 111.4 |
| 48160f8f-49d8-35a8-adc9-8058b896356d | -9.2084 | -46.9974 | 2025-09-18 14:00:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 93.5 |
| 082bbbb5-7562-355f-86d4-154e80452f3f | -10.0371 | -47.1952 | 2025-09-18 14:00:00 | GOES-19 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 98.1 |
| 37fe02cf-660d-3e09-bfd0-27a87b6c0029 | -8.3334 | -44.6507 | 2025-09-18 14:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 78.1 |
| 8492bc15-1196-38ae-b28c-c23e70f32440 | -8.0199 | -45.6394 | 2025-09-18 14:00:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 73.1 |
| 66c27c77-8525-37db-9f0c-2cfad8dc622d | -19.5865 | -57.7973 | 2025-09-18 14:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 86.5 |
| ed053170-379f-3333-921c-471fc2a41158 | -8.9449 | -45.521 | 2025-09-18 14:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 100.9 |
| a69c5aee-130b-304c-b136-b0788d6145bf | -11.1681 | -45.3373 | 2025-09-18 14:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 87.9 |
| 0d7b16df-3339-363d-ac5b-120a65e333ff | -8.352 | -44.6717 | 2025-09-18 14:00:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 114.2 |
| d4d242ce-fcc7-31b7-b8b6-8f07d2c2c53b | -7.5412 | -44.7532 | 2025-09-18 14:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 95.7 |
| 8f28e9c8-df55-3699-8ba1-c5badef266a0 | -8.8801 | -46.138 | 2025-09-18 14:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 65.9 |
| ef8e7a0e-5b62-33aa-a15c-a4b4126f8d5f | -15.8233 | -59.4016 | 2025-09-18 14:00:00 | GOES-19 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 69.6 |
| 9263358c-56cf-3b94-8205-d536d65de5e6 | -8.9536 | -46.2874 | 2025-09-18 14:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 76.4 |
| a6432e48-72da-30b1-a5ca-f491748b005b | -6.0071 | -44.3124 | 2025-09-18 14:00:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 101.9 |
| f93de27d-8429-339b-be1a-88e4b7a53634 | -6.0599 | -44.6747 | 2025-09-18 14:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 84.6 |
| 50add90f-b854-31ea-a351-d540ee1aeea2 | -8.0092 | -44.9589 | 2025-09-18 14:00:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 70.2 |
| 5a1b5c6e-0be3-385e-b03b-cb80bcc131e2 | -7.5789 | -44.7496 | 2025-09-18 14:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 50.4 |
| bb7ab76b-1a78-3b09-a519-a366a42b8963 | -3.8659 | -43.1554 | 2025-09-18 14:00:00 | GOES-19 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 113.1 |
| d19030b5-a501-3e1e-a8ba-02a67357aefc | -6.9978 | -44.62 | 2025-09-18 14:00:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 162.2 |
| 1035e27c-6774-3bdd-9748-895a502873f6 | -3.2692 | -43.0441 | 2025-09-18 14:00:00 | GOES-19 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 90.6 |
| 28de0c4a-e991-3152-9c1a-987f4edcd255 | -8.669 | -46.4291 | 2025-09-18 14:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 98.2 |
| a87569ca-3e47-3b66-81ab-a646b9f8dd4f | -3.8658 | -43.1787 | 2025-09-18 14:00:00 | GOES-19 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 88.0 |
| f6234175-fcc7-330b-8abb-4a64764754fe | -11.1869 | -45.3577 | 2025-09-18 14:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 103.7 |
| 30cb843f-d0ec-3a25-a478-e1d7f133c821 | -19.5872 | -57.7557 | 2025-09-18 14:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 155.4 |
| d41f31a6-fd92-377c-8a6e-bd7109bccb29 | -7.6386 | -44.4686 | 2025-09-18 14:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 84.4 |
| 31301d2e-2b05-3c47-95ad-f06cfa7701cd | -7.5164 | -45.2796 | 2025-09-18 14:00:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 62.6 |
| 72549d7a-130c-30b3-84cd-192c9dcf6c85 | -9.0671 | -44.8685 | 2025-09-18 14:00:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 102.0 |
| c4cbc9fd-9a02-3077-9522-a140d0c6206c | -6.9212 | -44.764 | 2025-09-18 14:00:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 85.0 |
| a3ef2d46-e7d5-3d70-b7c9-fa0465707779 | -11.1677 | -45.3603 | 2025-09-18 14:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 108.4 |
| 44de36f9-6ffc-32bc-9ce1-5accd8233901 | -8.7076 | -46.3579 | 2025-09-18 14:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 88.9 |
| 9f9cb58f-ede2-37c3-99cd-2b32dd8b9a5e | -6.0597 | -44.6976 | 2025-09-18 14:00:00 | GOES-19 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 65.0 |
| f5eaa268-9fd5-3c7d-9a49-3a9ab4e6c9d4 | -8.9911 | -46.3059 | 2025-09-18 14:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 154.9 |
| 5233f036-a8f1-3e6f-aa72-33acefc0dee1 | -6.0786 | -44.6733 | 2025-09-18 14:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 81.4 |
| af7357ba-5a82-3df8-9c07-b306af9e61f5 | -8.9985 | -45.7418 | 2025-09-18 14:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 147.0 |
| 624bd44e-1057-3a41-a3e0-0e5f7cd33638 | -6.9981 | -44.5971 | 2025-09-18 14:00:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 68.3 |
| 47595af8-29fa-381c-86b8-a679354c3340 | -5.786 | -43.9147 | 2025-09-18 14:00:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 65.3 |
| 68441814-5550-3099-abd1-c58d27eededd | -8.6885 | -46.3823 | 2025-09-18 14:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 86.7 |
| fcbc50f5-3fb1-3f70-89ed-5c2f9645034f | -8.9638 | -45.519 | 2025-09-18 14:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 85.6 |
| 0a070504-1312-32c6-9125-16019dbe6c5e | -8.899 | -46.136 | 2025-09-18 14:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 81.2 |
| 2a483f7a-e56c-37de-9d64-b0238d4f1e64 | -6.0069 | -44.3354 | 2025-09-18 14:00:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 152.6 |
| 6b4587cb-e2b3-318a-bf17-e39b67d39857 | -7.5818 | -44.4971 | 2025-09-18 14:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 73.8 |
| 22e9cb08-9a38-3644-90ac-c85e5f447e63 | -8.3523 | -44.6487 | 2025-09-18 14:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 155.9 |
| d26c6ede-4e0d-3afd-9231-c95aee77aa63 | -8.935 | -46.267 | 2025-09-18 14:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 62.3 |
| c8853f84-b434-3c4f-97d1-4ece39d0b260 | -3.1562 | -43.2587 | 2025-09-18 14:00:00 | GOES-19 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 77.8 |
| 05038f83-db00-3002-b9ac-cb93ebd6b44f | -15.8236 | -59.3816 | 2025-09-18 14:00:00 | GOES-19 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 97.1 |
| 2349f9b4-fc8b-37d9-9ad8-0917dc6824a9 | -8.7262 | -46.3784 | 2025-09-18 14:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 119.6 |
| f2b29ebd-d57b-3721-ace0-be13ed132e0c | -7.8698 | -45.6087 | 2025-09-18 14:00:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 67.5 |
| cd1dd922-95ed-3801-a759-540017bcd612 | -8.6027 | -45.7162 | 2025-09-18 14:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 52.8 |
| 1e6206c2-602c-3715-bf72-2422a68a2cd0 | -17.1777 | -45.9131 | 2025-09-18 14:00:00 | GOES-19 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 98.6 |
| c4270741-e75e-386b-9be9-8568b9bf5f79 | -8.9722 | -46.3079 | 2025-09-18 14:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 69.0 |
| 38e01b96-048c-3e49-8a40-9df2897f292e | -9.7241 | -46.5839 | 2025-09-18 14:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 94.8 |
| 26089787-a7eb-3771-a1a0-66a46aa41347 | -7.5162 | -45.3024 | 2025-09-18 14:10:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 104.2 |
| 942c3d6e-867f-3d86-a64a-d11879d9f1a4 | -6.6321 | -45.5374 | 2025-09-18 14:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 63.7 |
| 49a76411-8b84-3308-8a8a-4a8a23876f40 | -15.881 | -59.4362 | 2025-09-18 14:10:00 | GOES-19 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 61.3 |
| 87a00cee-6cbb-3e58-bc9f-2b6796d15aad | -7.8512 | -45.5879 | 2025-09-18 14:10:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 62.2 |
| 473c9227-dbad-3f2b-8f1c-f0287d215026 | -7.5412 | -44.7532 | 2025-09-18 14:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 90.2 |
| 6592b589-575e-3f63-b7f5-a39c937fd7e2 | -8.7076 | -46.3579 | 2025-09-18 14:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 103.1 |
| c93d772f-e2a5-3da9-a99d-0714986cfffa | -8.7073 | -46.3804 | 2025-09-18 14:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 134.5 |
| 02294e3b-9542-3392-baab-118153847823 | -8.4645 | -44.7286 | 2025-09-18 14:10:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 56.1 |
| cf030caa-16d6-3f29-99d4-99c72d4f8386 | -9.7129 | -47.3867 | 2025-09-18 14:10:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 68.7 |
| b798a465-13ae-34a8-a4af-567aab9300ef | -8.6268 | -45.3054 | 2025-09-18 14:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 75.5 |
| 241b00a2-be62-32f3-9fa3-f0eccd4446dc | -3.8756 | -41.6188 | 2025-09-18 14:10:00 | GOES-19 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 84.0 |
| 82df8a82-04c3-3d47-a2ca-7453feaa6806 | -11.1677 | -45.3603 | 2025-09-18 14:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 97.8 |
| 28550c40-4b73-310d-aa1f-f4a41f4abf53 | -6.9024 | -44.7656 | 2025-09-18 14:10:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 74.3 |
| fe0d38c2-bcf5-3099-9474-facd65217593 | -8.7863 | -46.1029 | 2025-09-18 14:10:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 70.4 |
| de602cfb-5274-33d5-ba9e-302cb35217d0 | -7.3967 | -44.2386 | 2025-09-18 14:10:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 72.1 |
| 3163f658-f44e-36ba-821e-5a38d270a068 | -17.1777 | -45.9131 | 2025-09-18 14:10:00 | GOES-19 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 97.6 |
| b41d497c-9224-319f-bb3f-6bfe67130cda | -19.5869 | -57.7765 | 2025-09-18 14:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 150.8 |
| 374e355f-bcef-36fb-8430-930edf36502a | -8.3523 | -44.6487 | 2025-09-18 14:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 253.1 |
| f36c827b-797a-3124-ba67-ac8cd03e17d5 | -11.1869 | -45.3577 | 2025-09-18 14:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 118.0 |
| cb1dda86-933f-3ccd-8dfa-648c52653a17 | -3.8659 | -43.1554 | 2025-09-18 14:10:00 | GOES-19 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 130.8 |
| e6a1e7bd-f20b-3822-8543-6dffa8dc2675 | -6.1876 | -41.234 | 2025-09-18 14:10:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 166.4 |
| 8cb0bdec-02a6-3841-961d-a4c9548e5160 | -7.5786 | -44.7725 | 2025-09-18 14:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 57.4 |
| 6c28ded6-aa9c-33d5-aeff-67a7f2ce99d0 | -8.8054 | -46.0784 | 2025-09-18 14:10:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 156.4 |
| 7e4904ec-ddce-3b25-a7d3-98e61e2a2cb3 | -7.5818 | -44.4971 | 2025-09-18 14:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 87.7 |
| ba9e67e6-74b0-3251-b82c-04665451b641 | -7.8698 | -45.6087 | 2025-09-18 14:10:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 64.8 |
| 3d53b758-ea63-39ad-933b-26309f27406e | -3.8658 | -43.1787 | 2025-09-18 14:10:00 | GOES-19 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 81.6 |
| a1da9a7a-7597-3ef0-98a5-354b3fee3f81 | -8.9638 | -45.519 | 2025-09-18 14:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 81.0 |
| 4b506ead-4094-3774-8956-75e5a9269748 | -8.669 | -46.4291 | 2025-09-18 14:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 106.0 |
| 38ce98c1-6f98-3f72-9f9e-4b3cac2659ac | -6.6508 | -45.5359 | 2025-09-18 14:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 65.4 |
| fb46c809-1dcb-3783-9693-ef5a43403b84 | -6.9022 | -44.7885 | 2025-09-18 14:10:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 60.1 |
| fa61a09c-b799-338d-a9e5-e9948931ccb9 | -10.0558 | -47.2153 | 2025-09-18 14:10:00 | GOES-19 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 65.3 |
| 047fdfc6-10ee-3efc-afb4-ebda802f9953 | -3.8463 | -40.3607 | 2025-09-18 14:10:00 | GOES-19 | FORQUILHA | CEARÁ | Brasil | 2304350 | 23 | 33 | nan | nan | nan | Caatinga | 85.9 |


[Clique aqui para ver as próximas entradas](README38.md)
