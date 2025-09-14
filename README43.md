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

## Dados Diários - Página 43

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ac692b35-61d4-3e76-8e01-1bc4fb1a3833 | -15.7992 | -52.21117 | 2025-09-14 04:42:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 233421a5-3686-3929-a450-3d8209bbfe1a | -17.4077 | -49.26098 | 2025-09-14 04:42:00 | NOAA-21 | PROFESSOR JAMIL | GOIÁS | Brasil | 5218391 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 77b1090c-2a47-3dce-a4ee-31adcd14a7db | -14.43417 | -43.20773 | 2025-09-14 04:42:00 | NOAA-21 | PALMAS DE MONTE ALTO | BAHIA | Brasil | 2923407 | 29 | 33 | nan | nan | nan | Cerrado | 8.2 |
| aa314108-3573-3c59-b87d-67ff847ac802 | -14.42807 | -47.34167 | 2025-09-14 04:42:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| ea819de5-11f0-308c-9d22-8c479c97836a | -15.80639 | -52.20868 | 2025-09-14 04:42:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 65be4c09-be71-31db-9e16-3f7380d24124 | -12.70378 | -54.71524 | 2025-09-14 04:42:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 13.2 |
| f3d81902-3633-30b0-8aa8-4cfae7f42b99 | -15.69515 | -54.34676 | 2025-09-14 04:42:00 | NOAA-21 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3b957533-dd6d-38de-b3ea-adaf6b63b615 | -17.31628 | -46.0802 | 2025-09-14 04:42:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 86815bff-0fcc-3113-9d27-cf2f9a40d53e | -14.62742 | -46.36404 | 2025-09-14 04:42:00 | NOAA-21 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 92c621f9-0e5b-3b30-baae-2853af406b22 | -14.49977 | -53.88458 | 2025-09-14 04:42:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a1ded27c-07fa-3936-894f-e4f450b4015a | -15.15585 | -52.46743 | 2025-09-14 04:42:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 56e5cad2-08c9-3752-9eb0-1cb86249132e | -12.92328 | -54.75071 | 2025-09-14 04:42:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 22e5231a-4629-3266-a1ab-3b8f11724658 | -19.98457 | -46.90519 | 2025-09-14 04:42:00 | NOAA-21 | TAPIRA | MINAS GERAIS | Brasil | 3168101 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4b478edb-37e6-3c8e-ab4d-5c8d2fd9de70 | -17.95824 | -46.93982 | 2025-09-14 04:42:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d277e414-d548-34f2-a038-35bd666c5840 | -14.20405 | -46.33105 | 2025-09-14 04:42:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 7.5 |
| d593ea13-1247-33e1-a79e-5b27e324e2c2 | -15.76873 | -53.47956 | 2025-09-14 04:42:00 | NOAA-21 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 58886097-b3ab-380c-b759-6ab6f798e58d | -17.40779 | -49.25937 | 2025-09-14 04:42:00 | NOAA-21 | PROFESSOR JAMIL | GOIÁS | Brasil | 5218391 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 89645a66-c511-3194-b244-dc65194aacc4 | -12.93214 | -54.74314 | 2025-09-14 04:42:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7fa47ef6-5c71-3838-8f94-4dcefd1a3b80 | -14.49151 | -53.89133 | 2025-09-14 04:42:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d1a09025-aeef-3671-ab3d-d09c5a5681d1 | -15.76486 | -52.23483 | 2025-09-14 04:42:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| f1d82187-c32e-322c-8d0a-9af17a36ed0c | -14.48044 | -47.32492 | 2025-09-14 04:42:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 6fac0451-074a-35f4-99cc-72052e15569b | -14.47355 | -47.31892 | 2025-09-14 04:42:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 07c221a0-c268-34b8-b6a7-34f407373941 | -15.67372 | -49.90963 | 2025-09-14 04:42:00 | NOAA-21 | ITAPURANGA | GOIÁS | Brasil | 5211206 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ac4e0004-0712-354f-aef8-072e7b802abd | -18.15061 | -49.19281 | 2025-09-14 04:42:00 | NOAA-21 | BURITI ALEGRE | GOIÁS | Brasil | 5203906 | 52 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 6f255cbb-a853-37d3-a8df-c4632c165d6e | -15.93016 | -49.97941 | 2025-09-14 04:42:00 | NOAA-21 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2c03a466-d30e-3f12-98e4-c869f7a6fe4b | -16.66094 | -49.77248 | 2025-09-14 04:42:00 | NOAA-21 | PALMEIRAS DE GOIÁS | GOIÁS | Brasil | 5215702 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f01fecc3-db10-3a64-ab5e-f4181777574a | -15.78002 | -53.48091 | 2025-09-14 04:42:00 | NOAA-21 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 209f2a8f-0a48-3b72-905a-5126a61f17da | -12.68028 | -54.69721 | 2025-09-14 04:42:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 36a027ee-610d-32ec-8a11-de8755e28cec | -15.57211 | -54.73217 | 2025-09-14 04:42:00 | NOAA-21 | DOM AQUINO | MATO GROSSO | Brasil | 5103601 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 483332e7-b18f-3863-ac1d-a47588bb4829 | -15.76818 | -52.23535 | 2025-09-14 04:42:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| cbe59900-3d8a-3d45-8dfd-d6f624de3300 | -14.86997 | -55.83694 | 2025-09-14 04:42:00 | NOAA-21 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| de082517-b458-3b2f-b8ed-cfc6ad3be949 | -12.68538 | -54.71182 | 2025-09-14 04:42:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 6f7aca2f-f779-35f7-aee0-530b09974641 | -14.27027 | -45.05788 | 2025-09-14 04:42:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 47f05a84-60f1-3124-a09d-206c480db56e | -18.58899 | -47.19352 | 2025-09-14 04:42:00 | NOAA-21 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 5c34cced-7f08-39a7-a7c0-9748872165da | -15.29604 | -53.78687 | 2025-09-14 04:42:00 | NOAA-21 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1db0d02b-7536-37e1-a02a-fcf2e191f68f | -18.28123 | -49.4686 | 2025-09-14 04:42:00 | NOAA-21 | ITUMBIARA | GOIÁS | Brasil | 5211503 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6cd576d8-ee4a-3a76-86f2-3fd6b09c85f8 | -14.36755 | -52.93768 | 2025-09-14 04:42:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c8cc5569-c319-37d7-b3f1-d83a96ae2a96 | -18.09248 | -42.93531 | 2025-09-14 04:42:00 | NOAA-21 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Mata Atlântica | 12.6 |
| 30a8a682-05cc-3940-858c-1b796a468409 | -12.91147 | -54.75325 | 2025-09-14 04:42:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 4ae6548e-450d-3ae9-bdd3-7cdf5e0b5fae | -14.63195 | -46.36081 | 2025-09-14 04:42:00 | NOAA-21 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2e21f1dd-0efd-3523-89b9-55a11ad877f1 | -14.41437 | -46.40295 | 2025-09-14 04:42:00 | NOAA-21 | BURITINÓPOLIS | GOIÁS | Brasil | 5203962 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 16850300-ae66-399b-b064-a2033dd4d4de | -18.60861 | -47.20012 | 2025-09-14 04:42:00 | NOAA-21 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b4cf58b8-290e-364f-ab8e-ef060072203f | -15.76589 | -52.24971 | 2025-09-14 04:42:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 969e5108-6a13-3e25-96d9-32a564780742 | -14.6365 | -52.03104 | 2025-09-14 04:42:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| ca7b8e4d-2639-3f49-a61d-533f76450327 | -16.43589 | -45.6904 | 2025-09-14 04:42:00 | NOAA-21 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 24.4 |
| 7c1f6012-1144-3412-9ef3-685ccdd4a725 | -19.72179 | -45.4285 | 2025-09-14 04:42:00 | NOAA-21 | BOM DESPACHO | MINAS GERAIS | Brasil | 3107406 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 52147d02-8ab7-3c76-b685-f20fb2335799 | -13.92784 | -48.30131 | 2025-09-14 04:42:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| ec034872-9601-3c6c-9498-dd6d361e4362 | -12.69934 | -54.71901 | 2025-09-14 04:42:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 13.2 |
| ff026f18-6394-3552-ad91-db83819b92f7 | -15.19512 | -50.11058 | 2025-09-14 04:42:00 | NOAA-21 | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 7.1 |
| a6484e89-6043-369d-86d4-9bae69d36ce8 | -14.17806 | -46.15783 | 2025-09-14 04:42:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| f1e44205-64a5-3adf-ab53-361ec06c14bc | -17.41779 | -49.2395 | 2025-09-14 04:42:00 | NOAA-21 | PROFESSOR JAMIL | GOIÁS | Brasil | 5218391 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ac578419-59cc-36c9-8288-6671c1e48b87 | -14.81576 | -48.76207 | 2025-09-14 04:42:00 | NOAA-21 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ff4802d3-d788-3e79-ac38-1f7d67a6e642 | -15.18928 | -52.46975 | 2025-09-14 04:42:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3be3fa81-0036-3838-8dab-5aef3b1a1634 | -12.66263 | -54.68951 | 2025-09-14 04:42:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 4498c153-f3c2-3e8b-aeef-d5b2b84bbe53 | -14.62051 | -52.02471 | 2025-09-14 04:42:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 64938626-8fcc-3f45-b7af-f6504ee40932 | -15.7675 | -53.48714 | 2025-09-14 04:42:00 | NOAA-21 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 2196fd5f-c31a-3ad7-a321-1e883543db58 | -17.57779 | -49.07773 | 2025-09-14 04:42:00 | NOAA-21 | MORRINHOS | GOIÁS | Brasil | 5213806 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 518b3175-e609-3b96-8053-059169a9fa71 | -12.6781 | -54.68775 | 2025-09-14 04:42:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 65418995-b456-3f04-bbde-c219d206ee74 | -14.61175 | -46.32811 | 2025-09-14 04:42:00 | NOAA-21 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 51cb2608-170f-360c-a21f-51f4b59ff4a8 | -13.89212 | -48.29639 | 2025-09-14 04:42:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 990751aa-1b1e-3559-96fb-6d9aaf505cb3 | -14.20086 | -46.17223 | 2025-09-14 04:42:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 821a44e2-e519-3904-99ee-9162faa2e7e1 | -14.94943 | -55.95998 | 2025-09-14 04:42:00 | NOAA-21 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 729e2c42-9663-3a2a-a5a2-fe59b9e696d2 | -12.4563 | -57.78426 | 2025-09-14 04:42:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 04c0a17f-19ea-3cf8-9a86-edf106427e39 | -17.17373 | -49.37911 | 2025-09-14 04:42:00 | NOAA-21 | CROMÍNIA | GOIÁS | Brasil | 5206503 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 349ea87a-1ea6-3d35-81f8-69fabfa0db20 | -15.68885 | -49.90737 | 2025-09-14 04:42:00 | NOAA-21 | ITAPURANGA | GOIÁS | Brasil | 5211206 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 6c0f5009-6b66-3357-9667-497b73e8f437 | -15.17609 | -52.31932 | 2025-09-14 04:42:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 42935295-e412-3a8d-87f3-848cba7420ec | -14.84026 | -48.33342 | 2025-09-14 04:42:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| bad68c11-69dc-3bee-b69a-1c6aaf6119ac | -18.59209 | -47.20127 | 2025-09-14 04:42:00 | NOAA-21 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 8a637da8-6ce9-32c4-abfe-ecf9576d49d1 | -17.07214 | -47.15647 | 2025-09-14 04:42:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 90062666-d6eb-33ab-87d1-9f5918e9de9a | -15.18264 | -52.46862 | 2025-09-14 04:42:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f8f946f0-c767-3e5c-9bb5-0000c186c2da | -12.61572 | -57.004 | 2025-09-14 04:42:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| f42dc80a-8fe0-3764-b654-3b923ffb8321 | -17.94337 | -45.25549 | 2025-09-14 04:42:00 | NOAA-21 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1fa4d657-576b-354e-8e87-bb7a956d5d2b | -15.5843 | -54.74135 | 2025-09-14 04:42:00 | NOAA-21 | DOM AQUINO | MATO GROSSO | Brasil | 5103601 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 19732726-6c71-372e-9129-2f87d7458f6c | -15.16916 | -52.46951 | 2025-09-14 04:42:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 5f8d2cdf-0051-33f1-8d23-a684638c8b5d | -12.6701 | -54.66806 | 2025-09-14 04:42:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 915e39b4-5148-34b3-aa7a-32e8a755a2a1 | -14.61646 | -52.07151 | 2025-09-14 04:42:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e67c7b69-1bee-362b-a3a5-a8e97e57ec4a | -15.65885 | -49.43816 | 2025-09-14 04:42:00 | NOAA-21 | JARAGUÁ | GOIÁS | Brasil | 5211800 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 37ca1ec5-cac5-33ff-8391-f60e8941784c | -15.76429 | -52.23842 | 2025-09-14 04:42:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 22557225-f3b7-3324-b3d0-8867a19a41db | -14.81867 | -48.76686 | 2025-09-14 04:42:00 | NOAA-21 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e8d6cc25-6201-36c7-8adc-776b6c0955b3 | -15.57143 | -54.77335 | 2025-09-14 04:42:00 | NOAA-21 | DOM AQUINO | MATO GROSSO | Brasil | 5103601 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 54721d86-827a-37c6-8e73-cedc440fbef7 | -16.58147 | -55.16751 | 2025-09-14 04:42:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| c9202eb8-c568-32b2-b1db-938f6cf5f577 | -15.19456 | -50.11429 | 2025-09-14 04:42:00 | NOAA-21 | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| ad7c78d8-e1ba-30c1-851c-4b1300f1dbc8 | -14.81517 | -48.76619 | 2025-09-14 04:42:00 | NOAA-21 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a5b896d2-370b-3e6e-8de8-032be255b5f8 | -15.11687 | -52.49763 | 2025-09-14 04:42:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c82be9ae-6a95-364c-affc-624c82c05429 | -15.20075 | -50.11897 | 2025-09-14 04:42:00 | NOAA-21 | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 37558ad8-c1a3-3cbc-a789-11d019d859d0 | -14.75777 | -60.21413 | 2025-09-14 04:42:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 88670078-f4ea-396a-9152-461966cd74ab | -12.93582 | -54.7438 | 2025-09-14 04:42:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 255c4367-d242-31b0-9b06-8e01faf6b442 | -14.33333 | -46.61438 | 2025-09-14 04:42:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cdd0af87-2c82-31fd-aae1-4e3aa3b35dd6 | -17.3129 | -46.1074 | 2025-09-14 04:42:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| cad3848a-d158-3589-b644-976625593bd3 | -16.48553 | -55.12283 | 2025-09-14 04:42:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 4dacf46e-835b-3062-8d70-f000fe241e7c | -15.27647 | -56.02845 | 2025-09-14 04:42:00 | NOAA-21 | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 32ff9fa3-cd8a-30bb-80e9-e5666631226a | -12.68188 | -54.66562 | 2025-09-14 04:42:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 10.9 |
| e5819208-109c-3aac-a696-94fe0c2e4e35 | -17.27627 | -46.12457 | 2025-09-14 04:42:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 4a25a3cf-5be8-3db9-a576-35457e7dd9b0 | -17.36658 | -52.90425 | 2025-09-14 04:42:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 75edb2ab-64ab-314f-a153-684b9d9bffc6 | -17.39021 | -52.92707 | 2025-09-14 04:42:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| d474cee5-6e8f-390f-8df1-3640bbaf4176 | -18.00939 | -46.95903 | 2025-09-14 04:42:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 9f454642-35fd-3004-8689-65de1a4786e3 | -19.7219 | -45.43053 | 2025-09-14 04:42:00 | NOAA-21 | BOM DESPACHO | MINAS GERAIS | Brasil | 3107406 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 4290056f-aec8-3cd3-9d47-8aea1dc04463 | -16.71429 | -54.96254 | 2025-09-14 04:42:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a2892003-51b4-32b7-b205-268526b35421 | -12.69869 | -54.7005 | 2025-09-14 04:42:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 15.1 |
| d7907584-0976-3df8-ac6d-d86b147ad1a4 | -14.88083 | -44.45491 | 2025-09-14 04:42:00 | NOAA-21 | MIRAVÂNIA | MINAS GERAIS | Brasil | 3142254 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |


[Clique aqui para ver as próximas entradas](README44.md)
