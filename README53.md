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

## Dados Diários - Página 53

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| dec0884f-8a2e-3f34-a4ab-d2ae9aa7874e | -3.69649 | -51.80471 | 2024-12-01 04:44:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| f5fe2aee-5557-3e8b-ace1-1bbfa2faadb0 | -6.91821 | -43.53645 | 2024-12-01 04:44:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 4.8 |
| a58f2201-a9eb-3183-b4e9-884097dce214 | -1.43507 | -52.40118 | 2024-12-01 04:44:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| db4c8bb5-3507-3b82-96f5-e6a2ca7e5432 | -2.80819 | -53.0438 | 2024-12-01 04:44:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 816f56f7-0fa3-385f-b44b-9af8d0ccf1d6 | -2.37415 | -50.40337 | 2024-12-01 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9a52fe6f-8b46-37ff-ab3d-1b5861e14dc2 | -2.67443 | -46.61431 | 2024-12-01 04:44:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ffa2c798-2fba-3625-bb2e-387905e7825b | -3.08948 | -53.70821 | 2024-12-01 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8b31a106-1849-3e33-972e-6ae697fce3a1 | -1.49384 | -52.64866 | 2024-12-01 04:44:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 06ea2c75-c926-3765-bce4-c80e8b9c907b | -3.09307 | -50.35037 | 2024-12-01 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| acec6d4a-4b75-3fc9-b417-92330f8fc26a | -2.12091 | -45.96399 | 2024-12-01 04:44:00 | NPP-375D | GOVERNADOR NUNES FREIRE | MARANHÃO | Brasil | 2104677 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0eca5d71-aa11-3e98-9fdf-2b6c742cab7e | -1.0882 | -53.63808 | 2024-12-01 04:44:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d23af144-ba10-3355-a2c0-c4e97601e53a | -2.51515 | -51.83345 | 2024-12-01 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6c8357ec-bf28-3858-8419-e0413e8e764d | -3.93026 | -46.50434 | 2024-12-01 04:44:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9182ebfe-6157-3c1b-9a24-eef2c0121cca | -3.24469 | -53.65179 | 2024-12-01 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 00fd478c-d569-3d12-8d25-62391b09daff | -2.62396 | -46.95845 | 2024-12-01 04:44:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 60c8d7c5-3106-3702-931c-214230c613f6 | -3.09628 | -54.02098 | 2024-12-01 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 16fe155e-f9bc-30ff-be12-1da497e6d1df | -2.45875 | -53.71157 | 2024-12-01 04:44:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c4d6cf70-021b-3844-b6c3-18973f3eec7f | -2.47044 | -46.56038 | 2024-12-01 04:44:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4c45df94-438f-3442-b296-a8d858a065bf | -1.148 | -53.67299 | 2024-12-01 04:44:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 20a553af-c75d-367b-bb21-7eac464157d1 | -2.84307 | -54.03502 | 2024-12-01 04:44:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 180d53b6-08bb-3caf-bc28-4da93fdf531b | -2.63507 | -51.76224 | 2024-12-01 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 5267d498-d606-3ddf-8ead-6dbdd59e6e12 | -2.59149 | -53.99005 | 2024-12-01 04:44:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4867ceeb-9f8c-3881-905d-96eae8b08e17 | -1.08067 | -53.63689 | 2024-12-01 04:44:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a136036f-a57b-3894-8165-51384db30241 | -3.25603 | -54.22817 | 2024-12-01 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7d589dc4-911a-30d8-8e87-64a7c31d9ddd | -3.25853 | -50.05091 | 2024-12-01 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d0f0dfd2-5db7-3c73-a830-4e9c62f9d2d7 | -1.23656 | -51.61882 | 2024-12-01 04:44:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 8c088271-72ac-3e95-a2fe-fac2884b45b5 | -3.3055 | -50.03346 | 2024-12-01 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 328e7100-7b92-31ac-bc9a-e323c4c45d9a | -1.51552 | -45.90628 | 2024-12-01 04:44:00 | NPP-375D | LUÍS DOMINGUES | MARANHÃO | Brasil | 2106201 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| dab589cd-ef0e-3d4d-a787-25ebd6534cae | -3.8451 | -40.98084 | 2024-12-01 04:44:00 | NPP-375D | UBAJARA | CEARÁ | Brasil | 2313609 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 0aebb25d-616e-34af-b2cb-6e616c6f5773 | -2.38388 | -50.32001 | 2024-12-01 04:44:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1a6fb982-2fdd-30c4-b52f-02c9e29f35da | -2.85289 | -54.19139 | 2024-12-01 04:44:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 5ccc1b64-a5eb-3462-b49b-52de8040a023 | -1.73277 | -49.81546 | 2024-12-01 04:44:00 | NPP-375D | CURRALINHO | PARÁ | Brasil | 1502806 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fba01710-e59e-399c-9c75-9a81f1844cf3 | -2.10017 | -47.6273 | 2024-12-01 04:44:00 | NPP-375D | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a5c2ca16-f98a-3b3c-99c9-59219b4e051d | -2.87568 | -51.82979 | 2024-12-01 04:44:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| d1caffcb-6dc1-3409-b645-48cebe52916e | -1.64576 | -53.87094 | 2024-12-01 04:44:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d18fb3b1-6fee-381e-83d1-74e3784295b7 | -1.58733 | -52.28403 | 2024-12-01 04:44:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| efe24938-2cb2-3dd9-a3f5-1d0849de9d64 | -3.76281 | -46.51355 | 2024-12-01 04:44:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 193512c6-388c-3bc3-ada8-cb0538efba85 | -1.2112 | -51.736 | 2024-12-01 04:44:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 18449789-1757-37ee-835b-5b650e237050 | -3.12485 | -53.09524 | 2024-12-01 04:44:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 2f42bab2-5120-342d-9e0a-e22a5b3001d3 | -3.31084 | -53.86448 | 2024-12-01 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 11.1 |
| e1222912-27fa-38e4-98e1-16f7aa6c6f5b | -3.6678 | -50.24585 | 2024-12-01 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d56dc094-9f7d-364c-b9ed-d90a4d65d2f8 | -4.55522 | -43.30845 | 2024-12-01 04:44:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 38.8 |
| 55bff950-777e-300f-8bcc-51506ff2761b | -3.30856 | -53.36914 | 2024-12-01 04:44:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e7e29226-50c9-3dc9-94f2-2c11fa3c3a8f | -5.79942 | -49.98724 | 2024-12-01 04:44:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6d916a06-f85a-389a-a0a6-8ab838d18597 | -4.07443 | -50.0293 | 2024-12-01 04:44:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 779cea72-93d8-356f-82fd-20bfe411b310 | -2.98587 | -45.57047 | 2024-12-01 04:44:00 | NPP-375D | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 784aeaa0-4708-3945-8ef7-88ed1eea63b2 | -1.70467 | -52.76511 | 2024-12-01 04:44:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 90b558bf-3a7e-33e2-96e9-b19375e7e6d2 | 0.07891 | -60.46471 | 2024-12-01 04:44:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f59c62a4-7082-33f1-a24d-482f67383137 | -3.6914 | -51.81497 | 2024-12-01 04:44:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| deee01e9-0d82-3d46-8f3c-0d6719228191 | -1.56978 | -53.52002 | 2024-12-01 04:44:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0e993232-2ae2-3e1b-931d-b007993e875e | -2.19696 | -53.77681 | 2024-12-01 04:44:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 601ffcf4-3cce-3f88-884e-993355e4d472 | -0.82009 | -51.61887 | 2024-12-01 04:44:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 32db8689-52bd-33c7-abd0-dd19f9b802f8 | -1.46133 | -52.69287 | 2024-12-01 04:44:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ed5cc5a5-0e64-362e-9d03-5c3d178c9b79 | -1.00604 | -51.72342 | 2024-12-01 04:44:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 96348cf7-ff16-3a1e-b420-57f81b5676cc | -1.66858 | -52.49928 | 2024-12-01 04:44:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 52fd7ad4-3dd2-37fa-bec0-c6fed4e685f8 | -3.11395 | -53.98235 | 2024-12-01 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 74dfa800-636e-3870-961e-680f94400513 | -3.34673 | -50.82183 | 2024-12-01 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 3956a88e-7a04-3a00-95b2-60af013860f3 | -4.10315 | -50.98355 | 2024-12-01 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5a019c33-7506-3d19-b2f7-f94f8b6217e4 | -2.6797 | -46.11097 | 2024-12-01 04:44:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 8aef247a-4454-382e-844f-bba8bf708dd8 | -4.78086 | -44.80868 | 2024-12-01 04:44:00 | NPP-375D | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f92b0c30-b2f4-3c67-a166-fd6614005547 | -3.48094 | -50.446 | 2024-12-01 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2188717d-139c-3e55-8dbe-572f2db0e80a | -2.80007 | -54.03985 | 2024-12-01 04:44:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 0efc29e8-3619-3171-aed6-b8adc8cfd470 | -4.17409 | -48.6138 | 2024-12-01 04:44:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d896b394-6fab-398b-b68e-b2f6791ac8da | -2.60964 | -51.81079 | 2024-12-01 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1f30d611-fa9d-3519-bd90-e72ea9f23c3d | -1.70383 | -52.43665 | 2024-12-01 04:44:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 313d72e7-ce87-3d42-a0bc-e6b61ea90cb2 | -2.19482 | -50.57403 | 2024-12-01 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| ca747796-9d26-3600-94c3-40d1df84a917 | -1.07078 | -53.62626 | 2024-12-01 04:44:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e7d85902-f055-393e-8ebe-767a3f31aa4f | -2.74042 | -54.97314 | 2024-12-01 04:44:00 | NPP-375D | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 33.3 |
| ee3e8517-e4bf-3e8f-88e0-27b4bee6ec73 | -1.12888 | -53.1906 | 2024-12-01 04:44:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 0719afdb-31a5-3738-af36-20f40101cb1c | -2.34542 | -53.86476 | 2024-12-01 04:44:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 371dbf19-5a79-3e6f-adc7-9738d72147ae | -3.41656 | -50.35818 | 2024-12-01 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8044b2c4-b525-3a1d-8691-4fb32b9c2e9a | -4.53816 | -45.69649 | 2024-12-01 04:44:00 | NPP-375D | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 952a2511-66da-3b34-bf9e-c402ca92ef83 | -1.26182 | -51.5883 | 2024-12-01 04:44:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2a0b32d1-08dc-3fec-9682-9e975da6711f | -4.14496 | -48.22236 | 2024-12-01 04:44:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7d7081f7-efe0-3452-aeea-c684ec21b504 | -7.6895 | -47.73568 | 2024-12-01 04:44:00 | NPP-375D | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 516b272b-b93c-33f2-a079-718873aec00c | -3.60087 | -49.98433 | 2024-12-01 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1d0039bc-b2e7-3a5c-8e64-451496e03488 | -1.09644 | -53.39348 | 2024-12-01 04:44:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b394cf57-ace9-3511-95c2-e77b09d9c24a | -2.12456 | -50.63414 | 2024-12-01 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ed9263b2-e8bf-38f4-b243-1c8f17c25227 | -3.44498 | -49.98796 | 2024-12-01 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d758820e-72d5-385d-9cea-4fe9f539864d | -3.49275 | -53.8069 | 2024-12-01 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ac938709-1267-375b-98c7-a1f440b950e6 | -4.86934 | -50.86588 | 2024-12-01 04:44:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4d8dc45d-9f58-3694-909e-2abea8676e9e | -4.00869 | -54.62001 | 2024-12-01 04:44:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5740c15a-453c-397f-916e-faa51b825d2f | -2.38134 | -50.40095 | 2024-12-01 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2334c26b-7051-37ba-b476-29b97c9b33ff | -1.51622 | -45.90171 | 2024-12-01 04:44:00 | NPP-375D | LUÍS DOMINGUES | MARANHÃO | Brasil | 2106201 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 72cafb01-1bc5-3243-9d3a-0a8a56b1b81c | -3.0519 | -51.06514 | 2024-12-01 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 70308762-3344-356f-9301-5f5e42f19201 | -4.03738 | -50.56203 | 2024-12-01 04:44:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e119f8e4-2a90-3325-b244-7aef61e19cda | -3.33212 | -53.54689 | 2024-12-01 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 45a2fa7c-7c5c-3bee-92a2-a62199442081 | -3.29092 | -51.15229 | 2024-12-01 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 5a3f1a57-ccc2-33c8-9392-f661f394944d | -1.55865 | -53.51806 | 2024-12-01 04:44:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3c1d4d61-a27b-3220-8733-bfa98399dd63 | -3.58393 | -50.51912 | 2024-12-01 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2b65fb55-7552-3bfc-b447-9df9521aba5d | -2.52837 | -54.07212 | 2024-12-01 04:44:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 54762b88-8361-33a4-84d3-efc2c4c77426 | -1.73609 | -49.81598 | 2024-12-01 04:44:00 | NPP-375D | CURRALINHO | PARÁ | Brasil | 1502806 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| dace5263-bf61-370c-92c3-b6ad9216b876 | -3.32013 | -51.62882 | 2024-12-01 04:44:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2e545db0-43bc-3215-b98e-9106f2d4fe98 | -3.06769 | -53.68938 | 2024-12-01 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a3238f01-c3e0-35c5-a9b9-3d91809c883a | -2.19204 | -50.57005 | 2024-12-01 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| ce531ee2-f4a2-3a41-85ee-365a71e8ee25 | -2.73619 | -47.98661 | 2024-12-01 04:44:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0bdc146f-9998-3c32-bd6c-f4a9029349da | -2.27106 | -53.46328 | 2024-12-01 04:44:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 122e2dc9-b533-3650-8a89-48008d213c1b | -3.68549 | -50.24153 | 2024-12-01 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 999f6c7b-db9f-302a-91a7-bc7456ab0135 | -2.94077 | -51.50743 | 2024-12-01 04:44:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f815f28e-a98a-3b10-9e99-75e334a2b26b | -3.10235 | -54.03117 | 2024-12-01 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |


[Clique aqui para ver as próximas entradas](README54.md)
