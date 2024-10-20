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

## Dados Diários - Página 22

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| fdf1babc-be8a-3f43-9e56-4eec6fae2da1 | -4.8397 | -49.9216 | 2024-10-20 04:08:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0e62b39c-ff6e-3f8b-9612-8ac833405d86 | -4.8286 | -49.95521 | 2024-10-20 04:08:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3379e1a5-7ef7-3196-b1e7-409ad0d2c123 | -4.82805 | -49.95835 | 2024-10-20 04:08:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8f5b17c6-8271-381e-9120-3466adf0c07a | -4.58519 | -50.67623 | 2024-10-20 04:08:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 30d29932-c4bf-3068-8399-11129161a068 | -4.48068 | -50.45122 | 2024-10-20 04:08:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b6a77d74-ca4d-3d92-ac6a-3d512935b6b7 | -4.46929 | -50.45283 | 2024-10-20 04:08:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fb15d7b0-8c5b-3031-9306-45f74ab48084 | -4.46872 | -50.45623 | 2024-10-20 04:08:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 352d6e88-a8fe-37c9-a971-ee20642d40f2 | -4.44136 | -50.68898 | 2024-10-20 04:08:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 19131e49-19c4-3123-a8f6-6bb6ea84b30a | -4.41116 | -50.5325 | 2024-10-20 04:08:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3eefd8b1-546a-3105-92fb-845aac9fd06c | -3.94368 | -49.472 | 2024-10-20 04:08:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 71f814aa-7076-3402-97c2-bc2369785bd3 | -4.5913 | -50.67349 | 2024-10-20 04:08:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 830d04cd-1537-382b-ab39-5c1713c566a9 | -4.59068 | -50.67705 | 2024-10-20 04:08:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c33d99ad-d01b-3cd2-a022-19d5af6b21b6 | -4.58581 | -50.67266 | 2024-10-20 04:08:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 89a34957-4323-3c9e-a001-1754e39e0685 | -4.48269 | -50.4531 | 2024-10-20 04:08:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 686f6813-48fc-3a58-a45a-4b97bcf23f79 | -4.48011 | -50.45462 | 2024-10-20 04:08:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 42656324-49b3-369a-9a3f-6f57dca82859 | -4.47728 | -50.45222 | 2024-10-20 04:08:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 94631507-ec77-3e07-aaf6-c821996a3877 | -4.32361 | -50.80997 | 2024-10-20 04:08:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f8780f79-43cb-345f-b024-999ed520d9d3 | -3.69171 | -50.19466 | 2024-10-20 04:08:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 967c4f36-9f81-307c-b2fc-95dae370976f | -3.60826 | -50.58418 | 2024-10-20 04:08:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| cc41cb6b-7b3e-391b-8934-7e0a697b25e4 | -3.60821 | -50.58368 | 2024-10-20 04:08:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 3354e734-ebd3-3ccc-95d2-8b7d8e695971 | -3.60269 | -50.58271 | 2024-10-20 04:08:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| b2a786b8-d967-3ee2-a682-6adb95d4c583 | -3.60209 | -50.58622 | 2024-10-20 04:08:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5e6b808f-7470-3e6e-8335-46e449b10b26 | -3.60156 | -50.59033 | 2024-10-20 04:08:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 53294571-8c45-3653-a8d6-152323ecb1a7 | -3.60147 | -50.58981 | 2024-10-20 04:08:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8b5b38d1-f8bf-31cc-92ca-f423a597194e | -3.60885 | -50.5806 | 2024-10-20 04:08:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 9df8948a-dd64-3582-94b0-825ffc51647a | -3.60767 | -50.58776 | 2024-10-20 04:08:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| cb2403cb-563f-3447-a7bc-455f61b84bf6 | -3.6076 | -50.58723 | 2024-10-20 04:08:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| fc97618a-a16d-34cf-a2cb-b72887dfd032 | -3.6033 | -50.57919 | 2024-10-20 04:08:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 957d5353-f401-3eb8-a6e9-29b1d11ccb92 | -3.60274 | -50.5832 | 2024-10-20 04:08:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| fcfabce0-d0f8-3ed4-aa8f-871c8a59ffaa | -3.60216 | -50.58671 | 2024-10-20 04:08:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| f0089353-b1a5-333b-8e48-921c01b410aa | -5.01672 | -50.83885 | 2024-10-20 04:08:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5e1090c1-872f-3f9a-9010-40961d0c5b9e | -5.01121 | -50.838 | 2024-10-20 04:08:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f9c0e848-a02e-3e9e-b5e5-f14ba8852b58 | -5.01059 | -50.84155 | 2024-10-20 04:08:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 440142cc-34a0-31d9-8040-dd9fa7ad121b | -6.21725 | -50.88826 | 2024-10-20 04:08:00 | NOAA-21 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6c95609d-023c-3378-8c7f-94ecb7a10658 | -5.8608 | -51.07754 | 2024-10-20 04:08:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| dccec9c9-953c-371c-9c45-c89a7b15f4bd | -5.86017 | -51.08116 | 2024-10-20 04:08:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 780ec64f-67c6-318c-ab57-069be4d56674 | -5.85954 | -51.08479 | 2024-10-20 04:08:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a4512f02-775c-3a42-a182-d93a27495ae8 | -5.54377 | -50.16325 | 2024-10-20 04:08:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cac1675f-7262-3d22-93a7-d30c6983d1c3 | -5.51385 | -50.58778 | 2024-10-20 04:08:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3683c8e5-747b-3f50-a9f2-e9e0716c6f40 | -5.50908 | -50.58348 | 2024-10-20 04:08:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 70b3bb77-c65f-3699-b243-482a488fdcef | -5.50849 | -50.58687 | 2024-10-20 04:08:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| aa10e165-e4dc-372a-acde-5937018e0202 | -5.50791 | -50.59027 | 2024-10-20 04:08:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 0e7f60f3-e74a-36b0-8371-f6713dd61829 | -5.50312 | -50.586 | 2024-10-20 04:08:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 5b2cc2ff-92b2-3292-bbe6-e50f642aec9f | -5.50254 | -50.5894 | 2024-10-20 04:08:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| dae8d12a-2494-3046-b9e6-61bdc049602d | -5.50195 | -50.59282 | 2024-10-20 04:08:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c6345dcb-ed17-37d3-9c36-17eb41fbbbe6 | -5.49775 | -50.58518 | 2024-10-20 04:08:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 02a80b56-7ec3-3203-9ba3-d008556060d2 | -5.49716 | -50.58857 | 2024-10-20 04:08:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 66f159d0-e42d-301c-8e50-448d827b9540 | -5.49657 | -50.59196 | 2024-10-20 04:08:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ecd4e208-74a1-3913-9be7-99f87c5c9a46 | -5.49179 | -50.58767 | 2024-10-20 04:08:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3bc2a087-107a-3629-b5c0-3a6a9ce96e1d | -5.47686 | -50.54675 | 2024-10-20 04:08:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4c67a35f-4e7f-3375-882a-a3c43f36cdd9 | -5.4733 | -50.53563 | 2024-10-20 04:08:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 48c17c08-4f01-30c5-a286-a9da6dce7dc3 | -5.47089 | -50.54937 | 2024-10-20 04:08:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9f78a8f1-28c5-3bf2-ba86-c7cfdcf7457c | -5.2096 | -50.00523 | 2024-10-20 04:08:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| afde0c09-4960-3166-9a3f-4e11e6715444 | -5.2083 | -50.00422 | 2024-10-20 04:08:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0984214a-570f-3231-a05f-fdf7b1e28173 | -5.20777 | -50.00734 | 2024-10-20 04:08:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 224741aa-6ed2-358a-be36-f10c5843bcf4 | -5.16334 | -50.71183 | 2024-10-20 04:08:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| f7cfafa8-4658-3016-a7ba-b134148e3c54 | -5.16271 | -50.7155 | 2024-10-20 04:08:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 85384aa8-9be4-302f-a669-0df3b66ee53c | -5.16208 | -50.71922 | 2024-10-20 04:08:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 7a015bb1-bbbd-3b10-a343-b78e015bee56 | -5.01734 | -50.83526 | 2024-10-20 04:08:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7719461c-8f7a-3739-8890-95d0fb7aef67 | -2.23165 | -50.45444 | 2024-10-20 04:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a1195da8-bbe9-39f6-a95e-19b815efb8cd | -2.22954 | -50.45589 | 2024-10-20 04:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3e7c37c0-a0f5-35fe-9e00-f732f1e53569 | -2.22604 | -50.45358 | 2024-10-20 04:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9a2d2fea-b044-3e31-bcbd-6f08b0705e6b | -2.22422 | -50.46485 | 2024-10-20 04:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| c0c386af-a547-3772-bcdc-aa87dd48f5fc | -2.22393 | -50.45504 | 2024-10-20 04:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f0014d32-467f-35a1-83dc-e6846e6328bf | -2.22266 | -50.46253 | 2024-10-20 04:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 5040be09-c59c-319f-a2b0-7e4a87c1d051 | -2.2186 | -50.464 | 2024-10-20 04:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b809486b-af0a-32b3-bb9d-0423b1a0a146 | -2.21271 | -50.45332 | 2024-10-20 04:08:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 0e1e6ef1-fb5b-34bb-afef-4935167397c7 | -2.21206 | -50.45712 | 2024-10-20 04:08:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 4aa9be9c-dbbe-3c5f-a222-5a677a830e10 | -2.21079 | -50.46464 | 2024-10-20 04:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 3678dae8-34e4-3988-8871-44e34dc19e56 | -2.20799 | -50.45844 | 2024-10-20 04:08:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| eeb7c094-96a4-3a64-877a-77fd2bbf0993 | -2.20711 | -50.45237 | 2024-10-20 04:08:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| dab12237-3a62-3cd4-9753-9f13764233c6 | -2.20677 | -50.46598 | 2024-10-20 04:08:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 152e6d4c-5d8b-342f-9b29-64c4f600486c | -2.20455 | -50.46741 | 2024-10-20 04:08:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 0d2b8789-3eea-3d40-a3ae-c7dcefb4e393 | -2.23225 | -50.45072 | 2024-10-20 04:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 21c774c8-f758-3e1f-a267-5f732d69c183 | -2.23017 | -50.45217 | 2024-10-20 04:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d82247ea-d32a-3b77-be70-ac33f967b3c5 | -2.22483 | -50.46109 | 2024-10-20 04:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| ed941e42-b912-30dc-9133-4c13166f7a9c | -2.2233 | -50.45879 | 2024-10-20 04:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 711785c8-3d9e-3fb3-92d1-5f9b59f9bd4e | -2.22203 | -50.4663 | 2024-10-20 04:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a3272bdf-8e21-35bd-a347-0eb4e1c6fa1d | -2.2142 | -50.45562 | 2024-10-20 04:08:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 94b0d850-cd55-339d-92c7-fc93e959ec39 | -2.21142 | -50.4609 | 2024-10-20 04:08:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 86fda084-1cc0-3735-abc1-e437bd0172b2 | -2.21015 | -50.46838 | 2024-10-20 04:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 578265a1-b8e5-38b1-96d8-077904ae0581 | -2.2086 | -50.45465 | 2024-10-20 04:08:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| fd2d780f-bc85-3682-ad53-81ce3420c98f | -2.20738 | -50.46223 | 2024-10-20 04:08:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 272c13cc-9e36-331f-9747-36efede50358 | -2.20647 | -50.45614 | 2024-10-20 04:08:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| e8c6c334-31a2-35f1-a9e4-8f596109118e | -2.20583 | -50.4599 | 2024-10-20 04:08:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 53d0ba09-f497-3230-b46b-664a69cb81d0 | -2.20519 | -50.46367 | 2024-10-20 04:08:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| b372178e-2650-38b8-9851-8962ac430624 | -2.20178 | -50.46126 | 2024-10-20 04:08:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 9d762658-7657-3cff-8c7d-e75a43f9cbd2 | -3.28181 | -50.94187 | 2024-10-20 04:08:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 4dab1d6e-3169-33e9-8c17-0fbe2d3ccd61 | -3.28109 | -51.05145 | 2024-10-20 04:08:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3bfeeeab-81a0-3f59-90c0-6558fc4564a2 | -3.28043 | -51.05542 | 2024-10-20 04:08:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d76afe44-cb84-3e13-afa5-6f128f962c7c | -3.27649 | -50.66536 | 2024-10-20 04:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 25769144-38c5-30cb-84a1-fbdab2b3799e | -3.27088 | -50.66456 | 2024-10-20 04:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 19b581fb-a976-39d6-82cd-75020a52e0b1 | -3.24237 | -50.84805 | 2024-10-20 04:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 338151d5-be9a-384a-bca2-105485f1e920 | -3.23672 | -50.84706 | 2024-10-20 04:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 71262645-fce4-3d17-94c1-a43147b47150 | -3.23609 | -50.85094 | 2024-10-20 04:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9d7a2b3f-54e6-364f-a74e-2a803064ca80 | -3.17626 | -51.25127 | 2024-10-20 04:08:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| eab4f096-eb8e-33ad-b05a-8cc22a0ffc7c | -3.12398 | -51.34982 | 2024-10-20 04:08:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 30afba20-ac54-39cd-bf66-adc6304b6c67 | -3.10855 | -51.33418 | 2024-10-20 04:08:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| a80fb62d-2e1a-38aa-96c8-cf1c9ff5fcc8 | -3.09186 | -51.22008 | 2024-10-20 04:08:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a2b128f4-056a-36e6-9cb0-231c0dd9a973 | -3.08672 | -51.21523 | 2024-10-20 04:08:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |


[Clique aqui para ver as próximas entradas](README23.md)
