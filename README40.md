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

## Dados Diários - Página 40

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7991deef-aff7-3527-89b7-f7d1b2e34b88 | -1.5164 | -52.1696 | 2024-11-08 12:40:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 73.6 |
| edf5db5c-cb1c-3ac7-85ae-32b63cbf7486 | 0.0277 | -49.4311 | 2024-11-08 12:40:00 | GOES-16 | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 128.7 |
| 4437d5b4-8d41-336b-8f55-5f8466a204a9 | -3.546 | -43.6126 | 2024-11-08 12:40:00 | GOES-16 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 266.4 |
| d5be1be4-72c0-3dcf-a39c-c33f2c80eb37 | -3.9669 | -48.1716 | 2024-11-08 12:40:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 96.9 |
| d74176c8-b0a9-3a07-9749-2d251c1394ff | -3.7591 | -42.2917 | 2024-11-08 12:40:00 | GOES-16 | MORRO DO CHAPÉU DO PIAUÍ | PIAUÍ | Brasil | 2206670 | 22 | 33 | nan | nan | nan | Caatinga | 89.4 |
| 62b02311-a638-3004-9fdf-ced7fa10aa37 | -2.0805 | -54.7076 | 2024-11-08 12:40:00 | GOES-16 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 115.0 |
| c9c60c11-77a9-37b3-a92b-4f812017d740 | -2.0805 | -54.7076 | 2024-11-08 12:50:00 | GOES-16 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 100.1 |
| a28da1bf-010f-3574-9f18-afa837d1d508 | -2.6764 | -51.8189 | 2024-11-08 12:50:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 85.5 |
| 76e47380-9305-3357-a7e6-e0cf98012cf0 | -3.665 | -42.3911 | 2024-11-08 12:50:00 | GOES-16 | LUZILÂNDIA | PIAUÍ | Brasil | 2205805 | 22 | 33 | nan | nan | nan | Caatinga | 143.2 |
| b786219b-4a53-351e-b243-651080165edb | -1.5164 | -52.1696 | 2024-11-08 12:50:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 97.9 |
| 9d414946-e0b4-3a59-ae59-8c012d78c7bc | -3.9669 | -48.1716 | 2024-11-08 12:50:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 99.8 |
| 3b1a8d32-0152-32dc-9c87-949e72d1365e | -2.6948 | -51.8185 | 2024-11-08 12:50:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 64.4 |
| cc2e0f58-80af-357e-af16-b9e1db527497 | -1.5347 | -52.1694 | 2024-11-08 12:50:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 89.9 |
| 8be03041-23aa-325f-9983-c7fc8c3035ca | 0.0277 | -49.4311 | 2024-11-08 12:50:00 | GOES-16 | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 136.3 |
| 1a3ee88f-be4b-35b3-b720-a221e17aa5d1 | -1.5164 | -52.1491 | 2024-11-08 13:00:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 61.1 |
| 47c6d775-7b81-30c6-88d0-c139c687b6a0 | -3.665 | -42.3911 | 2024-11-08 13:00:00 | GOES-16 | LUZILÂNDIA | PIAUÍ | Brasil | 2205805 | 22 | 33 | nan | nan | nan | Caatinga | 105.3 |
| 5d1ec2c2-f8ce-3660-830e-c3a55abca6cd | -2.6948 | -51.8185 | 2024-11-08 13:00:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 69.7 |
| 64aef073-df8c-302d-beaf-7975a760307c | -1.5347 | -52.1694 | 2024-11-08 13:00:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 61.3 |
| b207d6fa-ebd5-3896-9228-940ea70828ad | -2.0805 | -54.7076 | 2024-11-08 13:00:00 | GOES-16 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 95.6 |
| 025d3717-ea8d-3429-9252-908fc3b11529 | -5.5391 | -44.3241 | 2024-11-08 13:00:00 | GOES-16 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 82.7 |
| 0e5d212c-4ee8-3f57-8457-91451a4551e1 | -3.546 | -43.6126 | 2024-11-08 13:00:00 | GOES-16 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 203.9 |
| 42e54201-164f-3d78-9c0d-ee526889b2d5 | -1.5164 | -52.1696 | 2024-11-08 13:00:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 109.8 |
| 45dc3b66-08ab-3a88-a4b4-0dc898bc526a | -3.9669 | -48.1716 | 2024-11-08 13:00:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 126.3 |
| 452e5d6c-de42-32a8-9c51-4a3e5096241d | -4.6074 | -49.5774 | 2024-11-08 13:00:00 | GOES-16 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 68.7 |
| 21c55c04-6c6a-33eb-9b77-8391fd3e7dfb | -2.3061 | -46.4825 | 2024-11-08 13:00:00 | GOES-16 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 69.3 |
| 3fc338f6-58c4-31d7-9ae8-82f2fd2a703d | 0.0277 | -49.4311 | 2024-11-08 13:00:00 | GOES-16 | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 138.1 |
| 9c9f2309-4ff1-3d9c-ba15-917c97b2a033 | -2.6764 | -51.8189 | 2024-11-08 13:00:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 74.4 |
| eb40d842-7083-3e52-a96b-7a997252699f | -4.7224 | -48.9751 | 2024-11-08 13:00:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 70.4 |
| 9860641d-cb71-3600-b7bd-635a82554dbe | -3.0865 | -50.5625 | 2024-11-08 13:00:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 136.3 |
| 9aee840f-704e-3b55-85fc-2f704af24bcf | -3.52 | -43.59 | 2024-11-08 13:00:00 | MSG-03 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 34a74b04-3e44-39f4-a928-dee3e5384261 | -3.55 | -43.6 | 2024-11-08 13:00:00 | MSG-03 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 6263188d-3eb8-3297-9dd9-72658406f9f1 | -2.6764 | -51.8189 | 2024-11-08 13:10:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 122.8 |
| d79a472b-e87c-3280-9bcb-b7d0273ef910 | -1.5347 | -52.1694 | 2024-11-08 13:10:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 87.7 |
| ef7ca8a3-efc0-33b2-803a-6c66e99a2738 | -5.5391 | -44.3241 | 2024-11-08 13:10:00 | GOES-16 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 78.5 |
| 2f705c75-1520-3afb-935a-3c38a0655dfe | -2.3061 | -46.4825 | 2024-11-08 13:10:00 | GOES-16 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 65.8 |
| 594dba10-11b7-3611-adfa-5cc024d4ed7d | 0.0277 | -49.4311 | 2024-11-08 13:10:00 | GOES-16 | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 118.2 |
| 26afe2f5-1eba-3f24-9930-d751b991aec6 | -3.546 | -43.6126 | 2024-11-08 13:10:00 | GOES-16 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 285.7 |
| c122bf91-41f6-348a-b4b6-a2eb03346fc0 | -1.9317 | -47.8477 | 2024-11-08 13:10:00 | GOES-16 | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 93.1 |
| 652a9d0c-1d1e-3f3f-ad62-fabcf899d79d | -1.5164 | -52.1696 | 2024-11-08 13:10:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 106.8 |
| 71060f6c-94dd-344f-9b4e-d74cf0c77c91 | -1.5164 | -52.1491 | 2024-11-08 13:10:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 59.6 |
| 17e2e38b-26dd-3d5e-b8cf-8fdba57fd598 | -4.6074 | -49.5774 | 2024-11-08 13:10:00 | GOES-16 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 77.6 |
| f0aebafe-bbe2-3af3-b530-1b4b9b80046c | -5.5439 | -41.6741 | 2024-11-08 13:10:00 | GOES-16 | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 115.7 |
| cb2b8f63-0f7e-3669-baf5-14123832e4a8 | -2.6948 | -51.8185 | 2024-11-08 13:10:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 59.3 |
| a7a9989c-fdb9-3160-a2cd-2cab5d5dd200 | -4.7224 | -48.9751 | 2024-11-08 13:10:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 78.4 |
| 14e7d7c5-2c90-3434-a983-e99775f5ec7e | -4.7409 | -48.9742 | 2024-11-08 13:20:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 84.2 |
| ece37898-c642-3b5e-b0d3-c2feb4f17a9a | -1.1489 | -52.0099 | 2024-11-08 13:20:00 | GOES-16 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 72.8 |
| 1434b7bd-fbe6-3774-b5f2-4dcfccef836a | -2.1765 | -46.4417 | 2024-11-08 13:20:00 | GOES-16 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 68.0 |
| edd96f85-5e18-3f05-a75a-9fa5f36ada38 | -0.046 | -50.7963 | 2024-11-08 13:20:00 | GOES-16 | AFUÁ | PARÁ | Brasil | 1500305 | 15 | 33 | nan | nan | nan | Amazônia | 104.2 |
| 23caf18f-a722-3be5-9122-df2292bc87f7 | -3.068 | -50.5631 | 2024-11-08 13:20:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 102.2 |
| e259ac34-cd4e-34d8-8d3b-7eaade1d7e7d | -6.9613 | -42.8108 | 2024-11-08 13:20:00 | GOES-16 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 71.1 |
| bd295f48-e575-3b2b-97fc-3b07865d7904 | -5.5437 | -41.6981 | 2024-11-08 13:20:00 | GOES-16 | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 84.3 |
| a0e5499b-aa7a-35f5-a24f-6092d67fd36c | -2.3061 | -46.4825 | 2024-11-08 13:20:00 | GOES-16 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 75.5 |
| 754fc295-0baf-30ff-80d2-1fbce27243de | -5.5439 | -41.6741 | 2024-11-08 13:20:00 | GOES-16 | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 93.8 |
| 2eb06140-7ab6-34ac-a691-7b3e8fc3e691 | -1.5164 | -52.1696 | 2024-11-08 13:20:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 105.5 |
| 643f1332-f9c6-3d5c-9f3e-292526aa1718 | -3.0865 | -50.5625 | 2024-11-08 13:20:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 159.6 |
| 09817980-f22d-3872-983c-91be04c249a9 | -2.6764 | -51.8395 | 2024-11-08 13:20:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 70.5 |
| 9f37bab9-5801-3d5d-8647-157b487350a8 | 0.0277 | -49.4311 | 2024-11-08 13:20:00 | GOES-16 | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 117.0 |
| c29bd894-ddb2-3c6c-91e0-11deb5796b2c | -0.046 | -50.7755 | 2024-11-08 13:20:00 | GOES-16 | AFUÁ | PARÁ | Brasil | 1500305 | 15 | 33 | nan | nan | nan | Amazônia | 91.1 |
| 65bdd41f-5c3b-300f-9f69-0df5e515d7a4 | -5.455 | -43.2192 | 2024-11-08 13:20:00 | GOES-16 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 74.2 |
| 6ef710a5-15ee-313f-b13e-16116a2f9b21 | -6.9591 | -41.3539 | 2024-11-08 13:20:00 | GOES-16 | BOCAINA | PIAUÍ | Brasil | 2201804 | 22 | 33 | nan | nan | nan | Caatinga | 61.7 |
| 637a0527-c147-316c-9df6-7a7a35feb210 | -1.5164 | -52.1491 | 2024-11-08 13:20:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 62.8 |
| b28fe741-21c7-3480-92e9-ffb5c04fc2ee | 0.0277 | -49.4311 | 2024-11-08 13:30:00 | GOES-16 | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 119.0 |
| c695c95d-c012-351f-b8ee-28199eafbaf3 | -1.5809 | -47.5724 | 2024-11-08 13:30:00 | GOES-16 | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 66.5 |
| 9b00deb0-36aa-336e-814c-7fa9a1bad268 | -3.068 | -50.5631 | 2024-11-08 13:30:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 131.6 |
| 634da651-0079-3227-ad0c-1e6132afe1bf | -3.0865 | -50.5625 | 2024-11-08 13:30:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 194.1 |
| 91ad2ec6-51cf-3443-a729-3c3c9700d442 | -5.5439 | -41.6741 | 2024-11-08 13:30:00 | GOES-16 | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 137.6 |
| 77bd48f7-c2d6-3b94-9813-cd6effba62f3 | -3.9669 | -48.1716 | 2024-11-08 13:30:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 106.7 |
| 674d183d-c75a-31aa-954e-3a1855570052 | -1.5164 | -52.1491 | 2024-11-08 13:30:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 62.2 |
| 2563f003-fb34-3476-bd23-250e837a29c9 | -6.9613 | -42.8108 | 2024-11-08 13:30:00 | GOES-16 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 76.7 |
| 5783d1ac-edde-309b-b318-db93053fd3a9 | -1.1489 | -52.0099 | 2024-11-08 13:30:00 | GOES-16 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 73.2 |
| 64a98c9e-c220-3f7e-9d49-8c9206e2815c | -6.9591 | -41.3539 | 2024-11-08 13:30:00 | GOES-16 | BOCAINA | PIAUÍ | Brasil | 2201804 | 22 | 33 | nan | nan | nan | Caatinga | 67.3 |
| 7193ad94-9c21-3a04-b639-ad17116dd2cf | -1.5164 | -52.1696 | 2024-11-08 13:30:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 106.6 |
| 343e96b8-1658-34b0-892e-0406348b80d0 | -3.9854 | -48.1708 | 2024-11-08 13:30:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 76.3 |
| 4da890f3-6ca8-30f5-b2a0-6541aad23b09 | -4.7224 | -48.9751 | 2024-11-08 13:30:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 71.9 |
| c4e8d265-e9e6-3ff3-b7ac-879cd7edc2c9 | -2.6764 | -51.8395 | 2024-11-08 13:30:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 58.7 |
| c07de682-d233-3d72-bc0b-bc0604b60245 | -2.1765 | -46.4417 | 2024-11-08 13:30:00 | GOES-16 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 68.8 |
| 20048f4d-c390-3714-b59f-c5a2f49561a5 | -6.9424 | -42.8126 | 2024-11-08 13:30:00 | GOES-16 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 63.8 |
| 00cf9243-61ad-3284-b241-6636e3a5bd55 | -5.5437 | -41.6981 | 2024-11-08 13:30:00 | GOES-16 | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 123.3 |
| bc4273e7-639e-3485-af27-9f4c908a0fcc | -2.3061 | -46.4825 | 2024-11-08 13:30:00 | GOES-16 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 101.5 |
| 6756d40b-c865-30dc-a551-fafaa0744e25 | -5.5439 | -41.6741 | 2024-11-08 13:40:00 | GOES-16 | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 110.4 |
| 399cbf6b-6ec6-38ce-b574-ac92074296db | -6.9591 | -41.3539 | 2024-11-08 13:40:00 | GOES-16 | BOCAINA | PIAUÍ | Brasil | 2201804 | 22 | 33 | nan | nan | nan | Caatinga | 70.2 |
| 9eb376e1-859e-3660-bb2f-db235084f4b1 | -5.4359 | -43.2673 | 2024-11-08 13:40:00 | GOES-16 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 105.5 |
| fbad488b-e777-344b-9738-ab38c8db31f9 | -2.3061 | -46.4825 | 2024-11-08 13:40:00 | GOES-16 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 124.9 |
| 8e55e79e-6c30-37e5-a603-df337dac0046 | -4.7409 | -48.9742 | 2024-11-08 13:40:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 64.8 |
| 6bc215d3-c08d-3a9c-bc4e-6924a59c373d | -0.046 | -50.7963 | 2024-11-08 13:40:00 | GOES-16 | AFUÁ | PARÁ | Brasil | 1500305 | 15 | 33 | nan | nan | nan | Amazônia | 74.3 |
| 4b7d857c-0df3-3215-a6e1-9c6562099412 | -1.5164 | -52.1491 | 2024-11-08 13:40:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 78.5 |
| a202eaa1-4c0b-366c-87ea-be226a031ab1 | -5.5437 | -41.6981 | 2024-11-08 13:40:00 | GOES-16 | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 99.3 |
| 4b8f363d-7f7a-363d-96f3-26c1ca83a96a | -1.5348 | -52.1489 | 2024-11-08 13:40:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 61.0 |
| 864c6642-8219-3f95-8e95-29a8857949d5 | -8.6373 | -40.4514 | 2024-11-08 13:40:00 | GOES-16 | DORMENTES | PERNAMBUCO | Brasil | 2605152 | 26 | 33 | nan | nan | nan | Caatinga | 80.9 |
| 98d05403-a40d-3882-b8a0-b0109b01fcf1 | -1.5347 | -52.1694 | 2024-11-08 13:40:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 90.0 |
| 0541247f-6068-3aac-9ff1-fd4e32748bf4 | -1.5164 | -52.1696 | 2024-11-08 13:40:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 130.8 |
| da6f6858-4d5a-3279-aa0a-e74fc4a2057c | -3.0865 | -50.5625 | 2024-11-08 13:40:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 140.4 |
| 85cd2fb5-a3c6-3b8d-8b82-65768bb23094 | -5.5627 | -41.6726 | 2024-11-08 13:40:00 | GOES-16 | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 84.5 |
| d355fc53-b160-3dfc-825f-7c0e06ea6116 | -2.0805 | -54.7076 | 2024-11-08 13:40:00 | GOES-16 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 85.8 |
| 9f022373-0177-3f59-835a-9b559a7ab68e | -3.068 | -50.5631 | 2024-11-08 13:40:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 236.9 |
| 29bf7d76-f225-3f0a-8c69-94debb77e343 | -1.5164 | -52.1491 | 2024-11-08 13:50:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 96.1 |
| e3844171-c69b-3a78-8ef4-5a510ab1c057 | -10.2243 | -42.4476 | 2024-11-08 13:50:00 | GOES-16 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 90.6 |
| 64ea51dd-7e23-373f-9e68-a04d8eb2c24b | -6.9974 | -41.3016 | 2024-11-08 13:50:00 | GOES-16 | SANTO ANTÔNIO DE LISBOA | PIAUÍ | Brasil | 2209401 | 22 | 33 | nan | nan | nan | Caatinga | 68.2 |
| 9ca76430-e04a-3ad0-87dc-3144e0b50224 | -2.3061 | -46.5046 | 2024-11-08 13:50:00 | GOES-16 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 82.1 |
| 20e0e7ad-eb65-3068-9da9-4dac8fc652b8 | -2.3061 | -46.4825 | 2024-11-08 13:50:00 | GOES-16 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 164.1 |


[Clique aqui para ver as próximas entradas](README41.md)
