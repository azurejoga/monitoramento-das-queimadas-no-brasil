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

## Dados Diários - Página 100

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3d8e6f46-5822-31e6-8942-e1811b375fe9 | -18.34272 | -51.6982 | 2025-10-17 04:53:00 | NPP-375D | SERRANÓPOLIS | GOIÁS | Brasil | 5220504 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 965e3af1-9855-3a6d-ad5b-000040bce524 | -18.04335 | -50.93975 | 2025-10-17 04:53:00 | NPP-375D | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a1aaf8c5-984a-3ac3-972e-47a17ecdd3d8 | -16.55162 | -52.44093 | 2025-10-17 04:53:00 | NPP-375D | DOVERLÂNDIA | GOIÁS | Brasil | 5207253 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9fd231a4-3d6f-325c-8206-8cbbc162346a | -19.44088 | -55.92161 | 2025-10-17 04:53:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 19d7d62e-ee12-39cb-b73e-2ac43ff22ad3 | -18.09324 | -42.45158 | 2025-10-17 04:53:00 | NPP-375D | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 18da3dfd-b9e8-3de4-b2dc-85e94033a429 | -15.82235 | -53.60272 | 2025-10-17 04:53:00 | NPP-375D | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9e24f8a3-f277-3ad5-be62-1d9425475ba6 | -18.27198 | -51.30172 | 2025-10-17 04:53:00 | NPP-375D | APARECIDA DO RIO DOCE | GOIÁS | Brasil | 5201454 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 353cf61f-ac51-3245-a99d-8514e9bff4fa | -17.56658 | -45.60758 | 2025-10-17 04:53:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| b709181d-c6ad-3b7e-ac01-6bb4decd8784 | -19.45112 | -55.92352 | 2025-10-17 04:53:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 838d2da2-fcde-3dd7-88bf-8d62af4b3a85 | -17.96294 | -39.88388 | 2025-10-17 04:53:00 | NPP-375D | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 2e3541a8-c2aa-33a9-bca9-7cbebee8311d | -18.35028 | -51.70718 | 2025-10-17 04:53:00 | NPP-375D | SERRANÓPOLIS | GOIÁS | Brasil | 5220504 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 89e03edf-e1c8-3cbd-8548-003995effbfc | -14.89777 | -52.42727 | 2025-10-17 04:53:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| eda09faa-00c4-3eb5-b86d-571a44d2e595 | -18.08719 | -42.45095 | 2025-10-17 04:53:00 | NPP-375D | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.8 |
| 90a481a6-3998-33f7-91aa-8faa1f190257 | -19.44218 | -55.91386 | 2025-10-17 04:53:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 0.9 |
| fd3df0d7-4ca2-382f-8556-dc05774e3f35 | -18.3352 | -51.70106 | 2025-10-17 04:53:00 | NPP-375D | SERRANÓPOLIS | GOIÁS | Brasil | 5220504 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 99704fec-9b86-3d91-b981-d611f903dcce | -18.33233 | -51.69649 | 2025-10-17 04:53:00 | NPP-375D | SERRANÓPOLIS | GOIÁS | Brasil | 5220504 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c7baa773-3093-356e-b02b-7cdde2a3c9a4 | -14.89443 | -52.42673 | 2025-10-17 04:53:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 434c49bc-38ca-33f1-bc8e-a1564102a207 | -18.09417 | -42.45042 | 2025-10-17 04:53:00 | NPP-375D | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.7 |
| 30e1544f-ae64-34d2-9b86-85029be4eb7b | -18.34212 | -51.70219 | 2025-10-17 04:53:00 | NPP-375D | SERRANÓPOLIS | GOIÁS | Brasil | 5220504 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2e88ed7c-2f93-3d64-8696-c26341d638de | -17.2 | -46.97296 | 2025-10-17 04:53:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2d3036a8-6eaf-362f-89d3-77f077333d69 | -14.8682 | -52.42965 | 2025-10-17 04:53:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 32e4e860-abc9-3128-b937-f12bd64bc51a | -21.43404 | -54.15619 | 2025-10-17 04:53:00 | NPP-375D | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fced3f0c-deb3-32f3-9d3a-2ad696916ed1 | -18.345 | -51.70671 | 2025-10-17 04:53:00 | NPP-375D | SERRANÓPOLIS | GOIÁS | Brasil | 5220504 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e84b7ec3-d1ee-3186-bce7-aacd8dde487e | -14.87766 | -52.43489 | 2025-10-17 04:53:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 12a22dc1-4b3d-318d-b816-3868bd721829 | -19.44836 | -55.91901 | 2025-10-17 04:53:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 63055672-f9a1-3cf7-ade8-219c95b9f94a | -18.08812 | -42.44981 | 2025-10-17 04:53:00 | NPP-375D | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.7 |
| 2f6eccf9-520e-318f-b2af-214c4eed3850 | -16.39971 | -41.96133 | 2025-10-17 04:53:00 | NPP-375D | ITINGA | MINAS GERAIS | Brasil | 3134004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 55a990db-d97a-3aa9-a63c-fd612813bf9d | -18.25767 | -47.82132 | 2025-10-17 04:53:00 | NPP-375D | OUVIDOR | GOIÁS | Brasil | 5215504 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 07f49bce-93d3-3c69-9dee-051d847b6730 | -14.89499 | -52.42313 | 2025-10-17 04:53:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ee1de79d-f9c6-3db2-b126-f2f4e4412404 | -14.89221 | -52.41896 | 2025-10-17 04:53:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 12cfa933-1e5d-3a9a-9d69-6a0697903059 | -18.3807 | -55.4645 | 2025-10-17 04:53:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 6ff4464a-0ef1-311c-85ce-1011e27abfe0 | -19.4477 | -55.92289 | 2025-10-17 04:53:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 5.6 |
| 6174fd67-8d69-3b08-a9ae-832ee8ca9d97 | -14.87154 | -52.43021 | 2025-10-17 04:53:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a0ecc62e-5bf7-3541-85a7-2d25567393f6 | -16.65981 | -51.55921 | 2025-10-17 04:53:00 | NPP-375D | PALESTINA DE GOIÁS | GOIÁS | Brasil | 5215652 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5e63229b-8dc9-31dd-adbd-40a2aa1cd80a | -18.34154 | -51.70617 | 2025-10-17 04:53:00 | NPP-375D | SERRANÓPOLIS | GOIÁS | Brasil | 5220504 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e2fcf035-9151-3179-8f01-2776ed651c95 | -14.89555 | -52.41952 | 2025-10-17 04:53:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| aa32074a-12f8-33ee-a337-790f4ec461de | -18.02526 | -54.02432 | 2025-10-17 04:53:00 | NPP-375D | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7e2856d8-7da9-32f8-98d9-d83b73556648 | -19.21662 | -44.11845 | 2025-10-17 04:53:00 | NPP-375D | CORDISBURGO | MINAS GERAIS | Brasil | 3118908 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 64aea7e3-3435-3611-88b5-7d14fbc523b0 | -18.33866 | -51.70163 | 2025-10-17 04:53:00 | NPP-375D | SERRANÓPOLIS | GOIÁS | Brasil | 5220504 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cea9ae3e-7bfb-3382-a0ff-80ff824bbdcf | -18.08762 | -42.44671 | 2025-10-17 04:53:00 | NPP-375D | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.8 |
| 05a8eca5-6c34-366b-ba9e-ab5a604b37e9 | -17.96996 | -39.88461 | 2025-10-17 04:53:00 | NPP-375D | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| 12140955-b6ee-3405-8e08-37cfcfdc4da0 | -14.87211 | -52.42659 | 2025-10-17 04:53:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 14c31711-38e3-3eb7-a6ac-c257578b1a21 | -17.56722 | -45.60202 | 2025-10-17 04:53:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0b00c09e-c534-366b-a25c-524c29373a7d | -18.08673 | -42.4554 | 2025-10-17 04:53:00 | NPP-375D | SÃO SEBASTIÃO DO MARANHÃO | MINAS GERAIS | Brasil | 3164506 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.7 |
| bb81697f-f281-369a-9010-e0d6d5cab1b7 | -21.43616 | -54.15589 | 2025-10-17 04:53:00 | NPP-375D | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b4049f65-b80c-3f42-b981-6fee911934d4 | -19.05952 | -57.4906 | 2025-10-17 04:53:00 | NPP-375D | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 2.1 |
| f230206b-8d29-32c2-bb1f-3bb5f4f31e2a | -14.87042 | -52.4374 | 2025-10-17 04:53:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1e68a185-f79a-30f8-a408-8ffe9ab6c695 | -18.56462 | -54.54097 | 2025-10-17 04:53:00 | NPP-375D | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a481a3c3-cd81-398f-999b-578dac8f38be | -17.57149 | -45.60811 | 2025-10-17 04:53:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 40e1c540-7d1e-302e-9c90-7eff937014d6 | -14.89888 | -52.42007 | 2025-10-17 04:53:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7d6b9899-7f19-34e8-9d68-e86083212ad0 | -18.2755 | -51.30227 | 2025-10-17 04:53:00 | NPP-375D | APARECIDA DO RIO DOCE | GOIÁS | Brasil | 5201454 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5f45cc48-9001-3785-882a-5bbcbf30952e | -18.38197 | -55.45688 | 2025-10-17 04:53:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 51ecf2ba-70c5-3cf2-af6a-d213b0fd0d39 | -19.21623 | -44.12223 | 2025-10-17 04:53:00 | NPP-375D | CORDISBURGO | MINAS GERAIS | Brasil | 3118908 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 69a42e6f-ef14-3cf4-9187-df3860b0ad9b | -21.43559 | -54.15961 | 2025-10-17 04:53:00 | NPP-375D | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0bbc0289-ca9c-3d91-bf02-304c88b35767 | -18.08853 | -42.44548 | 2025-10-17 04:53:00 | NPP-375D | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.7 |
| d868a130-a028-32c1-921a-60d491cfcfb0 | -27.82735 | -50.30433 | 2025-10-17 04:53:00 | NPP-375D | LAGES | SANTA CATARINA | Brasil | 4209300 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 40872c52-c979-3ef6-b681-b8e073d6d46f | -14.87098 | -52.4338 | 2025-10-17 04:53:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 569e47a6-31ff-3fa7-954e-55feef09446b | -19.43812 | -55.91709 | 2025-10-17 04:53:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 3639ba20-54e7-3451-b96f-ac43b4146cad | -20.38858 | -50.44356 | 2025-10-17 04:53:00 | NPP-375D | ESTRELA D'OESTE | SÃO PAULO | Brasil | 3515202 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| e5239a3e-a155-3f46-b673-02b772fa6543 | -19.4456 | -55.9145 | 2025-10-17 04:53:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 399968ab-0eec-3925-bad1-80f6355b9441 | -15.6534 | -48.36263 | 2025-10-17 04:53:00 | NPP-375D | COCALZINHO DE GOIÁS | GOIÁS | Brasil | 5205513 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 57208b07-8ba0-3267-949b-7931ecce51d1 | -19.45177 | -55.91965 | 2025-10-17 04:53:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.1 |
| aad47017-bc5f-3994-b6e2-ce4afccfe067 | -18.3841 | -55.46513 | 2025-10-17 04:53:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| eff01dc5-a8b9-3cc4-bca8-dd0db2e846e0 | -14.89721 | -52.43087 | 2025-10-17 04:53:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f5d9717a-2d0f-3d98-8df4-ca83ef155800 | -16.35532 | -43.41521 | 2025-10-17 04:53:00 | NPP-375D | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 597ad957-e867-32d8-b146-b3e96324c1cf | -14.68303 | -60.26216 | 2025-10-17 04:53:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ccbb4e62-c929-3379-871b-af8e8bacd426 | -18.08771 | -42.45409 | 2025-10-17 04:53:00 | NPP-375D | SÃO SEBASTIÃO DO MARANHÃO | MINAS GERAIS | Brasil | 3164506 | 31 | 33 | nan | nan | nan | Mata Atlântica | 14.6 |
| 856a2e18-f22c-3130-8441-8104c8db77bf | -17.4057 | -53.25673 | 2025-10-17 04:53:00 | NPP-375D | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 4d61d53d-03df-3a82-ae04-6300f25da7f6 | -18.38536 | -55.4575 | 2025-10-17 04:53:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 5ff319d0-6435-3b15-8b09-5d4976d0c020 | -18.34559 | -51.70275 | 2025-10-17 04:53:00 | NPP-375D | SERRANÓPOLIS | GOIÁS | Brasil | 5220504 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| eb138363-20d7-324d-9e1c-c078643562fe | -19.21034 | -44.1253 | 2025-10-17 04:53:00 | NPP-375D | CORDISBURGO | MINAS GERAIS | Brasil | 3118908 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 62619b3b-2cc5-3287-aa9c-f2c3307452fa | -18.386 | -55.45369 | 2025-10-17 04:53:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.8 |
| c6b1b8b6-c779-3a3d-86bb-326773dae41b | -18.34738 | -51.70267 | 2025-10-17 04:53:00 | NPP-375D | SERRANÓPOLIS | GOIÁS | Brasil | 5220504 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a8ef765e-b6b6-3ded-8fd4-1d511903265a | -16.40014 | -41.95716 | 2025-10-17 04:53:00 | NPP-375D | ITINGA | MINAS GERAIS | Brasil | 3134004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 4c52c683-7f51-38bd-8559-c8aa45fe2f1d | -16.68569 | -52.13244 | 2025-10-17 04:53:00 | NPP-375D | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| fefa4dbc-3d51-3edd-89b4-df6a26454526 | -14.89388 | -52.43032 | 2025-10-17 04:53:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 0bdb1963-af50-3b2d-8451-70577fda1772 | -18.3875 | -55.46574 | 2025-10-17 04:53:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| de712081-10c1-3065-a558-d599120c4bac | -14.86764 | -52.43325 | 2025-10-17 04:53:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0f7344e6-c518-30b8-8fbd-331d12ca1644 | -19.44429 | -55.92225 | 2025-10-17 04:53:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 5.6 |
| 2130b52a-4a72-31f2-82a9-e40da9df2f62 | -19.45519 | -55.92028 | 2025-10-17 04:53:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 5ae834b4-314c-3636-989a-08cc5ea7782f | -15.83727 | -53.97175 | 2025-10-17 04:53:00 | NPP-375D | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7fea3eb7-60f7-3a06-bb76-997079e96836 | -19.44494 | -55.91837 | 2025-10-17 04:53:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 713540d2-cdc0-3e05-8134-cdd793f1f075 | -15.82464 | -45.77034 | 2025-10-17 04:53:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1eaf7916-335e-38e4-84ec-6aae6b5b3b78 | -19.06317 | -57.4913 | 2025-10-17 04:53:00 | NPP-375D | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 1c0d8413-f3da-36d7-8d05-ad82421ee836 | -19.44901 | -55.91513 | 2025-10-17 04:53:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 8ba1c203-82d4-3357-8fcc-6a2ca30fa429 | -14.89109 | -52.42617 | 2025-10-17 04:53:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5ea740ac-aaab-3191-9a81-944975d7307e | -14.30173 | -58.15245 | 2025-10-17 04:53:00 | NPP-375D | CAMPO NOVO DO PARECIS | MATO GROSSO | Brasil | 5102637 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a910181c-308a-314a-841a-b617b0d898a0 | -18.33638 | -51.69308 | 2025-10-17 04:53:00 | NPP-375D | SERRANÓPOLIS | GOIÁS | Brasil | 5220504 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| fb700cf0-4ecd-32e5-9425-a7f4b2cf9c6b | -16.65582 | -51.56241 | 2025-10-17 04:53:00 | NPP-375D | PALESTINA DE GOIÁS | GOIÁS | Brasil | 5215652 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7101fb1e-e88d-3da5-bcf7-4995b50ba6d1 | -20.38921 | -50.43884 | 2025-10-17 04:53:00 | NPP-375D | ESTRELA D'OESTE | SÃO PAULO | Brasil | 3515202 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| fb5644e9-7d10-3224-999c-ffc07d5a47cf | -14.23393 | -60.19458 | 2025-10-17 04:53:00 | NPP-375D | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2ed8e49c-3ab0-32cc-8b2b-8b54c9173853 | -4.4061 | -43.3816 | 2025-10-17 05:00:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 30.0 |
| ee8a35a3-3b74-3a39-91af-0d7457ad4a3e | -4.4059 | -43.4049 | 2025-10-17 05:00:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 50.0 |
| 13d6ffa5-be7a-3127-86be-fbc42186faff | -3.236 | -45.9639 | 2025-10-17 05:00:00 | GOES-19 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 28.1 |
| 9b6733b6-7d7a-33b6-b97c-44845af8671b | 4.52594 | -60.86028 | 2025-10-17 05:06:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2145edd3-c941-32a6-8246-2cb6e8ce2afd | 4.52651 | -60.86409 | 2025-10-17 05:06:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f7799e2f-4f83-3bf4-9364-37aa145fa9e3 | 3.14081 | -60.335 | 2025-10-17 05:06:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a993e49a-e9f1-355b-81f8-860ee88bb89d | 4.38689 | -59.77368 | 2025-10-17 05:06:00 | NOAA-20 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6c997945-a850-3c19-ba86-cf0ec40e4641 | 4.38744 | -59.77726 | 2025-10-17 05:06:00 | NOAA-20 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c2d19265-9759-33ec-86f7-5ed2d32033be | 4.38287 | -59.77437 | 2025-10-17 05:06:00 | NOAA-20 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |


[Clique aqui para ver as próximas entradas](README101.md)
