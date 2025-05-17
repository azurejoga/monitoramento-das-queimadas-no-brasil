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
| b15d8a2c-ed10-30e3-a73f-d3d64ad706c3 | -13.32231 | -45.3785 | 2025-05-17 04:17:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| eff41865-5804-33f5-8af5-60fc033017bc | -18.95088 | -52.24163 | 2025-05-17 04:17:00 | NPP-375D | CASSILÂNDIA | MATO GROSSO DO SUL | Brasil | 5002902 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 14f98ee7-1657-35fa-9adc-d15bd3aa5002 | -13.30619 | -45.37212 | 2025-05-17 04:17:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 28ce4db1-6dff-3cd4-acec-f5883bc8cb57 | -13.14627 | -45.3934 | 2025-05-17 04:17:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 4172c3e4-45cf-3f78-aea2-5895a96a6ae7 | -11.35841 | -52.95304 | 2025-05-17 04:17:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d448afa8-f1e4-3e8f-8810-d6d810a58bdb | -13.30562 | -45.37569 | 2025-05-17 04:17:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ac39d22c-897a-36f8-9103-d38a7a07237f | -8.69683 | -49.02615 | 2025-05-17 04:17:00 | NPP-375D | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| ca148882-3eee-38a0-ad56-6919b54f6f2f | -13.58638 | -47.37389 | 2025-05-17 04:17:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a15d180d-997d-30d8-8ca6-9363f4837a7c | -11.66504 | -54.93921 | 2025-05-17 04:17:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| cf309959-16b8-329b-bbff-b80c1f14c685 | -11.34029 | -46.50978 | 2025-05-17 04:17:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| be24d70c-82a7-3fc6-9508-53a668a1cc7a | -8.74776 | -49.75037 | 2025-05-17 04:17:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6a4b0ecd-376d-33ab-bfd8-25d35a4adbf0 | -11.58363 | -47.62457 | 2025-05-17 04:17:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| b38ec6e3-c4fb-344d-a709-242a8f948dd8 | -13.31621 | -45.3738 | 2025-05-17 04:17:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f6848afb-3a48-3715-bc7a-f338affca550 | -13.06538 | -47.82117 | 2025-05-17 04:17:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 701c2efd-c396-3c1f-bec0-dd84afe270e2 | -17.755 | -56.3099 | 2025-05-17 04:17:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.7 |
| d38a1105-976b-304f-892b-80f92d773175 | -11.58272 | -47.86956 | 2025-05-17 04:17:00 | NPP-375D | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 8e645c2d-72e1-3aaf-a2fd-909832817a63 | -11.57778 | -47.61469 | 2025-05-17 04:17:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| faee5864-4a95-3cbe-b41e-bee5c8f13bb2 | -11.64646 | -48.02029 | 2025-05-17 04:17:00 | NPP-375D | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e3ec0494-9b31-390d-848c-6279bd7d8153 | -13.36216 | -43.08751 | 2025-05-17 04:17:00 | NPP-375D | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 7c788652-b711-399c-b1bd-a02e8e2cca62 | -19.96905 | -44.21746 | 2025-05-17 04:17:00 | NPP-375D | BETIM | MINAS GERAIS | Brasil | 3106705 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| deb0a574-10d6-304f-8515-ae839b30818e | -13.3245 | -45.38621 | 2025-05-17 04:17:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5a6fc4f7-1ddf-3de2-bae2-b3d3823b4ebe | -10.60964 | -44.76525 | 2025-05-17 04:17:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 2a07823e-756f-3ea8-a93c-58b9c0c00d09 | -13.50667 | -47.39832 | 2025-05-17 04:17:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5a861917-16df-317c-aa7b-6947285cf50a | -9.14238 | -41.00101 | 2025-05-17 04:17:00 | NPP-375D | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| c90d8ad2-b036-3b90-bd57-f39ff4d935fe | -11.33833 | -46.50874 | 2025-05-17 04:17:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| cd298335-624a-380f-ba6f-ab5a356f5e43 | -13.30896 | -45.37626 | 2025-05-17 04:17:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5b3c48f9-0e10-3361-9e29-960c2fb0bf26 | -9.79696 | -47.74042 | 2025-05-17 04:17:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 943ffbde-d9bb-30f3-abe9-3bba314c4914 | -13.31506 | -45.38095 | 2025-05-17 04:17:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 852e512a-7be7-362b-83f7-da54f3bd39e5 | -17.76061 | -56.31122 | 2025-05-17 04:17:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| d09ae095-bc5c-39c2-a482-b50f599297d9 | -11.36521 | -52.94498 | 2025-05-17 04:17:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 685601e6-72aa-3593-a5e6-3ded770c29b4 | -11.97228 | -48.1078 | 2025-05-17 04:17:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 02aaff66-c407-3522-8371-e00f6de2e613 | -9.66979 | -47.55823 | 2025-05-17 04:17:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 35cab9e6-8be4-3736-b53f-7c5b9965d454 | -12.35352 | -49.96419 | 2025-05-17 04:17:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f1ac2f86-2ece-3f3e-a48c-7033c1d0439e | -13.32669 | -45.39392 | 2025-05-17 04:17:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2f7413e9-b6ce-374a-9a8c-ee67c0755115 | -9.31374 | -44.83181 | 2025-05-17 04:17:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 60eef54d-97de-3467-b68b-749762c5a6bd | -13.31344 | -45.36966 | 2025-05-17 04:17:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8220842a-8483-33ca-afb7-d52e941574ff | -12.72541 | -54.9789 | 2025-05-17 04:17:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| dd27d3fb-06d7-3524-9647-12b9487e5a50 | -13.31705 | -47.46077 | 2025-05-17 04:17:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| d0791424-668d-32c4-9ac4-7538761c2131 | -19.05958 | -53.45588 | 2025-05-17 04:17:00 | NPP-375D | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 7706b32a-36cd-347b-8992-ca9334f1c3ff | -11.3692 | -52.95198 | 2025-05-17 04:17:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7fd66b63-60b5-34a6-8bfc-ef7af30b4a1e | -11.40166 | -52.9518 | 2025-05-17 04:17:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7169b2d0-e135-3b77-8785-0495d693cf30 | -11.79598 | -47.40697 | 2025-05-17 04:17:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c167772d-81e5-3afd-b5df-e24c70543171 | -11.7902 | -47.39736 | 2025-05-17 04:17:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| cd0f7870-ffdf-3316-88f9-c6dfb962554c | -11.36409 | -52.95101 | 2025-05-17 04:17:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 91b2183b-db6e-3600-a727-eef2e82e7e7e | -11.58434 | -47.62032 | 2025-05-17 04:17:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| d0ac14da-cac3-3be0-baca-b39d36e9592d | -13.32612 | -45.3975 | 2025-05-17 04:17:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1fdb08c0-148a-39b3-823c-53b7c81261cc | -11.16095 | -48.6799 | 2025-05-17 04:17:00 | NPP-375D | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 61096d85-9b0e-3f95-8cc8-e2251056249b | -11.64042 | -48.03314 | 2025-05-17 04:17:00 | NPP-375D | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 00d223cd-367f-3b1c-97df-208818f2ee36 | -17.57669 | -47.48696 | 2025-05-17 04:17:00 | NPP-375D | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 398e0999-b876-3fe0-baa0-3061a8fb897a | -9.31095 | -44.82769 | 2025-05-17 04:17:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9beb12ba-5524-33ba-8a80-2b6a767bfcd1 | -11.34028 | -46.49707 | 2025-05-17 04:17:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| eb41f569-9a4d-3ae7-81f1-e0c5fb7c0639 | -14.06499 | -45.42238 | 2025-05-17 04:17:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e84f8092-859e-34eb-9d15-b0481fed22ce | -13.32336 | -45.39336 | 2025-05-17 04:17:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a58035c5-9a31-3a27-b529-8f8dbb016fbe | -13.30285 | -45.37156 | 2025-05-17 04:17:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6e8e1fe4-31a5-30b4-9e68-71b1dbd1780e | -11.40208 | -52.94595 | 2025-05-17 04:17:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a40c2a9c-2822-3366-b354-204ba1b06ef4 | -20.64072 | -47.08901 | 2025-05-17 04:17:00 | NPP-375D | CAPETINGA | MINAS GERAIS | Brasil | 3112406 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| c1d18b4d-d533-3cca-8172-685be085b4cd | -12.99426 | -46.32269 | 2025-05-17 04:17:00 | NPP-375D | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 35d17a22-b7bd-3d52-b71e-5a1e167a1345 | -11.41969 | -44.70843 | 2025-05-17 04:17:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ccde19bb-c383-39e5-9e24-982cdb1b941c | -11.64491 | -48.02929 | 2025-05-17 04:17:00 | NPP-375D | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0cbf65aa-aabe-3e32-a68d-940dc77fd346 | -13.32116 | -45.38564 | 2025-05-17 04:17:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 15ad13fb-c22f-3054-94d2-bbedc7c1f5d7 | -11.58345 | -47.62341 | 2025-05-17 04:17:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6dfacd34-1ea2-3025-81f5-f310b3377d7b | -13.06704 | -47.81961 | 2025-05-17 04:17:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 221f054b-3c9d-3384-89bc-f61fc0a78851 | -11.6494 | -48.02545 | 2025-05-17 04:17:00 | NPP-375D | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2bcd6629-caec-346c-95ba-d570293b546b | -13.39854 | -48.45572 | 2025-05-17 04:17:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9ce000f5-d23b-3714-b770-4951cbae807e | -13.32508 | -45.38263 | 2025-05-17 04:17:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 802ea6fd-f0fc-3962-bf02-7433811a0164 | -20.51604 | -47.35867 | 2025-05-17 04:17:00 | NPP-375D | FRANCA | SÃO PAULO | Brasil | 3516200 | 35 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c93152c5-f4d3-3fd3-9409-20d96fd4154f | -13.3184 | -45.38151 | 2025-05-17 04:17:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 36bde0a0-075a-3846-acbd-380c3a611db9 | -12.35699 | -49.9687 | 2025-05-17 04:17:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bd441597-2893-331c-968f-d85680d51749 | -19.85019 | -43.84595 | 2025-05-17 04:17:00 | NPP-375D | SABARÁ | MINAS GERAIS | Brasil | 3156700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.2 |
| 9d503bbc-beff-3e65-a3c3-b7c4113239bf | -13.05738 | -47.82453 | 2025-05-17 04:17:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 5ae85a2a-578f-34e9-8ae5-93a75f7ab319 | -11.41579 | -44.71141 | 2025-05-17 04:17:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8fcf06b0-5f44-364e-9698-0a4f464de7ce | -11.33809 | -46.50143 | 2025-05-17 04:17:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a922aa6a-0d0d-39d4-8abf-53ffce12cfa6 | -11.60309 | -46.45744 | 2025-05-17 04:17:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3b5ae35c-3071-3b8e-ab67-e5b2d1b07e96 | -9.42071 | -49.34363 | 2025-05-17 04:17:00 | NPP-375D | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 5b940dfd-8a30-3621-b4dd-f2de2a73ccab | -10.63847 | -48.0892 | 2025-05-17 04:17:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 9af77f46-c318-3fb0-8d01-ca16a75d3d36 | -13.30734 | -45.36498 | 2025-05-17 04:17:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 1c56a11e-a6be-3af2-9398-82153ca28d8e | -11.58142 | -47.61534 | 2025-05-17 04:17:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 7132d9df-10ac-3857-8850-49c075a6f67c | -13.30343 | -45.36799 | 2025-05-17 04:17:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1d510713-a7e9-39fe-a7be-21a1c0d647bc | -13.32393 | -45.38978 | 2025-05-17 04:17:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1b9be819-0b87-3488-8d52-9b2773e4740b | -9.0351 | -47.76661 | 2025-05-17 04:17:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e5eb5c4d-2f39-36b9-85d8-97c13c1de11b | -11.67026 | -54.94062 | 2025-05-17 04:17:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 594c36b7-1985-3593-9a63-b7428734a314 | -10.47759 | -49.14619 | 2025-05-17 04:17:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e0d7dd14-177e-3bff-aee5-e811d5bcb3de | -13.39405 | -48.45963 | 2025-05-17 04:17:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 31f2aaaf-35bd-339a-a57a-e5dbbe84dbf3 | -7.80176 | -46.21785 | 2025-05-17 04:17:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b3c10a05-df0f-368c-99e8-121a9aab5c73 | -18.92499 | -47.00396 | 2025-05-17 04:17:00 | NPP-375D | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8bafd7df-45fb-3fa0-be4b-b25edc66fa3d | -7.9489 | -49.76175 | 2025-05-17 04:17:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ffe0dc13-c491-384b-be84-665138a88b19 | -8.1207 | -45.89796 | 2025-05-17 04:17:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 300c0801-ff89-31e5-a6e2-1383027c4e05 | -13.3101 | -45.36911 | 2025-05-17 04:17:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9f77b15a-2ec0-3f61-9201-7c9afd27ce31 | -11.64413 | -48.03378 | 2025-05-17 04:17:00 | NPP-375D | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 813a5ecc-7703-3200-9073-e6ecc86648ed | -13.31057 | -45.38755 | 2025-05-17 04:17:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 56926454-9af3-356a-aca8-e17467fc7c22 | -11.43799 | -44.7223 | 2025-05-17 04:17:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 71aefb35-d9eb-3544-ae53-fba9ae17af0b | -13.39438 | -48.46302 | 2025-05-17 04:17:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 435b4cf5-a37c-3a99-9a75-d5ba22af981b | -11.78854 | -47.34146 | 2025-05-17 04:17:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 10916494-be9c-3950-9589-febd8cf4b0e2 | -17.66674 | -46.68649 | 2025-05-17 04:17:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bb67f112-a784-3461-9433-1634e79b333d | -13.32002 | -45.3928 | 2025-05-17 04:17:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| fa0696b6-ebf7-39e2-85b8-626c3a8c7589 | -8.1242 | -45.89851 | 2025-05-17 04:17:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 62a16ab5-7ad5-3aad-9d42-2b8aa6d737c0 | -13.29951 | -45.37101 | 2025-05-17 04:17:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fe8b8b4d-c143-3d50-9476-4a455d01c17f | -12.99311 | -46.31171 | 2025-05-17 04:17:00 | NPP-375D | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b6d5e760-d670-3bfb-8aee-45923dd9f021 | -19.06416 | -53.45691 | 2025-05-17 04:17:00 | NPP-375D | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 5.1 |
| a807c5fb-aa36-3451-94c1-367d58c12c4e | -13.32727 | -45.39034 | 2025-05-17 04:17:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |


[Clique aqui para ver as próximas entradas](README7.md)
