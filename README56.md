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

## Dados Diários - Página 56

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0766c58a-6e34-32c7-9eaa-5d17c1c1a3c0 | -4.2563 | -43.4368 | 2024-10-31 13:55:30 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 146.8 |
| d9da6c97-c6a8-32b8-9d79-1fcbfce39b7e | -4.8432 | -42.4634 | 2024-10-31 13:55:33 | GOES-16 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 160.4 |
| 6b458cdc-f34a-370e-b2ab-1ee996448fdc | -4.957 | -42.29 | 2024-10-31 13:55:34 | GOES-16 | COIVARAS | PIAUÍ | Brasil | 2202737 | 22 | 33 | nan | nan | nan | Caatinga | 92.7 |
| 710f5e71-b1a4-3b02-ae35-8d07e0fe8949 | -4.9757 | -42.2887 | 2024-10-31 13:55:34 | GOES-16 | COIVARAS | PIAUÍ | Brasil | 2202737 | 22 | 33 | nan | nan | nan | Caatinga | 98.2 |
| a5249a5d-fbc4-3854-b5fa-fb6690a21d56 | -6.2401 | -41.6153 | 2024-10-31 13:55:41 | GOES-16 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 280.4 |
| 6c34a1fa-a6b6-3cc4-9f36-fcae03fcc2fb | -6.2404 | -41.5912 | 2024-10-31 13:55:41 | GOES-16 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 128.4 |
| 7912fee7-fe9c-385f-85c0-1202a44b0358 | -6.2592 | -41.5895 | 2024-10-31 13:55:41 | GOES-16 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 130.5 |
| 73c9e0ab-33dd-35e2-a65a-1e92f9c44730 | -14.9598 | -59.003 | 2024-10-31 13:56:31 | GOES-16 | VALE DE SÃO DOMINGOS | MATO GROSSO | Brasil | 5108352 | 51 | 33 | nan | nan | nan | Cerrado | 75.2 |
| 7cdb63ea-236d-3b59-aa66-f45f6aaa86ce | -17.2737 | -57.488 | 2024-10-31 13:56:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 98.6 |
| 2a200f6d-97c3-3e25-9269-efcc5d3b78b7 | -17.2733 | -57.5085 | 2024-10-31 13:56:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 130.1 |
| 6dcd1c67-bb32-3eb2-aec2-6d0a1ffe6f72 | -17.6467 | -57.5051 | 2024-10-31 13:56:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 91.5 |
| 4ab1ad66-fb90-3959-aa14-ef6e33ede1f4 | -17.647 | -57.4846 | 2024-10-31 13:56:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 230.2 |
| 88f3c3b5-969c-386c-a8b3-ee35a819f581 | -17.6664 | -57.5028 | 2024-10-31 13:56:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 152.9 |
| c09c7ae6-26c2-38d1-8684-4e887a7cea41 | -17.6667 | -57.4822 | 2024-10-31 13:56:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 351.2 |
| de190d67-d2e6-32f3-8e4e-fbb02d3d6b45 | -17.8403 | -57.7076 | 2024-10-31 13:56:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 88.7 |
| a4d088fd-19fb-344b-8390-d891464d9f34 | -18.0455 | -57.2299 | 2024-10-31 13:56:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 86.0 |
| af5f9090-1a1e-3e56-891a-bccb681d1f06 | -18.0653 | -57.2274 | 2024-10-31 13:56:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 129.3 |
| 4efb99a8-ede7-3052-ad78-48529c2d177a | -18.2458 | -55.9583 | 2024-10-31 13:56:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 70.9 |
| ddfa56a5-ac5f-3bba-bc60-164a5c9630c9 | -18.2956 | -56.4935 | 2024-10-31 13:56:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 72.6 |
| 9dd6bdde-3135-3832-b33d-4fe633144073 | -18.6138 | -57.5711 | 2024-10-31 13:56:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 94.4 |
| 9aaf7b81-65f1-3693-8b4f-716274825658 | -23.2054 | -54.5965 | 2024-10-31 13:57:14 | GOES-16 | IGUATEMI | MATO GROSSO DO SUL | Brasil | 5004304 | 50 | 33 | nan | nan | nan | Mata Atlântica | 116.9 |
| 34e75198-811c-311c-935b-8dc1e2396e00 | -23.9923 | -54.1106 | 2024-10-31 13:57:18 | GOES-16 | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 91.2 |
| 2933361a-4860-3ded-82c4-484358d6b3c8 | -23.9929 | -54.0882 | 2024-10-31 13:57:18 | GOES-16 | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 120.1 |


