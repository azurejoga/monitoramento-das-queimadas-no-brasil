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

## Dados Diários - Página 9

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b863923c-2659-3f42-a239-e21805fadc0f | -14.46906 | -47.07961 | 2024-12-06 12:59:00 | TERRA_M-T | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 14.5 |
| 1a56c323-c8ab-3703-982c-7317dad85754 | -10.73468 | -52.06891 | 2024-12-06 12:59:00 | TERRA_M-T | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 8413455c-a141-3db6-9f21-d0d718dfaafe | -12.86376 | -51.94076 | 2024-12-06 12:59:00 | TERRA_M-T | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 11.3 |
| 9ed90aa2-e75f-3de5-bec1-50fdaf70869d | -11.6776 | -46.43703 | 2024-12-06 12:59:00 | TERRA_M-T | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 69.4 |
| 246e151e-9f45-32e6-9820-4b33fe114405 | -12.23688 | -52.4642 | 2024-12-06 12:59:00 | TERRA_M-T | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 5.7 |
| a01e5297-f4de-3575-a30b-586013509363 | -9.3315 | -50.17154 | 2024-12-06 12:59:00 | TERRA_M-T | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| b80342a7-32e5-31d7-8c47-f98a8295b813 | -18.01627 | -51.38649 | 2024-12-06 13:01:00 | TERRA_M-T | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| afe90a07-73c5-3d42-a161-f92c7c555e0b | -16.40269 | -48.95833 | 2024-12-06 13:01:00 | TERRA_M-T | ANÁPOLIS | GOIÁS | Brasil | 5201108 | 52 | 33 | nan | nan | nan | Cerrado | 10.6 |
| e4fb40c0-db54-3261-9378-47597ac0d414 | -19.87529 | -44.97423 | 2024-12-06 13:01:00 | TERRA_M-T | NOVA SERRANA | MINAS GERAIS | Brasil | 3145208 | 31 | 33 | nan | nan | nan | Cerrado | 31.0 |
| bf2e1a21-51c4-323c-8355-a108fb0b142e | -19.77398 | -49.03748 | 2024-12-06 13:01:00 | TERRA_M-T | COMENDADOR GOMES | MINAS GERAIS | Brasil | 3116902 | 31 | 33 | nan | nan | nan | Cerrado | 18.7 |
| 148f1d46-a446-30d1-b2e9-da105b1ca17c | -17.32343 | -46.56853 | 2024-12-06 13:01:00 | TERRA_M-T | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 63.2 |
| 0810c52b-308c-30c1-9d77-4513f9846460 | -16.32203 | -48.29394 | 2024-12-06 13:01:00 | TERRA_M-T | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 9.2 |
| dfd4ba71-2e3f-3a3b-a908-8760222e9792 | -17.73093 | -44.75195 | 2024-12-06 13:01:00 | TERRA_M-T | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 39.9 |
| 888461f6-7fb2-3e6c-b4c6-08a1aeb8fa55 | -17.30981 | -46.56691 | 2024-12-06 13:01:00 | TERRA_M-T | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 50.7 |
| f0c30c56-0864-38ae-ac69-2a4e06d2bbc0 | -17.80509 | -49.17852 | 2024-12-06 13:01:00 | TERRA_M-T | MORRINHOS | GOIÁS | Brasil | 5213806 | 52 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 2ce041c5-8281-3a39-ab62-e366f612b050 | -15.75413 | -51.81238 | 2024-12-06 13:01:00 | TERRA_M-T | MONTES CLAROS DE GOIÁS | GOIÁS | Brasil | 5213707 | 52 | 33 | nan | nan | nan | Cerrado | 9.8 |
| f5b9f9ac-b273-3868-948a-24357f00690e | -22.65319 | -48.1219 | 2024-12-06 13:01:00 | TERRA_M-T | ANHEMBI | SÃO PAULO | Brasil | 3502309 | 35 | 33 | nan | nan | nan | Cerrado | 23.0 |
| 73bbaf99-3a06-37fa-bdb1-096ee7a2247e | -20.81659 | -49.50658 | 2024-12-06 13:01:00 | TERRA_M-T | MIRASSOL | SÃO PAULO | Brasil | 3530300 | 35 | 33 | nan | nan | nan | Mata Atlântica | 14.8 |
| 246229a0-f22a-334f-8bd8-8fd7fffb834a | -18.10137 | -49.87484 | 2024-12-06 13:01:00 | TERRA_M-T | BOM JESUS DE GOIÁS | GOIÁS | Brasil | 5203500 | 52 | 33 | nan | nan | nan | Cerrado | 15.4 |
| 947d5a6c-7dac-3c27-a252-b433a0c6900a | -17.73677 | -44.74563 | 2024-12-06 13:01:00 | TERRA_M-T | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 45.6 |
| 191f0cc5-c2fb-3113-9b9c-2580898431c6 | -15.75127 | -51.57108 | 2024-12-06 13:01:00 | TERRA_M-T | MONTES CLAROS DE GOIÁS | GOIÁS | Brasil | 5213707 | 52 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 7909cee9-45da-3b3e-94cc-9222027e55f0 | -22.96642 | -53.79003 | 2024-12-06 13:03:00 | TERRA_M-T | NAVIRAÍ | MATO GROSSO DO SUL | Brasil | 5005707 | 50 | 33 | nan | nan | nan | Mata Atlântica | 7.7 |
| c2a412c5-b692-3c36-97c2-706d657a3079 | -25.63614 | -53.34346 | 2024-12-06 13:03:00 | TERRA_M-T | NOVA PRATA DO IGUAÇU | PARANÁ | Brasil | 4117255 | 41 | 33 | nan | nan | nan | Mata Atlântica | 7.7 |
| f601a60d-8f5f-3a0e-94e8-088c36b62bb7 | -28.25171 | -51.89089 | 2024-12-06 13:03:00 | TERRA_M-T | CASEIROS | RIO GRANDE DO SUL | Brasil | 4304952 | 43 | 33 | nan | nan | nan | Mata Atlântica | 11.8 |
| bdce10e8-325f-3f05-96bc-ff10e4e903aa | -29.75339 | -50.90588 | 2024-12-06 13:05:00 | TERRA_M-T | TAQUARA | RIO GRANDE DO SUL | Brasil | 4321204 | 43 | 33 | nan | nan | nan | Mata Atlântica | 27.3 |
| b4d3f7c3-50ef-3fc5-9b69-421e5657c1b4 | -29.758 | -50.90049 | 2024-12-06 13:05:00 | TERRA_M-T | TAQUARA | RIO GRANDE DO SUL | Brasil | 4321204 | 43 | 33 | nan | nan | nan | Mata Atlântica | 16.5 |
| 3b9673c2-ab66-3b18-86e3-66bc10e1bfe3 | -29.75612 | -50.91887 | 2024-12-06 13:05:00 | TERRA_M-T | TAQUARA | RIO GRANDE DO SUL | Brasil | 4321204 | 43 | 33 | nan | nan | nan | Mata Atlântica | 10.0 |
| cd49bfb5-a1e4-3cb3-9c6a-ea8725bc1c88 | -12.6411 | -47.5515 | 2024-12-06 14:10:00 | GOES-16 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 70.4 |
| 2c139e6c-be73-366b-9595-af05640d8009 | -6.1145 | -46.9152 | 2024-12-06 14:20:00 | GOES-16 | LAJEADO NOVO | MARANHÃO | Brasil | 2105989 | 21 | 33 | nan | nan | nan | Cerrado | 96.0 |
| 6a53b19c-5f37-3953-9bd9-6f460e497fba | -6.1145 | -46.9152 | 2024-12-06 14:30:00 | GOES-16 | LAJEADO NOVO | MARANHÃO | Brasil | 2105989 | 21 | 33 | nan | nan | nan | Cerrado | 99.6 |


