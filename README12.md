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

## Dados Diários - Página 12

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0cebecb0-58f6-3add-b706-e64061bdb706 | -11.9335 | -46.73872 | 2025-08-04 04:10:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a9705766-f680-343e-b068-f5de79f5fe85 | -15.56509 | -47.0861 | 2025-08-04 04:10:00 | NOAA-21 | CABECEIRAS | GOIÁS | Brasil | 5204003 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 49267a18-e673-359d-a5f2-f28bfa5240b0 | -15.27243 | -43.07528 | 2025-08-04 04:10:00 | NOAA-21 | MONTE AZUL | MINAS GERAIS | Brasil | 3142908 | 31 | 33 | nan | nan | nan | Caatinga | 4.1 |
| a318ff72-d94d-307b-b7b2-c8842880437e | -13.25443 | -46.97329 | 2025-08-04 04:10:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b0fdc318-73e9-3fb2-adec-a08ce56f3795 | -15.69501 | -48.99779 | 2025-08-04 04:10:00 | NOAA-21 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4094b771-d6ac-3064-bc12-4cf08a8a43e0 | -11.40792 | -54.71992 | 2025-08-04 04:10:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4bd15162-d60d-3943-b56f-1ada15c267e0 | -14.66422 | -52.40678 | 2025-08-04 04:10:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 28.5 |
| a7d08358-5669-303a-a844-07f2e8003b71 | -13.24998 | -46.97708 | 2025-08-04 04:10:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b9f11b95-86ae-3488-bc5d-84866545df64 | -15.76755 | -46.56195 | 2025-08-04 04:10:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f7b8b2fa-aa4e-38bd-8172-952aad725b70 | -17.37356 | -46.08734 | 2025-08-04 04:10:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 1afc7444-4686-332e-8819-5a485d1307a8 | -15.63562 | -47.79919 | 2025-08-04 04:10:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 7.7 |
| e1654243-84f2-31da-a077-dd02dbb38c5d | -12.44222 | -44.85173 | 2025-08-04 04:10:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4bf73a59-63b9-39a9-9907-e8ddad136560 | -13.68729 | -41.36395 | 2025-08-04 04:10:00 | NOAA-21 | ITUAÇU | BAHIA | Brasil | 2917201 | 29 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 5cc71e93-cc2e-34ce-9fad-a75e762f3fb2 | -10.33394 | -50.06421 | 2025-08-04 04:10:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| fc75be14-35ab-34e4-ab1d-575168dac9ac | -17.69033 | -42.96211 | 2025-08-04 04:10:00 | NOAA-21 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e69d0d6c-cb96-37b5-871e-f5c6d1c88ac4 | -13.20735 | -47.25162 | 2025-08-04 04:10:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 28942f34-aac3-3f0c-ba87-f08d93490d2d | -14.21027 | -51.21739 | 2025-08-04 04:10:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 56ae991b-542f-3de1-816f-290afacb74e5 | -10.25063 | -50.16699 | 2025-08-04 04:10:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| bef63805-a759-39a8-ad3d-41f748cd7139 | -14.6661 | -52.40916 | 2025-08-04 04:10:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 16.6 |
| d26881b6-2d90-3c2b-9c8a-2b743c1a2cdf | -11.93158 | -44.96481 | 2025-08-04 04:10:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 350bd510-122a-3424-aa7e-deead701d046 | -17.37082 | -46.08277 | 2025-08-04 04:10:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b9a0d7d9-e407-326e-ac36-302403ddb661 | -12.41951 | -44.70704 | 2025-08-04 04:10:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 1080a83b-dac5-3fac-b89c-561008a465d8 | -18.0001 | -44.33453 | 2025-08-04 04:10:00 | NOAA-21 | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| efceed1e-c71a-3177-97d7-10bfd375f9ed | -10.24682 | -50.16096 | 2025-08-04 04:10:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 7f7c40fd-f8b6-3208-bd2d-df68c597ccf1 | -10.45102 | -47.22117 | 2025-08-04 04:10:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ebe83ff6-cd0f-3be0-b7a5-117b557281a3 | -14.66162 | -52.40499 | 2025-08-04 04:10:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| c4e39998-0589-3823-9b91-b6e0be4d2b89 | -11.93182 | -44.94174 | 2025-08-04 04:10:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ac7399ce-caf7-3edf-94c3-a304f937afd4 | -11.22873 | -48.43749 | 2025-08-04 04:10:00 | NOAA-21 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| c1aa4b63-0d2b-33c0-bb4f-27bfac7a2bc0 | -16.17607 | -46.95966 | 2025-08-04 04:10:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7725b1de-4418-30a5-b569-f674c8157206 | -11.92902 | -44.98053 | 2025-08-04 04:10:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a6372cc4-37ff-3b45-8f94-e6e040af4100 | -11.50908 | -44.29692 | 2025-08-04 04:10:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 51d0a1b2-b57e-3f9b-a813-3f9a48ef48ed | -11.7539 | -44.99749 | 2025-08-04 04:10:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2d395280-34ac-3518-823f-f1bf93f45e6f | -17.46743 | -47.1012 | 2025-08-04 04:10:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7b197bc1-77c1-300c-9857-fb23f85d2101 | -12.75861 | -44.41692 | 2025-08-04 04:10:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8349bf54-6b21-380e-9bab-6aa9cbbac0d0 | -11.76523 | -44.97168 | 2025-08-04 04:10:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 92d1e117-e4d8-32b9-99c2-48109fc6f029 | -13.25074 | -46.97262 | 2025-08-04 04:10:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e41d72f2-4eae-3b21-98c6-bdb2833df732 | -16.92372 | -49.46074 | 2025-08-04 04:10:00 | NOAA-21 | ARAGOIÂNIA | GOIÁS | Brasil | 5201801 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 03e905df-24a5-3591-94ef-b7869508a31d | -10.32829 | -50.06842 | 2025-08-04 04:10:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 7c473349-92ea-3a13-b6ea-8d4ec8d8a571 | -11.74984 | -45.00074 | 2025-08-04 04:10:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5598baf8-beff-366d-a973-74ac0e7ada13 | -10.78098 | -48.80205 | 2025-08-04 04:10:00 | NOAA-21 | FÁTIMA | TOCANTINS | Brasil | 1707553 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f5d3d3f0-cbaa-36f7-b88d-7c8588a93285 | -13.69357 | -41.36887 | 2025-08-04 04:10:00 | NOAA-21 | ITUAÇU | BAHIA | Brasil | 2917201 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| f2d80907-a1d4-3b4c-9256-4b14b12c7224 | -17.36871 | -46.07445 | 2025-08-04 04:10:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e0bf97fe-7f0c-3f0b-8eca-f345766bf37d | -12.14447 | -43.38266 | 2025-08-04 04:10:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c858bb23-529f-3ea1-b447-8bed07a4fb37 | -12.75525 | -44.41636 | 2025-08-04 04:10:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 7cac9e6c-3994-3549-9ded-8671bc76914c | -12.07933 | -43.36429 | 2025-08-04 04:10:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7995af0c-e56d-37f2-b55d-e032a2e81eaa | -13.04988 | -56.8975 | 2025-08-04 04:10:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 78a53687-9a23-3593-8c37-c90a0120defe | -13.69015 | -41.36832 | 2025-08-04 04:10:00 | NOAA-21 | ITUAÇU | BAHIA | Brasil | 2917201 | 29 | 33 | nan | nan | nan | Caatinga | 3.8 |
| fa263002-ab5b-32c5-8095-bdc616f984ef | -17.99679 | -44.33397 | 2025-08-04 04:10:00 | NOAA-21 | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 123ff0da-052b-3328-a1cc-b6a3f706b302 | -11.41011 | -54.72046 | 2025-08-04 04:10:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| d1f39eac-accd-3257-941f-614cd61b0613 | -13.05538 | -56.9053 | 2025-08-04 04:10:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 7a304608-7dca-3630-a8d5-a12e5a1ea854 | -12.72392 | -46.40126 | 2025-08-04 04:10:00 | NOAA-21 | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| bc1cf4aa-a63f-3be1-b838-0965cbeebd60 | -17.46676 | -47.10513 | 2025-08-04 04:10:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 91152df4-dc41-333d-8b60-2c9a58230e73 | -17.79311 | -42.90924 | 2025-08-04 04:10:00 | NOAA-21 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 440c1cc7-7a60-31ae-93e0-df9a36cbc366 | -11.92752 | -44.96814 | 2025-08-04 04:10:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| d1d46c9f-f12c-367c-88d9-56009f906bc5 | -14.66669 | -52.40609 | 2025-08-04 04:10:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 16.6 |
| f0492e2b-b513-352f-9b6c-71d0f11117c4 | -13.20061 | -47.24577 | 2025-08-04 04:10:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3bae7020-c374-320d-ab09-bc5cc5aab698 | -15.69902 | -48.99853 | 2025-08-04 04:10:00 | NOAA-21 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 531969dd-672f-3008-91b3-c0dc2227c6fc | -11.51655 | -44.35819 | 2025-08-04 04:10:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 22fd5664-2144-3968-b5ee-2e0bed802f6d | -15.77107 | -46.56254 | 2025-08-04 04:10:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c483b17a-9292-3a99-a641-f0d1a8ba4fa2 | -11.94272 | -44.98288 | 2025-08-04 04:10:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 50c0cb2a-bedd-3ca3-9f85-89008a40ecb0 | -14.84593 | -48.39502 | 2025-08-04 04:10:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 68fdbf6d-9bea-3bf9-af5c-61a3bf17cf7c | -17.71797 | -48.64277 | 2025-08-04 04:10:00 | NOAA-21 | CALDAS NOVAS | GOIÁS | Brasil | 5204508 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b612e14c-b646-3733-b042-449bbc7a1cb7 | -12.65168 | -45.05258 | 2025-08-04 04:10:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 3c445ecf-737a-3020-ab3a-e08d1637d81f | -13.69699 | -41.36943 | 2025-08-04 04:10:00 | NOAA-21 | ITUAÇU | BAHIA | Brasil | 2917201 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 17c027df-fabe-3080-a30e-f3fdc7d6f75a | -11.75836 | -44.97059 | 2025-08-04 04:10:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cf78c797-ea57-3ab5-9746-84bdfe913e17 | -11.78547 | -44.99863 | 2025-08-04 04:10:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 96a9fc0a-fef4-3862-bed6-de94af455266 | -11.75555 | -44.96625 | 2025-08-04 04:10:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f0b5cd11-6acd-361e-bbcb-cce9d239686d | -10.24969 | -50.17216 | 2025-08-04 04:10:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b87950d3-2ff6-3299-b730-1ab44391fc24 | -11.9474 | -44.9757 | 2025-08-04 04:10:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| df1e2ed8-3178-3639-8713-a50f78ae9431 | -11.93564 | -44.96149 | 2025-08-04 04:10:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d536a00a-6bea-396d-ad59-4c11c132e091 | -11.75899 | -44.96679 | 2025-08-04 04:10:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a4b65cff-2fa3-328c-b3e2-b082ee24315e | -17.37226 | -46.09517 | 2025-08-04 04:10:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 91834d75-3dca-361c-8e33-09ebbda613f3 | -15.07527 | -47.26488 | 2025-08-04 04:10:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fa7a12d9-31c7-3a23-8d7b-80a02f33a0fa | -20.02802 | -42.43634 | 2025-08-04 04:12:00 | NOAA-21 | RAUL SOARES | MINAS GERAIS | Brasil | 3154002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| 8a67d3d8-7067-381f-8d9b-8f708da482de | -22.31037 | -47.62748 | 2025-08-04 04:12:00 | NOAA-21 | CORUMBATAÍ | SÃO PAULO | Brasil | 3512704 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 20bdfc45-97fc-3f5c-afe5-02968a8f373f | -19.09728 | -43.60459 | 2025-08-04 04:12:00 | NOAA-21 | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ff6d1a1e-03b3-3a3b-962a-1e8522f99294 | -21.25487 | -43.97693 | 2025-08-04 04:12:00 | NOAA-21 | BARBACENA | MINAS GERAIS | Brasil | 3105608 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| f417cbc8-089d-3b28-99ce-b18e20d357f4 | -22.79284 | -42.11632 | 2025-08-04 04:12:00 | NOAA-21 | SÃO PEDRO DA ALDEIA | RIO DE JANEIRO | Brasil | 3305208 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 2d5e7c52-ffb6-3107-b97b-1706e66d9293 | -21.88114 | -46.13736 | 2025-08-04 04:12:00 | NOAA-21 | CALDAS | MINAS GERAIS | Brasil | 3110301 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| 62e4b0bb-0cc3-3b25-9b90-392bf51bb4a0 | -22.75447 | -43.73568 | 2025-08-04 04:12:00 | NOAA-21 | SEROPÉDICA | RIO DE JANEIRO | Brasil | 3305554 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| bb209d5c-547e-3e28-a9eb-6831030a3fe6 | -22.74032 | -45.08337 | 2025-08-04 04:12:00 | NOAA-21 | LORENA | SÃO PAULO | Brasil | 3527207 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 89ad9b52-6493-37c0-87e4-7cb1cd235e5e | -19.52269 | -46.9036 | 2025-08-04 04:12:00 | NOAA-21 | ARAXÁ | MINAS GERAIS | Brasil | 3104007 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 8b9e2bec-4233-3337-80da-15ab061efde9 | -22.83083 | -47.3355 | 2025-08-04 04:12:00 | NOAA-21 | SUMARÉ | SÃO PAULO | Brasil | 3552403 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| e7fda2cf-a380-35fc-9920-7a584f5f6cbc | -20.09544 | -44.00778 | 2025-08-04 04:12:00 | NOAA-21 | BRUMADINHO | MINAS GERAIS | Brasil | 3109006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 12c0f76e-a543-307c-994c-de03b05c4a9a | -22.83149 | -47.33157 | 2025-08-04 04:12:00 | NOAA-21 | SUMARÉ | SÃO PAULO | Brasil | 3552403 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.5 |
| b866a686-a73e-3fae-84d7-e54bbcf31444 | -22.90508 | -43.46642 | 2025-08-04 04:12:00 | NOAA-21 | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| 607fba08-1ada-3bc7-bd9a-917cbf366bea | -19.45954 | -42.54743 | 2025-08-04 04:12:00 | NOAA-21 | IPATINGA | MINAS GERAIS | Brasil | 3131307 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 48eeedcf-20ff-3dca-bb84-13b6caaa8165 | -19.5785 | -46.95069 | 2025-08-04 04:12:00 | NOAA-21 | ARAXÁ | MINAS GERAIS | Brasil | 3104007 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5c149d80-c80e-3fd2-9a51-00ac1d342410 | -22.46905 | -43.84369 | 2025-08-04 04:12:00 | NOAA-21 | BARRA DO PIRAÍ | RIO DE JANEIRO | Brasil | 3300308 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 5bbc2dad-4a3a-36f3-b9b4-e9a0b8fc05b3 | -22.72674 | -44.75078 | 2025-08-04 04:12:00 | NOAA-21 | AREIAS | SÃO PAULO | Brasil | 3503505 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 231ae63c-8881-30cb-b355-386b206b3be4 | -21.25431 | -43.98071 | 2025-08-04 04:12:00 | NOAA-21 | BARBACENA | MINAS GERAIS | Brasil | 3105608 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 4e78daa5-ae34-3cba-977d-a75ada4d5230 | -22.69849 | -47.45274 | 2025-08-04 04:12:00 | NOAA-21 | LIMEIRA | SÃO PAULO | Brasil | 3526902 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f0021fb6-9295-3561-9814-bff76bc04bee | -22.91575 | -43.70884 | 2025-08-04 04:12:00 | NOAA-21 | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 4.8 |
| f73b84ce-1163-3acd-9b9a-e7494af65413 | -23.46507 | -45.43074 | 2025-08-04 04:12:00 | NOAA-21 | NATIVIDADE DA SERRA | SÃO PAULO | Brasil | 3532306 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 0c9e2edc-cf1e-3ab7-96ea-67b75fb7bb95 | -22.30695 | -47.62675 | 2025-08-04 04:12:00 | NOAA-21 | CORUMBATAÍ | SÃO PAULO | Brasil | 3512704 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ed19c4d9-e95c-35eb-90b3-e6ccabf33abe | -21.9358 | -46.19726 | 2025-08-04 04:12:00 | NOAA-21 | SANTA RITA DE CALDAS | MINAS GERAIS | Brasil | 3159209 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| b512118b-b0af-3c60-9be1-a42e15c5c087 | -20.66888 | -44.07956 | 2025-08-04 04:12:00 | NOAA-21 | ENTRE RIOS DE MINAS | MINAS GERAIS | Brasil | 3123908 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| a8f995a0-3d3e-39d1-8ffe-acb5aeaa6fff | -19.75919 | -44.00843 | 2025-08-04 04:12:00 | NOAA-21 | RIBEIRÃO DAS NEVES | MINAS GERAIS | Brasil | 3154606 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 29054674-e109-39b2-9665-77cd6b578c90 | -19.30101 | -46.21137 | 2025-08-04 04:12:00 | NOAA-21 | RIO PARANAÍBA | MINAS GERAIS | Brasil | 3155504 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 385bf085-aaff-32cb-9f2d-cc8e4021b670 | -19.513 | -47.08649 | 2025-08-04 04:12:00 | NOAA-21 | PERDIZES | MINAS GERAIS | Brasil | 3149804 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |


[Clique aqui para ver as próximas entradas](README13.md)
