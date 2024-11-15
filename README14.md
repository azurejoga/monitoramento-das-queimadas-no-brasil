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

## Dados Diários - Página 14

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 19e481cb-6e94-3306-8719-45660d8456f5 | -2.32328 | -45.05558 | 2024-11-15 04:21:00 | NOAA-21 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 57196132-82f1-37ec-8d82-7f364646f0e6 | -2.90749 | -46.86216 | 2024-11-15 04:21:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9b14eb84-3cd5-3e05-aea0-f0ef16adb76b | -2.08084 | -47.15235 | 2024-11-15 04:21:00 | NOAA-21 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5ebddd9a-0d00-37f4-9d0f-644c188ce68c | -3.00244 | -40.28402 | 2024-11-15 04:21:00 | NOAA-21 | BELA CRUZ | CEARÁ | Brasil | 2302305 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 02788a42-0933-3c79-90cf-50fb687aaf2e | -2.65711 | -46.18893 | 2024-11-15 04:21:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 92d8c454-e53b-3a9e-9cb2-bdd2dd75e8db | -0.02331 | -51.24732 | 2024-11-15 04:21:00 | NOAA-21 | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8e97c8e3-128a-3ebb-95bd-a8db06bd9c1b | -4.02017 | -38.25174 | 2024-11-15 04:21:00 | NOAA-21 | AQUIRAZ | CEARÁ | Brasil | 2301000 | 23 | 33 | nan | nan | nan | Caatinga | 12.5 |
| 368f3b3f-072f-3abc-8cd8-fc8941f40b7c | -1.85838 | -47.82978 | 2024-11-15 04:21:00 | NOAA-21 | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 41cbc399-da79-32ce-93c4-edae94bcbaab | -3.71773 | -41.69025 | 2024-11-15 04:21:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 6.1 |
| febeba4a-1a38-3ec3-abf2-d04a1ada8af1 | -2.14219 | -46.40337 | 2024-11-15 04:21:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 64023987-1268-3ab4-964a-38e46db060ec | -3.35625 | -44.41134 | 2024-11-15 04:21:00 | NOAA-21 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| afef493d-c939-3dde-8983-d7653020ceb0 | -1.67155 | -47.98243 | 2024-11-15 04:21:00 | NOAA-21 | BUJARU | PARÁ | Brasil | 1501907 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 5d890aac-ef2d-358b-9db0-441ecf4ee3f3 | -3.53074 | -41.84246 | 2024-11-15 04:21:00 | NOAA-21 | CARAÚBAS DO PIAUÍ | PIAUÍ | Brasil | 2202539 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| db763b7e-45f6-362d-ad57-62bb94a5d7e0 | -3.72065 | -41.69471 | 2024-11-15 04:21:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 39ca5ade-cab3-33f0-9cb8-062d6f34a2c6 | -2.09621 | -46.33319 | 2024-11-15 04:21:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9280e7a2-5bab-35b6-ade4-70159913f0b3 | -3.30271 | -43.51146 | 2024-11-15 04:21:00 | NOAA-21 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 3f1298bd-d9b7-3cae-b836-8b645820df81 | -6.05018 | -44.0386 | 2024-11-15 04:23:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 12142ec2-4b6c-3dae-97f8-135a00cc4c77 | -15.31331 | -56.52615 | 2024-11-15 04:23:00 | NOAA-21 | JANGADA | MATO GROSSO | Brasil | 5104906 | 51 | 33 | nan | nan | nan | Cerrado | 5.2 |
| b7979c6a-fba0-3907-886a-3e69a33b87be | -4.63858 | -44.13023 | 2024-11-15 04:23:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| f9f3df38-7fe7-3c7c-addc-178cea82a615 | -3.1912 | -53.99332 | 2024-11-15 04:23:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f6585df4-6cd9-3caa-a383-3d069df55d7e | -10.2524 | -36.36542 | 2024-11-15 04:23:00 | NOAA-21 | FELIZ DESERTO | ALAGOAS | Brasil | 2702702 | 27 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 7b7b95fd-2904-3842-bd51-34b8b6bec945 | -3.55278 | -54.57873 | 2024-11-15 04:23:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4e36bcd7-70d0-3528-b6f9-8ada1832f311 | -4.00642 | -51.02937 | 2024-11-15 04:23:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 1a01b0f6-b5b2-3746-92e0-a2a728f09c6b | -6.50141 | -41.59697 | 2024-11-15 04:23:00 | NOAA-21 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 6.0 |
| a4b1626e-be1c-3484-a935-dc98d6410004 | -8.10179 | -40.19053 | 2024-11-15 04:23:00 | NOAA-21 | OURICURI | PERNAMBUCO | Brasil | 2609907 | 26 | 33 | nan | nan | nan | Caatinga | 0.8 |
| a36fe99a-b78e-35c1-9190-8056797e0d77 | -6.16538 | -41.16275 | 2024-11-15 04:23:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 45cd719a-4864-3a93-8f2f-960bd1729815 | -6.35473 | -39.81812 | 2024-11-15 04:23:00 | NOAA-21 | SABOEIRO | CEARÁ | Brasil | 2311900 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 187731b2-3a1a-3671-9e8b-63e9ec18efad | -5.98071 | -38.3201 | 2024-11-15 04:23:00 | NOAA-21 | ERERÊ | CEARÁ | Brasil | 2304277 | 23 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 6f00001e-9cd4-3ffc-944b-f46c9c5479a2 | -6.93426 | -42.80953 | 2024-11-15 04:23:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| d2bf84ea-6f65-3938-be2c-7a2e26b18377 | -15.31471 | -56.51931 | 2024-11-15 04:23:00 | NOAA-21 | JANGADA | MATO GROSSO | Brasil | 5104906 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| fe8d3a2f-5dde-3d4f-b9ef-2c69f798890c | -4.00718 | -51.02474 | 2024-11-15 04:23:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 27f3ef0c-0f1e-3d12-9fb9-31e505e59daa | -11.8686 | -38.35658 | 2024-11-15 04:23:00 | NOAA-21 | INHAMBUPE | BAHIA | Brasil | 2913705 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| f635bffe-0a62-39ab-978a-85514ab8e216 | -7.30815 | -39.17867 | 2024-11-15 04:23:00 | NOAA-21 | MISSÃO VELHA | CEARÁ | Brasil | 2308401 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 108ae786-3cca-3ffe-b42c-1f0acd31316a | -15.29873 | -56.52664 | 2024-11-15 04:23:00 | NOAA-21 | JANGADA | MATO GROSSO | Brasil | 5104906 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2fcc92a7-0a2d-3112-88ea-605b02a2e609 | -6.97515 | -38.37881 | 2024-11-15 04:23:00 | NOAA-21 | NAZAREZINHO | PARAÍBA | Brasil | 2510006 | 25 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 8859440b-7da9-39f3-920b-7a5253015ead | -3.19183 | -53.98955 | 2024-11-15 04:23:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 54ad350e-23e8-30ce-99c3-ed2cb4cca7d2 | -12.57656 | -57.81246 | 2024-11-15 04:23:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 7eaee949-af9a-3ec2-a402-6cc4a7768e8a | -15.62527 | -57.51387 | 2024-11-15 04:23:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7c1557ad-8a7d-313c-8692-bf1f3a7bc2c1 | -5.79615 | -38.32301 | 2024-11-15 04:23:00 | NOAA-21 | IRACEMA | CEARÁ | Brasil | 2306009 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 8595c4aa-1336-3212-be4d-6c1e94acc292 | -3.55412 | -54.57071 | 2024-11-15 04:23:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| cad1a845-0971-35ec-be7a-a67ccde1143d | -6.40557 | -38.87468 | 2024-11-15 04:23:00 | NOAA-21 | ICÓ | CEARÁ | Brasil | 2305407 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| a1206b69-2afd-3921-81ee-5688943b4710 | -6.1591 | -41.16343 | 2024-11-15 04:23:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 18c49b7f-09b2-363f-9f01-3e6ade21f734 | -4.73054 | -43.2507 | 2024-11-15 04:23:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8b2aa682-8aff-3b9e-ac1a-139ee8f93b9a | -15.29405 | -56.52227 | 2024-11-15 04:23:00 | NOAA-21 | JANGADA | MATO GROSSO | Brasil | 5104906 | 51 | 33 | nan | nan | nan | Cerrado | 4.8 |
| df2d72a2-3707-3beb-a23b-bfe5ec3abd0d | -7.82287 | -38.51618 | 2024-11-15 04:23:00 | NOAA-21 | SERRA TALHADA | PERNAMBUCO | Brasil | 2613909 | 26 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 2e60fdd9-a943-36d0-8b28-55f0eb35e25e | -6.16103 | -41.1666 | 2024-11-15 04:23:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| d9409b98-30c7-3fb2-a3ac-cd7a2401cb43 | -5.39003 | -40.74486 | 2024-11-15 04:23:00 | NOAA-21 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 18214eb7-2e3f-3f95-acb4-b90c733d7f25 | -6.95009 | -41.64894 | 2024-11-15 04:23:00 | NOAA-21 | DOM EXPEDITO LOPES | PIAUÍ | Brasil | 2203404 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 37262079-9f38-3026-8a5e-79b02a2805fa | -15.31609 | -56.52293 | 2024-11-15 04:23:00 | NOAA-21 | JANGADA | MATO GROSSO | Brasil | 5104906 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| badd0654-9322-3830-ac75-20f851f4a5ae | -5.59938 | -43.19274 | 2024-11-15 04:23:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Caatinga | 5.5 |
| 5871b850-2ea2-39bf-93a3-b0a98e7753af | -14.28604 | -57.64015 | 2024-11-15 04:23:00 | NOAA-21 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 2b004acd-2d06-3f20-9df6-941838aca7ad | -15.40911 | -58.61852 | 2024-11-15 04:23:00 | NOAA-21 | INDIAVAÍ | MATO GROSSO | Brasil | 5104500 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6b5c9948-a488-3a34-9f62-c931bcd5bbde | -15.62606 | -57.51001 | 2024-11-15 04:23:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3a55bdb2-3ca3-3d71-9b44-8376f30964ff | -15.48017 | -60.04912 | 2024-11-15 04:23:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 351da98e-c4ae-3c0f-a3a5-bce247b4d563 | -15.90827 | -59.11249 | 2024-11-15 04:23:00 | NOAA-21 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ff4d09c5-a5b1-3e2c-a727-d634a8d12f16 | -15.85506 | -59.29758 | 2024-11-15 04:23:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5435e46b-9cf8-361a-9eea-10af5b4d22a3 | -6.16603 | -41.15835 | 2024-11-15 04:23:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| a86e24c8-7999-3bb4-bc2d-a46fdceb8abb | -15.31676 | -56.51952 | 2024-11-15 04:23:00 | NOAA-21 | JANGADA | MATO GROSSO | Brasil | 5104906 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| d1ed7ed0-1495-3ea7-b7fb-9eab516e7c30 | -15.31077 | -56.52184 | 2024-11-15 04:23:00 | NOAA-21 | JANGADA | MATO GROSSO | Brasil | 5104906 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| d577a1ab-4dea-3fdb-98dc-8526a23fcc6e | -6.85875 | -38.87891 | 2024-11-15 04:23:00 | NOAA-21 | LAVRAS DA MANGABEIRA | CEARÁ | Brasil | 2307502 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 26d3325a-4bf2-3f68-93f7-8304835a78ed | -6.04702 | -44.03754 | 2024-11-15 04:23:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7618e071-8077-305a-a29d-0d9854038c8b | -14.28105 | -57.63489 | 2024-11-15 04:23:00 | NOAA-21 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 04bcdc03-65b7-3f9b-b543-07493fc330ee | -7.11499 | -46.1489 | 2024-11-15 04:23:00 | NOAA-21 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2d2b1aaf-1183-39e0-ba03-2f7bbfbea477 | -12.57674 | -57.81531 | 2024-11-15 04:23:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 1bc896cd-fa21-3a68-b9de-a880b8ce7472 | -10.3877 | -44.87536 | 2024-11-15 04:23:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c5376584-5837-3c93-aee8-316fd854fa21 | -6.97067 | -38.37803 | 2024-11-15 04:23:00 | NOAA-21 | NAZAREZINHO | PARAÍBA | Brasil | 2510006 | 25 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 7b72dde6-13a6-3c3c-9165-0fe5720740f7 | -3.547 | -54.57791 | 2024-11-15 04:23:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 142b34eb-7cc9-39bf-8e90-62859b8e369b | -7.52739 | -35.1571 | 2024-11-15 04:23:00 | NOAA-21 | ALIANÇA | PERNAMBUCO | Brasil | 2600708 | 26 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 00d67ed8-c427-348f-9aee-54f6b14680f0 | -15.31541 | -56.52639 | 2024-11-15 04:23:00 | NOAA-21 | JANGADA | MATO GROSSO | Brasil | 5104906 | 51 | 33 | nan | nan | nan | Cerrado | 5.8 |
| c9962203-ffbc-32c3-8883-373a2c951f6f | -7.12822 | -35.23148 | 2024-11-15 04:23:00 | NOAA-21 | SAPÉ | PARAÍBA | Brasil | 2515302 | 25 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 620485a7-a105-3ab6-b3bf-a2012cc40f2c | -10.72238 | -40.52742 | 2024-11-15 04:23:00 | NOAA-21 | MIRANGABA | BAHIA | Brasil | 2921401 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| ecfa738e-251f-3f1e-a91a-8925595947e5 | -5.9862 | -44.3198 | 2024-11-15 04:23:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 10009ba0-3312-3120-9e68-8097e8dceb6b | -5.98008 | -38.32449 | 2024-11-15 04:23:00 | NOAA-21 | ERERÊ | CEARÁ | Brasil | 2304277 | 23 | 33 | nan | nan | nan | Caatinga | 2.0 |
| e9c47a86-b424-3515-9202-8800240498b3 | -7.07017 | -39.61141 | 2024-11-15 04:23:00 | NOAA-21 | NOVA OLINDA | CEARÁ | Brasil | 2309201 | 23 | 33 | nan | nan | nan | Caatinga | 5.0 |
| 9e9e2c0e-c2d0-35ee-a7c5-3bef0ffddbfc | -3.45066 | -53.46565 | 2024-11-15 04:23:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ccc4acb5-9024-37b5-af87-64d51c4c1383 | -7.65541 | -35.16964 | 2024-11-15 04:23:00 | NOAA-21 | ALIANÇA | PERNAMBUCO | Brasil | 2600708 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 9ba4a725-7c1b-3a5c-a8bd-5f12ef4b89a1 | -10.25196 | -36.36881 | 2024-11-15 04:23:00 | NOAA-21 | FELIZ DESERTO | ALAGOAS | Brasil | 2702702 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 9248f129-9210-36a6-b67a-565a8fb2ce84 | -6.85814 | -38.88326 | 2024-11-15 04:23:00 | NOAA-21 | AURORA | CEARÁ | Brasil | 2301703 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| d0cc21fd-1d39-3e1e-83dd-5400976e7b46 | -3.45007 | -53.46912 | 2024-11-15 04:23:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c6023399-f8a3-3a01-96d6-f9aebe8ec69e | -6.0437 | -44.03703 | 2024-11-15 04:23:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e8b0dc42-5318-3fd9-b706-94f1fca2e35e | -6.14717 | -43.91726 | 2024-11-15 04:23:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1267838f-aaeb-3079-b3db-79890953c1f3 | -15.30938 | -56.51828 | 2024-11-15 04:23:00 | NOAA-21 | JANGADA | MATO GROSSO | Brasil | 5104906 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 47390516-0541-303c-a27a-d34e8d4ae792 | -10.72649 | -40.52796 | 2024-11-15 04:23:00 | NOAA-21 | MIRANGABA | BAHIA | Brasil | 2921401 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 4b2e420b-00f5-3377-973e-8ee6205215b0 | -15.30868 | -56.52169 | 2024-11-15 04:23:00 | NOAA-21 | JANGADA | MATO GROSSO | Brasil | 5104906 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 15fe847d-8b50-3087-b26c-366e3d5800cc | -15.31144 | -56.51845 | 2024-11-15 04:23:00 | NOAA-21 | JANGADA | MATO GROSSO | Brasil | 5104906 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 066f140a-5cb0-3f64-9373-3153aa2c0f4b | -7.12772 | -35.2353 | 2024-11-15 04:23:00 | NOAA-21 | SAPÉ | PARAÍBA | Brasil | 2515302 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 92e41fb1-8ff0-3f27-b736-a4bbef284b6f | -6.14772 | -43.91375 | 2024-11-15 04:23:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 14c05ef2-20ea-3888-9c9c-eddda1d2b6d8 | -15.29338 | -56.52567 | 2024-11-15 04:23:00 | NOAA-21 | JANGADA | MATO GROSSO | Brasil | 5104906 | 51 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 73d01b65-8853-3a5b-a5a0-2b080848d427 | -3.55345 | -54.57471 | 2024-11-15 04:23:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8f1cced0-4d45-3ec0-b251-b985c56e54b0 | -15.29805 | -56.53005 | 2024-11-15 04:23:00 | NOAA-21 | JANGADA | MATO GROSSO | Brasil | 5104906 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 37396532-aded-3e61-80fa-4ecf78bdb29c | -15.40827 | -58.6179 | 2024-11-15 04:23:00 | NOAA-21 | INDIAVAÍ | MATO GROSSO | Brasil | 5104500 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 58604a9d-1f76-37c1-bfd2-9566dd475bb3 | -10.18294 | -36.25965 | 2024-11-15 04:23:00 | NOAA-21 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 477e6f71-3b61-3a98-862a-afd2ee252bda | -6.04648 | -44.04103 | 2024-11-15 04:23:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4a99da81-e6cb-37c9-8ace-8898df35c071 | -10.18148 | -36.25911 | 2024-11-15 04:23:00 | NOAA-21 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 53ffe309-4a86-3c14-87ce-0bb049c3ddd5 | -14.28019 | -57.63908 | 2024-11-15 04:23:00 | NOAA-21 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 137db709-5c39-38b7-85de-0cf683476d95 | -6.35374 | -39.81789 | 2024-11-15 04:23:00 | NOAA-21 | SABOEIRO | CEARÁ | Brasil | 2311900 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| f1df9330-e43d-3078-8981-157fca0d3489 | -6.16414 | -41.15521 | 2024-11-15 04:23:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| fced92d9-93fe-383c-a875-b9aa7f0b40f7 | -15.31401 | -56.52271 | 2024-11-15 04:23:00 | NOAA-21 | JANGADA | MATO GROSSO | Brasil | 5104906 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| a4c5ac5e-af09-3923-a4b2-266a44af9db2 | -6.98345 | -38.46946 | 2024-11-15 04:23:00 | NOAA-21 | CAJAZEIRAS | PARAÍBA | Brasil | 2503704 | 25 | 33 | nan | nan | nan | Caatinga | 1.4 |
| fa64277d-61d6-3a35-b11f-f335837aabd2 | -6.16347 | -41.15961 | 2024-11-15 04:23:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |


[Clique aqui para ver as próximas entradas](README15.md)
