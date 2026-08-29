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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5331e9fe-aaf8-3e75-a72b-afc5eaf060b1 | -11.0445 | -57.2023 | 2026-08-29 00:00:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 59.6 |
| bd411036-d042-36b7-b600-b5b44741f453 | -5.8895 | -57.7513 | 2026-08-29 00:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 212.7 |
| 10d0297d-361d-35d0-8736-60f933a1d655 | -6.77 | -55.6445 | 2026-08-29 00:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 53.5 |
| fb2d0e7e-6081-3490-abe4-d2a71768325f | -5.871 | -57.7715 | 2026-08-29 00:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 55.4 |
| 5393cfd2-ef12-38f2-88c3-65739b61e27a | 2.4155 | -60.8699 | 2026-08-29 00:00:00 | GOES-19 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 49.1 |
| b65bba4f-cbfd-3a1d-9210-5baf2dcaf3cf | -5.4179 | -43.1752 | 2026-08-29 00:00:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 45.6 |
| b3d81247-dd60-35bd-a60b-9ba077c0678b | -6.7529 | -55.4462 | 2026-08-29 00:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 65.6 |
| 4e0b5d0f-24f3-3026-95d0-f130696ae373 | -9.9288 | -60.4277 | 2026-08-29 00:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 67.7 |
| 76412673-0f76-3b11-bf08-a15b37e33016 | -6.6315 | -43.7533 | 2026-08-29 00:00:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 85.5 |
| b751f5f5-50eb-3269-9347-69206fa161b4 | 0.1367 | -60.393 | 2026-08-29 00:00:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 68.8 |
| 5a9fd0be-90d8-3e32-90cd-1ced273a88d9 | 2.3972 | -60.8891 | 2026-08-29 00:00:00 | GOES-19 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 46.2 |
| e8bb7e09-4e75-3754-b8c7-a0822bfe016f | -6.7514 | -55.6654 | 2026-08-29 00:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 90.5 |
| 9a5d0b22-ddd4-34c3-904d-f7b1d0dbef3e | -7.2847 | -45.8652 | 2026-08-29 00:00:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 148.4 |
| cc38645c-6538-3feb-a26c-94ebe146c2de | -8.5358 | -55.3629 | 2026-08-29 00:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 126.4 |
| a9c8099d-f927-3ad4-a585-b22675acd97f | -6.7528 | -55.4661 | 2026-08-29 00:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 161.0 |
| a6b406f4-a9e5-318f-b02d-c93d06d9e1a5 | -11.0443 | -57.2222 | 2026-08-29 00:00:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 131.3 |
| 98ac5cca-93eb-35da-b481-603cb04986be | -20.9406 | -57.5905 | 2026-08-29 00:00:00 | GOES-19 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 79.7 |
| c722b717-55f4-3a41-83d4-5feebaccd51a | -14.9386 | -56.3216 | 2026-08-29 00:00:00 | GOES-19 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 119.0 |
| 87acc865-55d0-34fa-a594-416957d68de0 | -10.9187 | -46.6192 | 2026-08-29 00:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 39.4 |
| 386e90d3-ec5d-3739-ac74-bb667d0dccb5 | -20.9614 | -57.5665 | 2026-08-29 00:00:00 | GOES-19 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 73.4 |
| 92fdad65-9c6c-3757-a907-2791744f86d1 | -5.4177 | -43.1986 | 2026-08-29 00:00:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 35.6 |
| 7091949f-a01e-31ae-a33e-c65de23bb956 | -6.7344 | -55.4471 | 2026-08-29 00:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 60.2 |
| 2b64784b-1575-3164-9ab4-927bc086f660 | -7.6213 | -61.3599 | 2026-08-29 00:00:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 53.4 |
| 1c7c96fe-0099-363b-8fc7-d10230b4caf5 | -12.43 | -43.4182 | 2026-08-29 00:00:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 77.6 |
| d7fc8efe-d932-362a-9148-567048ad0379 | -6.7884 | -55.6635 | 2026-08-29 00:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 63.1 |
| 9e378120-c11b-380a-b779-d0644a18deb4 | -14.9011 | -52.6267 | 2026-08-29 00:00:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 59.1 |
| 98b8b5fd-6883-378d-9c71-67b0720c41a9 | -20.941 | -57.5694 | 2026-08-29 00:00:00 | GOES-19 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 128.5 |
| 4e8756b4-1ac2-33c2-b4e0-c04c184801f1 | 2.3972 | -60.8701 | 2026-08-29 00:00:00 | GOES-19 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 44.6 |
| 3a07b759-ebc2-3fc4-bf7b-84ec33fc0fe4 | -7.5139 | -55.2851 | 2026-08-29 00:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 76.8 |
| 74ae676e-54af-3326-b582-08a39d51f7c9 | -6.7699 | -55.6644 | 2026-08-29 00:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 198.8 |
| e4d17c83-0608-3a34-9418-743c2cb7b68e | -7.5137 | -55.3051 | 2026-08-29 00:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 126.6 |
| f0c62d95-ae09-37a2-838b-fbc86857ec5f | -5.9078 | -57.77 | 2026-08-29 00:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 57.6 |
| ee30c763-499e-329d-ab66-324a5e0351ef | -11.0252 | -57.2436 | 2026-08-29 00:00:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 103.4 |
| 570b3513-7d07-362e-bd4a-3ee93363cc7d | -7.4952 | -55.3062 | 2026-08-29 00:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 62.0 |
| d9f3b795-da0a-36df-801a-bab157f1e1ca | -20.9606 | -57.6086 | 2026-08-29 00:00:00 | GOES-19 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 71.0 |
| 58cc87a6-8e17-38d7-b98a-670d9455980c | -6.6127 | -43.7549 | 2026-08-29 00:00:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 53.4 |
| 11756ec4-c23d-3c45-98c7-17b1c57d3acc | -5.9819 | -57.6892 | 2026-08-29 00:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 52.4 |
| da8a8c44-7661-3e98-be9c-210f11ff2c67 | -7.5845 | -61.3423 | 2026-08-29 00:00:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 59.7 |
| 8e87bcd8-4547-310b-b286-401dbc99d9fd | -7.4953 | -55.2862 | 2026-08-29 00:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 67.2 |
| 38fd607d-3025-3534-9bc2-4dbd0235b1ac | -5.8894 | -57.7708 | 2026-08-29 00:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 182.6 |
| aa577bcf-e676-337b-a5f6-18c662b5a334 | -8.5359 | -55.3428 | 2026-08-29 00:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 105.4 |
| 94d043ca-4b51-348b-9e81-857d6ec5190c | 2.4154 | -60.8888 | 2026-08-29 00:00:00 | GOES-19 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 50.4 |
| 95b0e3b0-5968-3272-a484-8eb96e67231a | -6.6319 | -43.7068 | 2026-08-29 00:00:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 53.8 |
| b1d682c1-47bc-30b7-a2bd-37081e66355d | -6.6129 | -43.7317 | 2026-08-29 00:00:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 85.9 |
| 6c72c30b-7f32-3d79-8403-ec6f09bfd32e | -6.6505 | -43.7284 | 2026-08-29 00:00:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 41.8 |
| 5224f8f0-2b6b-373c-a09f-756ec7f33c83 | -11.0256 | -57.2038 | 2026-08-29 00:00:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 46.1 |
| 475b8e1f-38c0-373c-b6a7-9e7aaf233452 | -5.9079 | -57.7506 | 2026-08-29 00:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 101.6 |
| 69b030ba-8a70-32a4-a3e1-a087ec59ef2a | -6.1657 | -57.7793 | 2026-08-29 00:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 49.0 |
| 786e8c16-02c0-3b39-8d43-0c340496c5d9 | -7.2849 | -45.8427 | 2026-08-29 00:00:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 137.8 |
| e6bbdcf7-7314-3442-a37b-aef476818b92 | -6.6317 | -43.73 | 2026-08-29 00:00:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 126.7 |
| fd982e50-9ae4-3cc6-86f8-0d16ec6957c3 | -2.5042 | -48.1366 | 2026-08-29 00:00:00 | GOES-19 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 64.2 |
| 29dbe23b-0841-345c-b78b-585388254eea | -11.0254 | -57.2237 | 2026-08-29 00:00:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 111.2 |
| 6d46ced7-0453-3869-9aef-46c5e69dccc8 | -11.0441 | -57.2421 | 2026-08-29 00:00:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 90.2 |
| 7644ca23-42c1-300e-a1fe-796703016ddf | -6.7698 | -55.6844 | 2026-08-29 00:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 111.6 |
| 5b905a3a-8aa3-397b-90e0-3ed0fde69e18 | -6.7343 | -55.4671 | 2026-08-29 00:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 155.0 |
| 43788b96-6ee7-3602-b762-3c2f6f30ed15 | -27.86981 | -50.57961 | 2026-08-29 00:01:00 | TERRA_M-M | CAPÃO ALTO | SANTA CATARINA | Brasil | 4203253 | 42 | 33 | nan | nan | nan | Mata Atlântica | 10.5 |
| 8ecefae1-a07d-3efb-bc23-8450091694c8 | -27.86823 | -50.56498 | 2026-08-29 00:01:00 | TERRA_M-M | CAPÃO ALTO | SANTA CATARINA | Brasil | 4203253 | 42 | 33 | nan | nan | nan | Mata Atlântica | 10.3 |
| 982ffcb9-9329-3ff7-8764-449ae1ada423 | -17.99032 | -42.6013 | 2026-08-29 00:03:00 | TERRA_M-M | SÃO SEBASTIÃO DO MARANHÃO | MINAS GERAIS | Brasil | 3164506 | 31 | 33 | nan | nan | nan | Mata Atlântica | 15.2 |
| d90f4a00-5636-3406-923e-40901657b791 | -21.71667 | -47.14109 | 2026-08-29 00:03:00 | TERRA_M-M | CASA BRANCA | SÃO PAULO | Brasil | 3510807 | 35 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 74ea93ea-e6c5-3a8f-8754-87b2f64c0016 | -20.96782 | -57.63316 | 2026-08-29 00:03:00 | TERRA_M-M | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 94.5 |
| 596546c4-cc8b-3ded-8a7f-7d5d2d578edd | -20.94155 | -57.60331 | 2026-08-29 00:03:00 | TERRA_M-M | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 87.6 |
| 30f19303-8ae2-3c52-bf84-4b5ac18e3cd8 | -17.42355 | -40.04635 | 2026-08-29 00:03:00 | TERRA_M-M | MEDEIROS NETO | BAHIA | Brasil | 2921104 | 29 | 33 | nan | nan | nan | Mata Atlântica | 23.7 |
| 4b3ea957-5c6c-3fe5-a26a-c63d70c2acd8 | -21.53053 | -48.62548 | 2026-08-29 00:03:00 | TERRA_M-M | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 23.7 |
| 6e77171c-7a44-3520-89b7-bd1ec32893ac | -19.00359 | -47.44565 | 2026-08-29 00:03:00 | TERRA_M-M | IRAÍ DE MINAS | MINAS GERAIS | Brasil | 3131604 | 31 | 33 | nan | nan | nan | Cerrado | 56.3 |
| edee2c09-f533-3599-9a82-8eb4d60e14a2 | -19.00228 | -47.43631 | 2026-08-29 00:03:00 | TERRA_M-M | IRAÍ DE MINAS | MINAS GERAIS | Brasil | 3131604 | 31 | 33 | nan | nan | nan | Cerrado | 32.8 |
| 2675e580-20ab-3fa8-a48b-648d680611e9 | -18.8498 | -47.40591 | 2026-08-29 00:03:00 | TERRA_M-M | MONTE CARMELO | MINAS GERAIS | Brasil | 3143104 | 31 | 33 | nan | nan | nan | Cerrado | 13.5 |
| 36bd98c7-b168-3fbe-8df4-21ab7110aefe | -21.38273 | -45.34613 | 2026-08-29 00:03:00 | TERRA_M-M | TRÊS PONTAS | MINAS GERAIS | Brasil | 3169406 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.6 |
| b4c4e85c-a3e7-319b-ace5-784c6a64453a | -21.70917 | -47.15198 | 2026-08-29 00:03:00 | TERRA_M-M | CASA BRANCA | SÃO PAULO | Brasil | 3510807 | 35 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 1c6808d0-b8bc-301d-b4c7-f3df226c8f53 | -18.85112 | -47.41529 | 2026-08-29 00:03:00 | TERRA_M-M | MONTE CARMELO | MINAS GERAIS | Brasil | 3143104 | 31 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 1b9ec234-b689-34a6-ab82-c9f92260b009 | -17.8214 | -39.70281 | 2026-08-29 00:03:00 | TERRA_M-M | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 24.1 |
| 633a6b56-67e9-3a89-981e-05e9dcad2c14 | -23.19645 | -46.85777 | 2026-08-29 00:03:00 | TERRA_M-M | JUNDIAÍ | SÃO PAULO | Brasil | 3525904 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.9 |
| c581f370-49a3-31b9-bbf5-f31782940739 | -21.70785 | -47.14254 | 2026-08-29 00:03:00 | TERRA_M-M | CASA BRANCA | SÃO PAULO | Brasil | 3510807 | 35 | 33 | nan | nan | nan | Cerrado | 10.1 |
| e7d42bcb-8305-3bd6-8348-7c47de561c7b | -20.9453 | -57.56022 | 2026-08-29 00:03:00 | TERRA_M-M | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 152.9 |
| e21b5874-4449-36fd-a6be-287312d3e953 | -22.86854 | -47.15087 | 2026-08-29 00:03:00 | TERRA_M-M | CAMPINAS | SÃO PAULO | Brasil | 3509502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.9 |
| 349dae59-de9b-3e02-81af-021ba0998507 | -20.9383 | -57.56623 | 2026-08-29 00:03:00 | TERRA_M-M | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 168.3 |
| 0724f41f-97ea-3625-82fb-f745c170dba7 | -23.08402 | -48.62909 | 2026-08-29 00:03:00 | TERRA_M-M | ITATINGA | SÃO PAULO | Brasil | 3523503 | 35 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 229587d0-6b3c-32be-9b2d-f183f05be20d | -20.92893 | -57.5617 | 2026-08-29 00:03:00 | TERRA_M-M | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 47.4 |
| 1ac68171-0797-389e-ad6e-f73b070735d8 | -20.33386 | -47.53906 | 2026-08-29 00:03:00 | TERRA_M-M | JERIQUARA | SÃO PAULO | Brasil | 3525409 | 35 | 33 | nan | nan | nan | Cerrado | 5.8 |
| de0039fd-0774-360e-8a82-55bf8029fca2 | -20.94833 | -57.59733 | 2026-08-29 00:03:00 | TERRA_M-M | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 179.5 |
| a7a77df6-3c36-3743-ad45-3a792024e904 | -23.19733 | -46.99432 | 2026-08-29 00:03:00 | TERRA_M-M | JUNDIAÍ | SÃO PAULO | Brasil | 3525904 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.1 |
| 79b9600d-50bf-3ac3-8761-db59b0c95412 | -18.78784 | -45.59947 | 2026-08-29 00:03:00 | TERRA_M-M | BIQUINHAS | MINAS GERAIS | Brasil | 3107000 | 31 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 1d1ff552-3bd5-30f7-943b-690f77d45ff9 | -22.57323 | -44.8608 | 2026-08-29 00:03:00 | TERRA_M-M | LAVRINHAS | SÃO PAULO | Brasil | 3526605 | 35 | 33 | nan | nan | nan | Mata Atlântica | 11.9 |
| 0fd22eb6-4bf8-3316-ad39-4c536797e11d | -20.97443 | -57.62608 | 2026-08-29 00:03:00 | TERRA_M-M | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 122.4 |
| 7fedc3eb-88cb-3f7c-831f-19c785d28567 | -22.56388 | -44.86242 | 2026-08-29 00:03:00 | TERRA_M-M | LAVRINHAS | SÃO PAULO | Brasil | 3526605 | 35 | 33 | nan | nan | nan | Mata Atlântica | 12.5 |
| fdab9efa-7959-3b7e-bb18-cd75a1222f12 | -23.08274 | -48.61895 | 2026-08-29 00:03:00 | TERRA_M-M | ITATINGA | SÃO PAULO | Brasil | 3523503 | 35 | 33 | nan | nan | nan | Cerrado | 20.1 |
| 111eb8e6-977f-355d-8953-d896cae67ace | -23.07495 | -48.63047 | 2026-08-29 00:03:00 | TERRA_M-M | ITATINGA | SÃO PAULO | Brasil | 3523503 | 35 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 40c6579a-24d1-338d-a446-2700c472797e | -20.93192 | -57.5988 | 2026-08-29 00:03:00 | TERRA_M-M | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 38.4 |
| 7b2915df-d97e-3c81-a6d6-d3236822a833 | -20.95305 | -44.3502 | 2026-08-29 00:03:00 | TERRA_M-M | RITÁPOLIS | MINAS GERAIS | Brasil | 3156106 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.0 |
| 4586b59e-7c04-3baa-95db-c55a1da5d956 | -21.96834 | -48.18156 | 2026-08-29 00:03:00 | TERRA_M-M | RIBEIRÃO BONITO | SÃO PAULO | Brasil | 3542909 | 35 | 33 | nan | nan | nan | Cerrado | 9.1 |
| b23a4c84-1823-3027-a90c-5f81a0c07886 | -23.07367 | -48.62035 | 2026-08-29 00:03:00 | TERRA_M-M | ITATINGA | SÃO PAULO | Brasil | 3523503 | 35 | 33 | nan | nan | nan | Cerrado | 21.3 |
| 77455441-38e3-343d-a44c-04bdface46ba | -20.96474 | -57.59586 | 2026-08-29 00:03:00 | TERRA_M-M | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 47.1 |
| d0c62fcd-87c6-3752-8d60-aa963b674ee1 | -21.71799 | -47.15054 | 2026-08-29 00:03:00 | TERRA_M-M | CASA BRANCA | SÃO PAULO | Brasil | 3510807 | 35 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 802b8ec0-4e30-328c-8bda-bb9b311ba748 | -15.76473 | -50.03878 | 2026-08-29 00:05:00 | TERRA_M-M | GUARAÍTA | GOIÁS | Brasil | 5209291 | 52 | 33 | nan | nan | nan | Cerrado | 6.6 |
| bff141ba-7b4d-3769-a71f-c8a31f220c02 | -14.91978 | -52.61877 | 2026-08-29 00:05:00 | TERRA_M-M | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 19.1 |
| bd73938c-b393-34cf-bcb7-2813b5deeb4c | -15.64552 | -45.93016 | 2026-08-29 00:05:00 | TERRA_M-M | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 9.7 |
| bbb8a9df-d948-3bc2-b045-bb84bc8bcdc9 | -14.62733 | -50.90027 | 2026-08-29 00:05:00 | TERRA_M-M | ARUANÃ | GOIÁS | Brasil | 5202502 | 52 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 590c77d9-61e9-3a6f-a565-e2004afbe6bb | -14.76159 | -48.75011 | 2026-08-29 00:05:00 | TERRA_M-M | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 5b2acd23-75f0-3443-87a6-acbfeda59cde | -17.28402 | -46.0332 | 2026-08-29 00:05:00 | TERRA_M-M | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 4dcef2f5-63ed-398f-a45d-1a5901e0726d | -14.18332 | -48.76244 | 2026-08-29 00:05:00 | TERRA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 19.9 |
| 72f0d1bb-545c-31e9-9f21-458d5e0b5a42 | -14.90956 | -52.62037 | 2026-08-29 00:05:00 | TERRA_M-M | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 34.3 |


[Clique aqui para ver as próximas entradas](README2.md)
