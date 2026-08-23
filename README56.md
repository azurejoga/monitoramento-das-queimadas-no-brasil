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
| 23616c12-f6ac-338f-8880-53b0c394d462 | -12.11928 | -57.20866 | 2026-08-23 05:06:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e0970aa0-e857-3fe2-af75-575e4fd6f16a | -14.50202 | -59.83533 | 2026-08-23 05:06:00 | NOAA-20 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 36290dd9-ffd8-393c-b698-8e6cd0999ff0 | -14.50893 | -59.81766 | 2026-08-23 05:06:00 | NOAA-20 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cfa0b0c1-6d0e-32fb-8d73-580a97667002 | -15.25134 | -52.84338 | 2026-08-23 05:06:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3dcbf1a0-ea62-3f89-b9bc-a284469998c8 | -13.21543 | -51.43224 | 2026-08-23 05:06:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8cb96021-fcd2-3244-a860-f451f3f8308a | -15.25439 | -52.84836 | 2026-08-23 05:06:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 084f4ef2-a017-3a2f-bb31-dc931d091de7 | -11.68175 | -54.58319 | 2026-08-23 05:06:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 67e49bbf-0ca6-393d-a8ec-859d1ebfa255 | -12.84248 | -48.47924 | 2026-08-23 05:06:00 | NOAA-20 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ef6b38f7-cc28-36d0-a490-671b2142b8d0 | -15.8598 | -55.56101 | 2026-08-23 05:06:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| eb7d98dd-7d7a-376b-8603-f28ac648fa48 | -16.05852 | -50.43408 | 2026-08-23 05:06:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 1e4eef39-8606-3033-97a1-56e775e2e025 | -10.56113 | -61.45747 | 2026-08-23 05:06:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8878ed51-e907-341d-aa02-6dab695cbce1 | -14.36649 | -51.78013 | 2026-08-23 05:06:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 801a1c23-b82a-3a82-a396-c260608e79a3 | -14.38197 | -51.78241 | 2026-08-23 05:06:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 43ec4de4-5187-3dff-8483-56a58f23ee53 | -13.43192 | -43.85496 | 2026-08-23 05:06:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7791a948-6af7-353f-9dcb-fd4261c9b6cc | -14.9966 | -52.68946 | 2026-08-23 05:06:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 8.6 |
| e502f7be-881d-3095-ad19-8de539f58a48 | -14.53942 | -52.9977 | 2026-08-23 05:06:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a6af7c53-e293-30ac-b90f-53968f475e49 | -13.18893 | -51.44677 | 2026-08-23 05:06:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| abf07ec3-1b0b-3125-8319-8fd36e385558 | -12.94621 | -56.62377 | 2026-08-23 05:06:00 | NOAA-20 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 86b98689-b74a-3be9-ac73-e14ddbe4c076 | -14.96769 | -52.66531 | 2026-08-23 05:06:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 84993e2d-0398-37ec-9e50-c685e88943c0 | -13.39877 | -54.36166 | 2026-08-23 05:06:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| dfff770f-5806-3ca7-93cd-88c9a223e982 | -14.97075 | -52.67038 | 2026-08-23 05:06:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 77850c00-207e-3a33-81d4-eb8566913281 | -12.11798 | -57.20952 | 2026-08-23 05:06:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| dc0fc87a-7d20-302f-a349-d8039cf58beb | -13.6576 | -51.8654 | 2026-08-23 05:06:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 94bc904d-3581-3dc0-8a43-dc33f65768b8 | -17.90471 | -44.50079 | 2026-08-23 05:06:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9b88f228-deec-3060-b893-cb18c3c789bc | -14.41962 | -56.46016 | 2026-08-23 05:06:00 | NOAA-20 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4620034a-5482-3d27-8dc9-262fe2fb01f6 | -18.5978 | -47.12605 | 2026-08-23 05:06:00 | NOAA-20 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 4abeb8cb-78ec-3064-9aff-de5447ae7493 | -14.40836 | -51.79133 | 2026-08-23 05:06:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 049c48e1-a4c1-3666-96c1-8a8e7ab150e1 | -13.55721 | -44.09881 | 2026-08-23 05:06:00 | NOAA-20 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3206d5d5-ee1e-3eeb-8cee-0a0cd3bd83de | -13.18009 | -51.42513 | 2026-08-23 05:06:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 38b24ca2-9763-3202-ab68-724d35795b75 | -11.68674 | -54.57299 | 2026-08-23 05:06:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| bf07eadf-ff8b-3b8e-b330-d64f75ca6ecc | -13.15286 | -51.42115 | 2026-08-23 05:06:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 35.4 |
| f3923222-33b6-36f5-b4fa-7fb1a491af46 | -12.7586 | -48.38526 | 2026-08-23 05:06:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 3ee9b6fb-b8fc-3704-aeec-5232349d87b8 | -13.19566 | -51.4274 | 2026-08-23 05:06:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 751cf80e-9ba9-3c2a-852b-a3f5b407261f | -14.31158 | -53.23009 | 2026-08-23 05:06:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b9dbca09-f83a-3f80-9e51-e86ee62aba5b | -16.74744 | -49.33978 | 2026-08-23 05:06:00 | NOAA-20 | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| e02d90b0-3aab-36d6-b718-314ebc935967 | -14.56285 | -53.04055 | 2026-08-23 05:06:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b3963ada-534c-30cf-9668-a25ecd28c9da | -13.55666 | -44.10379 | 2026-08-23 05:06:00 | NOAA-20 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 12289e82-89fe-3531-b663-16cb43dff354 | -14.55923 | -53.04 | 2026-08-23 05:06:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 25855fd4-e84a-3856-bacc-4397e72d88dc | -16.06337 | -50.43049 | 2026-08-23 05:06:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 5fd89b1a-0411-3b7f-ac85-f6460106ab40 | -12.59427 | -47.88579 | 2026-08-23 05:06:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 8912e9b3-a546-3add-b983-d12e4032d626 | -17.21294 | -47.52299 | 2026-08-23 05:06:00 | NOAA-20 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 8.9 |
| e826c0d6-8829-3b8f-8a2d-147827170937 | -12.64629 | -47.6416 | 2026-08-23 05:06:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 89b932e4-541f-3d5a-8592-2e65cfc84290 | -14.4318 | -52.91682 | 2026-08-23 05:06:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ac8be9a1-b652-3ccd-a689-ed1ae3bd3541 | -14.38971 | -51.78355 | 2026-08-23 05:06:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 63ba0821-f48f-35d6-a3ac-27eb0bfb21eb | -16.05905 | -50.42993 | 2026-08-23 05:06:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 7.4 |
| e7a1b7d7-19d0-3d84-a72b-a2272d7709cb | -16.05368 | -50.43767 | 2026-08-23 05:06:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 6834b161-6dd2-3c57-9243-94730827abca | -13.14827 | -51.42557 | 2026-08-23 05:06:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 31.1 |
| 8ea243c3-ba0d-3a47-82aa-b32596dce935 | -14.36262 | -51.77956 | 2026-08-23 05:06:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 16c7315b-781a-3b81-9bb3-a1041bf15d41 | -16.26804 | -57.6666 | 2026-08-23 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| c5d4700a-b70f-34fe-a968-c81642ccd489 | -13.93874 | -45.34824 | 2026-08-23 05:06:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| aa8904f4-27cb-3fdc-a93a-243bc510ac2b | -18.5385 | -47.16087 | 2026-08-23 05:06:00 | NOAA-20 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5273c2de-024d-3f83-8c63-0566351470f9 | -15.04594 | -48.69441 | 2026-08-23 05:06:00 | NOAA-20 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 57375a7b-d3ab-365c-8aef-fc46cd7a6fe5 | -16.40071 | -51.85186 | 2026-08-23 05:06:00 | NOAA-20 | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 932daad2-64aa-30fa-b35f-08f21398b697 | -16.74684 | -49.34486 | 2026-08-23 05:06:00 | NOAA-20 | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 521030a6-29fd-3dce-bbe0-68b93dc17be1 | -14.80124 | -48.78411 | 2026-08-23 05:06:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 29.2 |
| 0bb3e668-68ee-334c-ba1b-bc316367e95d | -13.17231 | -51.424 | 2026-08-23 05:06:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 743cbdd7-cd6c-3b14-99b9-89e3f73a61b2 | -15.55298 | -56.3159 | 2026-08-23 05:06:00 | NOAA-20 | VÁRZEA GRANDE | MATO GROSSO | Brasil | 5108402 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 657a05ef-4e63-3d33-87a3-748d264d8660 | -16.0542 | -50.43353 | 2026-08-23 05:06:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 4d879849-103c-3cde-9e08-c5954dcb8d22 | -13.16632 | -51.43838 | 2026-08-23 05:06:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5f54c957-4e5a-352b-9064-c0247d3876f3 | -13.16313 | -51.43283 | 2026-08-23 05:06:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 64dd2b73-e62a-3f60-8ced-b5f75924e21c | -12.84992 | -48.47409 | 2026-08-23 05:06:00 | NOAA-20 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 5bc98f35-c623-3c91-8cfd-d87285cbaa76 | -14.95723 | -52.65908 | 2026-08-23 05:06:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 23bbf951-1889-3a45-bed4-50f63bfab2d3 | -13.17691 | -51.41957 | 2026-08-23 05:06:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 586dd282-a818-35a5-9327-6f6564e33b04 | -16.058 | -50.43824 | 2026-08-23 05:06:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 8.7 |
| cf8c2e67-2bb7-3741-86dd-49fd590fdd7c | -17.9043 | -44.50523 | 2026-08-23 05:06:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2aefbc4d-6200-36c0-a486-7a1044b4e15b | -17.20761 | -47.52246 | 2026-08-23 05:06:00 | NOAA-20 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 4db6f6e5-0e7a-3b08-8d30-bf6967347b6b | -17.91082 | -44.5055 | 2026-08-23 05:06:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1b8d00d2-c0d1-3348-9675-9c5f867d3e79 | -16.05315 | -50.44184 | 2026-08-23 05:06:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 9e014db2-7500-3b8b-97b5-2f577c76e6ea | -12.65051 | -47.64794 | 2026-08-23 05:06:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 50be1e1c-07d5-3b5a-a647-f934a7e22264 | -16.04935 | -50.43723 | 2026-08-23 05:06:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 61.8 |
| 45409b6c-b0bc-33f3-83d4-367b44b7355e | -13.88582 | -53.98595 | 2026-08-23 05:06:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f0f54f50-7fdd-3179-a044-46a42ce8eb9f | -13.18787 | -51.42626 | 2026-08-23 05:06:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 2484887b-f325-390f-941a-5b6cb8eaa880 | -16.40359 | -51.84016 | 2026-08-23 05:06:00 | NOAA-20 | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5c6d444d-043d-3d7c-98c1-0ec4227728a1 | -17.15802 | -46.41091 | 2026-08-23 05:06:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| fc741779-7e3d-3a2d-9573-7f378781ae19 | -13.83527 | -54.01765 | 2026-08-23 05:06:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 347de644-f212-3381-86ac-2c567c281f3d | -14.4045 | -51.79076 | 2026-08-23 05:06:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 79887121-d6d5-33ef-808b-d9b950de7b86 | -14.35974 | -51.82957 | 2026-08-23 05:06:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a420ba4d-ea67-36a5-ac09-accc44d9a83f | -12.11989 | -57.205 | 2026-08-23 05:06:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0bbbdaa2-64ad-365d-a268-4a8b991bb95f | -14.40332 | -52.93465 | 2026-08-23 05:06:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 665a8531-87ba-36ca-848f-7ca156f02fa8 | -13.59081 | -55.16468 | 2026-08-23 05:06:00 | NOAA-20 | SORRISO | MATO GROSSO | Brasil | 5107925 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 3fd7b642-fcd6-39bc-bac7-afe95ae2337c | -13.58247 | -55.17439 | 2026-08-23 05:06:00 | NOAA-20 | SORRISO | MATO GROSSO | Brasil | 5107925 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2a50bf96-cd6c-3b9b-a3af-4870e47ce875 | -18.52704 | -47.16319 | 2026-08-23 05:06:00 | NOAA-20 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 9.6 |
| a9a22eef-f249-30cb-a563-d1d48191f405 | -14.50652 | -59.83126 | 2026-08-23 05:06:00 | NOAA-20 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 470bc43b-a8be-3626-9741-9fec85377489 | -18.51052 | -46.59919 | 2026-08-23 05:06:00 | NOAA-20 | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6576edd4-ab09-3fdc-9e22-6cb85179d97b | -13.45708 | -57.05499 | 2026-08-23 05:06:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d85570bd-d348-3d9e-ac78-1b2974995261 | -14.52088 | -52.00955 | 2026-08-23 05:06:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| dac9f5e0-7511-3729-995d-5df3d7c5f18b | -13.1967 | -51.4479 | 2026-08-23 05:06:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c5dcf04c-306d-3110-834b-7b126a70dd1f | -15.04116 | -48.69373 | 2026-08-23 05:06:00 | NOAA-20 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 5120a908-8e8d-3533-9d38-48eeea5a0c65 | -14.50268 | -59.81421 | 2026-08-23 05:06:00 | NOAA-20 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 35c691fd-7723-362d-b6c5-c078569c70f4 | -18.52743 | -47.1595 | 2026-08-23 05:06:00 | NOAA-20 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 45d51af3-7ae5-3031-9c77-bc6aa8c2bb06 | -16.05263 | -50.44603 | 2026-08-23 05:06:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 21773fca-1e8d-38ef-b7c9-6e115b320d96 | -14.08803 | -53.98899 | 2026-08-23 05:06:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 8ea36230-0f48-32f3-bab1-c2fb336d40e3 | -12.05826 | -58.04422 | 2026-08-23 05:06:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 07ebe368-c981-36bc-82b4-b9426ee8a553 | -17.15994 | -46.41046 | 2026-08-23 05:06:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 52b08ab4-d367-3da3-a9ed-d79d418c167e | -15.72925 | -56.01458 | 2026-08-23 05:06:00 | NOAA-20 | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| e138ff33-bc84-3126-a7be-ba881000c2c4 | -14.34992 | -51.77527 | 2026-08-23 05:06:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 705be17b-2f3a-30ee-808a-d1eb37df073c | -14.38584 | -51.78298 | 2026-08-23 05:06:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e46812e7-4fe0-3489-999e-25362c235426 | -12.72718 | -48.39578 | 2026-08-23 05:06:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| ab2e764f-4e03-385b-a851-e19453883ade | -18.5162 | -46.60054 | 2026-08-23 05:06:00 | NOAA-20 | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| dd683457-bc71-3493-9e16-72366aa7d1c0 | -18.51537 | -46.59782 | 2026-08-23 05:06:00 | NOAA-20 | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |


[Clique aqui para ver as próximas entradas](README57.md)
