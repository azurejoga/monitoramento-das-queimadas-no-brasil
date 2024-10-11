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
| 40bf681c-6bbf-3cbf-a5f3-880e9e012b54 | -3.49835 | -50.80347 | 2024-10-11 05:16:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| bd770dd8-134d-3cbe-97ee-1914f9e711cf | -3.49396 | -51.58168 | 2024-10-11 05:16:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9e9b41d9-bd7c-39fe-a092-e43436df69cd | -3.49201 | -51.58307 | 2024-10-11 05:16:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 990d64b0-d0c8-30a5-9dca-ccf589da88a5 | -3.47187 | -51.37713 | 2024-10-11 05:16:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1c28d691-fb04-3ff8-8c81-eda33274a533 | -3.39149 | -51.34857 | 2024-10-11 05:16:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| cd95446a-74fe-3fef-8204-31d6db0ab926 | -3.34052 | -50.80812 | 2024-10-11 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 81fddf37-256d-3827-8dd3-05f1b9761649 | -3.33652 | -50.80231 | 2024-10-11 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 20506aef-8c50-3813-9fe5-067ab827c00f | -3.33577 | -50.8074 | 2024-10-11 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| d0ad539e-3f94-3ca9-a42d-d450a9394ea3 | -3.2859 | -50.94944 | 2024-10-11 05:16:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 75a40193-1d97-3be9-ad16-23eabcd71145 | -3.284 | -50.94701 | 2024-10-11 05:16:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 790559c9-826b-34d8-ab5b-d4fd21d77625 | -3.28323 | -50.95198 | 2024-10-11 05:16:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 79194e6f-5ce5-33ec-89c5-e60ce18b9635 | -3.28193 | -50.94369 | 2024-10-11 05:16:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| a99bc25a-3d83-35e1-8967-775a314dde42 | -3.2812 | -50.94869 | 2024-10-11 05:16:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| a549c2e3-c8b7-3025-aee1-51a05cd3e997 | -3.28048 | -50.95366 | 2024-10-11 05:16:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| bccb13a5-cc3a-3504-841c-0c92d7d077e5 | -3.2793 | -50.94629 | 2024-10-11 05:16:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 3a86a8a1-902a-3179-bbe5-546f87e471bf | -3.27854 | -50.95125 | 2024-10-11 05:16:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 9281ddc3-10a0-3d84-80a9-a7992d595275 | -3.27723 | -50.94296 | 2024-10-11 05:16:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| f3cc5f7e-a7d6-3c64-918e-3d416ed88e23 | -3.2765 | -50.94797 | 2024-10-11 05:16:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| fd58de1c-8905-3c90-b588-962ef0aa250f | -3.2746 | -50.94558 | 2024-10-11 05:16:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 5c211c35-b6a1-3132-b620-e1a6ae519261 | -3.26711 | -50.94646 | 2024-10-11 05:16:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4caf9060-1e96-3d87-a153-318c799be810 | -3.2364 | -50.84727 | 2024-10-11 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| d36dc505-bf68-3407-ba4b-3e046be66c4c | -3.23565 | -50.85229 | 2024-10-11 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 0e913aed-2670-3e57-b109-118c54482a57 | -3.23166 | -50.84662 | 2024-10-11 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| b6b6625a-e487-3cd9-9711-ea530487ed28 | -3.23092 | -50.85159 | 2024-10-11 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| c679b0a3-bca0-38fb-b413-14a52fc3cc2b | -3.0346 | -51.10145 | 2024-10-11 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5926f9df-f82a-369a-96ef-16e16154ae92 | -3.03388 | -51.10615 | 2024-10-11 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| bac8e8a7-9a9c-33c3-b189-834bd8d3f5e0 | -3.03353 | -51.10246 | 2024-10-11 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| e62dbbc5-1a08-391c-9331-02bf883e7f98 | -2.97647 | -51.3582 | 2024-10-11 05:16:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| fb20af86-1535-3b21-a11e-785cdc5eb1af | -2.97576 | -51.36282 | 2024-10-11 05:16:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| e05253d5-f3d1-34f2-8c09-e18a579522e1 | -2.97505 | -51.36749 | 2024-10-11 05:16:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| b89b04b7-be14-37c7-8156-1d88579186df | -2.97192 | -51.35749 | 2024-10-11 05:16:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| a2520cbc-3d06-3dae-901b-cc22538fff98 | -2.97151 | -51.11149 | 2024-10-11 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 505907f6-1f10-3cc3-933b-746fb2a4f864 | -2.97122 | -51.3621 | 2024-10-11 05:16:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| f30efde4-26d5-32e0-bf8f-63363d745f4b | -2.97051 | -51.36678 | 2024-10-11 05:16:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| c393de29-b9dc-304b-928b-83809013026c | -2.84244 | -51.37683 | 2024-10-11 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4f732e28-7187-38f9-a66b-c8bf4516463d | -2.81186 | -51.39542 | 2024-10-11 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b3258b76-9ecb-3420-894b-469ebe247546 | -2.80837 | -51.60183 | 2024-10-11 05:16:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| f37f840a-8fbc-3cb8-ab7d-5c490f0641c3 | -2.80833 | -51.01306 | 2024-10-11 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 20348b97-79f2-3451-b5f2-13542b42fa7f | -2.80443 | -51.00748 | 2024-10-11 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 17.1 |
| 95c1b26e-77a0-3653-a355-6d36e0823363 | -2.80369 | -51.01234 | 2024-10-11 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 17.1 |
| 7326293d-00e6-32c4-80b8-2d1d94d408b2 | -2.80297 | -51.01708 | 2024-10-11 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 38.4 |
| 16afe46e-c40a-3b28-a738-1516b0cf2601 | -2.79906 | -51.01151 | 2024-10-11 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 17.1 |
| e87d22b7-3dba-30c5-9b72-3e6edf27f2bd | -2.26558 | -51.2498 | 2024-10-11 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a493e913-b59b-3ca0-af95-a5c9649bba2a | -2.25347 | -50.70149 | 2024-10-11 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5b695546-89ce-35b7-91ae-6a49528788f2 | -2.64764 | -51.70953 | 2024-10-11 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3bc738a2-f55d-330b-b5e4-fb66ce700d6d | -2.64387 | -51.70451 | 2024-10-11 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 9ba7c6ce-5cbc-37dd-86a6-0fb9c9896c5d | -2.64322 | -51.70885 | 2024-10-11 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 37704281-aa78-3a78-a822-2118a1c91a12 | -2.63945 | -51.70383 | 2024-10-11 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 431bf3df-d8c1-35dc-9bb8-510613684440 | -2.58483 | -51.92142 | 2024-10-11 05:16:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| d23b0a53-ed10-3501-a1a1-8278d17fef5a | -2.58319 | -51.92322 | 2024-10-11 05:16:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4a27ba6b-15f4-397a-9b1f-d8e00b47c23b | -3.45653 | -52.02501 | 2024-10-11 05:16:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4e8da537-eff4-3dd4-9700-6aa2d04acf06 | -3.37554 | -52.17185 | 2024-10-11 05:16:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4f24ebba-defe-343c-907a-05ca5c97a544 | -4.27322 | -50.96301 | 2024-10-11 05:16:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 4656dbc5-24a9-3487-805c-267c1cfd8597 | -4.26846 | -50.96225 | 2024-10-11 05:16:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| b81fe78b-209f-3ec0-b943-2f35b5a0f104 | -4.09244 | -51.02361 | 2024-10-11 05:16:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 26eb1bec-8532-328d-8819-22ed0128e7eb | -4.09171 | -51.02853 | 2024-10-11 05:16:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 016aee02-5aaf-39d2-b71b-869f3bda6159 | -4.08769 | -51.02298 | 2024-10-11 05:16:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9d782a99-c0d7-3462-bb37-9f26030f3a68 | -4.08697 | -51.02786 | 2024-10-11 05:16:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 81acd447-0404-393e-be4c-e6c795a9784c | -4.08297 | -51.0222 | 2024-10-11 05:16:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c82596f4-302b-3435-aa17-5ef3c0ed1de5 | -4.08225 | -51.02706 | 2024-10-11 05:16:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 238a6577-0df6-3832-87b8-ff550b6a65b6 | -4.06494 | -51.11144 | 2024-10-11 05:16:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| a8e20167-5d73-34f2-9f27-f4ccbdead849 | -4.06416 | -51.11675 | 2024-10-11 05:16:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 1446759e-4369-31bf-95b9-23480cf114fb | -4.04528 | -51.1144 | 2024-10-11 05:16:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 83a63cfb-6309-3c01-b090-1b059eea370d | -4.01821 | -51.00153 | 2024-10-11 05:16:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| cd434bb0-16f5-384b-b061-cd36ab6067c0 | -3.92617 | -51.22449 | 2024-10-11 05:16:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c3c3743b-fbad-3858-9afb-20cdba6e4dd7 | -3.92152 | -51.22375 | 2024-10-11 05:16:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 2b27847a-e27f-39aa-bbdb-57b830207188 | -3.69255 | -51.06821 | 2024-10-11 05:16:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 9b8f4f02-7a11-3485-ae22-530ee9d05dc3 | -3.6902 | -51.0687 | 2024-10-11 05:16:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 69c1995b-821d-3671-8c0d-b47b0e8be303 | -3.68895 | -51.1231 | 2024-10-11 05:16:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b4c53614-6c5d-37eb-8496-b7c8b395954f | -3.68774 | -51.11875 | 2024-10-11 05:16:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 71b75863-894d-3be2-a140-36f9f77e6114 | -3.6871 | -51.07245 | 2024-10-11 05:16:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 9c6295b6-9fb4-3a0b-897d-a2266c189bbf | -3.68703 | -51.12368 | 2024-10-11 05:16:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 51e3050c-bc8c-308e-9f91-1862130e3561 | -3.68504 | -51.11742 | 2024-10-11 05:16:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e3435207-df81-367b-be81-d2f8ee5e68ac | -3.68479 | -51.07292 | 2024-10-11 05:16:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 72e48cf2-d552-3604-8d33-f5cd1adab175 | -3.68429 | -51.12233 | 2024-10-11 05:16:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 592d6369-8b92-3f3b-bb94-197d01bc6ff0 | -3.68307 | -51.118 | 2024-10-11 05:16:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 07dec28c-7846-3de8-9fcf-0ba95ff685eb | -3.68242 | -51.07169 | 2024-10-11 05:16:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 0e1f25dc-6b5b-3850-8203-93fdecb6d1b2 | -3.68166 | -51.07668 | 2024-10-11 05:16:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 1745003c-b58f-3148-bc23-22c3e3a65c29 | -3.68011 | -51.07215 | 2024-10-11 05:16:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 10.2 |
| ba485337-5e80-3858-9a51-48470dee3b05 | -3.67774 | -51.07095 | 2024-10-11 05:16:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f56d5d0d-a0d9-31ca-92b1-5ad723202804 | -3.93192 | -52.24519 | 2024-10-11 05:16:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8276e450-ff40-313f-9b68-0c9bd2cef79f | -3.93129 | -52.24934 | 2024-10-11 05:16:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ab6f3089-3fd3-3c36-b892-a75968722a4e | -3.89723 | -52.26938 | 2024-10-11 05:16:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 63ff8a74-14cb-35e2-8067-1b130d1de11c | -3.89117 | -51.821 | 2024-10-11 05:16:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f767d114-5a86-3242-9b62-6884e40a6ff4 | -3.88836 | -51.93995 | 2024-10-11 05:16:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fa784002-8527-38e3-a8f2-d4075c8efa8c | -3.87798 | -51.97825 | 2024-10-11 05:16:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5ded994b-dc3a-31ec-9ce7-4d3d860a3403 | -3.87724 | -51.9803 | 2024-10-11 05:16:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 31cd5840-e4f1-399c-a02a-3d2ffb5e2b77 | -3.87356 | -51.97759 | 2024-10-11 05:16:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 26eab724-1ce1-3137-9d49-a025ebcf65f9 | -3.82051 | -52.00025 | 2024-10-11 05:16:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c58be289-44af-3930-93e2-ccd8a9630a0d | -3.80802 | -52.26182 | 2024-10-11 05:16:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 668c4ffc-0421-3b5b-be4d-f857e2cc4cfd | -3.78085 | -51.86991 | 2024-10-11 05:16:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 657f83c6-1f6d-3de3-903c-ebc794c5dbe4 | -3.73543 | -51.81472 | 2024-10-11 05:16:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ebdeb847-d372-3b0d-b3ee-cfa36d434bcf | -3.73477 | -51.81916 | 2024-10-11 05:16:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e9726abf-aec2-3fe7-8cf7-4b8e4779393b | -4.65701 | -50.95162 | 2024-10-11 05:16:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8ba1c72b-db16-3e57-a2d2-64923a673f94 | -4.65221 | -50.9509 | 2024-10-11 05:16:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f9d86904-722a-34cf-88a9-cda6a064faf4 | -5.68366 | -51.29965 | 2024-10-11 05:16:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f3a3b963-7f81-3528-8ad0-0fff90f35dbc | -5.67889 | -51.29902 | 2024-10-11 05:16:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| fdc51b1d-14a3-380f-9f81-f20e72c51f77 | -5.64115 | -51.59022 | 2024-10-11 05:16:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ace3e324-3678-3878-92ee-1c75197fd838 | -5.61505 | -51.16504 | 2024-10-11 05:16:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4d0669dd-1aad-37d9-b35d-1675cb09ee38 | -5.61473 | -51.16702 | 2024-10-11 05:16:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |


[Clique aqui para ver as próximas entradas](README79.md)
