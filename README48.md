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

## Dados Diários - Página 48

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 758fe772-6402-37fd-bd28-40730daebff9 | -15.1314 | -50.6214 | 2026-08-30 05:10:00 | GOES-19 | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 63.9 |
| 838e348d-db08-3a3f-8f3c-f1ed34237820 | -11.8021 | -51.0343 | 2026-08-30 05:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 167.0 |
| 331ccc09-2ed0-3168-880b-eb52cb43897f | -11.8018 | -51.0556 | 2026-08-30 05:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 140.2 |
| 557a4e79-f79c-3b1e-80d8-290ea10274a1 | -11.8208 | -51.0535 | 2026-08-30 05:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 67.9 |
| 1081e253-d5c2-3643-9ce0-f5e74eb0757f | -11.8211 | -51.0322 | 2026-08-30 05:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 85.5 |
| 229ceb07-6c54-367a-b374-7407c6c1351f | -4.9604 | -55.8424 | 2026-08-30 05:10:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 89.6 |
| def01729-43b7-3d8b-8b10-803cff5cb475 | -4.9603 | -55.8622 | 2026-08-30 05:10:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 46.3 |
| 2cf5efcf-3d14-3cc9-807a-ca9769d56029 | 2.25512 | -50.75848 | 2026-08-30 05:14:00 | NOAA-21 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 60bc4c46-3ddc-321e-b3fd-089fa777cf05 | 1.972 | -50.99136 | 2026-08-30 05:14:00 | NOAA-21 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6103ea5c-ac8d-3715-892f-86b447b550e8 | 2.51878 | -50.85552 | 2026-08-30 05:14:00 | NOAA-21 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 3.0 |
| d8e4c6da-33d1-331e-84b5-ea1d3256e084 | 1.95824 | -50.98924 | 2026-08-30 05:14:00 | NOAA-21 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1b19962a-cfb4-3fbc-9dd1-2b2ffd6eebf8 | 3.87761 | -59.64001 | 2026-08-30 05:14:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 97cbe2bc-b7a8-327b-8ec3-1f7f1bb5821b | 2.2412 | -50.75634 | 2026-08-30 05:14:00 | NOAA-21 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 268cd4f7-ed6c-31f8-bdd5-4f761d635708 | 2.51811 | -50.85132 | 2026-08-30 05:14:00 | NOAA-21 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 3.0 |
| f6a74e1f-c549-31e0-a0f5-641381495baf | 2.18981 | -50.71454 | 2026-08-30 05:14:00 | NOAA-21 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 31552122-0f97-3068-9581-02cd58597c82 | 2.16796 | -50.69128 | 2026-08-30 05:14:00 | NOAA-21 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 5.0 |
| eee6c61d-4dc7-3096-b028-7a6cde44dc22 | 2.25002 | -50.75492 | 2026-08-30 05:14:00 | NOAA-21 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 2ec1e6e4-7233-3493-99ed-b15d3a9d4ee9 | 2.25071 | -50.7592 | 2026-08-30 05:14:00 | NOAA-21 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 71d8a471-74e9-347f-9078-b77356707bde | 2.52314 | -50.8548 | 2026-08-30 05:14:00 | NOAA-21 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 486b4e46-2175-3eec-a3d3-314978c3331b | 2.51441 | -50.85623 | 2026-08-30 05:14:00 | NOAA-21 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 414cf6a5-442c-397a-a160-6c15c83b951f | 2.23678 | -50.75703 | 2026-08-30 05:14:00 | NOAA-21 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 9b0b896d-40bb-3dda-84da-f02657932ab3 | 2.19424 | -50.71382 | 2026-08-30 05:14:00 | NOAA-21 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a9511fe1-d930-372e-b069-d171bdb1e98a | -4.95887 | -55.86116 | 2026-08-30 05:16:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f54ba058-abed-3601-873a-95f518b9805c | -3.63731 | -60.55849 | 2026-08-30 05:16:00 | NOAA-21 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 7.9 |
| da04f694-88b2-3383-802d-ad73d602fbf5 | -1.51342 | -55.92993 | 2026-08-30 05:16:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ebb3e7ac-fee2-314e-bfc5-78480ba4bd23 | -4.08186 | -45.93792 | 2026-08-30 05:16:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 3.3 |
| b9f90a66-9118-37c5-9581-595559ca4730 | -3.20157 | -61.16495 | 2026-08-30 05:16:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 170775a4-8bfa-39a0-91c4-36d5b830ad21 | -3.40523 | -61.32245 | 2026-08-30 05:16:00 | NOAA-21 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d89805bf-ba7b-39db-b74c-377ba3bfc9c4 | -4.34857 | -54.76365 | 2026-08-30 05:16:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f770a61b-4c7e-3500-9878-3e2c33715de7 | -4.0881 | -54.10622 | 2026-08-30 05:16:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 40725e68-98c0-39d4-824e-ba89d58d58f3 | -3.76325 | -59.33932 | 2026-08-30 05:16:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 381e9ed2-5c01-34ff-8a1a-8fc627b780e7 | -3.16687 | -60.13292 | 2026-08-30 05:16:00 | NOAA-21 | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c684560a-f6dd-310b-bc16-a5eb7a606be2 | -4.95774 | -55.84447 | 2026-08-30 05:16:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| d99f0720-80eb-37ca-b380-ad08726462ee | -4.96191 | -55.84096 | 2026-08-30 05:16:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 48.5 |
| c6bca49e-755a-3f0c-86f1-84ad4f7a5ca8 | -3.94087 | -59.33479 | 2026-08-30 05:16:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1daad5ba-0076-390a-a515-4f84f20f650a | -3.23485 | -61.2513 | 2026-08-30 05:16:00 | NOAA-21 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5dbff638-622b-368c-a348-d72d848b7fda | -3.61558 | -60.53974 | 2026-08-30 05:16:00 | NOAA-21 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8efa9f12-c47a-3402-94a4-99965ad1fec4 | -3.62129 | -60.54829 | 2026-08-30 05:16:00 | NOAA-21 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5a689a28-43fd-3896-bf19-08b79922f7d5 | -3.93809 | -59.33079 | 2026-08-30 05:16:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| dfdb7875-3637-353c-967e-c237d651101a | -4.6919 | -55.66566 | 2026-08-30 05:16:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| be5b86bf-f807-385e-87b7-eee0a2cb84fc | -3.76047 | -59.33533 | 2026-08-30 05:16:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2e99f6be-dca3-3415-85ae-1d7860eb2488 | -4.16011 | -60.69236 | 2026-08-30 05:16:00 | NOAA-21 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 43fede32-bb2c-3178-9c5b-ac3b4392c376 | -3.25969 | -60.65914 | 2026-08-30 05:16:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ffb55e86-6eda-31d3-b32a-f0e10733944a | -3.61499 | -60.54348 | 2026-08-30 05:16:00 | NOAA-21 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 663c2c25-6403-3a1c-824f-d526a6e91f18 | -1.24587 | -55.70572 | 2026-08-30 05:16:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 84944fd4-3bde-35d9-89c1-f286ea5d9a79 | -4.35824 | -55.02849 | 2026-08-30 05:16:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3685071d-362a-3a7c-a95c-b02453fe36ed | -4.9282 | -55.77317 | 2026-08-30 05:16:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 651a1174-0e57-35e6-a017-5c47d06a364f | -4.15549 | -60.69934 | 2026-08-30 05:16:00 | NOAA-21 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 31861a21-fe11-3b22-b9bd-4561d61ddb82 | -4.96427 | -55.84955 | 2026-08-30 05:16:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 14.5 |
| 1d121232-74b1-3711-a00f-8fa06a100579 | -3.574 | -58.63624 | 2026-08-30 05:16:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c2ec2a8e-1572-364e-9fe1-39e9d256502e | -4.36778 | -47.77774 | 2026-08-30 05:16:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 24.3 |
| 90d7c87c-bea3-3a70-a649-1d115fc24e88 | -4.37086 | -47.77766 | 2026-08-30 05:16:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 15.5 |
| 3dd2232e-17b2-3452-9c84-c4c92cfafb6a | -2.91542 | -54.11713 | 2026-08-30 05:16:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 9ea0fbc0-190a-3073-b29b-c8d78bb9c4ec | -3.22345 | -49.22948 | 2026-08-30 05:16:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ece5c67f-43a0-3734-afea-ad183e8bb350 | -3.49647 | -54.66021 | 2026-08-30 05:16:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| da260fdc-7b4d-37a1-bc98-40712b283dd7 | -3.23549 | -61.24728 | 2026-08-30 05:16:00 | NOAA-21 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c9e63c0b-c514-39f2-b48f-9401d86f78dd | -3.76435 | -59.33236 | 2026-08-30 05:16:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1b5184dc-8bd1-3341-b4e6-5c96ee40e92e | -4.15952 | -60.69613 | 2026-08-30 05:16:00 | NOAA-21 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 9.1 |
| d643b19b-6c8a-3239-8c29-486e3df777a2 | -3.69134 | -51.99799 | 2026-08-30 05:16:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| bad5838f-6804-3a27-9d06-124bb84bae2b | -4.4785 | -55.76024 | 2026-08-30 05:16:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a825e17d-ddd4-379a-8ef3-9b8e3790e7e1 | -4.59319 | -56.05342 | 2026-08-30 05:16:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f95bd276-b078-34e6-9fee-ffc517eead9f | 0.96758 | -60.40837 | 2026-08-30 05:16:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7e6197a0-9a59-3e4d-9834-ec4da6d5e580 | -3.0033 | -56.66221 | 2026-08-30 05:16:00 | NOAA-21 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| aab15c92-92f2-3618-aeca-d5b202e13d0b | -3.93863 | -59.32731 | 2026-08-30 05:16:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 78cdd135-33dc-3129-903f-90ea5cee1f81 | -4.36839 | -47.77331 | 2026-08-30 05:16:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 28.8 |
| bbb78069-6701-3189-bf24-35346ae80aba | 0.19952 | -60.50295 | 2026-08-30 05:16:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fda9e158-ccda-3c89-8ded-af2dacb484ed | -2.47988 | -46.85516 | 2026-08-30 05:16:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 46eaf6de-3dec-316d-a0a2-3aa5f8eb0678 | -4.15726 | -60.68807 | 2026-08-30 05:16:00 | NOAA-21 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| ec49baf5-abbf-33c7-adfa-15a9ff866d45 | -3.59522 | -55.30014 | 2026-08-30 05:16:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5f88dc5c-3987-32c9-a484-8c297413e8ca | -4.05658 | -56.29152 | 2026-08-30 05:16:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a5c525c8-f51f-390a-b68e-39102c1c9164 | -4.15667 | -60.69183 | 2026-08-30 05:16:00 | NOAA-21 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| f25c7b5c-72a8-3025-9596-416d7ad8f9ba | -3.63387 | -60.55794 | 2026-08-30 05:16:00 | NOAA-21 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 59041d37-3ad6-355a-8820-a7b9eea5e8ed | -4.35889 | -55.02416 | 2026-08-30 05:16:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 645d9c77-be80-3d3b-9e2c-1acb2b12d071 | -4.08512 | -45.9366 | 2026-08-30 05:16:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 8332aaf8-080a-3e50-a45c-a32f0580edec | -4.40127 | -55.43524 | 2026-08-30 05:16:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b93983f0-a43d-3652-a270-6d4112ab4e6b | -4.6696 | -55.9309 | 2026-08-30 05:16:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7724f07b-12f8-3050-8126-cbcfd74f4324 | -1.24731 | -55.70226 | 2026-08-30 05:16:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| eef90259-4d07-32ac-8563-a3b3ad6c6e72 | -3.63219 | -60.54616 | 2026-08-30 05:16:00 | NOAA-21 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1e1a20fb-47b3-3e07-9a68-0cdc58fbb3ba | -2.80144 | -49.57974 | 2026-08-30 05:16:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| b84a458f-2782-3ffd-847f-2d16653876d9 | -4.15657 | -60.71493 | 2026-08-30 05:16:00 | NOAA-21 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 66078abe-df28-32a3-9be4-6b3616af222d | -3.49274 | -54.65966 | 2026-08-30 05:16:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| cd5dc0d8-facb-3544-9305-acdac1806be5 | -1.24672 | -55.70604 | 2026-08-30 05:16:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d758ebbc-b318-3682-8fdf-9de936675dae | -3.49408 | -54.65069 | 2026-08-30 05:16:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cfcef41d-cbf4-3abb-a062-a6d555449287 | -4.09937 | -50.42882 | 2026-08-30 05:16:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b82a7e5f-59ab-3be6-a4cf-d30e944d01cc | -3.63102 | -60.55365 | 2026-08-30 05:16:00 | NOAA-21 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 46a596ab-458c-30fd-8047-d8dbae60d741 | -4.08734 | -54.11115 | 2026-08-30 05:16:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0e2dd0ad-88fa-34cc-ab2e-959b41c52323 | -1.43325 | -55.30682 | 2026-08-30 05:16:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cf429107-bfe2-349a-867a-d5a5292bd7d0 | -3.18366 | -48.01965 | 2026-08-30 05:16:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 561eb195-aaeb-34dd-af41-c5d449bf3bad | -2.02013 | -52.11163 | 2026-08-30 05:16:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2e94bece-042e-368f-95e4-e48ccf8897c5 | -4.22219 | -56.08352 | 2026-08-30 05:16:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| fe1c0aa7-2502-37fc-83fb-618beb6e7e8d | -3.62187 | -60.54455 | 2026-08-30 05:16:00 | NOAA-21 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6415a81d-7a8b-3009-9341-751f55c314d1 | -1.62493 | -55.1682 | 2026-08-30 05:16:00 | NOAA-21 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 42fab8f0-6b66-341e-9a15-92a899b46167 | -2.50118 | -56.07285 | 2026-08-30 05:16:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 44c02d79-a9bc-37f6-b3c4-53da43b5b559 | -3.63328 | -60.56169 | 2026-08-30 05:16:00 | NOAA-21 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 20.4 |
| 5f8fc658-61f8-3155-b054-f686cbd678b6 | -3.93531 | -59.32679 | 2026-08-30 05:16:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 66286b59-dbcd-3a8c-a12e-fe9f77e26641 | -3.51807 | -59.0373 | 2026-08-30 05:16:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 855460e4-1707-3185-854f-3c58cc844575 | 0.19595 | -60.50349 | 2026-08-30 05:16:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 33c2dbdc-aced-3c29-a125-6227c06bd29a | -3.7638 | -59.33584 | 2026-08-30 05:16:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 2ab317d9-273e-356d-a72d-c4e022a4ca05 | -4.96269 | -56.27022 | 2026-08-30 05:16:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6dea683b-c5bd-3c21-8ad4-6c5d34b59558 | -3.48967 | -54.65462 | 2026-08-30 05:16:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |


[Clique aqui para ver as próximas entradas](README49.md)
