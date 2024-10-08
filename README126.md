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

## Dados Diários - Página 126

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 77c477cd-ad82-3dcb-ae6e-1a14aa35e06e | -11.52154 | -65.13859 | 2024-10-08 05:23:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 30df7cd0-4c96-35c3-ac6a-2926f68d385a | -11.5208 | -65.14296 | 2024-10-08 05:23:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 01c3a21f-1d9c-3c15-9673-e53b0c3c9fad | -11.52005 | -65.14735 | 2024-10-08 05:23:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 5.1 |
| f44d479e-8d23-3a1e-809a-d97326f26a66 | -11.51789 | -65.13794 | 2024-10-08 05:23:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 69cc1090-cd47-3443-a413-96d4b23dc195 | -11.51714 | -65.14231 | 2024-10-08 05:23:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c7a97ae7-bf9c-3a6e-8d2d-441fe635bc49 | -11.51577 | -65.10624 | 2024-10-08 05:23:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b63d1b2e-f701-333a-9d5f-694158bb72c0 | -11.51508 | -65.08829 | 2024-10-08 05:23:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f9ef32ca-8e5b-3b90-82ae-134654b9f4c8 | -11.51212 | -65.1056 | 2024-10-08 05:23:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| fec6f1a9-ba7a-347b-978c-93e261e73aac | -11.5107 | -65.09198 | 2024-10-08 05:23:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a6f72327-1b31-3641-9e3e-53a02829a8a0 | -11.50996 | -65.09631 | 2024-10-08 05:23:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 91af7ac1-b0af-32ca-acad-8a2b573fa4e3 | -11.50922 | -65.10064 | 2024-10-08 05:23:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4e53d261-3476-3e8c-ad6a-f5241ff3e489 | -11.50848 | -65.10497 | 2024-10-08 05:23:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f2c82dec-b3a9-3647-b00f-e3885c18f995 | -11.50705 | -65.09135 | 2024-10-08 05:23:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| de54e65a-09f8-3bea-a06b-7db5388085d9 | -11.50631 | -65.09568 | 2024-10-08 05:23:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bc57c330-5c1c-3a55-bf3c-48055c3066a0 | -11.50587 | -65.23061 | 2024-10-08 05:23:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 13ec256a-0ec6-32c9-bc02-f27881aa5de8 | -21.39128 | -55.68558 | 2024-10-08 05:25:00 | NOAA-20 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 9.6 |
| cd8ecd21-9cdf-3b34-97a2-42eaa64fdba2 | -22.18673 | -49.97425 | 2024-10-08 05:25:00 | NOAA-20 | MARÍLIA | SÃO PAULO | Brasil | 3529005 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 949b78a6-9ce7-3042-b0e4-745b2477dcdf | -22.18544 | -49.96982 | 2024-10-08 05:25:00 | NOAA-20 | MARÍLIA | SÃO PAULO | Brasil | 3529005 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 91b777b2-17fb-398f-a45d-1dca611555c3 | -22.18499 | -49.97663 | 2024-10-08 05:25:00 | NOAA-20 | MARÍLIA | SÃO PAULO | Brasil | 3529005 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 6ff2e789-d901-3d79-ae7c-5c9c338206f4 | -21.38932 | -55.68113 | 2024-10-08 05:25:00 | NOAA-20 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 369d0898-8c99-3a02-acbe-064c7d1a9b49 | -14.8105 | -50.80712 | 2024-10-08 05:25:00 | NOAA-20 | MOZARLÂNDIA | GOIÁS | Brasil | 5214002 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 00f1c4b9-c871-3a23-bfdd-1cd01bad5c7c | -23.11796 | -52.40813 | 2024-10-08 05:25:00 | NOAA-20 | PARANAVAÍ | PARANÁ | Brasil | 4118402 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 1e46ce9e-107d-37b4-9c71-3854f56fc1aa | -23.11757 | -52.41296 | 2024-10-08 05:25:00 | NOAA-20 | PARANAVAÍ | PARANÁ | Brasil | 4118402 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| faefc6c6-8381-31f4-b856-9be962a1d4e3 | -23.25345 | -54.9368 | 2024-10-08 05:25:00 | NOAA-20 | AMAMBAI | MATO GROSSO DO SUL | Brasil | 5000609 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| c20e6bb4-1913-3858-b1b0-2648f07bb7ef | -23.25308 | -54.93647 | 2024-10-08 05:25:00 | NOAA-20 | AMAMBAI | MATO GROSSO DO SUL | Brasil | 5000609 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| c27dda12-a9da-3839-834f-fab11fed144b | -24.24866 | -54.25967 | 2024-10-08 05:25:00 | NOAA-20 | GUAÍRA | PARANÁ | Brasil | 4108809 | 41 | 33 | nan | nan | nan | Mata Atlântica | 13.0 |
| 5f64de55-5cc4-3807-85aa-11a25dec8f8e | -24.2483 | -54.26368 | 2024-10-08 05:25:00 | NOAA-20 | GUAÍRA | PARANÁ | Brasil | 4108809 | 41 | 33 | nan | nan | nan | Mata Atlântica | 8.2 |
| 3e466316-c8f6-3bd0-9d55-3366a4d9f7d2 | -24.24309 | -54.25927 | 2024-10-08 05:25:00 | NOAA-20 | GUAÍRA | PARANÁ | Brasil | 4108809 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 447be7c8-e612-3b21-b7ee-014271e83d51 | -24.24274 | -54.26316 | 2024-10-08 05:25:00 | NOAA-20 | GUAÍRA | PARANÁ | Brasil | 4108809 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| ec3a1b2e-1f52-33d8-908b-a4c52432fcad | -13.29629 | -53.70776 | 2024-10-08 05:25:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b5e68f84-b969-311f-9686-62af6173b0dd | -13.29593 | -53.71075 | 2024-10-08 05:25:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fd420241-2acc-3bc4-883e-69da9b164b9b | -13.2909 | -53.7102 | 2024-10-08 05:25:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 112794da-33ef-3577-9932-5d21aeef0ed5 | -13.29054 | -53.71319 | 2024-10-08 05:25:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f9dd53b0-c794-3eb7-b252-36d77efcb699 | -13.28624 | -53.70659 | 2024-10-08 05:25:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6cb320bd-0438-3f69-8316-a79da3029fe2 | -13.28608 | -53.70805 | 2024-10-08 05:25:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e931f1cf-c1e0-3c12-a9b2-7e6064738304 | -13.28587 | -53.70959 | 2024-10-08 05:25:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| fbecaf1a-bcf7-321d-b0fc-3831e9dafe9a | -13.2857 | -53.71105 | 2024-10-08 05:25:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 993a0e33-b789-3e5e-b061-82b2891552ec | -13.28551 | -53.71259 | 2024-10-08 05:25:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0a9c1b95-6ccc-3a94-8dfd-cd5598a43951 | -13.28531 | -53.71403 | 2024-10-08 05:25:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4e66dd8c-256a-35a4-b40d-9202e4816982 | -13.28069 | -53.71037 | 2024-10-08 05:25:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6f81e738-81e5-38db-b5b9-f203cf6b82a2 | -13.2805 | -53.7119 | 2024-10-08 05:25:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0a93a387-7ad7-3070-866b-c85e3b345731 | -13.2803 | -53.71336 | 2024-10-08 05:25:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c245273b-7972-3b79-9d84-01460594de3b | -14.83101 | -53.88975 | 2024-10-08 05:25:00 | NOAA-20 | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f74acba3-7a9c-3d35-b992-c506676c9092 | -14.82595 | -53.88905 | 2024-10-08 05:25:00 | NOAA-20 | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 630abce1-41c4-33e1-893f-3b4487f32739 | -14.81114 | -53.92672 | 2024-10-08 05:25:00 | NOAA-20 | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0752b002-885f-373c-9c33-c29338c9be64 | -14.80649 | -53.92274 | 2024-10-08 05:25:00 | NOAA-20 | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 538cdfdd-7a42-3446-b75d-9363e0f73bd3 | -14.80613 | -53.9258 | 2024-10-08 05:25:00 | NOAA-20 | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4e6fb8e0-2701-3379-825e-c0192837949c | -14.80576 | -53.92882 | 2024-10-08 05:25:00 | NOAA-20 | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 467cd352-b762-3c77-bc48-5057dd1bf42b | -14.80541 | -53.93176 | 2024-10-08 05:25:00 | NOAA-20 | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4b27bd86-224e-380f-98c4-3680118d5dba | -14.80003 | -53.9339 | 2024-10-08 05:25:00 | NOAA-20 | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d28ad9ae-0fb6-3644-8ca3-da23cd5f4df9 | -20.78804 | -54.83892 | 2024-10-08 05:25:00 | NOAA-20 | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 475000cd-f9b4-3f68-b13a-5720a11aa749 | -20.78773 | -54.84193 | 2024-10-08 05:25:00 | NOAA-20 | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| caf581c9-2886-3c57-b529-f41ea87fbea0 | -20.78263 | -54.841 | 2024-10-08 05:25:00 | NOAA-20 | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 22ddfd80-da0e-3421-b571-a9a609644fee | -20.07733 | -54.51989 | 2024-10-08 05:25:00 | NOAA-20 | JARAGUARI | MATO GROSSO DO SUL | Brasil | 5004908 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 140e3d13-3c65-3de4-b4e5-07c0f4242835 | -21.39421 | -55.68183 | 2024-10-08 05:25:00 | NOAA-20 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 3.6 |
| ad6bf2e8-8be5-30fc-bc72-55aae06bacf8 | -21.39362 | -55.68754 | 2024-10-08 05:25:00 | NOAA-20 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 4fbf744d-e909-399b-8885-bd39c84f19c2 | -21.38871 | -55.68705 | 2024-10-08 05:25:00 | NOAA-20 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3aa79a82-c511-3fc9-8ea2-b64e241c451e | -21.36304 | -55.69556 | 2024-10-08 05:25:00 | NOAA-20 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| feae7d5a-3fca-39cc-900b-88f233cdc3b7 | -21.3625 | -55.70085 | 2024-10-08 05:25:00 | NOAA-20 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 2eafc3c8-848f-31d2-8aa6-16c5873dcd54 | -21.34021 | -54.63987 | 2024-10-08 05:25:00 | NOAA-20 | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b80fe574-9ffb-3481-8bb0-d4b171251689 | -21.33986 | -54.64322 | 2024-10-08 05:25:00 | NOAA-20 | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7027b548-062c-3398-95db-e258049d77ba | -21.33953 | -54.64655 | 2024-10-08 05:25:00 | NOAA-20 | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d7a06eff-3353-3048-a745-472e38808231 | -21.33919 | -54.64986 | 2024-10-08 05:25:00 | NOAA-20 | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 89119ef3-1fbc-34f4-be78-86c167931551 | -21.33496 | -54.63933 | 2024-10-08 05:25:00 | NOAA-20 | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7f8572d0-3250-3b4a-897a-404c4826b7bb | -21.33462 | -54.64267 | 2024-10-08 05:25:00 | NOAA-20 | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 66468e67-5a63-3ebe-817d-1887c89323c1 | -21.33428 | -54.646 | 2024-10-08 05:25:00 | NOAA-20 | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2fb64b46-7509-3721-a30e-b31200182490 | -23.24345 | -55.47811 | 2024-10-08 05:25:00 | NOAA-20 | CORONEL SAPUCAIA | MATO GROSSO DO SUL | Brasil | 5003157 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 88ddc0e7-8fab-3239-8b55-a11a2a6bd478 | -14.7808 | -55.92251 | 2024-10-08 05:25:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 16b113a5-161c-311f-8e75-64bca0dd05df | -20.07311 | -55.96414 | 2024-10-08 05:25:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 82c26300-1e5f-34ec-bdc5-80866f2fdabb | -20.0692 | -55.96979 | 2024-10-08 05:25:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 3d82874f-b8e7-3350-ba32-c5d4852a62bc | -19.58787 | -56.53337 | 2024-10-08 05:25:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 3984bb23-6685-3167-8dd9-25c2fff35d13 | -20.07923 | -55.96572 | 2024-10-08 05:25:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 6c973934-ae91-3326-8d0e-f1303f8ba5ac | -20.07451 | -55.9651 | 2024-10-08 05:25:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 89724382-d3ce-3d01-a21a-d8427258b061 | -19.64834 | -56.56555 | 2024-10-08 05:25:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 2b2f4f7a-f87a-3da2-b625-ec94ec50a415 | -19.57882 | -56.53217 | 2024-10-08 05:25:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 0.9 |
| c0ce40df-71e0-3e95-84a6-b37061e310c5 | -20.07249 | -55.96942 | 2024-10-08 05:25:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.7 |
| ec26d370-316c-3bd0-a55f-6b28b471f889 | -19.64272 | -56.49672 | 2024-10-08 05:25:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| f0e3999e-7ec1-3ad3-ac27-badf6a7d90dc | -19.58153 | -56.53468 | 2024-10-08 05:25:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 5ffd298b-4b94-3ec6-ac27-b764e6d18898 | -20.06978 | -55.9645 | 2024-10-08 05:25:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| bac7d5ed-4bac-3393-91ab-07b103a3572d | -19.58334 | -56.53277 | 2024-10-08 05:25:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| bfb5b851-1816-3d43-b877-f172872e7c11 | -19.58211 | -56.52991 | 2024-10-08 05:25:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 0464fb0c-b1b5-3dcd-a835-eb3a1648c5d4 | -19.577 | -56.5341 | 2024-10-08 05:25:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 8122bd5d-f8b9-3a2a-ad24-20e6002a08d0 | -21.43004 | -57.23003 | 2024-10-08 05:25:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4a7d7109-f14f-3869-9bdb-39657faf75dd | -21.42955 | -57.23436 | 2024-10-08 05:25:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| dee04bd5-719f-3fcc-8f64-db9fe974ecf3 | -21.4267 | -57.21976 | 2024-10-08 05:25:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 83066770-d568-3b94-8b92-201ebda38322 | -21.42509 | -57.23409 | 2024-10-08 05:25:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 79ebd702-911a-3408-92be-08b62bffb3a4 | -21.40014 | -57.2602 | 2024-10-08 05:25:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a0251a42-6e92-31ae-aa6e-5f576bd041f7 | -21.39718 | -57.24729 | 2024-10-08 05:25:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 66b7733d-1dd5-3520-acdf-3f801d416e46 | -21.39274 | -57.24686 | 2024-10-08 05:25:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0b4899df-4cca-3440-b78d-6b48aab20082 | -21.39614 | -57.25608 | 2024-10-08 05:25:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8f0166d1-d234-3966-97c3-eaa5fede2647 | -21.43057 | -57.22532 | 2024-10-08 05:25:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| eaadd6c7-815b-32cf-8957-03fb0ff6c208 | -21.42718 | -57.22186 | 2024-10-08 05:25:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ee08fcf1-15f1-31ca-b101-99a3d4ca14aa | -21.40413 | -57.2644 | 2024-10-08 05:25:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5ef36188-f2c9-312a-aa52-fd579acaceff | -12.65404 | -59.80253 | 2024-10-08 05:25:00 | NOAA-20 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3a73d0b5-1dba-34d3-acee-e1223b764ec8 | -13.42519 | -61.91758 | 2024-10-08 05:25:00 | NOAA-20 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8ffbaa15-4e43-3bac-93bf-b628a8b71b75 | -13.42463 | -61.92112 | 2024-10-08 05:25:00 | NOAA-20 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a381f39d-bacf-3c66-890c-6ec231492015 | -13.42132 | -61.92057 | 2024-10-08 05:25:00 | NOAA-20 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 171bb944-606a-30e2-ba2b-25c8e45f6b8c | -13.41029 | -61.92603 | 2024-10-08 05:25:00 | NOAA-20 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6220d169-a8a7-3463-902b-edf1dcab2ef7 | -13.40919 | -61.93309 | 2024-10-08 05:25:00 | NOAA-20 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 3.1 |
| c3cee2d7-18bf-35b7-bc87-1bafbc59d341 | -13.40754 | -61.92196 | 2024-10-08 05:25:00 | NOAA-20 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |


[Clique aqui para ver as próximas entradas](README127.md)
