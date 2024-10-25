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

## Dados Diários - Página 34

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ecc7372d-5c72-30a1-a002-bee4f97c2e6b | -3.26741 | -50.77166 | 2024-10-25 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 4691b2d5-0b22-3fc2-9a3e-2af5238ffe98 | -3.26235 | -50.77082 | 2024-10-25 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 9ad25bce-efee-3304-87fd-8c4173f1b3d3 | -3.26184 | -50.7738 | 2024-10-25 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 71a8ca41-4541-302d-81cf-459e1a0f317c | -3.24405 | -50.84785 | 2024-10-25 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 51c56e34-338a-3a4f-860e-b34d2bc4b5b6 | -3.21611 | -51.01212 | 2024-10-25 04:14:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 60113304-bfad-3811-ab7c-babfaa2a47c7 | -3.20338 | -51.34129 | 2024-10-25 04:14:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| ad76cd48-2a3a-3719-86d2-2c47d26384b0 | -2.2943 | -50.84056 | 2024-10-25 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2541a333-e211-385b-81b6-5cc639a63fd2 | -2.29045 | -50.43023 | 2024-10-25 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e1332f0a-4b0c-3385-afb6-6251cad90e8b | -2.28494 | -50.43237 | 2024-10-25 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 18c50b08-a968-3887-ad1e-f14de5c8f8da | -2.27752 | -50.44616 | 2024-10-25 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 8b729436-1815-3cac-bb39-f31ab391ffca | -2.27704 | -50.4491 | 2024-10-25 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 95303b04-cb46-34e7-8c86-c7df5162938b | -2.87931 | -51.31218 | 2024-10-25 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2cfb3f90-10d6-3618-8dbd-5df0f21770ae | -2.87402 | -51.31134 | 2024-10-25 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4d30db22-a224-3d75-8b51-0b4f967ab17e | -2.8646 | -51.59906 | 2024-10-25 04:14:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| bae0a3ef-d130-392e-9e49-38524c6ca705 | -2.8592 | -51.59821 | 2024-10-25 04:14:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 066d6429-a935-3feb-8539-fc240f2c3246 | -2.85863 | -51.60168 | 2024-10-25 04:14:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 84de956b-b465-3b0f-8081-d6314e2ab81f | -2.83607 | -51.80595 | 2024-10-25 04:14:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 0f07744e-aa9e-316a-8c0b-c46b05f62b58 | -2.83548 | -51.80949 | 2024-10-25 04:14:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 10.9 |
| b7a5e75f-662b-3461-9df0-dbb1063e26ef | -2.8349 | -51.81303 | 2024-10-25 04:14:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 19.5 |
| f49106e0-2a2e-31f2-aa42-ef661824ba4b | -2.83 | -51.80866 | 2024-10-25 04:14:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 671bd270-5e90-3c6f-9f9d-d7b98b7e2bd9 | -2.82942 | -51.81219 | 2024-10-25 04:14:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 107bbbc6-12e9-3d75-983f-9d9b2e1dda68 | -2.81415 | -51.35004 | 2024-10-25 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ebcd4560-d96d-3fe3-b029-b0ff9d19ba6a | -2.81361 | -51.35336 | 2024-10-25 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6710a0ac-37dc-31a8-95f6-4828ae2db589 | -2.80345 | -51.60011 | 2024-10-25 04:14:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 39caa225-f450-393e-acf4-2c42f0989221 | -2.80139 | -51.59766 | 2024-10-25 04:14:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d569b1fd-314f-3798-9e29-8abd84910d12 | -2.80085 | -51.60101 | 2024-10-25 04:14:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ee2aa719-34d0-3f6c-b745-4b875a6cdf0b | -2.79864 | -51.5958 | 2024-10-25 04:14:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4c48615f-3793-36d5-b5ff-492c73b9628e | -2.79806 | -51.59917 | 2024-10-25 04:14:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c0c3bbfe-cc20-3546-b4dd-5ef49d305045 | -2.60295 | -51.77757 | 2024-10-25 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3978b0f5-5b8f-32c8-b938-0cfc60fe3d57 | -2.58451 | -51.9231 | 2024-10-25 04:14:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 917c15c5-29f3-3c23-807a-8af63405cd14 | -3.64034 | -51.2465 | 2024-10-25 04:14:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| da0afa2f-d731-34a5-8b80-8cf5a2c58772 | -3.63516 | -51.24553 | 2024-10-25 04:14:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8c1f29c4-12a0-3a39-bc8b-a1af5f79bce5 | -3.51512 | -51.02139 | 2024-10-25 04:14:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5546d28c-f818-3229-9155-320a2ba63453 | -3.45832 | -51.20402 | 2024-10-25 04:14:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a4d2821b-9f85-3580-bca8-2e1f19ade2da | -3.4578 | -51.20715 | 2024-10-25 04:14:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e816b191-4e2e-3aeb-bbda-e963b8fea907 | -3.3502 | -51.65325 | 2024-10-25 04:14:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c4474772-6b1d-3067-897d-f2d3843c5eab | -3.34542 | -51.64893 | 2024-10-25 04:14:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 522600b1-75f4-367a-8175-0a80c02409e4 | -3.34484 | -51.6523 | 2024-10-25 04:14:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2724ec91-c6e6-30cc-b645-0c0463037c9f | -3.30954 | -51.05561 | 2024-10-25 04:14:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 14c41512-fd8b-32bb-b63c-98dfcc666d4f | -3.2977 | -50.74612 | 2024-10-25 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 54ed351c-72b2-3dcf-b7eb-2f2d39c0eaa9 | -3.26691 | -50.77463 | 2024-10-25 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| aa040dfc-f31a-32af-980f-7639a0d4c174 | -3.24354 | -50.85085 | 2024-10-25 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| bf5dab87-f517-34f6-bd2e-e745e6bf7899 | -3.24095 | -50.8476 | 2024-10-25 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e7caae76-ff9c-329b-b8e5-9ed149d10a8e | -3.24046 | -50.8506 | 2024-10-25 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f9f615c2-b32a-3110-866c-ee4433105c87 | -3.23896 | -50.84698 | 2024-10-25 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 81af4951-1142-3575-bf7b-305ac8cf06e0 | -3.23845 | -50.84999 | 2024-10-25 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3dfb16ef-3036-36f1-9d99-2eaad6866c1a | -3.16588 | -51.24348 | 2024-10-25 04:14:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 54cadf06-d406-3b91-b81b-5ab60684fcda | -3.08712 | -51.26338 | 2024-10-25 04:14:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 3d5419bd-eaca-3b04-9b1d-b2548e812fa6 | -3.08187 | -51.26254 | 2024-10-25 04:14:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 3d980643-09f8-31ab-bba4-928b151cead7 | -3.08133 | -51.26572 | 2024-10-25 04:14:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 77909ba7-251b-3cdf-82ef-5c466a76d557 | -4.66998 | -50.97267 | 2024-10-25 04:14:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 032b0e22-75e5-397f-a2e3-0807219c26b5 | -4.66547 | -50.96889 | 2024-10-25 04:14:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 1aff6455-4d43-3539-be07-2284cd39a455 | -4.66497 | -50.97183 | 2024-10-25 04:14:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| b37ce0e2-ebe7-378a-9c55-0f4292cd7936 | -4.53625 | -50.97057 | 2024-10-25 04:14:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9066e8f9-2343-3ad1-8f87-a3283de4ee27 | -4.53576 | -50.97343 | 2024-10-25 04:14:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| fb8a56bd-fdaa-3e01-a7bf-fabcb3bb7b27 | -4.07766 | -51.12265 | 2024-10-25 04:14:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0355ca3b-60ef-3261-a1c3-75e8060f0a5f | -3.95176 | -52.25218 | 2024-10-25 04:14:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 6204c030-27f8-31c4-b1dd-a0a8f67fe8ca | -3.95113 | -52.25592 | 2024-10-25 04:14:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| aa845ea2-9e0a-3ac2-846b-9365e0744acb | -3.9505 | -52.25969 | 2024-10-25 04:14:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| b682a57c-781a-3fd3-b606-9e7d79161bf9 | -3.94563 | -52.25481 | 2024-10-25 04:14:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 8d785d33-6dfd-30a6-b3cf-0e0ce93fae99 | -3.94498 | -52.25863 | 2024-10-25 04:14:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| c4fea933-0690-377c-95be-9bb0d96029a0 | -3.88985 | -50.98679 | 2024-10-25 04:14:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3c406ed9-46bd-337b-a151-9ad1b8c1207e | -3.86953 | -52.13409 | 2024-10-25 04:14:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a084f46d-82cf-382a-af71-927cbb40cbf0 | -3.86893 | -52.13771 | 2024-10-25 04:14:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d0cbe1cf-010e-3a82-9745-280071c38747 | -3.83131 | -51.36192 | 2024-10-25 04:14:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 70f7de9c-aac9-3849-b5a2-4b55d48bdba2 | -3.82665 | -51.35774 | 2024-10-25 04:14:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9e160c30-39e7-39df-a921-2d04c922eff6 | -3.8261 | -51.36096 | 2024-10-25 04:14:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5b9682af-6fea-3c00-8ef2-f39840d225ec | -3.82608 | -51.89457 | 2024-10-25 04:14:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8c74394a-157c-376b-86d7-dbcac5889eb7 | -3.8241 | -51.894 | 2024-10-25 04:14:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a50a8605-23bd-3621-80e2-7ffe5590dd57 | -3.82354 | -51.8974 | 2024-10-25 04:14:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 50f91ace-d400-3f89-8071-e03eef45a451 | -3.80739 | -51.05298 | 2024-10-25 04:14:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bfb1c148-93f6-3099-aacd-05ba3cebd99f | -3.68394 | -52.09106 | 2024-10-25 04:14:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2b4a71b6-2e44-331f-9bb0-59236872fbc7 | -3.68387 | -52.09307 | 2024-10-25 04:14:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ce238343-1275-3bca-aaa9-71d8a71a8675 | -3.68313 | -51.08723 | 2024-10-25 04:14:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 29cfe594-1dd7-3efd-99cc-946717fa30c8 | -3.6826 | -51.09037 | 2024-10-25 04:14:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 6f74034c-1942-3f34-b954-6f1d2d502bb0 | -3.68365 | -51.08412 | 2024-10-25 04:14:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 25eed8d3-77e5-3611-86fb-b43fe7cfd943 | -3.68333 | -52.09477 | 2024-10-25 04:14:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| be5c3054-cb91-3a95-ac9d-57cf5ecc7d99 | -4.67501 | -50.97348 | 2024-10-25 04:14:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 22e02268-95af-332d-be93-2f7f73611ebe | -4.67048 | -50.96973 | 2024-10-25 04:14:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| bfcdbaa9-d04f-37f6-8f2d-a0ea6635314b | -4.66949 | -50.97559 | 2024-10-25 04:14:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| ae081f4f-8a67-3962-8fca-c25bed1ab8d1 | -4.66899 | -50.97851 | 2024-10-25 04:14:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 6d88dcd8-877f-3c52-956a-85447a43ff72 | -4.66597 | -50.96594 | 2024-10-25 04:14:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 53a57693-6b51-32a7-b29e-719b279d0a56 | -4.64441 | -50.91155 | 2024-10-25 04:14:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 495a5115-b0ad-3c9a-af62-1b06d45f90a4 | -4.64392 | -50.91436 | 2024-10-25 04:14:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 078af3f2-2ce3-32e1-878a-56845f16ba9d | -4.64342 | -50.91726 | 2024-10-25 04:14:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| be116c11-22c0-35fb-a8fd-92aef76cde63 | -4.54081 | -50.97411 | 2024-10-25 04:14:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 14.0 |
| d7b9fe8a-6d70-3000-b883-c7e3e9643a5d | -4.07713 | -51.12571 | 2024-10-25 04:14:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a6b20145-61e5-355c-8b7a-66994e53c7d0 | -6.39165 | -52.65095 | 2024-10-25 04:14:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 29d39a07-2125-3491-877c-9b21237fb111 | -6.3862 | -52.64998 | 2024-10-25 04:14:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 346e726b-316e-3466-8195-bfd50e64907e | -6.38527 | -52.64946 | 2024-10-25 04:14:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2aeae8ee-af61-3a5a-8385-17f24ac63c32 | -6.14742 | -52.64706 | 2024-10-25 04:14:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 7b368107-86f6-34a0-b1df-5b0a3077c3df | -6.14131 | -52.64977 | 2024-10-25 04:14:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b8c1d5d5-7119-3adf-879a-a3da594f33aa | -5.89167 | -51.29672 | 2024-10-25 04:14:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7a4dd33f-7f78-3f3c-b410-8d68a67daa32 | -6.39073 | -52.65041 | 2024-10-25 04:14:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ee201ac4-2da1-37e3-b020-135fac56f553 | -0.5318 | -51.87872 | 2024-10-25 04:14:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 703f7f58-2ad8-3d29-9812-c9e6d8b26669 | -1.8381 | -52.16817 | 2024-10-25 04:14:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| dd94bf54-b6b7-398d-8c81-1ca7c9ec88a8 | -1.83176 | -52.17132 | 2024-10-25 04:14:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 70edbc75-4d8b-34cc-ab17-1cd42d5318d1 | -1.74241 | -52.04179 | 2024-10-25 04:14:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c308d4ee-8150-3afa-ac50-19880cc00930 | -1.64928 | -52.04161 | 2024-10-25 04:14:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 134398f0-e39e-3e86-8bd9-270794e9709d | -1.64727 | -52.03676 | 2024-10-25 04:14:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |


[Clique aqui para ver as próximas entradas](README35.md)
