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

## Dados Diários - Página 67

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e33a09b6-f9f9-31ea-9f66-3b3b8abaa892 | -9.0762 | -47.0113 | 2025-09-05 13:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 73.6 |
| 9575daa8-ffa7-3dc0-9627-32a9908aad35 | -15.7565 | -53.6324 | 2025-09-05 13:50:00 | GOES-19 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 153.9 |
| 243d6763-4085-382e-963a-c000f4f20969 | -9.7031 | -51.0802 | 2025-09-05 13:50:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 101.1 |
| 7e0a0d03-dfe7-32f6-b344-bdb6107e83ef | -6.2609 | -43.2727 | 2025-09-05 13:50:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 87.6 |
| 8bbf0059-2bad-3b20-ab26-c48af0c47f5a | -15.2156 | -52.372 | 2025-09-05 13:50:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 80.7 |
| 1efd4613-b6d5-32da-aa37-7794042f2886 | -5.8794 | -46.0433 | 2025-09-05 13:50:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 84.3 |
| 2a49ba4e-55be-3a1f-9290-5b16fb520837 | -15.8584 | -52.3031 | 2025-09-05 13:50:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 63.0 |
| 41635f33-2613-3bac-ad6f-2c0353c00faf | -13.24 | -51.8209 | 2025-09-05 13:50:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 64.5 |
| c5438dc0-c2f4-3f75-a3e4-75ed9941727a | -14.0496 | -54.0122 | 2025-09-05 13:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 148.1 |
| 855dc8f6-a0f9-3d1d-8452-9fdb2d40b6b6 | -8.4297 | -47.5397 | 2025-09-05 13:50:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 74.7 |
| 615be654-ccec-3d49-8bb6-fc315d05ef6a | -15.7561 | -53.6535 | 2025-09-05 13:50:00 | GOES-19 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 237.6 |
| db756a3a-fa8c-344c-aae2-189a63e18d53 | -15.7186 | -53.5743 | 2025-09-05 13:50:00 | GOES-19 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 79.1 |
| 3ffdc231-e683-36fd-acc8-1ecde2d9e500 | -10.7688 | -45.2769 | 2025-09-05 13:50:00 | GOES-19 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 221.4 |
| 8486da7a-25ae-3e0a-82b3-cbfce0922697 | -7.8967 | -44.9244 | 2025-09-05 13:50:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 82.9 |
| dd67daac-ef61-33ec-b729-e6bf866c9106 | -13.3192 | -51.6626 | 2025-09-05 13:50:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 115.6 |
| 44d8b7ea-fd76-3dae-aabc-5801556a217c | -11.171 | -50.0366 | 2025-09-05 13:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 109.1 |
| 09e77ef6-b7e6-3073-82b7-637e3a3b47a0 | -7.6083 | -43.8477 | 2025-09-05 13:50:00 | GOES-19 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 76.1 |
| 9366faf1-6ab2-39f4-a1da-cfc52ade7707 | -9.0721 | -50.4181 | 2025-09-05 13:50:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 78.4 |
| 05b91387-9531-37b4-8792-9b03bbb4c736 | -5.9846 | -44.7261 | 2025-09-05 13:50:00 | GOES-19 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 121.8 |
| 52a7e247-4fc1-3748-8b86-3bc4d9986483 | -14.0691 | -53.9892 | 2025-09-05 13:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 146.4 |
| 48207fbe-5e7b-3ffa-98d8-b3d8602585b3 | -15.7558 | -53.6746 | 2025-09-05 13:50:00 | GOES-19 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 153.2 |
| 351662ff-cbae-3c6e-bb97-b5328e00a855 | -10.7688 | -45.2769 | 2025-09-05 14:00:00 | GOES-19 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 74.6 |
| 11c112d8-3367-3613-a0b6-b9df53d54c75 | -11.864 | -50.7075 | 2025-09-05 14:00:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 117.3 |
| 86d0b248-45a0-3223-90ae-b9a263696415 | -15.7558 | -53.6746 | 2025-09-05 14:00:00 | GOES-19 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 137.7 |
| ca4bd347-7ea4-3e7e-b86c-67729936a955 | -11.5961 | -52.176 | 2025-09-05 14:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 79.2 |
| 1885312e-08d4-3871-9f0b-1a60ee5861de | -5.6443 | -45.1373 | 2025-09-05 14:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 83.2 |
| 419ec7b5-8f3f-3176-b11e-98f97dc32ca4 | -11.0058 | -45.93 | 2025-09-05 14:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 111.0 |
| 270f91b2-bb7f-353d-9550-3c4472bfc5e3 | -9.4187 | -46.7967 | 2025-09-05 14:00:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 72.2 |
| b09e2136-b21b-3813-a05b-e381d534ba7d | -13.884 | -47.9929 | 2025-09-05 14:00:00 | GOES-19 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 183.3 |
| 327d463b-e68b-3f23-b739-2a0688455e46 | -6.2609 | -43.2727 | 2025-09-05 14:00:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 84.8 |
| a1415cbc-7206-3b0c-ac14-bd5fde0dfcca | -14.0691 | -53.9892 | 2025-09-05 14:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 86.5 |
| b9bb470c-367b-3b27-b4e8-828b605b5a1d | -9.7034 | -51.0591 | 2025-09-05 14:00:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 55.6 |
| c04315d8-4213-3de5-a6ba-3f0ed2d5d003 | -12.5365 | -48.0557 | 2025-09-05 14:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 57.7 |
| 036f82a3-2161-384f-82f7-68ee24b4f47c | -13.9034 | -47.9899 | 2025-09-05 14:00:00 | GOES-19 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 77.3 |
| 4376f950-150a-3624-aa4c-9deb38c58940 | -13.8849 | -47.9481 | 2025-09-05 14:00:00 | GOES-19 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 136.3 |
| 50cba25f-5a21-3c19-b4c8-b7c92ccf9b54 | -11.338 | -50.2968 | 2025-09-05 14:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 143.2 |
| 75636333-b952-31e7-a51c-0020bbacc99f | -15.7179 | -53.6165 | 2025-09-05 14:00:00 | GOES-19 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 77.8 |
| 54a20dd4-5ff2-3ba5-843f-aa71b25d3aa7 | -15.7561 | -53.6535 | 2025-09-05 14:00:00 | GOES-19 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 271.6 |
| 2b2c67a2-53d2-31b4-8db9-51f2470a1cb7 | -8.9034 | -45.7973 | 2025-09-05 14:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 86.4 |
| 6e7e934f-3099-3ffa-a0cb-71b1761b374a | -8.8851 | -45.7541 | 2025-09-05 14:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 70.3 |
| 4b9b48eb-08a7-36b0-8618-7f85a235a8ef | -15.7756 | -53.6509 | 2025-09-05 14:00:00 | GOES-19 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 142.5 |
| 5da2d2da-e5f6-39a8-897d-0a9f504608b6 | -5.7923 | -45.3078 | 2025-09-05 14:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 76.9 |
| 7193d2c4-2444-31f0-a7d2-bd4ed967cc20 | -9.0721 | -50.4181 | 2025-09-05 14:00:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 81.6 |
| ddcfde67-bd8a-39d7-9898-61ebc50431ab | -13.8836 | -48.0152 | 2025-09-05 14:00:00 | GOES-19 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 109.1 |
| 5b2eb684-3bbf-3c40-8114-b371a7b8c61e | -8.479 | -45.0704 | 2025-09-05 14:00:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 139.9 |
| 9b70d275-2fb6-3931-8441-7651a79c84d7 | -14.7465 | -47.4955 | 2025-09-05 14:00:00 | GOES-19 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 118.9 |
| 01dbf65f-2d46-3579-9d83-de74bfccc62c | -8.3364 | -47.4824 | 2025-09-05 14:00:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 89.0 |
| 1783d7e4-5191-3edb-8272-f3d7cdd90e91 | -9.0719 | -50.4394 | 2025-09-05 14:00:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 76.6 |
| 600dd1c0-000d-3a24-bfdb-749bcb0301fa | -5.55 | -43.0719 | 2025-09-05 14:00:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 72.3 |
| a05f8588-9aa3-34a5-9812-4448640bd46d | -15.7182 | -53.5954 | 2025-09-05 14:00:00 | GOES-19 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 163.6 |
| 37a485f6-2a18-3bfc-9494-99637e0081b2 | -14.1447 | -51.7062 | 2025-09-05 14:00:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 91.3 |
| 16fec544-fc32-3872-85a1-91e3f994d98c | -8.3456 | -48.3133 | 2025-09-05 14:00:00 | GOES-19 | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Cerrado | 73.8 |
| bfc3f6cf-8c6b-3653-a1dd-782834025fd7 | -7.8923 | -45.2893 | 2025-09-05 14:00:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 80.4 |
| 4bfca601-f602-3ff2-9906-1f157cd656b5 | -15.3435 | -53.9382 | 2025-09-05 14:00:00 | GOES-19 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 170.0 |
| d308b152-4e78-39b9-b2c4-831bb617d1a6 | -8.5187 | -51.3293 | 2025-09-05 14:00:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 64.8 |
| 455a133f-5b25-37d8-bad4-4337e4035a2e | -7.358 | -44.3344 | 2025-09-05 14:00:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 71.4 |
| 014af051-cedf-33b0-b11f-a436679c0f7e | -6.1493 | -43.165 | 2025-09-05 14:00:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 67.2 |
| 5acdcd74-a706-3278-8a83-e531a62af370 | -6.2484 | -42.6394 | 2025-09-05 14:00:00 | GOES-19 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 67.9 |
| 7dd5f6a0-91a0-3f2b-ad46-91f8e597150d | -14.0499 | -53.9914 | 2025-09-05 14:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 143.7 |
| 111595a9-7734-3a56-85ea-37e48458c845 | -16.3149 | -52.9415 | 2025-09-05 14:00:00 | GOES-19 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 89.6 |
| 6781ef04-a446-38fc-bfb7-1c788ca6b317 | -13.8655 | -47.951 | 2025-09-05 14:00:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 63.2 |
| 481720d6-4c79-3f19-8496-b875d1333b99 | -9.6916 | -48.9872 | 2025-09-05 14:00:00 | GOES-19 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 75.0 |
| 3a478851-f21f-319e-bd84-55ff66f7a199 | -11.3383 | -50.2753 | 2025-09-05 14:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 112.3 |
| fe08e7d2-e54a-3a88-bc22-8f3a846c800e | -6.2606 | -43.2961 | 2025-09-05 14:00:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 63.1 |
| 74863488-1b36-3a96-a3bd-95e550ef9ffa | -15.2156 | -52.372 | 2025-09-05 14:00:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 92.8 |
| eef794f2-f2d3-3212-a372-5b5d84f75ab8 | -14.0496 | -54.0122 | 2025-09-05 14:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 154.2 |
| 8a5fd337-e8cd-3e5f-8dc9-527ab71388bc | -8.0414 | -45.4109 | 2025-09-05 14:00:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 101.2 |
| e5aceb1b-fcd3-3dab-8048-44c9c020d38e | -10.2373 | -50.5417 | 2025-09-05 14:00:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 89.2 |
| c77464df-f29b-331b-baed-f8b50a44d357 | -10.7682 | -47.7523 | 2025-09-05 14:00:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 72.0 |
| 9cd0caf0-e4a7-32dc-8d77-7961313b9772 | -6.9568 | -44.9434 | 2025-09-05 14:00:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 61.3 |
| 95c97fea-44a9-3bd2-8136-b03266ebe7a4 | -9.7105 | -48.9853 | 2025-09-05 14:00:00 | GOES-19 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 73.7 |
| 3f3f7a76-8dbd-3dc6-b8b8-9b7e2d01b935 | -9.0762 | -47.0113 | 2025-09-05 14:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 111.2 |
| 84404d3d-f47a-3fe8-a50a-bab712c3a528 | -8.885 | -47.2304 | 2025-09-05 14:00:00 | GOES-19 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 79.1 |
| b2374c7f-0545-345d-9f8d-4986bec382dc | -6.2421 | -43.2743 | 2025-09-05 14:00:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 81.2 |
| 26518656-4564-374a-bfc2-484faad31e21 | -15.7565 | -53.6324 | 2025-09-05 14:00:00 | GOES-19 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 217.8 |
| 64d1f4f2-44ad-37b7-a886-292890df3d23 | -8.0226 | -45.4127 | 2025-09-05 14:00:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 127.5 |
| 2b3098a4-99e2-313a-965f-f6d86159edb8 | -5.5884 | -45.1185 | 2025-09-05 14:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 414.2 |
| c03f97ee-6284-3875-bc5b-c84e4d09e9ee | -7.0314 | -43.2742 | 2025-09-05 14:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 74.5 |
| 1f1d2df1-8f8b-374f-8834-b8110408c043 | -11.0055 | -45.9527 | 2025-09-05 14:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 110.8 |
| baaf2fb9-be5a-3b3e-a9d3-febbe3ea20a2 | -6.2296 | -42.641 | 2025-09-05 14:00:00 | GOES-19 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 66.6 |
| d1ad8386-caf7-361d-8c0c-36a2b0555fd1 | -5.8794 | -46.0433 | 2025-09-05 14:00:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 77.0 |
| 25c0c048-939d-3d84-9611-2365330b1648 | -15.235 | -52.3693 | 2025-09-05 14:00:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 81.5 |
| 3d795bd5-420d-325e-992c-a5f989b3f4b8 | -8.3458 | -48.2916 | 2025-09-05 14:00:00 | GOES-19 | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Cerrado | 94.5 |
| 6aee0312-df46-3e3b-ab7a-e5bbbbb50e57 | -9.7031 | -51.0802 | 2025-09-05 14:00:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 126.1 |
| 70dc006b-c3d9-34e2-bbd2-7ab468132481 | -13.8651 | -47.9734 | 2025-09-05 14:00:00 | GOES-19 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 111.8 |
| 2f0f8ce7-f26c-3066-874c-eab81d5291f2 | -5.9844 | -44.7489 | 2025-09-05 14:00:00 | GOES-19 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 97.9 |
| d3ddda6f-517f-3bb3-a37c-718c78d77cb2 | -14.5597 | -48.0879 | 2025-09-05 14:00:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 50.0 |
| dd29e05d-d1ef-36f6-81b6-bb07e71b65a5 | -8.9037 | -45.7747 | 2025-09-05 14:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 74.6 |
| 879a42f1-0b31-3664-80fd-d1030721551e | -5.9846 | -44.7261 | 2025-09-05 14:00:00 | GOES-19 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 101.4 |
| d54470cf-f209-383a-947b-a03ad1e1b416 | -7.358 | -44.3344 | 2025-09-05 14:10:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 67.1 |
| b0a7b7af-da2c-30c9-a176-24d1e4a91092 | -7.7128 | -61.5276 | 2025-09-05 14:10:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 70.9 |
| 923838ff-39ca-3915-a8a0-6d31e0a657b4 | -11.5961 | -52.176 | 2025-09-05 14:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 85.9 |
| cdeced2b-7f2e-39b9-a376-97c60a6720bd | -15.3435 | -53.9382 | 2025-09-05 14:10:00 | GOES-19 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 179.7 |
| 08d5fdd8-6f0a-3dc9-ae9b-0629c217549c | -11.1714 | -50.0151 | 2025-09-05 14:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 105.7 |
| a166733b-4483-3b7f-8ac7-7fec149c8603 | -10.1494 | -45.9936 | 2025-09-05 14:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 67.0 |
| dcaf7fa6-0786-34ff-821e-42f6be4c977c | -6.2299 | -42.6173 | 2025-09-05 14:10:00 | GOES-19 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 89.3 |
| c15ac544-f99c-37fa-9779-c5e24921596f | -8.9034 | -45.7973 | 2025-09-05 14:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 118.6 |
| 16e23dc7-b7e2-3079-b8d6-4f4a158853a7 | -10.1301 | -46.0185 | 2025-09-05 14:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 102.3 |
| 714a4608-88f8-33f5-a7f2-7ec3c1fe4694 | -11.0058 | -45.93 | 2025-09-05 14:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 89.9 |
| 0f2f13f8-8e02-3db3-9285-1e65c8150537 | -6.2038 | -43.3475 | 2025-09-05 14:10:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 69.9 |


[Clique aqui para ver as próximas entradas](README68.md)
