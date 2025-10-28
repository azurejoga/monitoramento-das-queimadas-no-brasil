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

## Dados Diários - Página 95

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c7379d46-9a0d-37f6-9b92-fe56724eb1b6 | -7.9459 | -45.5335 | 2025-10-28 14:40:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 51.6 |
| b563ce0a-4be6-3bfe-b0f3-a21365bf4fdd | -3.8973 | -44.1255 | 2025-10-28 14:40:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 77.5 |
| 8c6d7294-2292-3a19-b9ba-45e6d1367439 | -9.0582 | -46.9465 | 2025-10-28 14:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 179.5 |
| ea03f176-b78b-3d32-b762-7f1653f8bf93 | -13.9469 | -47.7371 | 2025-10-28 14:40:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 66.9 |
| d92dcfdc-0b75-3f1b-8a5f-7db8240c5c19 | -9.5487 | -46.9608 | 2025-10-28 14:40:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 108.6 |
| e61b3f19-4644-3d25-9d7d-48c1c826b666 | -6.0786 | -44.6733 | 2025-10-28 14:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 110.8 |
| d47f65ce-fc1a-327c-bc41-3019b52d4620 | -6.4678 | -45.0981 | 2025-10-28 14:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 41.5 |
| 76b9aab7-e2c3-37db-9715-0790ddb8ce73 | -3.5834 | -43.5877 | 2025-10-28 14:40:00 | GOES-19 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 77.4 |
| 2f77133e-1ef4-333f-9d08-b36d2edefdd7 | -7.6673 | -46.9028 | 2025-10-28 14:40:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 84.1 |
| e1743c19-424c-39cc-9a31-db90d6d5285a | -10.9605 | -47.5962 | 2025-10-28 14:40:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 133.3 |
| 70fce332-cdf9-3128-8ac9-9e058e33af2e | -7.9693 | -46.7423 | 2025-10-28 14:40:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 88.5 |
| f3ca3bd7-fdfa-37e0-a21d-3af1ec309a42 | -9.5301 | -46.9405 | 2025-10-28 14:40:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 124.8 |
| 186f28d8-2ef5-3aa1-89e1-cbc67bc1b1ef | -6.8822 | -44.9043 | 2025-10-28 14:40:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 51.8 |
| bd440c1e-0fe2-34a0-a9ff-7bb6bd3f294b | -8.679 | -47.1403 | 2025-10-28 14:40:00 | GOES-19 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 68.0 |
| 558edc96-c2e2-39ea-83e7-4d60533eac19 | -10.9415 | -47.5985 | 2025-10-28 14:40:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 106.3 |
| b02387f8-4246-3db9-ab78-0b32d7f3e715 | -14.4289 | -47.8401 | 2025-10-28 14:40:00 | GOES-19 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 80.4 |
| b7102004-afeb-3917-9977-b57bf6c3eeac | -7.0628 | -43.8305 | 2025-10-28 14:40:00 | GOES-19 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 46.2 |
| 2f2ba21f-8ad0-3fad-a511-52417d535cc0 | -3.6975 | -43.2106 | 2025-10-28 14:40:00 | GOES-19 | MATA ROMA | MARANHÃO | Brasil | 2106409 | 21 | 33 | nan | nan | nan | Cerrado | 80.1 |
| f669ba58-c277-3c07-9d43-93fa572f7c58 | 2.6724 | -60.1643 | 2025-10-28 14:40:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 77.8 |
| 1ed501c0-e50c-3c59-9c89-32db3f6ab607 | -10.0191 | -47.1305 | 2025-10-28 14:40:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 110.4 |
| bbd4f4db-9ea4-336e-aed8-808cd7a8391b | -14.9037 | -52.4779 | 2025-10-28 14:40:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 90.8 |
| 82917b80-844d-3050-aa04-d5a7bda18d05 | -4.8951 | -43.001 | 2025-10-28 14:40:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 74.0 |
| ea48eeef-6ab0-34be-88a1-90efbb18419b | -9.5295 | -46.9851 | 2025-10-28 14:40:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 409.5 |
| 6a84cd2a-9ce6-3e79-b348-bbf388c70d08 | -8.4962 | -48.2778 | 2025-10-28 14:40:00 | GOES-19 | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 346.2 |
| 11eb117e-ac63-3979-90c9-f4f7d219e8ff | -6.1653 | -41.5739 | 2025-10-28 14:40:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 53.3 |
| 8edeff37-9fd1-3646-b747-356ebbe7dc4a | -7.9696 | -46.7201 | 2025-10-28 14:40:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 65.7 |
| d419c668-3c89-3d52-b9b9-4947a2a8751a | -7.9072 | -47.2573 | 2025-10-28 14:40:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 105.4 |
| e2a669b0-5689-3659-b8bf-b5efc16197d4 | -9.8814 | -44.8862 | 2025-10-28 14:40:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 144.3 |
| 19b7f599-0f55-35ae-8751-78cd872b1f3d | -4.4604 | -43.6337 | 2025-10-28 14:40:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 77.8 |
| 0b1c4f52-36e8-3fca-92ab-25858400b335 | -4.1846 | -42.9745 | 2025-10-28 14:40:00 | GOES-19 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 81.6 |
| 2a592f9e-3067-3a7b-8c5e-d13701f469ad | -7.4583 | -47.1641 | 2025-10-28 14:40:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 115.4 |


