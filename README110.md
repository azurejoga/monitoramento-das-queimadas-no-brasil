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

## Dados Diários - Página 110

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 10986b53-09eb-3bbf-b595-27be7a87ca2b | -6.3723 | -41.5793 | 2024-10-29 14:15:42 | GOES-16 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 133.8 |
| 6fa2ec2f-a318-3a88-a9d0-a0814172420d | -6.3534 | -41.581 | 2024-10-29 14:15:42 | GOES-16 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 544.2 |
| 50c49c36-e36c-3ed6-a0eb-2eaebd3d105c | -6.6781 | -44.6935 | 2024-10-29 14:15:44 | GOES-16 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 68.5 |
| 8ca966d5-e83c-3470-9ed0-7287fe1520eb | -7.0157 | -41.3481 | 2024-10-29 14:15:45 | GOES-16 | SUSSUAPARA | PIAUÍ | Brasil | 2210938 | 22 | 33 | nan | nan | nan | Caatinga | 133.7 |
| f77c750e-57df-39c5-88f3-f69a3b659c77 | -6.8482 | -42.8215 | 2024-10-29 14:15:45 | GOES-16 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 110.3 |
| d6ed72ca-51e7-3cf6-88c0-94be996b6a09 | -6.8485 | -42.7979 | 2024-10-29 14:15:45 | GOES-16 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 92.5 |
| 7f2b85b7-f7db-3411-b444-1def5d07029e | -6.9971 | -41.3258 | 2024-10-29 14:15:45 | GOES-16 | BOCAINA | PIAUÍ | Brasil | 2201804 | 22 | 33 | nan | nan | nan | Caatinga | 138.0 |
| 01533cbc-e564-3e51-abee-3417fe594661 | -6.9968 | -41.35 | 2024-10-29 14:15:45 | GOES-16 | SUSSUAPARA | PIAUÍ | Brasil | 2210938 | 22 | 33 | nan | nan | nan | Caatinga | 125.5 |
| 6be43ba7-a963-3145-a85c-9cf7cd569a57 | -7.3964 | -44.2617 | 2024-10-29 14:15:48 | GOES-16 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 101.8 |
| 25b52b86-0fdf-3920-b7d8-28dd8192a812 | -7.8833 | -42.9534 | 2024-10-29 14:15:50 | GOES-16 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 364.9 |
| f3f1c0ac-12ec-3ddb-9137-0719f21ad604 | -7.9628 | -45.6901 | 2024-10-29 14:15:51 | GOES-16 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 52.8 |
| 4d1e3532-4fe7-3e8f-98b3-c7163ae7b10b | -8.8007 | -40.9711 | 2024-10-29 14:15:55 | GOES-16 | AFRÂNIO | PERNAMBUCO | Brasil | 2600203 | 26 | 33 | nan | nan | nan | Caatinga | 89.4 |
| 3e4d3642-f8d1-3bd5-955d-aa6095b13279 | -8.8468 | -44.3871 | 2024-10-29 14:15:56 | GOES-16 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 58.2 |
| ce234eae-ca96-3fbf-b2ed-733d9893319a | -12.3526 | -49.9184 | 2024-10-29 14:16:16 | GOES-16 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 98.6 |
| 6bb054e6-2d7f-3666-a51d-31b45ec492a7 | -12.6953 | -48.8503 | 2024-10-29 14:16:18 | GOES-16 | TALISMÃ | TOCANTINS | Brasil | 1720978 | 17 | 33 | nan | nan | nan | Cerrado | 98.6 |
| 447f3fd4-90be-365c-a42d-8e8547984717 | -13.4769 | -43.2593 | 2024-10-29 14:16:21 | GOES-16 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 114.3 |
| 36b51546-da3b-3de4-a3d6-ca93d2226c17 | -13.4774 | -43.2352 | 2024-10-29 14:16:21 | GOES-16 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 104.8 |
| 582fcfed-290b-3ecd-b690-dc0c889b7cc4 | -13.6139 | -42.3166 | 2024-10-29 14:16:22 | GOES-16 | CAETITÉ | BAHIA | Brasil | 2905206 | 29 | 33 | nan | nan | nan | Caatinga | 96.4 |
| 13f788d7-3426-3077-8311-aaeaa9c5b571 | -13.908 | -43.9665 | 2024-10-29 14:16:24 | GOES-16 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 100.1 |
| 0d35afe9-de60-3236-8ce8-6fdb14982af5 | -19.5465 | -56.6983 | 2024-10-29 14:16:55 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 68.8 |
| ce7bb354-3de2-347e-b424-1b0ae6034a73 | -22.7959 | -53.5071 | 2024-10-29 14:17:12 | GOES-16 | TAQUARUSSU | MATO GROSSO DO SUL | Brasil | 5007976 | 50 | 33 | nan | nan | nan | Mata Atlântica | 102.9 |
| 5729a85a-0c0e-39a2-b321-7d9448d3ef64 | -24.0134 | -54.1063 | 2024-10-29 14:17:18 | GOES-16 | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 70.0 |


