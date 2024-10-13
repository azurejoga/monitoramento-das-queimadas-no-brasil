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

## Dados Diários - Página 78

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 94a9450d-2d86-3867-a16b-b504d813b1a2 | -3.04324 | -51.129 | 2024-10-13 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c0fd2362-ce9b-312f-b549-b7999264cd82 | -3.04256 | -51.13348 | 2024-10-13 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8c4ba16b-f8a0-3325-b8ad-e1b97bb91deb | -3.03881 | -51.13292 | 2024-10-13 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c92949a6-dc84-30dd-b3f2-8ede28a3a3eb | -3.02052 | -51.20302 | 2024-10-13 05:01:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4bcddbfe-db69-3c17-8585-7930851eea3b | -3.01985 | -51.20744 | 2024-10-13 05:01:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 038f2e65-f3aa-3f72-9f3d-30bfd8cdcc2e | -3.01918 | -51.21185 | 2024-10-13 05:01:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 999a4da1-de46-3abc-86ce-7d115dd849dd | -3.01679 | -51.20243 | 2024-10-13 05:01:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4aca7be9-d6c0-3215-a3da-8b8327a0b282 | -3.01612 | -51.20687 | 2024-10-13 05:01:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4512350e-5297-383d-adeb-66764b7f1100 | -3.01545 | -51.21128 | 2024-10-13 05:01:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9613ff9a-ce78-3986-ac68-e9018fd90bb4 | -2.97437 | -51.35757 | 2024-10-13 05:01:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e5b86f8d-ade8-3f22-8c25-9437d5cd7b87 | -2.97306 | -51.36628 | 2024-10-13 05:01:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3d43001f-2ccf-321b-b2b8-58fe32515160 | -3.58521 | -51.51319 | 2024-10-13 05:01:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e1b085fd-4e33-31b1-aabb-1360312bc0d2 | -3.58219 | -51.50827 | 2024-10-13 05:01:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e7837c68-0fac-3653-b337-fb17dbb96eca | -3.58152 | -51.51261 | 2024-10-13 05:01:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 9829bbd5-a9fc-318b-a6e4-ecb7b971dcf8 | -3.57783 | -51.51204 | 2024-10-13 05:01:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 69969339-03ea-331c-a41b-28e6348d50df | -3.559 | -51.487 | 2024-10-13 05:01:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f4dba526-68de-33ff-b11e-47d015b33484 | -3.46737 | -51.54999 | 2024-10-13 05:01:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3bdaee7e-9726-3678-a7e2-1d6538995443 | -3.4667 | -51.55431 | 2024-10-13 05:01:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1abca47b-3ee3-3633-8f54-5ce11dfb1f2b | -3.4637 | -51.54941 | 2024-10-13 05:01:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0d738d8e-7022-3cab-aba3-eff1813643ca | -3.46303 | -51.55373 | 2024-10-13 05:01:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 2732836b-81d7-31b3-b08e-e424c24feee6 | -3.44903 | -51.5955 | 2024-10-13 05:01:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 136870c3-b2d7-3459-8ec4-0df8fcddf5fe | -3.4076 | -51.57167 | 2024-10-13 05:01:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4190390c-73de-35a1-9157-4f232c89fbb5 | -3.36764 | -52.16745 | 2024-10-13 05:01:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| bdb2ae93-94bb-35f7-8598-6e569d78aa37 | -3.30032 | -51.49466 | 2024-10-13 05:01:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 43e9ce42-4cb0-32f4-bba9-e150a9e4762d | -3.20454 | -51.75523 | 2024-10-13 05:01:00 | NPP-375D | VITÓRIA DO XINGU | PARÁ | Brasil | 1508357 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6fa102f1-1289-3b70-890f-dd093b599dba | -4.61555 | -50.95123 | 2024-10-13 05:01:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| dda87018-7d3a-3af3-b1eb-4baf9abc0350 | -4.61482 | -50.95606 | 2024-10-13 05:01:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 50796b78-76b2-388c-b7b3-152f0c4c3254 | -4.61169 | -50.9506 | 2024-10-13 05:01:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 42b6ef33-106c-33cd-a6ca-158f198b8f02 | -4.27574 | -50.95611 | 2024-10-13 05:01:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a1b6e25a-6ed3-374a-881e-b7dc8f11f3ea | -4.27502 | -50.96089 | 2024-10-13 05:01:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| dc5dae29-fef2-3ded-864c-c577e95ad29e | -4.27189 | -50.9555 | 2024-10-13 05:01:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b36266ab-a739-3950-aea1-038eec84f360 | -4.27117 | -50.96027 | 2024-10-13 05:01:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0f57a45d-4f37-3cc4-baba-3f661e05c8f6 | -4.2642 | -50.95435 | 2024-10-13 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3af49bb3-a95e-3740-b0dc-e71a1c88976c | -4.12438 | -51.11351 | 2024-10-13 05:01:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 22b7e2b5-7e8e-3716-afdc-2ab6c11e762f | -4.12061 | -51.11272 | 2024-10-13 05:01:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 65114a0b-ba45-31c0-961f-1816c85125c7 | -4.03861 | -51.09812 | 2024-10-13 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 92ffc6af-57c4-3ba6-a911-6a6ae40f5fa3 | -4.0259 | -51.00143 | 2024-10-13 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0fec3a1d-4570-3948-bb66-a882744af258 | -4.02208 | -51.00076 | 2024-10-13 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a6126db5-029a-31f9-8ed1-1315fd0b22a7 | -3.97373 | -51.01961 | 2024-10-13 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6c74a3fc-20c4-314b-8c2b-ac1a7fa21d34 | -3.96992 | -51.019 | 2024-10-13 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| dec080fb-80ff-31ac-a6ba-a5d30fc99a47 | -3.92549 | -51.23288 | 2024-10-13 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3a40927a-bbd0-3e7e-a850-9b7f677d3dd6 | -3.92311 | -51.2232 | 2024-10-13 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b5018c7e-4a2e-3eb4-8abb-d56e41e760f6 | -3.92242 | -51.22776 | 2024-10-13 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 99cc2a63-ef5d-39a9-9142-a8ad3bf606fd | -3.92172 | -51.23229 | 2024-10-13 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ab556762-5135-370a-8098-221f03af406b | -3.91865 | -51.22717 | 2024-10-13 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 34d4d2bf-112d-3e5e-95c1-4e566d42dfa7 | -3.91796 | -51.23171 | 2024-10-13 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 4cf55938-305a-3d7e-93ef-9f54c35723df | -3.91727 | -51.23623 | 2024-10-13 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e64b2f81-0ed8-3c9b-bf72-da31a0a48367 | -3.96389 | -52.17313 | 2024-10-13 05:01:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 962cb5b0-b3ed-3024-b2e5-204420de1830 | -3.96328 | -52.17715 | 2024-10-13 05:01:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d5e8d069-e6a3-3afb-abdb-c201b42b81e7 | -3.92438 | -52.13514 | 2024-10-13 05:01:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a15cdd19-8062-38a3-84b4-ec409e356c84 | -3.9166 | -52.20866 | 2024-10-13 05:01:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b42d47c0-17a8-3da5-b434-9681ba87e5d7 | -3.91303 | -52.2081 | 2024-10-13 05:01:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| aa0b6355-79c0-3983-a1d6-24d6c21891a9 | -3.91239 | -52.21216 | 2024-10-13 05:01:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| e2825fc9-9acd-3961-b208-2b45aa306683 | -3.89808 | -52.21006 | 2024-10-13 05:01:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 68cb0290-565e-3789-8df4-b694f4b153b4 | -3.88801 | -51.9398 | 2024-10-13 05:01:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8819f695-3f6c-3d99-8b00-30d4086ed5a8 | -3.88738 | -51.94396 | 2024-10-13 05:01:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e53f7d3a-af8d-3221-a2e5-8c9aa39f45b8 | -3.88438 | -51.93926 | 2024-10-13 05:01:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 46e6f3b3-a247-3c99-ba1a-6f3e5342b72a | -3.88375 | -51.94343 | 2024-10-13 05:01:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 67083767-39eb-3918-addd-55ae858029be | -3.88312 | -51.9476 | 2024-10-13 05:01:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f2bf54b4-f63e-3a70-9eb3-353d08f93937 | -3.87871 | -51.97661 | 2024-10-13 05:01:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6889e052-96be-3509-a801-6791670ca9f2 | -3.87509 | -51.97606 | 2024-10-13 05:01:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a06c6b1f-6bef-3a7d-b425-259a5acc921c | -3.8617 | -51.89029 | 2024-10-13 05:01:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 97c18cd5-2e26-3864-a3c9-bbe05e95e4cd | -3.86122 | -52.18796 | 2024-10-13 05:01:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c7cf597b-0a78-33f4-ad03-5b6777b1e11d | -3.8606 | -52.19201 | 2024-10-13 05:01:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fa420c6e-c185-322f-b545-200d640cd26c | -3.83395 | -51.87749 | 2024-10-13 05:01:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 21f48fee-84ab-36ba-a5d5-1a27b0a07d11 | -3.83096 | -51.87276 | 2024-10-13 05:01:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a9b54fd0-80b8-36ac-b4d2-8d1efe7e33d4 | -3.83096 | -51.40168 | 2024-10-13 05:01:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 182ae3f1-5596-32aa-ba8f-ab4811aa7e6e | -3.83031 | -51.87694 | 2024-10-13 05:01:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7b76236c-bc2c-3718-87b1-870c442dae4d | -3.8303 | -51.4061 | 2024-10-13 05:01:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f22e0658-abf0-3e1f-a2ee-ac8eea2272ed | -3.82989 | -51.40303 | 2024-10-13 05:01:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 16ecc1af-85b8-35f5-ae89-195625c49a3c | -3.82964 | -51.4105 | 2024-10-13 05:01:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| bc1268d6-8f20-3671-85e4-a4163554fa34 | -3.82921 | -51.40743 | 2024-10-13 05:01:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 47c0db28-c078-30f9-9904-01222820b4e3 | -3.82852 | -51.41183 | 2024-10-13 05:01:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 52baebf1-f7f3-3dac-8f77-324dc9f82c89 | -3.7871 | -51.98945 | 2024-10-13 05:01:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8c2716c4-33f5-329b-8e02-f1aea13c106e | -3.77726 | -51.83459 | 2024-10-13 05:01:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 193165fa-6f85-34aa-8f77-fb9002f39913 | -3.77437 | -51.83089 | 2024-10-13 05:01:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| faa74c49-2949-3b70-bc00-8fd3a7a2377f | -3.77426 | -51.82979 | 2024-10-13 05:01:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fc4b1c78-2435-3330-8e87-b3519bf23724 | -3.7737 | -51.83512 | 2024-10-13 05:01:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| df5b8c48-d8cb-3a7f-8b75-7d4346601241 | -3.77362 | -51.83403 | 2024-10-13 05:01:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1dca4cbb-50e1-3f47-900e-44d8f3b25907 | -3.77276 | -52.24969 | 2024-10-13 05:01:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 72914720-0d97-357d-bcd0-4588c909e8c4 | -3.77268 | -51.8895 | 2024-10-13 05:01:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2edf9693-5abb-3518-bbe2-112760d36a9e | -3.75065 | -51.93723 | 2024-10-13 05:01:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f5b0ec45-3db2-3599-b806-32eda7b8ef17 | -3.72839 | -51.81514 | 2024-10-13 05:01:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 91bb1da5-f241-3cdb-ace4-f824443903ab | -3.71341 | -51.79134 | 2024-10-13 05:01:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 3321397b-4462-3fd1-8f77-e935fe7c013b | -3.71277 | -51.79554 | 2024-10-13 05:01:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 628144c4-e69a-3487-a7a0-d4e1f49bcf28 | -3.70976 | -51.7908 | 2024-10-13 05:01:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 2396f235-545b-3fd9-b403-b5c256af746e | -3.68684 | -52.01294 | 2024-10-13 05:01:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 742fdb30-f272-37b3-9bf8-90d1c20612ae | -3.64237 | -52.01456 | 2024-10-13 05:01:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4ba0311c-0780-3291-b4df-5dc931a82b17 | -3.641 | -52.04787 | 2024-10-13 05:01:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| e31d021d-5637-33f7-98e4-11cc08192232 | -3.78174 | -51.31864 | 2024-10-13 05:01:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a7f8511d-f891-3732-bbae-09ddde0167e5 | -3.78107 | -51.32304 | 2024-10-13 05:01:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 210e196f-1f37-3faf-a509-d51b2a37ae95 | -3.77799 | -51.31809 | 2024-10-13 05:01:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3918ac4c-0c24-39b1-b4f6-1b751e266e73 | -3.68359 | -51.07415 | 2024-10-13 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7f088491-fc79-33aa-a2f3-249134e36ca9 | -3.6829 | -51.07875 | 2024-10-13 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0c3e917a-d777-3357-a2eb-932c34e37717 | -3.67981 | -51.07355 | 2024-10-13 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3ee6d5cc-7464-3c8b-be36-b2033af65605 | -3.67911 | -51.07817 | 2024-10-13 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| fe065a28-ea0d-3699-929c-d8aef5038efa | -3.65188 | -51.25958 | 2024-10-13 05:01:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 84659e22-8ac4-3519-b528-94c91a2c803e | -6.24483 | -51.71986 | 2024-10-13 05:01:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e8479503-3e93-3ba0-91d2-a2152d9a7eb9 | -6.12977 | -52.65572 | 2024-10-13 05:01:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| ef666059-65d9-3c59-be18-043f88af433b | -6.05471 | -52.16328 | 2024-10-13 05:01:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |


[Clique aqui para ver as próximas entradas](README79.md)
