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

## Dados Diários - Página 152

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| acfd78d6-f0ce-331e-988d-42dd50b01e52 | -11.06751 | -46.51656 | 2024-10-04 04:57:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ca8bf903-3aac-3a57-92bd-fc4663503eaa | -11.06718 | -46.51908 | 2024-10-04 04:57:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 78330475-3c09-3dfb-9d93-de94e1f9fcbe | -11.06054 | -46.5298 | 2024-10-04 04:57:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 458e1484-9ae8-354e-8dce-97da911aa9b9 | -11.05542 | -46.52903 | 2024-10-04 04:57:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e8767278-b807-3eae-85dd-5885d4d33809 | -11.03773 | -46.50423 | 2024-10-04 04:57:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d4b2a5da-613d-3635-b555-84c5e0ce74dd | -11.03301 | -46.50028 | 2024-10-04 04:57:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e5606bc2-f0db-328b-a175-0948aea1725f | -10.90632 | -46.61413 | 2024-10-04 04:57:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 39600773-17b2-3ce7-a82e-f87c2ba5fdee | -13.5927 | -48.13024 | 2024-10-04 04:57:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 32468936-d92a-3863-ba31-708b81dff2eb | -12.8851 | -46.85611 | 2024-10-04 04:57:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6c740195-ce00-36bf-b460-4fd3073f9249 | -12.88471 | -46.85931 | 2024-10-04 04:57:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5850cced-397e-3012-9f61-f3dcdf3742c1 | -12.79791 | -47.43987 | 2024-10-04 04:57:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a9fb209b-7cc2-39ab-b76c-8358f44c2f64 | -12.79226 | -47.44487 | 2024-10-04 04:57:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 36c474c6-ee94-3730-86b9-34c9f279525e | -12.40832 | -46.43677 | 2024-10-04 04:57:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| e3c5624c-fe4c-39dc-a39e-b9dc03322b60 | -12.37895 | -47.68273 | 2024-10-04 04:57:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3fbf120e-e9c8-3273-87f3-c4c7edae1cb8 | -13.59343 | -48.12445 | 2024-10-04 04:57:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 46d2a55f-6fbe-3594-afd1-a2f90430c9bf | -13.56716 | -47.63901 | 2024-10-04 04:57:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| b6e29a92-14db-384c-8eb0-75fe1c6a7b22 | -13.59818 | -48.12531 | 2024-10-04 04:57:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3b367d40-4443-32b8-8ee0-5764949f43ea | -13.56788 | -47.63326 | 2024-10-04 04:57:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 5b83ea04-3ea3-309f-80a5-2d095f364ff4 | -12.40872 | -46.43357 | 2024-10-04 04:57:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 0560166f-8436-38df-ad61-385791f7a93a | -12.7972 | -47.44558 | 2024-10-04 04:57:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 688e678b-5a53-3e59-acca-75de45571de1 | -12.79157 | -47.45052 | 2024-10-04 04:57:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 3e841ca5-a356-3a19-8879-1cbd3357a13f | -12.79116 | -47.44367 | 2024-10-04 04:57:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 1a71c6bc-5ed8-3e99-9847-88856b090cff | -12.79042 | -47.44932 | 2024-10-04 04:57:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 9.5 |
| d040d3ce-f288-3ea6-aff3-ec41e1dc7046 | -12.78663 | -47.44979 | 2024-10-04 04:57:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 6e452ee4-e49f-3680-8a13-d6607ed7d36b | -15.21145 | -47.50944 | 2024-10-04 04:57:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| acffcd22-879b-306f-ba52-79e3c770dff1 | -15.02165 | -47.55951 | 2024-10-04 04:57:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 2205b941-abe5-3abd-b570-2aa848acb512 | -14.79945 | -48.09209 | 2024-10-04 04:57:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| f1f4af2b-e67e-30f1-ac88-e1aa676e140e | -14.79579 | -48.04143 | 2024-10-04 04:57:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 789fa887-140d-33c5-8c24-f43a194035a6 | -14.79333 | -48.1017 | 2024-10-04 04:57:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 9d83e72d-8c4d-31c5-9ef4-2b6af19eb946 | -14.79226 | -48.02967 | 2024-10-04 04:57:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 11d4f42e-8756-34e8-b13a-ebfd549b3092 | -14.79096 | -48.04036 | 2024-10-04 04:57:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| d4d159a7-a7c3-3732-b386-b6569ff09617 | -14.79026 | -48.04603 | 2024-10-04 04:57:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 184317b9-9210-3c20-8927-ebe507f17035 | -14.78255 | -48.02798 | 2024-10-04 04:57:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 04c9aced-ce1c-35ce-b131-dbb2f9cbe66b | -14.77705 | -48.03236 | 2024-10-04 04:57:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| bf04d052-5fbd-333d-bebe-2249bd802670 | -14.77643 | -48.03751 | 2024-10-04 04:57:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 85ea07f1-504b-3d3b-b178-7e52ffb36769 | -14.77221 | -48.03137 | 2024-10-04 04:57:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| cc299a41-743f-39df-8557-348707a94bf3 | -14.77157 | -48.03665 | 2024-10-04 04:57:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 2b09f4b2-fc81-38c3-8971-e2db434c3ea7 | -15.70972 | -47.80491 | 2024-10-04 04:57:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b97a5592-e60e-3338-b66c-586b3dbd5c2c | -15.70472 | -47.80411 | 2024-10-04 04:57:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 46ca369c-3fbb-3fbb-844c-4b32f0c7fcff | -15.62253 | -47.19727 | 2024-10-04 04:57:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 61266558-e756-3b90-99bc-2a3f82ae230b | -15.62215 | -47.20057 | 2024-10-04 04:57:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 0be21c8a-ab57-362d-ac70-b90602ca8b4c | -15.61731 | -47.19653 | 2024-10-04 04:57:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 8a2f1bed-3195-3da9-84bd-cd6c1acf6ca5 | -15.61694 | -47.19984 | 2024-10-04 04:57:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 9b915eaf-abcb-34f4-a496-b0325857e443 | -15.61618 | -47.20643 | 2024-10-04 04:57:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| dd6c0237-de97-3bb3-8000-49ee617b5fc5 | -15.61581 | -47.20973 | 2024-10-04 04:57:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 28d15f0a-1b19-3519-9a6f-076dfb320d78 | -15.61171 | -47.19916 | 2024-10-04 04:57:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0aca0d18-c8e9-37c2-b1e6-fa5a09e9c12f | -15.61134 | -47.20247 | 2024-10-04 04:57:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 148f2310-558b-393b-8215-a4b5f85cdce3 | -15.61096 | -47.20576 | 2024-10-04 04:57:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9a21d954-d376-321d-bea3-dcff718d8a56 | -15.61059 | -47.20905 | 2024-10-04 04:57:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9639f1fb-66de-3689-9476-d4fcce3a8583 | -15.41412 | -47.67812 | 2024-10-04 04:57:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3cf106a2-4273-39e5-b823-dc6789d09e71 | -15.41377 | -47.68118 | 2024-10-04 04:57:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bdd6e989-a7be-3194-b1bf-6c3d0367d777 | -15.40479 | -47.41697 | 2024-10-04 04:57:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 3240a1c3-f12e-340d-8cb7-0352455970de | -15.27192 | -47.50846 | 2024-10-04 04:57:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a4e7aea0-3890-33f5-9ce4-3410d71d268e | -15.26724 | -47.50433 | 2024-10-04 04:57:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9d3ed265-bc04-3452-926f-20235e06774c | -15.26199 | -47.50503 | 2024-10-04 04:57:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 927d081d-11f1-3f5d-8048-e2acd1bcba34 | -15.25687 | -47.50458 | 2024-10-04 04:57:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| dcfd4973-6736-3617-9c1d-7b631e805950 | -15.25233 | -47.4991 | 2024-10-04 04:57:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 064e74fb-7c1e-3ea6-8d6a-296bd6d115dc | -15.24719 | -47.4989 | 2024-10-04 04:57:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 16acee1f-77a9-3dd1-81fd-52fa5f1c51d2 | -15.23707 | -47.49697 | 2024-10-04 04:57:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0c7ead39-d619-3208-9a98-8725e30d741a | -15.23649 | -47.50201 | 2024-10-04 04:57:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6c1d8d9e-2449-3aa3-823f-adce8b8c2e50 | -15.22252 | -47.5034 | 2024-10-04 04:57:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| df317d4a-f1bc-36c4-83bf-f1450e70b2c4 | -15.21646 | -47.51071 | 2024-10-04 04:57:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| abd4a4e9-d614-3c28-bd53-06f158e619f2 | -16.73151 | -48.50418 | 2024-10-04 04:57:00 | NOAA-20 | VIANÓPOLIS | GOIÁS | Brasil | 5222005 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 05db218d-c304-378b-840b-d2c967e5e302 | -16.70247 | -48.63452 | 2024-10-04 04:57:00 | NOAA-20 | SILVÂNIA | GOIÁS | Brasil | 5220603 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cc4afd6e-51c2-3c62-a006-bcf05e580669 | -16.70173 | -48.63445 | 2024-10-04 04:57:00 | NOAA-20 | SILVÂNIA | GOIÁS | Brasil | 5220603 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ed07f812-637c-3456-b2ba-9d4f35f08636 | -16.6884 | -47.82566 | 2024-10-04 04:57:00 | NOAA-20 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e632a08e-0cea-34dd-a739-9f6cb85f761d | -16.68806 | -47.82856 | 2024-10-04 04:57:00 | NOAA-20 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fe3cebbf-3188-38b2-9d09-5f1445d56033 | -16.68681 | -47.82677 | 2024-10-04 04:57:00 | NOAA-20 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 27ca2bd2-0109-3e64-9d24-fcae3ed36147 | -16.68648 | -47.82972 | 2024-10-04 04:57:00 | NOAA-20 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ec05c2ef-d3a6-3c11-9ed4-0ec9c5b6d7f6 | -10.8672 | -48.14687 | 2024-10-04 04:57:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 9.0 |
| ea909299-dbf9-39d6-9650-4bd7b5d7d0c3 | -10.78512 | -48.73615 | 2024-10-04 04:57:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| d96ede78-d055-3d9d-ae5c-fe0626d2815d | -10.78071 | -48.73561 | 2024-10-04 04:57:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b0c4cfc8-de4c-3654-8cf2-1cd397cbbc7f | -10.76758 | -47.98852 | 2024-10-04 04:57:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 8f94ec98-db2d-3ee2-ade8-0425d125a8e5 | -10.76681 | -47.98543 | 2024-10-04 04:57:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 094ed0fd-f0cd-3395-bfbc-f591b698ee2b | -10.75049 | -47.97557 | 2024-10-04 04:57:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 10324a9e-9df3-33e2-9586-a1b410d5322a | -10.74666 | -47.64711 | 2024-10-04 04:57:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 995f963f-fd64-3bab-a7ff-97ab9970714e | -10.73391 | -47.70756 | 2024-10-04 04:57:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 8d717aa0-6c56-3635-8d33-f5d267e10f9e | -10.72985 | -47.70191 | 2024-10-04 04:57:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 79c104c7-3d38-3700-9d13-8db55d18235a | -10.86758 | -48.14496 | 2024-10-04 04:57:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| ae2c161b-ca57-3917-bf50-2e9ec322b99d | -10.86696 | -48.14969 | 2024-10-04 04:57:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| e0b403c1-24ec-3801-82cb-b592b931cf91 | -10.83087 | -48.27543 | 2024-10-04 04:57:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0b0d41e7-2db1-3548-ac82-33c0a62c230b | -10.78538 | -48.73517 | 2024-10-04 04:57:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 3e941441-fb06-3af4-808a-1d07c99500a3 | -10.78097 | -48.73464 | 2024-10-04 04:57:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| ed4450f4-9d00-32b8-a2fd-f31593e13ed7 | -10.76296 | -47.98783 | 2024-10-04 04:57:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 86773913-595e-3c2f-adc9-243917c41934 | -10.74912 | -47.98565 | 2024-10-04 04:57:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| a97eae4f-d935-3a1f-b739-35cb49ea9fea | -10.74544 | -47.72932 | 2024-10-04 04:57:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 70a14b7d-54d5-3405-b90e-501c9f1c19b8 | -10.7426 | -47.64127 | 2024-10-04 04:57:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 8c700fc6-2570-390c-a361-024ba183675c | -10.74137 | -47.72387 | 2024-10-04 04:57:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 268c74b2-20ea-39f9-b112-84a342d1235e | -10.74071 | -47.72884 | 2024-10-04 04:57:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 01e68038-98a5-3f6d-b492-64674bda6bd4 | -10.73851 | -47.63564 | 2024-10-04 04:57:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 5ade7978-6cc9-3918-a3c0-1adb90e5aca1 | -10.73663 | -47.72341 | 2024-10-04 04:57:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 17891d0c-a4e9-3e5d-8028-7613c2b65870 | -10.73442 | -47.62999 | 2024-10-04 04:57:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| d467f9bd-be39-31ab-9b19-42727672c09f | -10.73257 | -47.71777 | 2024-10-04 04:57:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 7af8abb5-1b0b-3980-baf9-d295c82d4971 | -10.73188 | -47.72301 | 2024-10-04 04:57:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 106e210d-6cc0-3b76-9481-db7f3fc56cd4 | -10.72969 | -47.62925 | 2024-10-04 04:57:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 3c0ac9c6-2393-3533-9a2f-4057336a9149 | -13.17411 | -48.67387 | 2024-10-04 04:57:00 | NOAA-20 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 4da885f7-0550-31cc-aca2-98265c80619a | -13.17933 | -48.66942 | 2024-10-04 04:57:00 | NOAA-20 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 14e59dca-c053-3cb9-8465-c321c2bd16dd | -12.12201 | -48.43871 | 2024-10-04 04:57:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d27e07d7-3bae-37c5-b74a-b04519d7befe | -12.12139 | -48.4407 | 2024-10-04 04:57:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e8610762-e7a0-3e20-bc96-359f62c474f1 | -11.90015 | -48.31497 | 2024-10-04 04:57:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |


[Clique aqui para ver as próximas entradas](README153.md)
