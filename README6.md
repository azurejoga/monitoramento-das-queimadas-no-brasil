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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6ea3a982-7a1b-3e8b-9bb7-5ded4231e9ae | -13.1724 | -54.924999 | 2025-08-18 00:58:00 | METOP-C | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b395e1ff-c241-353c-b045-ebfaa8133a1f | -6.1541 | -49.880501 | 2025-08-18 00:58:00 | METOP-C | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2e029894-1300-30c3-8035-8fd97b7483e4 | -21.794001 | -47.5513 | 2025-08-18 00:58:00 | METOP-C | SANTA RITA DO PASSA QUATRO | SÃO PAULO | Brasil | 3547502 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 4ecdc3ab-0774-3d06-8618-9dc64747877d | -15.0006 | -54.7928 | 2025-08-18 01:00:00 | GOES-19 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 93.0 |
| 495c28cb-7efb-3e2e-9904-8298541bcfd4 | -12.9971 | -56.8395 | 2025-08-18 01:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 96.3 |
| b2ad18a6-dd1a-3dbf-8261-d8b9b5a9ddc3 | -17.4045 | -42.6186 | 2025-08-18 01:00:00 | GOES-19 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 83.6 |
| b5706855-cd11-38da-aac8-195baa3751a4 | -17.17 | -46.2182 | 2025-08-18 01:00:00 | GOES-19 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 78.8 |
| be2d29ae-d265-3603-bc0c-f2dad678c3f9 | -13.219 | -50.7566 | 2025-08-18 01:00:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 51.5 |
| f3469f12-a68a-3b55-89a9-3926eebe0cce | -14.9815 | -54.7743 | 2025-08-18 01:00:00 | GOES-19 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 68.3 |
| f5176e07-01e1-3240-87e9-87e18eff4162 | -13.2375 | -50.7972 | 2025-08-18 01:00:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 54.4 |
| 50c78682-10c8-3f3d-b8de-7559ae81366d | -17.3844 | -42.6235 | 2025-08-18 01:00:00 | GOES-19 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 89.6 |
| 3cd53e00-029a-30ad-b8b6-4c2f36dfb332 | -13.2186 | -50.7781 | 2025-08-18 01:00:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 122.7 |
| 58d1c572-4455-30b8-9fe5-8850559cad32 | -13.2382 | -50.7541 | 2025-08-18 01:00:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 61.1 |
| bbc3b1f9-b78e-34b8-b1b7-44be6009c3a4 | -13.2183 | -50.7996 | 2025-08-18 01:00:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 44.3 |
| d3298952-166b-35cf-b9a7-42125e0a0c1d | -19.1467 | -47.0279 | 2025-08-18 01:00:00 | GOES-19 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 47.7 |
| df70e760-f6e8-388c-af3a-e0caa592361b | -12.9968 | -56.8597 | 2025-08-18 01:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 76.2 |
| 77d104c7-adaa-3e35-8de3-6411c7bf4e08 | -16.2331 | -50.1439 | 2025-08-18 01:00:00 | GOES-19 | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | 70.0 |
| 017db5ba-ff6b-3682-aa98-bea62859243e | -3.9819 | -42.5396 | 2025-08-18 01:00:00 | GOES-19 | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 114.9 |
| 6065c233-a57c-39e0-a518-ed079c29d29a | -13.2378 | -50.7756 | 2025-08-18 01:00:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 131.7 |
| f999ccd7-3566-3c73-9333-b435a74c5e26 | -3.982 | -42.516 | 2025-08-18 01:00:00 | GOES-19 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 89.1 |
| 0d96d517-5f65-3a48-9726-801292d4f4ab | -16.2335 | -50.1218 | 2025-08-18 01:00:00 | GOES-19 | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | 57.7 |
| f1bdf3d2-4a5d-38b6-aa78-31d34b57639b | -6.4335 | -44.7822 | 2025-08-18 01:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 62.9 |
| 54f80a3c-0d7a-36a0-aa74-69048fd33930 | -12.9968 | -56.8597 | 2025-08-18 01:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 85.3 |
| 6f9dfb91-52dd-3282-aaa0-8234a63c811f | -12.978 | -56.8413 | 2025-08-18 01:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 68.8 |
| 797ae8f4-ce42-3153-8754-b6207849387e | -12.9971 | -56.8395 | 2025-08-18 01:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 101.6 |
| 1067c0f2-9a71-3555-80fa-3d1a9969470c | -6.4335 | -44.7822 | 2025-08-18 01:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 65.7 |
| 6b4c262f-59cd-39d8-901b-c19aa73fe4e9 | -16.2331 | -50.1439 | 2025-08-18 01:10:00 | GOES-19 | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | 62.7 |
| 7d9d4643-a917-38b4-b03f-88de9ac163b1 | -13.2186 | -50.7781 | 2025-08-18 01:10:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 44.4 |
| fb1703e6-cee0-324e-a394-7ca6a3d87e21 | -3.982 | -42.516 | 2025-08-18 01:10:00 | GOES-19 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 66.9 |
| 17a4c6c0-db6d-3f34-9375-a30c36f8883a | -16.2335 | -50.1218 | 2025-08-18 01:10:00 | GOES-19 | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | 81.4 |
| 3a2898ab-21c8-3cca-be9c-0e5674c290fc | -17.4045 | -42.6186 | 2025-08-18 01:10:00 | GOES-19 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 109.4 |
| abdd1d9a-3add-331b-a836-ab799378b1b7 | -15.0006 | -54.7928 | 2025-08-18 01:10:00 | GOES-19 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 82.9 |
| 76aca1a0-3a06-3b63-acb6-dc7471922615 | -19.167 | -47.0234 | 2025-08-18 01:10:00 | GOES-19 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 48.5 |
| 90218277-2095-37c6-8f51-769532295f6d | -17.3844 | -42.6235 | 2025-08-18 01:10:00 | GOES-19 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 77.6 |
| ce7ae799-6370-30ad-af42-bcfc116a11d1 | -19.1467 | -47.0279 | 2025-08-18 01:10:00 | GOES-19 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 50.8 |
| 6d5c27c5-a96e-3d9c-a736-f5bf7f195ded | -3.9819 | -42.5396 | 2025-08-18 01:10:00 | GOES-19 | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 64.8 |
| 616e74ad-391e-3045-b7ba-29f854195b2b | -16.2532 | -50.1186 | 2025-08-18 01:10:00 | GOES-19 | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | 53.5 |
| 1a08ef40-161a-3b09-ad47-baebd324c77d | -17.17 | -46.2182 | 2025-08-18 01:10:00 | GOES-19 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 127.8 |
| 075de0cb-a3db-3681-ade2-59f778f4456d | -12.9778 | -56.8614 | 2025-08-18 01:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 68.7 |
| a3024f7e-db4e-33c8-941d-37fee6195c1e | -13.1746 | -54.9337 | 2025-08-18 01:10:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 53.3 |
| 13849306-cbdc-3531-a657-5b880358960f | -17.17 | -46.2182 | 2025-08-18 01:20:00 | GOES-19 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 272.1 |
| 6f1be1fa-6bad-37d6-8e9f-6d9b03fd957f | -15.462 | -49.6303 | 2025-08-18 01:20:00 | GOES-19 | URUANA | GOIÁS | Brasil | 5221700 | 52 | 33 | nan | nan | nan | Cerrado | 165.6 |
| 3c306fe8-fce7-34c6-8b4d-199b8f9c7fcf | -12.9971 | -56.8395 | 2025-08-18 01:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 110.0 |
| 29c70e48-f0f1-3560-9fa1-6a3976ed03af | -3.9819 | -42.5396 | 2025-08-18 01:20:00 | GOES-19 | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 106.0 |
| dcdb67ba-a46c-3988-87a4-ecad14164437 | -9.518 | -60.5268 | 2025-08-18 01:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 50.5 |
| 0a846f17-861d-3a88-bbf9-822f7cc5aa30 | -15.4421 | -49.6555 | 2025-08-18 01:20:00 | GOES-19 | URUANA | GOIÁS | Brasil | 5221700 | 52 | 33 | nan | nan | nan | Cerrado | 73.3 |
| 52138ea1-8144-3fee-afa9-662b244daf34 | -17.1501 | -46.2224 | 2025-08-18 01:20:00 | GOES-19 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 48.2 |
| f11a862f-b5b9-3028-abc7-003d9dced3cd | -6.4335 | -44.7822 | 2025-08-18 01:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 80.4 |
| ec28b95f-1e5b-358e-b710-90445bca37e8 | -12.978 | -56.8413 | 2025-08-18 01:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 68.9 |
| 02271b94-196b-3f78-826b-67c61085b94d | -3.982 | -42.516 | 2025-08-18 01:20:00 | GOES-19 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 89.5 |
| 7f5123c0-c172-3396-a210-f8321142407c | -15.4616 | -49.6524 | 2025-08-18 01:20:00 | GOES-19 | URUANA | GOIÁS | Brasil | 5221700 | 52 | 33 | nan | nan | nan | Cerrado | 216.0 |
| deab7fae-23aa-31da-85b3-30d5e6b8337b | -13.1746 | -54.9337 | 2025-08-18 01:20:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 61.0 |
| 5521658f-7082-3996-a8d0-775e54e0411f | -17.1694 | -46.2417 | 2025-08-18 01:20:00 | GOES-19 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 53.4 |
| d9192112-647c-326c-a293-f855f8ce773e | -12.9778 | -56.8614 | 2025-08-18 01:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 67.4 |
| d5088d6f-612a-3279-8b8e-d3885b4b4065 | -15.4425 | -49.6334 | 2025-08-18 01:20:00 | GOES-19 | URUANA | GOIÁS | Brasil | 5221700 | 52 | 33 | nan | nan | nan | Cerrado | 60.6 |
| 161c8f4c-3d22-3a68-a302-098f78d790fe | -17.3844 | -42.6235 | 2025-08-18 01:20:00 | GOES-19 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 59.5 |
| 00fc8dc8-e08f-352c-a22f-77cc06f070b6 | -19.167 | -47.0234 | 2025-08-18 01:20:00 | GOES-19 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 55.2 |
| 21873616-5d57-3258-a7f6-9d4208f070fe | -17.4045 | -42.6186 | 2025-08-18 01:20:00 | GOES-19 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 109.4 |
| 1d4c38ea-5fbb-3297-94b4-25b7348d5f9a | -12.9968 | -56.8597 | 2025-08-18 01:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 92.8 |
| f957f77a-9cac-325d-b82c-842c59629fc2 | -15.4816 | -49.6271 | 2025-08-18 01:20:00 | GOES-19 | URUANA | GOIÁS | Brasil | 5221700 | 52 | 33 | nan | nan | nan | Cerrado | 45.0 |
| 7f6fcbca-b8c3-320c-a55d-4463da28aa3b | -12.978 | -56.8413 | 2025-08-18 01:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 59.6 |
| ac9ae036-2095-3749-a73a-18a9ea5b182d | -9.518 | -60.5268 | 2025-08-18 01:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 50.4 |
| 8ff10b5e-625e-3c14-ab3a-120ed4e49459 | -3.9819 | -42.5396 | 2025-08-18 01:30:00 | GOES-19 | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 101.7 |
| 2ce30ce5-b8c1-35e9-9f91-5c72e632630b | -17.3844 | -42.6235 | 2025-08-18 01:30:00 | GOES-19 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 57.2 |
| 63098789-6006-3c25-b730-7bf0bb95ba42 | -13.1746 | -54.9337 | 2025-08-18 01:30:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 65.6 |
| 05ab33fc-960a-36c9-b8c9-e0df5ae5c70a | -12.9968 | -56.8597 | 2025-08-18 01:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 85.3 |
| cd77ec72-a2f9-3029-8a39-470842ad1a0a | -17.17 | -46.2182 | 2025-08-18 01:30:00 | GOES-19 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 105.0 |
| 20c3be4c-cc43-3a53-a79f-9b34c9117401 | -12.9778 | -56.8614 | 2025-08-18 01:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 58.2 |
| 04dab18b-3de2-3e3f-a161-ecbc17ce6a18 | -6.4335 | -44.7822 | 2025-08-18 01:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 68.0 |
| b7bb0e43-8a36-3c2f-8b9d-c6c7588e4eab | -12.9971 | -56.8395 | 2025-08-18 01:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 106.1 |
| 3a62769e-a871-36e6-9a7d-803562218dbd | -3.982 | -42.516 | 2025-08-18 01:30:00 | GOES-19 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 85.9 |
| b1525083-d3eb-3f58-aed6-e3a2f2e3eb18 | -17.4045 | -42.6186 | 2025-08-18 01:30:00 | GOES-19 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 103.8 |
| 4303770a-106b-38c9-b77a-bafbf72aac27 | -12.9971 | -56.8395 | 2025-08-18 01:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 102.0 |
| 27d6eb26-d2aa-32af-99ea-3de7f7121196 | -13.1746 | -54.9337 | 2025-08-18 01:40:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 53.1 |
| 2aab484a-a45d-3666-a7d2-337c573d70ab | -17.4045 | -42.6186 | 2025-08-18 01:40:00 | GOES-19 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 73.8 |
| 2a7a4609-213e-354c-90c4-fa960dbf9e03 | -9.518 | -60.5268 | 2025-08-18 01:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 51.1 |
| e3722b71-b148-3d1d-9013-112e28724fe9 | -17.3844 | -42.6235 | 2025-08-18 01:40:00 | GOES-19 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 97.5 |
| 0361b75c-a6f9-3ae5-9922-6ffc82c4933b | -6.5678 | -44.4738 | 2025-08-18 01:40:00 | GOES-19 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 63.4 |
| 8e7badcc-87d4-3968-8720-157fe27bbc70 | -3.982 | -42.516 | 2025-08-18 01:40:00 | GOES-19 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 69.8 |
| 7fc4dcf5-8133-3e94-a5a6-dc174e466de2 | -6.4335 | -44.7822 | 2025-08-18 01:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 69.9 |
| 736fc704-02cc-385d-8497-c141558884bd | -12.9968 | -56.8597 | 2025-08-18 01:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 85.1 |
| 896046c1-ade0-3aaa-bb4a-80dd1c20fd11 | -3.9819 | -42.5396 | 2025-08-18 01:40:00 | GOES-19 | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 86.3 |
| 4ee1ccfb-b58f-36b0-886a-aed4f0c1b085 | -12.9853 | -56.83701 | 2025-08-18 01:47:00 | TERRA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 65.0 |
| 0399c701-897b-34a7-9d08-2ec5f6b3b570 | -12.98929 | -56.84312 | 2025-08-18 01:47:00 | TERRA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 111.1 |
| 0bf1fc0c-e404-35c7-b6cc-16d326686622 | -12.99082 | -56.86736 | 2025-08-18 01:47:00 | TERRA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 88.2 |
| 460803d2-2aa8-3575-935c-45ec91a148b9 | -12.99455 | -56.87328 | 2025-08-18 01:47:00 | TERRA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 57.5 |
| 9edd171a-3348-3945-90e1-0bcda35410aa | -13.13227 | -57.14042 | 2025-08-18 01:47:00 | TERRA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 25.8 |
| 971d3085-76ad-31bd-95e7-9ee603582c87 | -15.00784 | -54.80942 | 2025-08-18 01:47:00 | TERRA_M-M | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 58.1 |
| 62b9c604-bb05-3384-8a60-d6eea7a7c86c | -13.13375 | -57.14557 | 2025-08-18 01:47:00 | TERRA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 33.1 |
| e8b8afff-5bf8-3129-bb85-455f2b7442cc | -13.00453 | -56.83999 | 2025-08-18 01:47:00 | TERRA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 44.1 |
| 75ecabf5-91f4-3881-affe-d9c1ac83d9b9 | -13.13738 | -57.16864 | 2025-08-18 01:47:00 | TERRA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 22.7 |
| 3266d96c-10ac-3854-8050-a33ff128d0ca | -13.00978 | -56.87027 | 2025-08-18 01:47:00 | TERRA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 26.3 |
| 9431ca80-8acb-3c7c-9716-f6fe207c28fb | -13.00604 | -56.86431 | 2025-08-18 01:47:00 | TERRA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 47.8 |
| 864c0047-b0a0-3e92-aaff-e5768e173ed5 | -13.00056 | -56.83402 | 2025-08-18 01:47:00 | TERRA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 41.5 |
| bbab3ab2-d4aa-3f27-a9ba-daf0f586ad40 | -14.98337 | -54.77328 | 2025-08-18 01:47:00 | TERRA_M-M | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 52.1 |
| e6b913d9-85e1-3eaf-8e8d-b53304e62069 | -13.1746 | -54.9337 | 2025-08-18 01:50:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 49.6 |
| 903295a6-6d79-3715-90f2-9c0a79665de2 | -12.9971 | -56.8395 | 2025-08-18 01:50:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 90.4 |
| a04cbfce-8b55-3fef-8ae2-19bd41980210 | -17.4045 | -42.6186 | 2025-08-18 01:50:00 | GOES-19 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 90.4 |
| 93bf77cd-7998-3678-af4c-7077b7a1ed5e | -17.3844 | -42.6235 | 2025-08-18 01:50:00 | GOES-19 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 67.1 |
| 611f3990-3304-3d72-9652-3ec0330e3271 | -21.4869 | -47.7663 | 2025-08-18 01:50:00 | GOES-19 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 51.8 |


[Clique aqui para ver as próximas entradas](README7.md)
