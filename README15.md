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

## Dados Diários - Página 15

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| afafc19d-6cc7-3957-bc61-1dd91130f03b | -7.69252 | -42.24191 | 2025-10-25 03:57:00 | NPP-375D | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 6d439f34-5cf8-3c4d-b279-c85b6e802b88 | -7.46136 | -41.90735 | 2025-10-25 03:57:00 | NPP-375D | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 43dc3e82-4257-3b5d-beb0-bf89ec81354c | -2.80628 | -49.13446 | 2025-10-25 03:57:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 14.2 |
| f214726f-22ba-32dd-ba40-fde99d67264e | -6.03073 | -39.62168 | 2025-10-25 03:57:00 | NPP-375D | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 0f653766-4589-3ce4-ae9a-5ba6487c8f80 | -3.85644 | -40.73814 | 2025-10-25 03:57:00 | NPP-375D | MUCAMBO | CEARÁ | Brasil | 2309003 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 555b4b32-af77-3dd5-a979-444065760e35 | -4.84958 | -42.38194 | 2025-10-25 03:57:00 | NPP-375D | ALTOS | PIAUÍ | Brasil | 2200400 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 8ac97d8c-0264-3915-8003-6fbac2a5a6be | -3.13944 | -50.62143 | 2025-10-25 03:57:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e4923a0f-af34-332a-a698-8215e87c4343 | -5.64538 | -45.97103 | 2025-10-25 03:57:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 89e9c331-27ae-3b1a-993d-07a8a2a20cf3 | -7.55388 | -47.11555 | 2025-10-25 03:57:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fd5cd549-e31f-3bef-b078-4802c64d4922 | -6.64378 | -43.60978 | 2025-10-25 03:57:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5fd2b13e-5676-398c-b1dd-624a9d7bca8b | -6.13009 | -41.71918 | 2025-10-25 03:57:00 | NPP-375D | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| bb0727a8-61dd-30de-b29d-492a3c88d1ff | -6.1112 | -41.74269 | 2025-10-25 03:57:00 | NPP-375D | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 03aeef77-7db5-3afb-b898-2d454822509e | -6.08854 | -39.19435 | 2025-10-25 03:57:00 | NPP-375D | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 6fb655ac-2911-3f12-a107-1a967e80d6df | -2.89777 | -48.06528 | 2025-10-25 03:57:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 798e3732-5ffd-390c-a1a7-c47bd8d8c77f | -6.51708 | -46.51151 | 2025-10-25 03:57:00 | NPP-375D | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9f974697-86a0-37a8-b1a2-2fd62a036fe3 | -4.25646 | -44.58065 | 2025-10-25 03:57:00 | NPP-375D | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 7234f521-431d-35d2-9690-9e4b27994250 | -3.40537 | -42.48053 | 2025-10-25 03:57:00 | NPP-375D | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 46a8dd12-af5b-3a01-a360-a4191cec7215 | -3.86587 | -51.89794 | 2025-10-25 03:57:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| f47c9c0f-4b18-393c-9977-6c17dfecc5c1 | -7.16878 | -45.84715 | 2025-10-25 03:57:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2b1c542f-bb23-31c4-bcbd-0c0b7c8622eb | -3.11274 | -51.2132 | 2025-10-25 03:57:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7cd6a027-dc1e-335c-b0dd-355dd20daf41 | -4.81057 | -45.57953 | 2025-10-25 03:57:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 8d32d785-5b40-323d-a49b-04c80fa8c30d | -8.31294 | -47.86562 | 2025-10-25 03:57:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 623fabe0-86c1-3035-bed4-ebd27a332e28 | -4.2572 | -44.57611 | 2025-10-25 03:57:00 | NPP-375D | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| caf08b9b-15be-30f1-83df-660e0e82e241 | -3.12486 | -49.10032 | 2025-10-25 03:57:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| dd30afbf-a04e-31ae-8985-9b6eb2a0563a | -3.99955 | -48.32244 | 2025-10-25 03:57:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 23965361-28ea-39fe-8a96-fcfa44266d65 | -2.77467 | -48.0213 | 2025-10-25 03:57:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 526f50ff-975c-3b87-886c-61ea776db498 | -3.26409 | -50.15037 | 2025-10-25 03:57:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e038f875-1a0e-35d9-96f1-e17cb907f72e | -8.2421 | -42.35282 | 2025-10-25 03:57:00 | NPP-375D | SÃO JOÃO DO PIAUÍ | PIAUÍ | Brasil | 2210003 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| d5ee0d88-db82-31ce-ad97-058819ae2bf3 | -7.42908 | -38.78479 | 2025-10-25 03:57:00 | NPP-375D | MAURITI | CEARÁ | Brasil | 2308104 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 7ebc6c4a-8745-345a-808b-d1d806134747 | -5.33552 | -44.72018 | 2025-10-25 03:57:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 005cfe52-5e79-3400-b1dc-0e43c5fcd48c | -7.55895 | -47.11651 | 2025-10-25 03:57:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 8dc1d979-8f66-3966-8c24-5e04f5af3f5b | -5.46192 | -46.47575 | 2025-10-25 03:57:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 0506d473-5cd6-3b9d-b15e-3bcbea1b1e35 | -5.915 | -39.19587 | 2025-10-25 03:57:00 | NPP-375D | DEPUTADO IRAPUAN PINHEIRO | CEARÁ | Brasil | 2304269 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 3436726e-6162-3b1e-90d3-5b8e83e1fe4f | -4.3741 | -38.88653 | 2025-10-25 03:57:00 | NPP-375D | BATURITÉ | CEARÁ | Brasil | 2302107 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 33bc019f-267c-3356-a48b-3e11056fbf63 | -6.23073 | -41.82643 | 2025-10-25 03:57:00 | NPP-375D | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| e45c40e8-36e7-3594-9646-37a74927e1d1 | -6.17983 | -42.62133 | 2025-10-25 03:57:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 11.0 |
| 70703c6c-0847-3cf7-a848-69512595d0b8 | -2.73054 | -49.16212 | 2025-10-25 03:57:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 07a04937-ee7e-33e1-a75b-35c4845a1b8c | -6.14382 | -44.73286 | 2025-10-25 03:57:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8b880fb3-27b9-3699-b1a0-5ec5d38fa22f | -5.80004 | -35.58207 | 2025-10-25 03:57:00 | NPP-375D | IELMO MARINHO | RIO GRANDE DO NORTE | Brasil | 2404606 | 24 | 33 | nan | nan | nan | Caatinga | 1.2 |
| a730326c-5c40-3b9d-a6e5-70facd80e837 | -7.37641 | -47.04979 | 2025-10-25 03:57:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 41e00519-5404-31e9-9514-a85a63f84ad8 | -3.86717 | -51.89078 | 2025-10-25 03:57:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 95faa77b-adad-319f-8010-04b4f0384b3c | -7.15368 | -44.12447 | 2025-10-25 03:57:00 | NPP-375D | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 28ac40ce-3d83-305d-b42c-aec49dc379a7 | -7.33728 | -46.14779 | 2025-10-25 03:57:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a16e129f-89ae-37ae-81c0-4dc3143003b2 | -6.31929 | -41.86307 | 2025-10-25 03:57:00 | NPP-375D | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 6e27636e-8a5e-341c-8847-7a9af3e60b43 | -5.45687 | -46.47486 | 2025-10-25 03:57:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| bdad95d9-e1fc-33ea-bf08-ca559c9c4ee6 | -6.31309 | -40.92216 | 2025-10-25 03:57:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 80286bc8-8c01-3694-9bff-a21f7bb3b27d | -8.83302 | -44.21392 | 2025-10-25 03:57:00 | NPP-375D | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 32f42073-f6ed-3a5d-80ab-8ab49f9b08fc | -8.60887 | -44.81435 | 2025-10-25 03:57:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6f6d5e9e-6eb9-3cfa-b2c8-81443860de99 | -6.70917 | -44.63279 | 2025-10-25 03:57:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 13cb82c5-5a44-38bd-bae0-4fbd3904b338 | -6.89941 | -45.17481 | 2025-10-25 03:57:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 5abcc64c-b75a-36e9-8be1-6fe633e6886f | -4.26991 | -40.70004 | 2025-10-25 03:57:00 | NPP-375D | IPU | CEARÁ | Brasil | 2305803 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| d979b60a-ca4a-343f-ab5a-1f74c2181e7b | -7.37693 | -47.04679 | 2025-10-25 03:57:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| eab80fe8-82c2-3171-a802-dad7cafbc60a | -3.16364 | -48.61236 | 2025-10-25 03:57:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 80608766-c6dd-3307-be96-adfa94f40709 | -6.12573 | -41.7228 | 2025-10-25 03:57:00 | NPP-375D | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| fea3a9a3-f1ef-3f6a-b9aa-f72a27d4b7f1 | -3.23995 | -48.75942 | 2025-10-25 03:57:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3bc65724-fe39-30a9-9b76-8332bab01a86 | -7.43823 | -46.60825 | 2025-10-25 03:57:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| af0da102-e839-3e74-b5a2-a7352fdbe825 | -5.56916 | -40.90094 | 2025-10-25 03:57:00 | NPP-375D | NOVO ORIENTE | CEARÁ | Brasil | 2309409 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| e64d8a22-4265-330d-8889-bd0b7e350e72 | -6.81261 | -45.42984 | 2025-10-25 03:57:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8d21dc43-4f06-382e-81b1-0447c1262fb3 | -4.32873 | -47.89031 | 2025-10-25 03:57:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6e9aad23-86ce-3370-9b3c-4c37ef7a4cf9 | -2.80545 | -49.13937 | 2025-10-25 03:57:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 14.2 |
| 7be22570-3793-3719-8a89-be0c3cb17d1c | -3.98934 | -50.52885 | 2025-10-25 03:57:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f69f36f2-b964-3d78-a469-c39090d31b79 | -4.28832 | -48.26437 | 2025-10-25 03:57:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 141c3452-021c-3b51-935a-a62e2276d758 | -5.96475 | -38.13616 | 2025-10-25 03:57:00 | NPP-375D | SÃO FRANCISCO DO OESTE | RIO GRANDE DO NORTE | Brasil | 2411908 | 24 | 33 | nan | nan | nan | Caatinga | 2.2 |
| f64a4033-3b39-330c-ae87-594d1e31c25b | -5.54627 | -46.52962 | 2025-10-25 03:57:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b22d4330-56ba-3207-9cf0-75a44b71939e | -6.22248 | -42.54178 | 2025-10-25 03:57:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| db864977-814b-3bfb-bc94-e4e99fa2f597 | -7.5635 | -47.12048 | 2025-10-25 03:57:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| c9951bad-ba51-3ed9-8576-f983fc159850 | -4.9727 | -48.3642 | 2025-10-25 03:57:00 | NPP-375D | ABEL FIGUEIREDO | PARÁ | Brasil | 1500131 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0f637142-dfc6-32b5-84a0-5102c56841a3 | -6.03016 | -39.62527 | 2025-10-25 03:57:00 | NPP-375D | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 607ebbc8-ea01-3dae-9851-dfe6320faebd | -6.4094 | -43.76845 | 2025-10-25 03:57:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a635bea7-318f-390a-afb3-c56288c0b444 | -7.50384 | -38.37611 | 2025-10-25 03:57:00 | NPP-375D | IBIARA | PARAÍBA | Brasil | 2506608 | 25 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 46c0e5b0-c652-31c4-8d67-d675b20ca2b9 | -4.80968 | -45.58482 | 2025-10-25 03:57:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 5a93d8fd-a855-3493-a417-09b5edd726f1 | -4.95979 | -47.59499 | 2025-10-25 03:57:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c30822d9-b6d6-3d3c-b0e7-86643d75a73c | -4.55922 | -46.68679 | 2025-10-25 03:57:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 890bd176-f00b-3daa-8b58-cf6e7bf45ee9 | -3.09943 | -50.2094 | 2025-10-25 03:57:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 1aced449-cf90-366a-a20e-3217d38484e7 | -2.72565 | -48.3493 | 2025-10-25 03:57:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 93564849-8067-39d7-ba31-9266e4ad3b16 | -2.72611 | -49.16901 | 2025-10-25 03:57:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 8853078a-5034-34bb-a828-a079e4fe653c | -4.29411 | -48.26538 | 2025-10-25 03:57:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6469ae68-7ce1-31ca-b043-60bc94690ac6 | -4.59666 | -49.59058 | 2025-10-25 03:57:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| a8e6a3a7-9e6b-34df-9a3e-ae9201a87774 | -6.22331 | -42.53689 | 2025-10-25 03:57:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 2a85fb5c-032a-3902-84d0-fb0ef7aec893 | -6.79081 | -45.42287 | 2025-10-25 03:57:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| bace5b07-5629-36ce-b826-80d729aed3f8 | -5.72654 | -49.0978 | 2025-10-25 03:57:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 3fd8e6bc-c5bc-3a9c-b4b5-e80be0de3ebc | -6.91365 | -45.17295 | 2025-10-25 03:57:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 95f92b03-4913-3383-9575-17041a750621 | -2.81002 | -49.1505 | 2025-10-25 03:57:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 8e0b9777-e1d5-31f5-830e-b61780c133db | -5.91165 | -39.19534 | 2025-10-25 03:57:00 | NPP-375D | DEPUTADO IRAPUAN PINHEIRO | CEARÁ | Brasil | 2304269 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 9a51c494-5f93-3048-a616-de9678ab84cf | -4.61 | -47.02264 | 2025-10-25 03:57:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7c5fc26f-e6ff-3746-9405-295b84be9a3c | -6.83297 | -44.77619 | 2025-10-25 03:57:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5593128e-cd12-3cc2-9104-3d2678b7fbab | -2.80376 | -49.14936 | 2025-10-25 03:57:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 10.2 |
| ebc8a7ee-847f-31ed-a131-9cf85d66094d | -9.62312 | -40.33781 | 2025-10-25 03:57:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 609a1938-d59f-3fbd-b4c1-29c530854021 | -9.11723 | -45.85751 | 2025-10-25 03:57:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 1ba399b1-dfe8-3616-a3ae-6a56624ddd5b | -5.83871 | -40.79763 | 2025-10-25 03:57:00 | NPP-375D | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 5a2db2d5-3f16-3a7b-8c82-c5c356985d4f | -4.22957 | -48.61618 | 2025-10-25 03:57:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a7e53ae5-02c7-30c9-9a62-c5275ab8ae63 | -6.28584 | -40.86621 | 2025-10-25 03:57:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 26376472-2529-372e-af84-93ef12d94b84 | -4.80201 | -46.74266 | 2025-10-25 03:57:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 98407a99-00cf-3b19-b173-996c17ecdbae | -5.80683 | -35.53824 | 2025-10-25 03:57:00 | NPP-375D | IELMO MARINHO | RIO GRANDE DO NORTE | Brasil | 2404606 | 24 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 0c466078-3a2e-397a-92ad-979f655f1f16 | -6.80713 | -42.39987 | 2025-10-25 03:57:00 | NPP-375D | CAJAZEIRAS DO PIAUÍ | PIAUÍ | Brasil | 2202075 | 22 | 33 | nan | nan | nan | Caatinga | 6.5 |
| 750077b7-936e-3540-b11d-561ee701e0b7 | -6.55376 | -43.23446 | 2025-10-25 03:57:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 23da8ed3-cf4c-3b45-aad3-e29e19e31c7d | -6.22632 | -42.54242 | 2025-10-25 03:57:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 7d2d5782-1cab-3e89-bb6c-5eaf22a3b4de | -4.8455 | -50.93867 | 2025-10-25 03:57:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| be56a97a-f724-35f4-aaa7-37552d1ef6d0 | -3.23354 | -48.75644 | 2025-10-25 03:57:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f65dd45d-d948-379e-bb99-f76966b61296 | -3.08086 | -49.47292 | 2025-10-25 03:57:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |


[Clique aqui para ver as próximas entradas](README16.md)
