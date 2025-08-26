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

## Dados Diários - Página 30

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2807c319-9cd6-38fc-9623-280092de8d63 | -15.02519 | -48.17137 | 2025-08-26 03:57:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 44ec3a21-3cc3-375c-8d3c-b126dfc436c9 | -19.79296 | -47.98229 | 2025-08-26 03:57:00 | NOAA-21 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6ca52f07-7c55-3ab6-800d-2c7b60ea8dee | -12.77753 | -48.11022 | 2025-08-26 03:57:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 5dd0458c-fd6c-3b9e-a196-c0617e8aed87 | -17.78553 | -44.48245 | 2025-08-26 03:57:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 424f8ea7-f1f7-3bf1-b11e-d133a3d01006 | -18.85531 | -47.0051 | 2025-08-26 03:57:00 | NOAA-21 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8006eb67-2215-3e37-9ab6-7b67f4c6d741 | -13.83292 | -46.69353 | 2025-08-26 03:57:00 | NOAA-21 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ef54f995-81ec-3897-8c3c-b44dc68b9157 | -14.11194 | -53.98232 | 2025-08-26 03:57:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 499b4771-b355-3d8f-97e1-0763d8ea8580 | -18.873 | -47.00103 | 2025-08-26 03:57:00 | NOAA-21 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 6.0 |
| b964eb99-0d50-3dc3-9c3d-6de74031aa4d | -19.1838 | -48.73069 | 2025-08-26 03:57:00 | NOAA-21 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 16.7 |
| 5bd1b1dc-b6cd-36fe-b023-2eaa8b37ca74 | -13.44703 | -47.00536 | 2025-08-26 03:57:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 2d64292a-8225-3261-9cb2-e1ba041e23ec | -20.04647 | -44.46962 | 2025-08-26 03:57:00 | NOAA-21 | MATEUS LEME | MINAS GERAIS | Brasil | 3140704 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 789badc5-fad4-31c2-aa3e-41b688d46709 | -16.74713 | -47.59751 | 2025-08-26 03:57:00 | NOAA-21 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1652936a-4831-3ab2-bfa3-572d1f1a5203 | -20.72946 | -40.66159 | 2025-08-26 03:57:00 | NOAA-21 | ANCHIETA | ESPÍRITO SANTO | Brasil | 3200409 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 64ca0a19-a601-3c65-b926-a3262153f5e2 | -14.72513 | -45.37102 | 2025-08-26 03:57:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e0f660db-dd84-3df3-b282-97e3184495d4 | -13.42125 | -46.90744 | 2025-08-26 03:57:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 4475d756-2dc7-30b2-9c2d-278b8ac0c92f | -12.74922 | -48.15283 | 2025-08-26 03:57:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 66b054f7-15b4-356d-a561-ff2423244b38 | -13.81941 | -45.89349 | 2025-08-26 03:57:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 24c767c7-ba0e-3008-82db-277763f47ec5 | -13.61953 | -48.14921 | 2025-08-26 03:57:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a7fa3500-5ca9-371a-b350-a131efcd7de9 | -18.86562 | -46.99521 | 2025-08-26 03:57:00 | NOAA-21 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b54b093a-35d8-3485-a93f-84dd7cd9d65e | -14.36252 | -51.91873 | 2025-08-26 03:57:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| c9e12f27-45bc-36be-b69e-6f44e7745074 | -12.747 | -48.16456 | 2025-08-26 03:57:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 82cb31ee-c344-3754-b547-98bbdfb9eaef | -14.28396 | -49.13359 | 2025-08-26 03:57:00 | NOAA-21 | CAMPINORTE | GOIÁS | Brasil | 5204706 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| ef9392fb-f144-3f17-882e-023c559e4254 | -13.51803 | -46.89784 | 2025-08-26 03:57:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5c1f8e0f-0a8e-3ecd-a0e1-fea38ebfbf22 | -15.11972 | -48.65269 | 2025-08-26 03:57:00 | NOAA-21 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c34ed5a0-a31d-32f7-9c23-38917a51d609 | -13.58956 | -48.20116 | 2025-08-26 03:57:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 6.8 |
| b2e3f5b0-c481-3958-81dc-7381588f464b | -17.21201 | -47.22467 | 2025-08-26 03:57:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c495ad20-35c1-3f37-8c8f-a1225c11629a | -12.70466 | -47.89157 | 2025-08-26 03:57:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 994c7426-4457-3bcf-884d-f64e9df362db | -13.41022 | -46.89217 | 2025-08-26 03:57:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 22760ebd-794f-38e7-97fe-ed8b782eedef | -20.0457 | -42.6069 | 2025-08-26 03:57:00 | NOAA-21 | SÃO PEDRO DOS FERROS | MINAS GERAIS | Brasil | 3164001 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 5d865659-ee45-3e01-aba6-755884ebc6b4 | -12.77396 | -48.12926 | 2025-08-26 03:57:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f6fd1c20-b981-3692-aeee-e15824eb7523 | -13.61043 | -48.17075 | 2025-08-26 03:57:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 2eb7c9cb-24d2-3ca6-8a2d-45c8884fb4ea | -15.8808 | -48.15394 | 2025-08-26 03:57:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 4.3 |
| b97a20ec-e368-340d-9773-a17497cb4fb2 | -11.54332 | -52.12413 | 2025-08-26 03:57:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 7c9887f3-6f02-3fd0-ae68-b6715c3058b4 | -13.43931 | -47.01118 | 2025-08-26 03:57:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4bb41248-62ed-31ef-9115-1c8bb79abe4c | -19.92152 | -44.62365 | 2025-08-26 03:57:00 | NOAA-21 | PARÁ DE MINAS | MINAS GERAIS | Brasil | 3147105 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.5 |
| 651e815c-7593-37f2-a021-b8b45b943bac | -14.35753 | -51.91248 | 2025-08-26 03:57:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 3a45f485-6531-3975-8f69-abd162c22c04 | -12.73675 | -48.13821 | 2025-08-26 03:57:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 7.8 |
| b524c947-c755-3189-92d4-90b9c4cca624 | -20.98735 | -42.99409 | 2025-08-26 03:57:00 | NOAA-21 | DIVINÉSIA | MINAS GERAIS | Brasil | 3121902 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| e9fd4b6f-78d8-312d-9d01-35eacabe3605 | -18.34674 | -40.01789 | 2025-08-26 03:57:00 | NOAA-21 | PINHEIROS | ESPÍRITO SANTO | Brasil | 3204104 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| f292aa3c-783b-3adb-b6ec-32e6b282d400 | -13.63386 | -48.1528 | 2025-08-26 03:57:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| fefc29a4-c648-3e8c-bfdb-9429b9c704dc | -13.61366 | -48.15375 | 2025-08-26 03:57:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 73b3517f-b0e5-324f-adb7-0eabd2c2a771 | -14.40178 | -51.94224 | 2025-08-26 03:57:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 5216a0ac-7a49-3a64-8bc9-9f34ef296df7 | -13.05921 | -46.31098 | 2025-08-26 03:57:00 | NOAA-21 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 0117a654-a234-3b92-b7b0-3e9384932f45 | -11.55944 | -52.11055 | 2025-08-26 03:57:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 0942bef5-a364-33a9-999b-358cb1e47d96 | -13.51886 | -46.89339 | 2025-08-26 03:57:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fb71bf3d-ba6b-31e1-9cd9-444da0309a24 | -12.70084 | -47.88527 | 2025-08-26 03:57:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 453bc028-26b0-35f3-8aa3-6c68f7373a7a | -18.86895 | -47.00005 | 2025-08-26 03:57:00 | NOAA-21 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3c91b237-fb18-3585-abc1-15e70627e1c2 | -12.9345 | -46.32338 | 2025-08-26 03:57:00 | NOAA-21 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| db9b335a-987a-3dac-beb3-af550f809bd0 | -17.21276 | -47.22063 | 2025-08-26 03:57:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f239f7db-89f5-3391-9096-8b793669b447 | -11.55084 | -52.12001 | 2025-08-26 03:57:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| b09d9c7a-911a-3948-96e8-740a62128ae5 | -17.86842 | -42.24215 | 2025-08-26 03:57:00 | NOAA-21 | MALACACHETA | MINAS GERAIS | Brasil | 3139201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 5ed01640-6bc8-3dd6-bbb1-b4a7429f416a | -12.7373 | -48.16208 | 2025-08-26 03:57:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 1280c4ae-4803-325f-96f1-3471e2a7a345 | -14.2435 | -53.04597 | 2025-08-26 03:57:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3da2b7af-3efe-3461-9638-06cbf55e615a | -13.44269 | -46.86593 | 2025-08-26 03:57:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 093f2cdd-faba-32f1-95a9-5ba13c13b731 | -17.22731 | -44.80934 | 2025-08-26 03:57:00 | NOAA-21 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c5987bee-80df-3712-991e-7123b2e6468d | -15.02508 | -48.50374 | 2025-08-26 03:57:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| b04e003e-55dc-3c24-911e-69c9324e843f | -19.17951 | -44.5174 | 2025-08-26 03:57:00 | NOAA-21 | PARAOPEBA | MINAS GERAIS | Brasil | 3147402 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 770f78ee-83d2-321f-a214-6ee81733b382 | -11.56054 | -52.10511 | 2025-08-26 03:57:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| a21c29ad-a4cb-3e13-ba8e-ed78b9cca284 | -15.13585 | -48.67337 | 2025-08-26 03:57:00 | NOAA-21 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2ea6095a-9a96-3f81-a550-0263e8f5646c | -13.43848 | -47.01576 | 2025-08-26 03:57:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 7a8ad60d-1f91-3aa7-9e02-f98e0bec3115 | -12.78261 | -48.13724 | 2025-08-26 03:57:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 12.8 |
| 8766128a-b353-37f8-b5f5-a399956f67c3 | -11.55194 | -52.11462 | 2025-08-26 03:57:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 5911674b-9188-31cf-b749-15c357199c1f | -11.57226 | -52.11322 | 2025-08-26 03:57:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 8820dae5-6e9c-3192-956e-b23a3ce8d5ef | -20.20157 | -47.01469 | 2025-08-26 03:57:00 | NOAA-21 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7ce61ec9-822e-3c6d-917b-8f09f3a8be20 | -18.98417 | -47.08101 | 2025-08-26 03:57:00 | NOAA-21 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6d629428-150f-3d52-814f-b99716d9b16a | -11.53462 | -52.13401 | 2025-08-26 03:57:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 4980621a-a390-30e7-bf34-0354c5730bbc | -13.40935 | -46.8969 | 2025-08-26 03:57:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 0d694aa2-190e-3bd5-8930-80c7627ccedc | -12.9337 | -46.30355 | 2025-08-26 03:57:00 | NOAA-21 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 9e78a38c-06a7-38a5-a77b-6031c59d9950 | -13.8373 | -46.69431 | 2025-08-26 03:57:00 | NOAA-21 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 81f54a7f-8c58-3f62-a617-3459cdda2d7d | -12.77264 | -48.10929 | 2025-08-26 03:57:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 40151392-2f8c-3c16-a93e-635a4a3821fb | -15.03488 | -48.68497 | 2025-08-26 03:57:00 | NOAA-21 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 255ff7a4-e6af-3b14-9cb6-d3b989d5b305 | -13.44918 | -47.00798 | 2025-08-26 03:57:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 9ad8442e-947f-3819-95df-0842e8a0e077 | -12.72756 | -48.15981 | 2025-08-26 03:57:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| e58d4bc6-e6a4-3068-b54e-e00ae497bdb4 | -13.16425 | -45.29253 | 2025-08-26 03:57:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 7502c851-479e-31dd-b29e-679faa5eaf29 | -14.34824 | -51.95238 | 2025-08-26 03:57:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 17.8 |
| ba6dcf6e-fbae-3121-a46e-fe61ab09a5ed | -14.23809 | -44.11767 | 2025-08-26 03:57:00 | NOAA-21 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 04c23409-3c6f-325a-8aea-9777f862b977 | -12.76099 | -48.1443 | 2025-08-26 03:57:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| d7d785fc-54a1-3c85-a6f4-7e15bb344d4b | -18.85453 | -47.00927 | 2025-08-26 03:57:00 | NOAA-21 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 33d5fbe9-06a1-3f61-96d6-5710db5275ad | -13.44385 | -47.01175 | 2025-08-26 03:57:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 8ef5d5cd-6196-3237-b89f-b41346a255eb | -21.09169 | -40.93724 | 2025-08-26 03:57:00 | NOAA-21 | MARATAÍZES | ESPÍRITO SANTO | Brasil | 3203320 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| a6e1a0ab-8c23-36ba-9574-97b3a132f8cf | -15.37765 | -43.17074 | 2025-08-26 03:57:00 | NOAA-21 | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 0.6 |
| de8f58cb-13b6-32ab-bef9-ee40d45dc0fe | -14.24179 | -44.11835 | 2025-08-26 03:57:00 | NOAA-21 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 612a8e1b-a8bd-3eae-9e12-fb18d53d4a2b | -19.83185 | -45.89409 | 2025-08-26 03:57:00 | NOAA-21 | CÓRREGO DANTA | MINAS GERAIS | Brasil | 3119807 | 31 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 50d34ac8-9515-3a4a-8297-09732559df94 | -11.54442 | -52.11874 | 2025-08-26 03:57:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| f8d6a346-4dc5-3445-b3b6-ae3829237884 | -15.14076 | -48.67408 | 2025-08-26 03:57:00 | NOAA-21 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a4aa72dd-7a4b-3c48-86f5-25e979810ba3 | -13.59929 | -48.2028 | 2025-08-26 03:57:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 0ba0180d-f46b-3288-b0a1-cc21a711d280 | -15.11733 | -48.64995 | 2025-08-26 03:57:00 | NOAA-21 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 82803689-fd71-3ed9-82a2-77384375c99c | -20.02526 | -45.55233 | 2025-08-26 03:57:00 | NOAA-21 | LAGOA DA PRATA | MINAS GERAIS | Brasil | 3137205 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 04f172c0-ac46-3215-807f-40a58c15e4cd | -16.31915 | -43.62043 | 2025-08-26 03:57:00 | NOAA-21 | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 344804a0-cac1-3e9e-8c7e-6f1b55d00155 | -20.05069 | -44.46617 | 2025-08-26 03:57:00 | NOAA-21 | MATEUS LEME | MINAS GERAIS | Brasil | 3140704 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| b9f28121-520e-3735-b920-24d19386493f | -20.07477 | -44.3687 | 2025-08-26 03:57:00 | NOAA-21 | IGARAPÉ | MINAS GERAIS | Brasil | 3130101 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 6db55444-090f-3daf-a41d-6afb51d6f746 | -19.18285 | -48.73551 | 2025-08-26 03:57:00 | NOAA-21 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 16.7 |
| 33baa7d4-f4bc-3c30-aa84-d3ea416d5efc | -15.05712 | -48.70082 | 2025-08-26 03:57:00 | NOAA-21 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| fab3be6a-f58d-3e79-9c1b-f9f3202b51ff | -11.55517 | -52.09864 | 2025-08-26 03:57:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a7523426-f2bd-3f77-8f2a-b0c095e4074e | -15.17407 | -48.19245 | 2025-08-26 03:57:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ff006edb-993d-39ce-b042-936458736a5d | -19.95936 | -47.00864 | 2025-08-26 03:57:00 | NOAA-21 | TAPIRA | MINAS GERAIS | Brasil | 3168101 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 230eb369-f02d-387f-b781-1eaa83a43b73 | -20.38347 | -42.19872 | 2025-08-26 03:57:00 | NOAA-21 | SANTA MARGARIDA | MINAS GERAIS | Brasil | 3157906 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 5cc92b3c-18fe-34b5-b612-99501eec27fa | -12.77509 | -48.12323 | 2025-08-26 03:57:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 6f883294-e44e-39b2-9c50-6c743274d042 | -15.05604 | -48.70644 | 2025-08-26 03:57:00 | NOAA-21 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 44a775cd-ef21-3349-8596-096e6844dd8a | -14.34864 | -51.95459 | 2025-08-26 03:57:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |


[Clique aqui para ver as próximas entradas](README31.md)
