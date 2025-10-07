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

## Dados Diários - Página 74

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 604f6eb5-5656-3e21-9f95-1dd9cdb734b8 | -12.23869 | -43.7795 | 2025-10-07 04:38:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| fb236fc3-fb05-395f-bda3-2bcb0e1f5355 | -14.7035 | -48.37258 | 2025-10-07 04:38:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7bc68a51-1a38-3bde-89af-f25f74a3d409 | -14.91223 | -46.8232 | 2025-10-07 04:38:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| e6df470c-993b-3e03-a0c2-71d14ae26a77 | -13.1022 | -48.01439 | 2025-10-07 04:38:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a588bc3a-2800-3858-a250-427ae76962ec | -11.94645 | -46.44806 | 2025-10-07 04:38:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 2fb2adeb-e282-3d98-957d-a24a5b6cba21 | -12.92335 | -54.72573 | 2025-10-07 04:38:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e70aa397-a237-3950-a21a-fbfbe8cc3591 | -15.60102 | -42.3685 | 2025-10-07 04:38:00 | NPP-375D | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 261e534d-b3f0-3911-b752-ced631add245 | -14.49809 | -46.93575 | 2025-10-07 04:38:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6ea17815-0f37-39c6-ad04-660e486ea970 | -14.75284 | -46.01081 | 2025-10-07 04:38:00 | NPP-375D | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 2d533ba6-3401-329a-9d23-53d28ac91956 | -11.06041 | -47.91357 | 2025-10-07 04:38:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9e0e5ec9-cbcf-38ff-99b4-c9ecb9350972 | -12.38223 | -51.07896 | 2025-10-07 04:38:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5a902428-2b89-3c02-b638-86e2579ee74a | -10.74259 | -50.46511 | 2025-10-07 04:38:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| eb1abdc6-9e7a-397e-b5e8-90ebc4649c9c | -10.30574 | -50.40141 | 2025-10-07 04:38:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7dd4bc35-67ea-31a4-9e44-7050baebd1ef | -13.28058 | -48.05676 | 2025-10-07 04:38:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 99c117e8-b0d9-3af1-84e6-2bf1059ab95e | -15.60407 | -47.29201 | 2025-10-07 04:38:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 14.8 |
| ee58eef4-84a9-36d0-9c29-1a8829619770 | -8.85952 | -62.36409 | 2025-10-07 04:38:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fd84251b-2405-3a16-9aea-a69cb3620112 | -15.29059 | -46.33365 | 2025-10-07 04:38:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0cc8afc2-f8c8-307e-b0f2-cc7b81b2627d | -15.02266 | -47.55587 | 2025-10-07 04:38:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 9488b29c-f4d0-3d4c-b85a-06f3371dbff7 | -12.17952 | -47.77798 | 2025-10-07 04:38:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3fad290d-f8a4-3bb1-b9ce-6f7f79084bce | -11.15122 | -47.95687 | 2025-10-07 04:38:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 956dc0c6-461f-36aa-b50e-56499a383f41 | -13.22807 | -51.69025 | 2025-10-07 04:38:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 30bcf840-e27a-3eaf-81ef-212a578a0de2 | -12.24768 | -47.85595 | 2025-10-07 04:38:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 18c71a78-a17c-38ed-bde0-959c946103f3 | -17.25126 | -46.9287 | 2025-10-07 04:38:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 4d27ccb7-43e5-3c77-8c1b-5fb4d5724888 | -12.94239 | -46.78668 | 2025-10-07 04:38:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 30ef450c-c3a8-3166-9313-291d76eb2b31 | -11.94789 | -51.48198 | 2025-10-07 04:38:00 | NPP-375D | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4536bfd3-38e2-3d12-8331-5a485f84cf48 | -14.92065 | -46.86743 | 2025-10-07 04:38:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d57597cb-cd82-3c98-8959-bbc6166e4c04 | -15.27255 | -46.35399 | 2025-10-07 04:38:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 5a99f7ef-96fc-31d8-abf6-3db9e2cf3b02 | -10.39157 | -50.30571 | 2025-10-07 04:38:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| d6b5232c-c552-3418-b8fe-2557ba0e92da | -9.60668 | -57.14525 | 2025-10-07 04:38:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6d5f865f-a888-3f32-b610-76876add4939 | -13.25291 | -48.05602 | 2025-10-07 04:38:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e7d79575-309b-3b99-bffa-68e8c965de10 | -13.05785 | -47.89472 | 2025-10-07 04:38:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 21fccdc1-5ef2-3c8b-809c-4d0fd2c3c58d | -13.96937 | -48.06451 | 2025-10-07 04:38:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 215f63de-106e-37a5-8f12-6dbc9ee1dd9c | -12.98897 | -46.78497 | 2025-10-07 04:38:00 | NPP-375D | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 92ab6890-f5df-33f5-a8db-0afcb5b6817c | -13.26129 | -47.79623 | 2025-10-07 04:38:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ee994c05-e080-30cf-95c8-20a90a04f4d6 | -9.3397 | -54.51981 | 2025-10-07 04:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7cdb5264-2c35-39c2-8e35-a86edc7efe41 | -13.33472 | -47.76929 | 2025-10-07 04:38:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 09c575ec-ef6b-31c8-8cf2-b9e4e3af1469 | -13.7736 | -43.94151 | 2025-10-07 04:38:00 | NPP-375D | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e5416d74-45ab-3749-a446-20e2c8a8719a | -13.24914 | -47.17149 | 2025-10-07 04:38:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 2487ed84-b4a0-3ebc-9942-2428d493b393 | -16.02 | -50.97303 | 2025-10-07 04:38:00 | NPP-375D | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 0b96779e-509c-3afd-967f-542e934c97a0 | -11.60832 | -43.11548 | 2025-10-07 04:38:00 | NPP-375D | MORPARÁ | BAHIA | Brasil | 2921609 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 3fa249b1-3699-3e83-8cba-b71b42d4eb83 | -12.02069 | -47.79095 | 2025-10-07 04:38:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 05887c0a-e4d3-33ee-85cd-95ab1aa398c1 | -15.49806 | -47.93162 | 2025-10-07 04:38:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| a1a56585-3120-36fd-b682-2e6b87200b6a | -12.40443 | -51.13701 | 2025-10-07 04:38:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 58be353c-76ad-366b-979e-ff5502c74ef5 | -14.49512 | -46.93108 | 2025-10-07 04:38:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5087f641-3ee9-3de4-b677-dbc7d6692920 | -11.96158 | -55.25787 | 2025-10-07 04:38:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4bf01002-0cb1-3b0c-819d-3ffadccfa95c | -15.55786 | -46.82454 | 2025-10-07 04:38:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 4900174c-1e0c-3791-91f3-7623283b3047 | -13.2539 | -47.79887 | 2025-10-07 04:38:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| dbe714be-fd17-31df-828b-1d28fdcb1b4b | -14.9088 | -46.84102 | 2025-10-07 04:38:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 3b4dbe6c-cabb-31ef-8d96-6bb2f94cbcdf | -13.80815 | -41.82618 | 2025-10-07 04:38:00 | NPP-375D | DOM BASÍLIO | BAHIA | Brasil | 2910107 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 0890ada6-5587-364f-be63-6fd40c4b4ca2 | -9.63376 | -57.02417 | 2025-10-07 04:38:00 | NPP-375D | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9d74a2ad-e99d-3049-b59e-843f417b2b78 | -10.37918 | -50.29281 | 2025-10-07 04:38:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.2 |
| 652607fe-da3b-31ed-af4a-68a295d197ee | -15.59291 | -47.26925 | 2025-10-07 04:38:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| e2c87f7b-5d12-3e34-a5f2-a963c3bf5b13 | -16.2902 | -50.98223 | 2025-10-07 04:38:00 | NPP-375D | ISRAELÂNDIA | GOIÁS | Brasil | 5210307 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ede7f407-321f-3cbb-a004-0ce1234660f8 | -14.92119 | -46.81199 | 2025-10-07 04:38:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 8ab935d1-b5e0-33b4-8761-e923f2a62523 | -15.86792 | -46.24904 | 2025-10-07 04:38:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c8d315d9-b8f9-3239-966f-d58739975325 | -15.38741 | -47.99829 | 2025-10-07 04:38:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0029b312-bf90-31cf-8c4a-777b3f0c5e51 | -15.38859 | -47.99047 | 2025-10-07 04:38:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d61d9c6e-c46c-37c6-9d34-52f3df715666 | -10.40734 | -50.31586 | 2025-10-07 04:38:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f64822fb-4bad-37f5-b458-9a1c558f53b0 | -10.73147 | -49.29538 | 2025-10-07 04:38:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d54565c7-641e-314a-aae2-6f40de2d8022 | -11.78801 | -45.09985 | 2025-10-07 04:38:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8ce12e50-b78b-38e6-a7be-c045e3bce11d | -17.60789 | -46.68747 | 2025-10-07 04:38:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 42ff931a-377a-362b-ac84-7c1126c0c4f1 | -11.78353 | -45.10399 | 2025-10-07 04:38:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| dfbb7235-4ce5-3173-a677-21bef1f328c1 | -10.42151 | -50.31445 | 2025-10-07 04:38:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 2e691283-7d57-342a-bc7f-3e08633b7f92 | -16.38209 | -48.99659 | 2025-10-07 04:38:00 | NPP-375D | ANÁPOLIS | GOIÁS | Brasil | 5201108 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 78faecf7-783c-3e82-a240-b7c3a16d9ece | -12.25615 | -47.84595 | 2025-10-07 04:38:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| be09b73d-d63d-33fd-880a-88523c903dd5 | -13.37325 | -48.04489 | 2025-10-07 04:38:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| aced1ded-9505-3b09-a915-167fc1923b71 | -11.6772 | -46.34362 | 2025-10-07 04:38:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 52caa7ae-0c21-38ad-8020-7b6500a92e3b | -10.4507 | -50.34945 | 2025-10-07 04:38:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 15.8 |
| 24c5ac31-5d66-37fd-ab2f-d8f262edf2bf | -12.31687 | -55.11143 | 2025-10-07 04:38:00 | NPP-375D | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0dfb3676-34b9-3186-8612-ea7880982e71 | -15.03823 | -56.02995 | 2025-10-07 04:38:00 | NPP-375D | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| d296c11b-cfb9-37a7-958c-8e2480b4f383 | -13.33532 | -47.76535 | 2025-10-07 04:38:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| aed8fd68-a71b-3999-9503-34aa45fb99b0 | -10.91806 | -47.0689 | 2025-10-07 04:38:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| b296cbec-0d5c-30fa-a037-cffc1cd0b398 | -15.49772 | -46.83088 | 2025-10-07 04:38:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| acb5654d-ac7d-3627-9b94-71de0eca24d4 | -10.38538 | -50.30092 | 2025-10-07 04:38:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 387b385d-96fb-3525-8b75-15c58e99230a | -13.27933 | -47.16031 | 2025-10-07 04:38:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 33ac32b9-3339-3809-9d6f-dff8953d5f71 | -14.64214 | -52.54126 | 2025-10-07 04:38:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 80ee16a3-cb16-3629-b029-b2143d4a85a4 | -13.22872 | -51.68636 | 2025-10-07 04:38:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f41db64e-40a3-34a1-855d-14d540563c57 | -12.40667 | -51.14078 | 2025-10-07 04:38:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 69f082d1-b24e-3875-a352-ed9b85b5740b | -10.56089 | -56.55309 | 2025-10-07 04:38:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 4321a8e5-89e0-358a-800e-9060ac2e4bb1 | -15.22934 | -49.30878 | 2025-10-07 04:38:00 | NPP-375D | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 60b4aef0-5698-3410-811a-d6063edda36d | -10.45416 | -50.41428 | 2025-10-07 04:38:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 7573e36d-5179-3752-a454-178457648a78 | -13.26479 | -47.18633 | 2025-10-07 04:38:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7a639f80-59ab-3a48-af3f-2c828790b246 | -13.06303 | -47.92946 | 2025-10-07 04:38:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 91f29d0d-b20d-302c-adc1-551ff07334bb | -14.64237 | -48.31672 | 2025-10-07 04:38:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a2b6bd14-6211-3fc9-85d4-b8162f94df5c | -14.93289 | -51.42138 | 2025-10-07 04:38:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 751ef9d2-c4e0-3e62-9699-b4d4b6062ea6 | -10.41532 | -50.30965 | 2025-10-07 04:38:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 16.5 |
| 85ce8820-76a4-3f40-822e-adf1f63ec578 | -11.78716 | -45.13252 | 2025-10-07 04:38:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7e4aae68-eac0-35ae-8b73-b2a4739043c5 | -15.31463 | -43.09282 | 2025-10-07 04:38:00 | NPP-375D | CATUTI | MINAS GERAIS | Brasil | 3115474 | 31 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 789878c5-a3f1-3726-a2be-f4d721c50e32 | -11.84382 | -44.91671 | 2025-10-07 04:38:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| bd6bf8b8-fbc4-3093-8e91-cb3130877ba8 | -13.24733 | -47.17615 | 2025-10-07 04:38:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 2e73d208-de42-341e-befb-4fa3c74acf4b | -13.36564 | -47.25647 | 2025-10-07 04:38:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e9f7031a-b0bc-3111-8686-b677c7376e6e | -13.72532 | -48.20163 | 2025-10-07 04:38:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| db9239e0-ff4f-3296-a0ff-d1840691da24 | -13.29472 | -48.05511 | 2025-10-07 04:38:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5a9a071c-2581-37d0-9a66-757afd4e8473 | -14.91838 | -51.4458 | 2025-10-07 04:38:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 7.8 |
| db0de37d-7c2f-3323-81d7-4fdeb4352eff | -14.68716 | -48.3889 | 2025-10-07 04:38:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c93fbf33-91c8-3010-bebb-afb99d8e1b85 | -16.00149 | -50.95156 | 2025-10-07 04:38:00 | NPP-375D | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 4dd1db1f-bf56-30df-9441-fd09cfc4aea8 | -13.31369 | -47.76954 | 2025-10-07 04:38:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b69220ff-8b94-3b4d-99bc-7205f5444c56 | -14.62214 | -52.4871 | 2025-10-07 04:38:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 4.9 |
| db7396d5-e338-3c00-8742-63c8e878cde3 | -15.20453 | -46.38125 | 2025-10-07 04:38:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 03cefe92-ed9d-3454-af6a-8477e04f8ef4 | -10.378 | -50.30346 | 2025-10-07 04:38:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |


[Clique aqui para ver as próximas entradas](README75.md)
