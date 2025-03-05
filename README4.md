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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 500dc3fd-31ad-345a-a8ef-bd03e42113b5 | 2.35738 | -61.05108 | 2025-03-05 04:55:00 | NOAA-21 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 933b65ec-0d08-30ce-93b7-2621670ca58a | 2.77359 | -60.88758 | 2025-03-05 04:55:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 3.6 |
| cfeb5446-5be2-35f2-ba09-87ed7af9f065 | 2.26771 | -60.25924 | 2025-03-05 04:55:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 3a9faccf-7d7e-34ce-a662-120802f29171 | 1.13006 | -60.50876 | 2025-03-05 04:55:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 9a770ad3-7b51-35cb-8cd5-6e1318a4d417 | 2.77311 | -60.88445 | 2025-03-05 04:55:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 07dca6bd-1415-3bbd-8691-906395fdc968 | 3.23507 | -61.20572 | 2025-03-05 04:55:00 | NOAA-21 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6cd2daf3-4ffb-3f9b-a05c-97465bae03a1 | 1.12744 | -60.513 | 2025-03-05 04:55:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 4.1 |
| b04a002c-a723-3a6d-b854-dc982ae3cf82 | 1.12514 | -60.50952 | 2025-03-05 04:55:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 5a79670a-4097-3923-98fc-ce9473f9bbca | 2.37181 | -60.23472 | 2025-03-05 04:55:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2156002b-0873-306f-8853-da268213cec4 | 3.34332 | -61.24863 | 2025-03-05 04:55:00 | NOAA-21 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3b0319db-8f66-3d7d-8853-e932d35005db | 1.9521 | -60.37587 | 2025-03-05 04:55:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f024c352-2eec-3d9f-8fed-45db1f737f1d | 2.62525 | -60.41485 | 2025-03-05 04:55:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 567caa14-d96f-3d73-9396-b6c7b98eae7c | 3.31107 | -61.21526 | 2025-03-05 04:55:00 | NOAA-21 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9bdeff90-0a82-3cdf-a171-28a1292a2646 | 0.83844 | -59.96906 | 2025-03-05 04:55:00 | NOAA-21 | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 30e165f0-c81b-307b-ba6a-81370c316601 | 1.13499 | -60.50802 | 2025-03-05 04:55:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 5.8 |
| e2a5cb12-74bc-3746-aa97-474aee9474a7 | 1.27622 | -60.09679 | 2025-03-05 04:55:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 16f07bd0-e28e-3f5e-900a-bd4f8ce55c7b | 2.62529 | -60.41479 | 2025-03-05 04:55:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 34e057a6-4586-3f70-a149-563663d89738 | 2.34977 | -61.0007 | 2025-03-05 04:55:00 | NOAA-21 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d0019144-bf68-30d4-8ae5-0bee3ae5d17f | 0.41607 | -60.50117 | 2025-03-05 04:55:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e51bbda9-b6ff-3ac6-867f-87490c3e9606 | 2.77453 | -60.89383 | 2025-03-05 04:55:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 3d5c2961-4e86-3d08-a7f5-2dbc57ae898b | 2.35691 | -61.04793 | 2025-03-05 04:55:00 | NOAA-21 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7e304b98-8758-33d0-80d8-898b72e4190a | 1.13094 | -60.51432 | 2025-03-05 04:55:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 4b2b7ba3-6593-3653-ac2d-d26519ab4cbd | 1.85548 | -60.58219 | 2025-03-05 04:55:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 0.4 |
| e77c862c-6729-3216-8cac-a485c907418b | 1.94221 | -60.37736 | 2025-03-05 04:55:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a2109d51-09c5-3bf1-9bdc-be76b635ea4a | 2.3511 | -61.00951 | 2025-03-05 04:55:00 | NOAA-21 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 7429da14-4b84-3143-95af-2df13531c03e | 3.31056 | -61.21175 | 2025-03-05 04:55:00 | NOAA-21 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8b665640-3dfd-322e-b574-28682f11241f | 2.43518 | -60.2757 | 2025-03-05 04:55:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7dfe597d-d6da-3ca3-8328-1da79d6e4d61 | 1.13237 | -60.51225 | 2025-03-05 04:55:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 135203a7-ee44-35d1-86c8-8395c6aab523 | 1.94716 | -60.37663 | 2025-03-05 04:55:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5241a26b-b96d-30df-bf9c-e180a6404276 | 2.77406 | -60.89071 | 2025-03-05 04:55:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 8ddf9aac-491a-3916-b62d-cefddbcfd7a9 | 2.86018 | -60.74771 | 2025-03-05 04:55:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 3.1 |
| b26d1fea-0758-381a-aa74-e6d990c09afd | 2.10164 | -60.23985 | 2025-03-05 04:55:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 47681222-715b-3c40-9c03-0032050869ca | 1.12601 | -60.51506 | 2025-03-05 04:55:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 5.8 |
| a3d29ead-f08b-3200-a711-cea583bab922 | 1.13587 | -60.51357 | 2025-03-05 04:55:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 3.6 |
| d93c7ae4-609c-338b-b156-5862774f85e1 | 1.12661 | -60.50746 | 2025-03-05 04:55:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 9f8fcd43-df4e-34d4-8a61-5d07fce364b3 | 2.35588 | -61.00594 | 2025-03-05 04:55:00 | NOAA-21 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 4.8 |
| dd032c2a-ddc2-3ca5-97d5-e12fe5ef4fb5 | 2.28237 | -61.23014 | 2025-03-05 04:55:00 | NOAA-21 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d4f326c2-0c7c-31dd-8242-f82a6475cdc4 | 2.35544 | -61.00306 | 2025-03-05 04:55:00 | NOAA-21 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 65039831-2901-3c4e-a0a6-8e37d4ec41c7 | 3.23457 | -61.20235 | 2025-03-05 04:55:00 | NOAA-21 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 28f8a0a9-4a1e-31e5-a71e-80cf775a21e4 | 0.9754 | -60.37133 | 2025-03-05 04:55:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e62ae9ba-35d0-3dc2-bc06-c14d8ce15e02 | 3.34867 | -61.24779 | 2025-03-05 04:55:00 | NOAA-21 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 8183cd2f-8374-301a-b3af-7cd7d0bee23c | 2.62481 | -60.41196 | 2025-03-05 04:55:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e69dcc0f-b739-385d-a9a5-360041803280 | 2.43031 | -60.64955 | 2025-03-05 04:55:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a9e41672-fd79-38b6-a48a-9f4e093c49ae | 1.28102 | -60.09607 | 2025-03-05 04:55:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2f5ef84d-2634-3471-95cd-9f31cb55d8e9 | 2.42985 | -60.64654 | 2025-03-05 04:55:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7b570d95-e77f-3225-92dd-bf6638691792 | 2.35023 | -61.00371 | 2025-03-05 04:55:00 | NOAA-21 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 06c71c3d-ae83-3260-9b05-e66b3599c3f6 | 1.13154 | -60.50671 | 2025-03-05 04:55:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 3.2 |
| fe4871b1-1bae-3619-9390-d2e1b4d8dc96 | 2.35628 | -61.00861 | 2025-03-05 04:55:00 | NOAA-21 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 37e9a168-de41-36a8-bd8f-c2dc3cb0e461 | 1.13646 | -60.50594 | 2025-03-05 04:55:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 3.2 |
| a0f4b1f2-9612-3af5-8f38-da2bde40bd91 | 1.12827 | -60.51857 | 2025-03-05 04:55:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 72fea4b6-df92-3fc7-8f2e-74d9de0f6456 | 1.19942 | -60.07606 | 2025-03-05 04:55:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 8754f614-a413-348c-95be-0082122a9d43 | 1.1373 | -60.5115 | 2025-03-05 04:55:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 3dd3e286-e58c-353f-941b-9be945f6d2fc | 1.85592 | -60.58506 | 2025-03-05 04:55:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 0.4 |
| c8f7813f-c195-3fc7-99f6-b538e99f9f91 | -7.09649 | -44.38668 | 2025-03-05 04:57:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 99aa39f3-ba23-36f7-bbfd-d58b78fde19f | -7.09702 | -44.38277 | 2025-03-05 04:57:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d68de936-a9b5-34c1-a21b-44e1d3c2ebe0 | -13.53703 | -47.94621 | 2025-03-05 04:59:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 082e5512-e991-394e-a3b5-753bac861c10 | -13.53636 | -47.95154 | 2025-03-05 04:59:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0e7dfd9b-e298-3634-89a8-759f1bbba158 | -15.08017 | -48.94497 | 2025-03-05 04:59:00 | NOAA-21 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 85e99bcd-08f6-3b0e-92b2-30132b1d9cca | -13.53521 | -47.94789 | 2025-03-05 04:59:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 56226542-b06d-3340-9ed1-4cf0509d2215 | -13.53588 | -47.94227 | 2025-03-05 04:59:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ff7f672c-cb91-3164-99e0-b87591bf7019 | -20.91537 | -55.55337 | 2025-03-05 05:01:00 | NOAA-21 | ANASTÁCIO | MATO GROSSO DO SUL | Brasil | 5000708 | 50 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 7312dffb-a4e6-3a4f-8084-0d0c963e1b42 | -20.91937 | -55.54997 | 2025-03-05 05:01:00 | NOAA-21 | ANASTÁCIO | MATO GROSSO DO SUL | Brasil | 5000708 | 50 | 33 | nan | nan | nan | Cerrado | 3.4 |
| c3485c1e-cfcd-3547-8cb9-c5a210fcca04 | -20.9188 | -55.55392 | 2025-03-05 05:01:00 | NOAA-21 | ANASTÁCIO | MATO GROSSO DO SUL | Brasil | 5000708 | 50 | 33 | nan | nan | nan | Cerrado | 3.4 |
| c3833e46-3cbb-3e07-bf93-3ce7e8b4085a | -21.38234 | -56.09613 | 2025-03-05 05:01:00 | NOAA-21 | GUIA LOPES DA LAGUNA | MATO GROSSO DO SUL | Brasil | 5004106 | 50 | 33 | nan | nan | nan | Cerrado | 0.5 |
| b3fdc8f1-8b8f-3b87-855b-0557615987d9 | -19.04776 | -52.28009 | 2025-03-05 05:01:00 | NOAA-21 | CASSILÂNDIA | MATO GROSSO DO SUL | Brasil | 5002902 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 679187d0-2aa5-3dfd-a511-c53e42542cc2 | -18.58453 | -53.05125 | 2025-03-05 05:01:00 | NOAA-21 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e67a512c-f7a3-3079-8497-5cb5ae8e54e8 | -19.37641 | -57.40464 | 2025-03-05 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 0a67b932-1bd1-3e70-b9b3-3ad5aecdf82c | -18.3721 | -55.70745 | 2025-03-05 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| ba7d68a5-6b1c-36e4-a3a5-42a7c9f7e129 | -18.37434 | -55.71547 | 2025-03-05 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.5 |
| f3b1a730-eb7c-3d31-98dd-047244556eb4 | -20.28588 | -50.9806 | 2025-03-05 05:01:00 | NOAA-21 | SANTA FÉ DO SUL | SÃO PAULO | Brasil | 3546603 | 35 | 33 | nan | nan | nan | Mata Atlântica | 8.1 |
| a7e88b62-bc7b-38ba-90aa-e4c0f49a807a | -20.28639 | -50.97622 | 2025-03-05 05:01:00 | NOAA-21 | SANTA FÉ DO SUL | SÃO PAULO | Brasil | 3546603 | 35 | 33 | nan | nan | nan | Mata Atlântica | 8.1 |
| e7c10ce8-6aeb-3cd8-94c3-e7a686e14877 | -18.87804 | -52.41813 | 2025-03-05 05:01:00 | NOAA-21 | CASSILÂNDIA | MATO GROSSO DO SUL | Brasil | 5002902 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b6faac96-2013-3ee7-bdbb-86722f10c933 | -18.37154 | -55.71119 | 2025-03-05 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 1666a463-5373-317a-a343-bfd2afd8a6d6 | -21.65054 | -46.4222 | 2025-03-05 05:01:00 | NOAA-21 | BOTELHOS | MINAS GERAIS | Brasil | 3108404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| acce6c65-4eb5-38ff-a109-8f7853394f2b | -18.95867 | -52.38375 | 2025-03-05 05:01:00 | NOAA-21 | CASSILÂNDIA | MATO GROSSO DO SUL | Brasil | 5002902 | 50 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ca68ca0c-2727-3dc3-b784-238b7eae6c60 | -20.29074 | -50.97685 | 2025-03-05 05:01:00 | NOAA-21 | SANTA FÉ DO SUL | SÃO PAULO | Brasil | 3546603 | 35 | 33 | nan | nan | nan | Mata Atlântica | 8.1 |
| 2b800df0-af1b-3c6c-99af-dcbada71e19a | -25.11204 | -52.72636 | 2025-03-05 05:03:00 | NOAA-21 | GUARANIAÇU | PARANÁ | Brasil | 4109302 | 41 | 33 | nan | nan | nan | Mata Atlântica | 5.0 |
| 5f3046ea-02dc-3cae-9842-af0e66715b3f | -25.10745 | -52.7297 | 2025-03-05 05:03:00 | NOAA-21 | GUARANIAÇU | PARANÁ | Brasil | 4109302 | 41 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 8dc9bd24-7ab8-32d5-9cc0-1dd8c0ea3c95 | -26.77814 | -49.37244 | 2025-03-05 05:03:00 | NOAA-21 | BENEDITO NOVO | SANTA CATARINA | Brasil | 4202206 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| e3ccfb70-c051-35fd-92ff-b43cf7dbab97 | -25.11157 | -52.73059 | 2025-03-05 05:03:00 | NOAA-21 | GUARANIAÇU | PARANÁ | Brasil | 4109302 | 41 | 33 | nan | nan | nan | Mata Atlântica | 5.0 |
| 480f4e35-e6e3-3267-a81c-a00e57536faf | -28.91193 | -55.87066 | 2025-03-05 05:03:00 | NOAA-21 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 1.5 |
| c911bafd-a4a7-3dca-b1ec-5be8294b9fc4 | -28.91228 | -55.87312 | 2025-03-05 05:03:00 | NOAA-21 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 1.5 |
| 74fec18e-ef93-31ba-8da6-412724858e41 | -25.1079 | -52.72562 | 2025-03-05 05:03:00 | NOAA-21 | GUARANIAÇU | PARANÁ | Brasil | 4109302 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| a4f97efb-a31c-39e1-b10b-c5fd300bd336 | -30.49468 | -51.83413 | 2025-03-05 05:03:00 | NOAA-21 | BARÃO DO TRIUNFO | RIO GRANDE DO SUL | Brasil | 4301750 | 43 | 33 | nan | nan | nan | Pampa | 6.5 |
| 22f78706-2b66-357d-83cc-87d57a090937 | -25.09786 | -49.56597 | 2025-03-05 05:03:00 | NOAA-21 | ITAPERUÇU | PARANÁ | Brasil | 4111258 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 5ee9c680-61b4-383f-8e0d-297a0d80f3f2 | -22.67148 | -42.8618 | 2025-03-05 05:08:00 | AQUA_M-M | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 5.8 |
| 6b568ea3-8cb0-38c1-bea9-4fb32e25abb3 | 3.56896 | -60.23419 | 2025-03-05 05:20:00 | NPP-375D | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 4b1c3b94-d2f5-329a-a76c-04a1ecd30288 | 3.5447 | -60.07948 | 2025-03-05 05:20:00 | NPP-375D | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d151a329-b82f-334b-acbd-80d3771066e2 | 3.34753 | -61.24514 | 2025-03-05 05:22:00 | NPP-375D | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0a477415-4fdf-3f0a-a9d5-465e3bc03699 | 2.35794 | -61.04433 | 2025-03-05 05:22:00 | NPP-375D | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ba1d3910-11e2-3459-a5c2-72fe5216d4d6 | 3.35172 | -61.24863 | 2025-03-05 05:22:00 | NPP-375D | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3bee1ef4-c4a3-3f19-a3e2-6fd45f1fc537 | 0.77123 | -60.4095 | 2025-03-05 05:22:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b950a6a6-27ca-36a2-a25e-ad450a765b3a | 1.64758 | -60.29709 | 2025-03-05 05:22:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a92602e5-f880-3612-9fd5-ab97ec228027 | 1.93926 | -60.3974 | 2025-03-05 05:22:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b4c8ff08-8438-342a-b57c-b486205697c7 | 1.13318 | -60.51291 | 2025-03-05 05:22:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cf795d27-6f0e-37c4-b854-1cbfd5385017 | 2.35333 | -61.06082 | 2025-03-05 05:22:00 | NPP-375D | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7149066f-7f59-3a40-bc59-c3d4d371b2ac | 1.13543 | -60.50512 | 2025-03-05 05:22:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4b8a0d27-c700-3e02-a9b2-fc33acce890b | 2.3115 | -60.18813 | 2025-03-05 05:22:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b5ce3c82-dcd3-3301-9751-2cc6d7e66eba | 2.35144 | -61.00261 | 2025-03-05 05:22:00 | NPP-375D | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 922509e6-1fd5-389e-aa03-a981c87f5a62 | 3.30988 | -61.21378 | 2025-03-05 05:22:00 | NPP-375D | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |


[Clique aqui para ver as próximas entradas](README5.md)
