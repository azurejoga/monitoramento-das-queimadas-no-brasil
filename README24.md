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

## Dados Diários - Página 24

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0a700f2d-2ffc-39a0-b06d-a73d95c985cd | -6.1477 | -57.702 | 2026-08-10 14:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 64.6 |
| 79be96a7-9730-366b-9fa9-5b531eae7702 | -7.5488 | -55.5629 | 2026-08-10 14:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 138.1 |
| 0b36cc2d-6e27-3234-961f-1ac146cc08cf | -7.3892 | -59.9731 | 2026-08-10 14:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 55.3 |
| 080aa707-72c0-3dcd-bab1-f3149975d7b0 | -10.2468 | -45.823 | 2026-08-10 14:20:00 | GOES-19 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 71.4 |
| dc529e22-7506-3adc-92af-8d7d37aa1c6d | -10.2655 | -45.8434 | 2026-08-10 14:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 131.2 |
| 93a503de-7e88-3061-8718-2114fc583d92 | -6.1292 | -57.7223 | 2026-08-10 14:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 71.9 |
| 169fe4fe-068f-30b8-a55c-f7147b1e608b | -13.8614 | -53.7636 | 2026-08-10 14:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 132.2 |
| f851ae0c-b65b-3054-8041-2b5adeb4194f | -11.4671 | -50.5604 | 2026-08-10 14:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 75.2 |
| ec9af73f-3e25-323b-97a2-c1e1dac17676 | -13.6481 | -46.2229 | 2026-08-10 14:20:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 353.1 |
| b90be035-a502-3c42-a5e8-7b21119e60ed | -8.3117 | -46.3976 | 2026-08-10 14:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 79.5 |
| 3f2a8ce0-a3e6-32bb-a5c2-739b0bb8edbf | -7.6216 | -42.7449 | 2026-08-10 14:20:00 | GOES-19 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 88.3 |
| 37a65eff-4ed1-3b3c-a11d-e67296043942 | -7.5487 | -55.5829 | 2026-08-10 14:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 115.3 |
| 4ea93fa2-6c1f-3fc3-ab20-03cc6ab1ea8a | -7.3891 | -59.9924 | 2026-08-10 14:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 64.8 |
| c6d71317-277b-3be9-8821-34ee5ac8b8d5 | -6.1476 | -57.7215 | 2026-08-10 14:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 123.8 |
| d0c2d6e5-2eff-39af-b686-f1b14b7d6bf7 | -7.6025 | -42.7705 | 2026-08-10 14:20:00 | GOES-19 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 126.4 |
| 01368efb-7a77-332f-9b62-028987f018b8 | -10.8407 | -46.7414 | 2026-08-10 14:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 199.1 |
| baad33bb-fc6e-3f61-8c79-8b18bdaa1905 | -13.8015 | -53.9161 | 2026-08-10 14:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 75.3 |
| 88a9a0fc-5d9e-347c-baa9-7967a61bf717 | -7.5487 | -55.5829 | 2026-08-10 14:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 104.1 |
| d0506f15-2327-31cd-85ab-fc9cf4ff1546 | -7.5674 | -55.5619 | 2026-08-10 14:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 73.4 |
| 3cb3c4c8-7e9e-3c0e-b22a-0812a2171fa8 | -8.3117 | -46.3976 | 2026-08-10 14:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 97.5 |
| 2bd25638-6576-3ed8-a22d-1ecce90241ea | -7.6214 | -42.7685 | 2026-08-10 14:30:00 | GOES-19 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 153.1 |
| 452a8fc7-28c1-36fa-a453-587912213f3c | -7.3891 | -59.9924 | 2026-08-10 14:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 70.7 |
| 50bb2082-aee4-32f3-9fe5-9930ce42715b | -16.4986 | -54.6673 | 2026-08-10 14:30:00 | GOES-19 | RONDONÓPOLIS | MATO GROSSO | Brasil | 5107602 | 51 | 33 | nan | nan | nan | Cerrado | 63.6 |
| 4c21a4e9-e7ea-3f47-9cae-f5cba3906eb1 | -14.2872 | -45.3069 | 2026-08-10 14:30:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 132.5 |
| 6f4067b3-dcee-3b94-a8fc-af31716d6ad0 | -7.6025 | -42.7705 | 2026-08-10 14:30:00 | GOES-19 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 134.2 |
| 26bc94e3-0101-3f55-9293-48207f3eac2d | -13.6481 | -46.2229 | 2026-08-10 14:30:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 799.1 |
| 4a273d54-300e-3b41-9322-b0765eeb5e75 | -10.9213 | -50.2785 | 2026-08-10 14:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 97.5 |
| 738fa1c5-40d8-3da4-ba37-abcfe2518637 | -10.2655 | -45.8434 | 2026-08-10 14:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 223.4 |
| 090ccf77-198a-3bfa-a6c1-cd0eb91b93bd | -10.8407 | -46.7414 | 2026-08-10 14:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 100.5 |
| 97869925-f605-3feb-84db-6f66f38282c6 | -10.2659 | -45.8206 | 2026-08-10 14:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 187.5 |
| 2c502543-022d-3b92-9d9d-b81af9837d7e | -13.863 | -53.6593 | 2026-08-10 14:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 84.3 |
| 015bba35-ba2c-3d97-8244-08a92eb65e4a | -10.2468 | -45.823 | 2026-08-10 14:30:00 | GOES-19 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 134.3 |
| 52b11b82-8e0b-3677-af34-2cd4e398bbe4 | -10.2455 | -45.9139 | 2026-08-10 14:30:00 | GOES-19 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 425.6 |
| 76f5e440-b8d4-3c7a-a18b-fcd90d2c72d7 | -11.9748 | -47.3315 | 2026-08-10 14:30:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 70.5 |
| 0647198c-4d08-391d-9d1d-7d28635681ec | -7.5488 | -55.5629 | 2026-08-10 14:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 153.9 |
| 8c67f332-c4d0-3ae2-bcb4-0a9957de3571 | -7.6216 | -42.7449 | 2026-08-10 14:30:00 | GOES-19 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 87.1 |
| d3c642a1-4db4-3925-862b-cd648ff16f9e | -10.921 | -50.2999 | 2026-08-10 14:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 157.2 |
| 6cc24394-5115-3490-bde8-c8c8cf555fab | -13.6287 | -46.226 | 2026-08-10 14:30:00 | GOES-19 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1103.4 |
| 65199cdc-a83f-369b-9406-58389efd1c87 | -10.2655 | -45.8434 | 2026-08-10 14:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 122.3 |
| 0d676ed7-f0e5-350b-8005-d5cd5a852944 | -11.9748 | -47.3315 | 2026-08-10 14:40:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 82.8 |
| 2673bf25-4888-37e0-9fd0-75b9644ff5fa | -11.4674 | -50.539 | 2026-08-10 14:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 71.2 |
| 02ff6137-af7e-3649-9262-2fdf8c20592f | -10.921 | -50.2999 | 2026-08-10 14:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 108.1 |
| b22a8834-6f55-386a-a791-15abb7d7fb03 | -14.2872 | -45.3069 | 2026-08-10 14:40:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 97.3 |
| a06c8b20-f52e-3e12-8db5-6b571307e5cd | -15.0743 | -52.6884 | 2026-08-10 14:40:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 103.3 |
| b5cabafb-830a-3a6f-a8c7-7cc3739c3640 | -11.4671 | -50.5604 | 2026-08-10 14:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 78.1 |
| 05c2ebf8-d04f-3031-9cde-233994dd0699 | -15.1326 | -52.6806 | 2026-08-10 14:40:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 106.7 |
| 87f71e16-1d24-30d6-aecf-87b80911dc36 | -7.6214 | -42.7685 | 2026-08-10 14:40:00 | GOES-19 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 251.3 |
| 4d1a6e05-7a68-3196-a0b0-71bfcb943330 | -8.3117 | -46.3976 | 2026-08-10 14:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 81.2 |
| 3d983191-580e-3b71-8522-39cc9a33e175 | -7.5488 | -55.5629 | 2026-08-10 14:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 219.0 |
| 48b5d47f-660d-3ad1-80f6-b614cb4238d5 | -13.4816 | -43.0426 | 2026-08-10 14:40:00 | GOES-19 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 191.0 |
| c9f32cc6-9926-30a6-8f8a-77ff112ea9a0 | -7.6216 | -42.7449 | 2026-08-10 14:40:00 | GOES-19 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 130.1 |
| fed5fe8a-5cfd-3246-9d2a-6c7628811cf6 | -13.6287 | -46.226 | 2026-08-10 14:40:00 | GOES-19 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 557.9 |
| 932fc225-3d71-3814-9fe7-587d2cdf8cbb | -10.8407 | -46.7414 | 2026-08-10 14:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 89.9 |
| 66d2e55b-5632-371e-97bb-a50f283e9df8 | -11.9557 | -47.3341 | 2026-08-10 14:40:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 57.3 |
| 482c03d6-2c2d-37c6-8485-726aad53fbed | -10.2455 | -45.9139 | 2026-08-10 14:40:00 | GOES-19 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 372.5 |
| 5af3a6ff-ba2a-3dce-bb42-273d7bee3a2c | -7.6025 | -42.7705 | 2026-08-10 14:40:00 | GOES-19 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 165.7 |
| 2c4127cb-4733-32a8-b435-07a77c9653cd | -13.8614 | -53.7636 | 2026-08-10 14:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 88.8 |
| 337f8fa2-18a7-37c4-b43f-e8d7bbd4cd87 | -6.8388 | -56.4146 | 2026-08-10 14:40:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 58.4 |


