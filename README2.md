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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ce81e670-1cfb-335a-9e12-4cda6afc4269 | -14.0337 | -53.364899 | 2025-05-22 00:28:00 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 6dcefbbb-2b3d-391a-8d35-3311b720cc88 | -12.1319 | -54.6497 | 2025-05-22 00:28:00 | METOP-B | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| efd8e631-fc56-3dc1-b89d-9c90b15dc6d0 | -9.0379 | -47.0285 | 2025-05-22 00:28:00 | METOP-B | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 6abfa44c-ea63-3720-9465-7ca20dcadd25 | -10.3272 | -47.0256 | 2025-05-22 00:28:00 | METOP-B | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 06cecca7-08b6-3daa-aaa9-c450eee11efb | -10.36 | -47.969501 | 2025-05-22 00:28:00 | METOP-B | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 5de3ceb6-baa9-3b8b-bd56-7ae9d54396a0 | -11.2954 | -53.9641 | 2025-05-22 00:28:00 | METOP-B | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 912f890b-907f-3955-b8ea-8c1b7e5b9daf | -14.0215 | -55.131401 | 2025-05-22 00:28:00 | METOP-B | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 35a27afc-9f24-3476-b9f9-82c6747c6c36 | -10.8238 | -56.936298 | 2025-05-22 00:28:00 | METOP-B | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 15f61133-2e54-39b9-8c8c-4f97614ba3e6 | -11.5793 | -47.6185 | 2025-05-22 00:28:00 | METOP-B | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| dbc095eb-a9a9-31ae-a4f8-100acdb88016 | -19.062401 | -53.4533 | 2025-05-22 00:28:00 | METOP-B | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 08a6e391-f8b7-3d59-a372-3f5c66dafc17 | -8.7424 | -49.741699 | 2025-05-22 00:28:00 | METOP-B | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9ee78ddd-90c8-3a13-bd94-6ade207727b3 | -10.3233 | -47.008999 | 2025-05-22 00:28:00 | METOP-B | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| d631b7f6-e448-3a07-bc5f-d10a40010481 | -12.0721 | -47.338699 | 2025-05-22 00:28:00 | METOP-B | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 9ac769ef-5f4e-3d54-95b0-0014aaaca0fa | -17.6138 | -54.166801 | 2025-05-22 00:28:00 | METOP-B | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| fad710b3-7922-3a6d-99a0-8890c2a26a16 | -8.4758 | -49.611099 | 2025-05-22 00:28:00 | METOP-B | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 285588c1-ecca-3eda-afde-4da39b52393e | -20.948601 | -56.5891 | 2025-05-22 00:28:00 | METOP-B | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 218a254e-74cf-354b-8dc9-516a84a8ace9 | -13.5194 | -43.698898 | 2025-05-22 00:28:00 | METOP-B | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| d2c4bf6c-3ea1-33fe-88d7-423e90e01299 | -9.0183 | -47.743999 | 2025-05-22 00:28:00 | METOP-B | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| b76dc03a-ca34-31d4-b13d-b6e55872a7d3 | -10.0944 | -47.0895 | 2025-05-22 00:28:00 | METOP-B | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 25597b7d-c0b8-3881-a965-e04a50dea36d | -10.6513 | -49.431801 | 2025-05-22 00:28:00 | METOP-B | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| e9992363-a0ff-35cb-9583-23f6f4fb92b4 | -20.9552 | -56.568298 | 2025-05-22 00:28:00 | METOP-B | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 13964ec2-a8c6-3cce-8d1c-8db060d28f49 | -8.4742 | -49.604099 | 2025-05-22 00:28:00 | METOP-B | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 30746f5c-3fa7-337a-858f-2325ef3d1eb7 | -7.3897 | -45.9398 | 2025-05-22 00:28:00 | METOP-B | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 94f56b87-b489-3440-bd7e-f830138d46a6 | -11.9573 | -44.158298 | 2025-05-22 00:28:00 | METOP-B | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| a67982ac-6ad1-3cb9-ace9-29b7b0c05808 | -10.3362 | -51.681301 | 2025-05-22 00:28:00 | METOP-B | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 621d0533-d1cb-36be-934f-87f354b990ff | -10.3583 | -47.961899 | 2025-05-22 00:28:00 | METOP-B | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| f76f9b26-3a2b-37ba-b191-3af3de15cbb1 | -11.7933 | -49.331902 | 2025-05-22 00:28:00 | METOP-B | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 0a98dbcb-5d3e-3f20-9ec8-6b2e73bee050 | -12.3499 | -49.982201 | 2025-05-22 00:28:00 | METOP-B | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| a85bbeda-079b-35e4-a454-32915880cefc | -12.0837 | -47.3442 | 2025-05-22 00:28:00 | METOP-B | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 2b1183a8-17aa-31f9-a885-edd142f0d4aa | -11.5776 | -47.610802 | 2025-05-22 00:28:00 | METOP-B | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| b0113169-fe18-3d8c-b630-ca30008dfe5f | -11.7949 | -49.338902 | 2025-05-22 00:28:00 | METOP-B | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 94967586-b463-3047-9e88-c16ef21097b4 | -11.2409 | -49.487801 | 2025-05-22 00:28:00 | METOP-B | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 2bc6ff5b-3ed2-310c-89f5-28a553721949 | -8.7316 | -47.976501 | 2025-05-22 00:28:00 | METOP-B | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| a12b0000-039f-31a5-af64-f2b4f1d5f4b5 | -10.8267 | -56.950401 | 2025-05-22 00:28:00 | METOP-B | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 235937db-ad40-3616-8aac-5deb6a551627 | -7.9413 | -49.754398 | 2025-05-22 00:28:00 | METOP-B | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 12ad2c33-73d5-339e-bffb-fcfc6d0a7e76 | -12.3581 | -49.973 | 2025-05-22 00:28:00 | METOP-B | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 9dd42de4-aec1-3f88-ad1b-e430bd1d3a77 | -11.2973 | -53.9734 | 2025-05-22 00:28:00 | METOP-B | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 06d44163-121e-314a-81c7-e6aab2b38bfd | -12.2959 | -52.488701 | 2025-05-22 00:28:00 | METOP-B | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 44ae8606-4fe5-32da-a79d-c5c887f509c7 | -13.6679 | -53.9249 | 2025-05-22 00:28:00 | METOP-B | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 176644b3-5231-33a5-bdf4-4c60a1b56cd4 | -16.309099 | -49.888 | 2025-05-22 00:28:00 | METOP-B | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| c3d2600c-4b95-32c8-a213-746d9d43a783 | -10.4625 | -49.1427 | 2025-05-22 00:28:00 | METOP-B | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| d6cba593-aa69-397b-8704-3c99b1eceac6 | -10.3378 | -51.688499 | 2025-05-22 00:28:00 | METOP-B | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 7b2645d4-5349-3e61-a085-250d8c01b33a | -13.7856 | -54.3055 | 2025-05-22 00:28:00 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 81108344-deac-3c33-9311-a1e96281f7cc | -12.2776 | -57.259602 | 2025-05-22 00:28:00 | METOP-B | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 5d064ee9-6147-3322-8767-315da67f280e | -16.320499 | -49.893101 | 2025-05-22 00:28:00 | METOP-B | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| b878f827-8361-3947-9ef6-46bfaea3d300 | -11.5615 | -47.451801 | 2025-05-22 00:28:00 | METOP-B | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 3f4ad43f-b812-3073-be7d-f59137cd19d9 | -10.0306 | -48.693298 | 2025-05-22 00:28:00 | METOP-B | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 6316a87f-2c56-39b2-9cf4-91ba91abe7df | -8.9093 | -50.0252 | 2025-05-22 00:28:00 | METOP-B | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a388c201-6e66-33ac-9c74-ad6b895e10e7 | -10.3174 | -47.027901 | 2025-05-22 00:28:00 | METOP-B | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 6af0f126-2ca1-32f2-b0ad-a7559480277c | -9.9646 | -49.8153 | 2025-05-22 00:28:00 | METOP-B | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 97978a2d-5e64-3b97-bde2-206732da435b | -8.7846 | -49.063301 | 2025-05-22 00:28:00 | METOP-B | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 67746975-d5d3-397f-9b06-bec98ee4bbaa | -20.9424 | -56.550999 | 2025-05-22 00:28:00 | METOP-B | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| fe614d41-edc1-389d-bc16-67e55a653444 | -13.5165 | -43.687302 | 2025-05-22 00:28:00 | METOP-B | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| e6f10eaa-7e95-3ad2-9228-7f241ed450f8 | -13.3884 | -48.449402 | 2025-05-22 00:28:00 | METOP-B | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 507e611d-50f8-322b-9ddf-17644eac4c60 | -6.1619 | -48.057999 | 2025-05-22 00:28:00 | METOP-B | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| fdd7c31d-122d-35a7-9c32-f35920c0b5dc | -10.3444 | -47.812099 | 2025-05-22 00:28:00 | METOP-B | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 0915949e-8e20-3625-9587-291fb9edd755 | -16.310699 | -49.895302 | 2025-05-22 00:28:00 | METOP-B | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| a4158ead-052e-3bee-95df-555fc2b8502f | -14.0168 | -55.107601 | 2025-05-22 00:28:00 | METOP-B | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 70c89aa8-8479-3366-a08e-5b887c16c803 | -13.6699 | -53.934898 | 2025-05-22 00:28:00 | METOP-B | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 6c97b50c-68bb-3a7c-97b7-b7621162ff81 | -11.558 | -47.436298 | 2025-05-22 00:28:00 | METOP-B | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| c45410f7-b978-3aef-8e32-4ae95044c098 | -14.0312 | -55.129398 | 2025-05-22 00:28:00 | METOP-B | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 3f0edea3-56c1-3def-99d4-abb43295cb8b | -10.7067 | -48.809799 | 2025-05-22 00:28:00 | METOP-B | OLIVEIRA DE FÁTIMA | TOCANTINS | Brasil | 1715507 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| dc7e3071-710d-3504-983d-310d82fdca10 | -19.060301 | -53.442101 | 2025-05-22 00:28:00 | METOP-B | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 668eee61-dd8c-30fa-87a4-fa7fc4ccddca | -11.6006 | -47.621498 | 2025-05-22 00:28:00 | METOP-B | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 5e751cd0-f72b-3598-932f-79edeafb65b2 | -11.5517 | -47.454102 | 2025-05-22 00:28:00 | METOP-B | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 1395159b-d433-3dc8-8b3e-55e34ccd697f | -10.6544 | -49.445702 | 2025-05-22 00:28:00 | METOP-B | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 931931d3-d3a2-3dab-b84a-156ddaf04a2b | -8.9077 | -50.0182 | 2025-05-22 00:28:00 | METOP-B | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c1cc1db5-c29e-3783-b78c-959f58219fda | -11.083 | -54.760899 | 2025-05-22 00:28:00 | METOP-B | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| d2850036-e3d1-3fcb-8c10-3d48ad6172f0 | -11.4116 | -44.719398 | 2025-05-22 00:28:00 | METOP-B | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 7c47d51c-ad20-39e4-a5a4-33fe59a112ec | -8.9062 | -50.011299 | 2025-05-22 00:28:00 | METOP-B | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cdf1acae-faa9-3b9b-b8d1-58805ce186b5 | -14.0356 | -53.374199 | 2025-05-22 00:28:00 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| ea8f0d15-b196-30a2-8f83-aa53eaa0c711 | -11.7917 | -49.324902 | 2025-05-22 00:28:00 | METOP-B | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 83d5dc38-0def-3336-b9b2-ee6ac896c5b2 | -11.9642 | -44.144299 | 2025-05-22 00:28:00 | METOP-B | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 3cab2533-90aa-3343-aa65-a8cb8adde200 | -11.2425 | -49.494801 | 2025-05-22 00:28:00 | METOP-B | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 34c274bf-79b6-3a93-bbd1-0d822cb36a21 | -12.2878 | -52.499001 | 2025-05-22 00:28:00 | METOP-B | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 2253789e-a81d-3dcf-bfd0-5754e38a91f3 | -8.7334 | -47.9842 | 2025-05-22 00:28:00 | METOP-B | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 688c98ff-60f2-3880-86a6-fbdeb5dd5fc5 | -10.705 | -48.802601 | 2025-05-22 00:28:00 | METOP-B | OLIVEIRA DE FÁTIMA | TOCANTINS | Brasil | 1715507 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 71e43464-d16d-3ec3-8031-e4bab3e99d81 | -11.5989 | -47.6138 | 2025-05-22 00:28:00 | METOP-B | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 2845b1ed-600b-3145-866e-60d9dd9500b1 | -11.1108 | -54.648998 | 2025-05-22 00:28:00 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| d859c75e-2c91-38b6-ab27-2faaf10d0896 | -20.952101 | -56.549301 | 2025-05-22 00:28:00 | METOP-B | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| dcf7723a-ebe6-33fe-b72b-2c70cb46ec01 | -12.2827 | -52.4748 | 2025-05-22 00:28:00 | METOP-B | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 9dec8e51-16af-3b36-97a9-f3e5c40c6803 | -11.967 | -44.1558 | 2025-05-22 00:28:00 | METOP-B | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 4d97bfe8-e2ee-3f6d-bf9d-df708d6642b3 | -11.5746 | -47.8675 | 2025-05-22 00:28:00 | METOP-B | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| bba8ff17-26b1-302c-8be9-dab6d60c92cf | -8.744 | -49.748699 | 2025-05-22 00:28:00 | METOP-B | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4b710693-c4f8-39a2-b8fc-92caf7fb790d | -11.5712 | -47.449501 | 2025-05-22 00:28:00 | METOP-B | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| ea8e1e6e-f88e-33fb-95e5-c2a1bdf579e7 | -12.3483 | -49.975201 | 2025-05-22 00:28:00 | METOP-B | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 9dae95ad-6dd3-3296-923d-a77d999d783f | -11.573 | -47.457298 | 2025-05-22 00:28:00 | METOP-B | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 4a3d2844-6639-3920-985e-5603fa54fe40 | -8.7863 | -49.070499 | 2025-05-22 00:28:00 | METOP-B | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| a3558a76-7d5c-3b73-b7a8-aebedf210b8c | -10.0208 | -48.695499 | 2025-05-22 00:28:00 | METOP-B | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| f8b3a1f3-2dc3-31cb-b238-220131e942d4 | -12.2842 | -57.2421 | 2025-05-22 00:28:00 | METOP-B | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b8465708-6c8e-37cf-8344-eddc4882badc | -11.5633 | -47.459599 | 2025-05-22 00:28:00 | METOP-B | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 6c040fa5-4795-344a-9ee7-920c7e072eb9 | -12.2844 | -52.482899 | 2025-05-22 00:28:00 | METOP-B | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e8c2e5e4-c3a2-32e6-a83e-0ee8028cff2c | -13.4387 | -47.536598 | 2025-05-22 00:28:00 | METOP-B | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 9253ac22-f85b-3ed5-903f-bd15517d4cb8 | -13.8021 | -52.884499 | 2025-05-22 00:28:00 | METOP-B | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| aa402990-3e56-3efe-9f73-0890bd24a11a | -11.5535 | -47.461899 | 2025-05-22 00:28:00 | METOP-B | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| ab2c77e5-79bc-3690-95ee-da4c22965987 | -17.125799 | -48.296799 | 2025-05-22 00:28:00 | METOP-B | ORIZONA | GOIÁS | Brasil | 5215306 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 042b94ef-cb9b-3a18-9567-df195eec25d6 | -12.2745 | -57.243999 | 2025-05-22 00:28:00 | METOP-B | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 39677944-f031-3a7b-81cc-4b9b3352d48b | -11.5694 | -47.4417 | 2025-05-22 00:28:00 | METOP-B | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| dd3b51ed-43a9-3bc6-a782-5edca16b122a | -8.5972 | -49.509602 | 2025-05-22 00:28:00 | METOP-B | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d3c13b55-a57b-33dd-b9d3-5d6fe9a5c92d | -16.312201 | -49.902599 | 2025-05-22 00:28:00 | METOP-B | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README3.md)
