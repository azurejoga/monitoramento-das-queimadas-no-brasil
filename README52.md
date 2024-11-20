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

## Dados Diários - Página 52

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3f375497-51cc-3886-b12f-5d0f084c91ef | -2.28487 | -53.63362 | 2024-11-20 04:50:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 91a86d9f-981c-3d20-99c1-b9eb204ba674 | -2.93353 | -48.3302 | 2024-11-20 04:50:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f95840ca-c378-3d90-985e-d59a73b4e4d3 | -1.63028 | -52.58125 | 2024-11-20 04:50:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 502fd297-3b45-3c6c-b209-809ff7115d98 | -3.01026 | -51.44451 | 2024-11-20 04:50:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| fe7d4caa-e4b9-3995-8184-e62f3c0e8909 | -9.1789 | -44.71895 | 2024-11-20 04:50:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| abc5f200-ec7f-358c-842a-a74806703382 | -1.30916 | -52.4042 | 2024-11-20 04:50:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a6fe4ef2-dd56-3199-9977-10d1bd91d3e0 | -0.89526 | -51.72496 | 2024-11-20 04:50:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b422884b-fa69-3048-a42f-570f5be8c0c9 | -1.71839 | -53.26461 | 2024-11-20 04:50:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 1bf1a39f-44b1-3864-b653-ea4d82d76d02 | -2.57929 | -54.02526 | 2024-11-20 04:50:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8f955cf4-7a94-3aeb-b95c-f9880ad622fe | -2.83801 | -54.0128 | 2024-11-20 04:50:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a3ad6861-edc1-319f-b83e-262aafedb2e3 | -1.14561 | -53.51052 | 2024-11-20 04:50:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 83fcd2ec-2b93-3959-bb54-e9151b65cd77 | -4.13255 | -53.61058 | 2024-11-20 04:50:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9eeecf1f-d9bd-3c7a-b17e-15bf6dc5e0ca | -1.22427 | -51.741 | 2024-11-20 04:50:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e2ced73b-6f79-376c-89f9-d0706f4282f5 | -2.57704 | -49.20425 | 2024-11-20 04:50:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| efc9aaa6-aa1f-3a41-8a27-5fdd3587d86d | -2.82083 | -54.09709 | 2024-11-20 04:50:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5ba97fab-af45-35d1-bef3-3cdb5f65e6a9 | -2.91355 | -48.31405 | 2024-11-20 04:50:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 13413cc8-3561-39b7-a831-59972430f205 | -4.02606 | -54.01108 | 2024-11-20 04:50:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b0a32666-3c98-3293-94ea-c96ed637ae8d | -3.7716 | -51.68036 | 2024-11-20 04:50:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 94225edc-1e8b-3713-a676-cb28765fa7b8 | -0.95872 | -51.7276 | 2024-11-20 04:50:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3637243e-ff45-30a2-ac43-bf79f3d1ab25 | -3.45556 | -53.30069 | 2024-11-20 04:50:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 19c80a2a-3d0d-3aa4-89bf-eb3583a0da4f | -0.83252 | -52.83609 | 2024-11-20 04:50:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9d93d128-642d-3e66-90d9-e8b1e4ed4b40 | -2.83514 | -54.00839 | 2024-11-20 04:50:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bbb27269-0ccb-3339-bc87-8f694fcb39c5 | -1.63024 | -52.6756 | 2024-11-20 04:50:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 18ec8e6b-e39e-30c0-9ded-134061fd78d2 | -1.48514 | -51.13561 | 2024-11-20 04:50:00 | NPP-375D | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 73283209-01e7-3be0-b60d-81f079cc688a | -1.25851 | -53.36913 | 2024-11-20 04:50:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 6406d3b3-8f2c-3c2f-860d-59d31ce5585c | -1.32623 | -51.86308 | 2024-11-20 04:50:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f192bcb3-5a8a-3515-89c1-65fb1be2b251 | -3.18765 | -53.2512 | 2024-11-20 04:50:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| f5ae4e4a-13a4-3e14-b533-222dfbe693ff | -1.64933 | -52.68588 | 2024-11-20 04:50:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| cc209032-8c56-3239-bf2d-03ad8e057054 | -3.50892 | -53.79667 | 2024-11-20 04:50:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| fe2c0640-2cac-30a2-b70d-219836e1eefb | -2.63084 | -46.56376 | 2024-11-20 04:50:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 272622d9-b9c6-3df5-9a62-617ccadef3bc | -1.73415 | -45.58486 | 2024-11-20 04:50:00 | NPP-375D | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2f42f469-aaa3-3a03-bdda-226fb7c573b9 | -3.1956 | -54.32647 | 2024-11-20 04:50:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 67ba4e49-af0f-39b1-b45d-38b8d82f4af9 | -1.304 | -52.26284 | 2024-11-20 04:50:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e89126cc-4308-3206-b572-1400c5d33336 | -2.66478 | -46.61243 | 2024-11-20 04:50:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b88cd6f7-1155-3c83-91c7-508d92585bb7 | -2.68901 | -46.23808 | 2024-11-20 04:50:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| be3245cf-a660-39a0-861e-94943d44a4ee | -4.2852 | -50.58307 | 2024-11-20 04:50:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d5a5655c-16de-3273-b698-88fd69cc310f | -4.13712 | -47.7361 | 2024-11-20 04:50:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8e21b0bc-8d6d-3982-9d9c-fcb7a8790e8e | -2.38108 | -54.43332 | 2024-11-20 04:50:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| c3827d9e-606a-3ce4-ad53-7a1d8cba5ea2 | -3.42679 | -53.28497 | 2024-11-20 04:50:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1c62f42d-9177-37f4-aeae-4adb43b8ac69 | -4.07629 | -50.04015 | 2024-11-20 04:50:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3b13cdbd-2423-317f-9d39-c14ed9e9f239 | -2.90318 | -53.05991 | 2024-11-20 04:50:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 2aedcfad-da62-30c9-9abd-cd1b29dcfc58 | -1.41801 | -52.82283 | 2024-11-20 04:50:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e04b9446-6cf8-3a88-9962-3e686d828e55 | -3.03576 | -49.45534 | 2024-11-20 04:50:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4025c5c5-599e-3b10-90f8-70729176fb85 | -1.21104 | -51.7602 | 2024-11-20 04:50:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| dcdbeaa2-7153-369d-b3c6-d6f9503dd161 | -6.82642 | -43.28745 | 2024-11-20 04:50:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 80c2cb8a-ef72-37eb-844a-d00e889fee37 | -3.13994 | -49.13094 | 2024-11-20 04:50:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 14596dda-6b92-34d3-a133-bcfca31bb837 | -0.81007 | -51.59839 | 2024-11-20 04:50:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fc9ef367-9b32-3234-8e04-241284364bcc | -3.40333 | -52.87915 | 2024-11-20 04:50:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8d50e84b-8597-3f70-adbb-414ada778857 | -2.56258 | -48.16922 | 2024-11-20 04:50:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cc6ef73e-8e0f-3dfe-8c5e-70a94143f9fd | -0.4873 | -52.07822 | 2024-11-20 04:50:00 | NPP-375D | LARANJAL DO JARI | AMAPÁ | Brasil | 1600279 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 60d5e27c-8b01-392e-a9a1-ced769a6477f | -1.4886 | -52.10542 | 2024-11-20 04:50:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 70429f43-3b5d-3246-97e6-f02859b91238 | -0.48506 | -52.0707 | 2024-11-20 04:50:00 | NPP-375D | LARANJAL DO JARI | AMAPÁ | Brasil | 1600279 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8aef5536-33f2-3962-96da-ec906fa20b49 | -2.65789 | -46.54987 | 2024-11-20 04:50:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 670209f9-4de9-3b8e-b811-f52fb2e7e358 | -2.34047 | -54.78174 | 2024-11-20 04:50:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| b21441f3-fb69-32d1-b127-e6b6805eabcb | -3.55423 | -50.27608 | 2024-11-20 04:50:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5bb5790c-1234-3103-a261-92b696466a40 | -2.85207 | -51.5895 | 2024-11-20 04:50:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1def2e41-052f-3fac-ab77-6fc5afb8a45f | -2.62656 | -51.79807 | 2024-11-20 04:50:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 7db516cd-c101-31dd-b5ab-c0ec72d64eb8 | -2.36032 | -46.19321 | 2024-11-20 04:50:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 1d6a222b-6525-37a6-9589-4ddc74721108 | -2.56437 | -54.97106 | 2024-11-20 04:50:00 | NPP-375D | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f0f9f2d0-2860-33f3-b055-4d55c90c58e4 | -1.19889 | -51.77248 | 2024-11-20 04:50:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 9234c3b1-0cbe-3889-b1d4-1b1fd60d8350 | -2.85527 | -53.97224 | 2024-11-20 04:50:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0743f41a-6327-3479-9512-bb623691c72d | -6.2362 | -47.27541 | 2024-11-20 04:50:00 | NPP-375D | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8f96e0a4-3fcf-307d-bf12-b8991412cee7 | -3.66979 | -54.27338 | 2024-11-20 04:50:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 23fbc993-198e-32b8-aa27-6ec1dbcde66f | -2.66533 | -46.60889 | 2024-11-20 04:50:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| db49fb15-39ab-35d4-86d6-1128d3d712c8 | -0.96384 | -51.78158 | 2024-11-20 04:50:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 17a1c6d7-b206-30de-b112-659f85379cff | -1.72404 | -52.69391 | 2024-11-20 04:50:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7ddc5632-7fc6-3da4-bbce-b358f7edfc88 | -1.28515 | -52.46918 | 2024-11-20 04:50:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0c501ed6-3355-369e-8279-7214ce4d6002 | -3.20036 | -54.31915 | 2024-11-20 04:50:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b6ac8d03-beff-3b67-9532-c02791ecd971 | -1.11219 | -51.74496 | 2024-11-20 04:50:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 372d7b56-48c1-3a39-ab19-af91907a9e85 | -2.78777 | -51.71716 | 2024-11-20 04:50:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1d0d1f7b-02da-380f-ad70-34906262c864 | -2.76065 | -54.06458 | 2024-11-20 04:50:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 79615640-4105-30b0-b34d-b1f9027491d9 | -1.21056 | -51.78492 | 2024-11-20 04:50:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7de749dc-02cc-3575-9c57-915f86936ad3 | -3.06029 | -54.40681 | 2024-11-20 04:50:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a4e0f8fa-b936-31f4-a749-7eb33f1b70bf | -2.36502 | -46.19018 | 2024-11-20 04:50:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| cece167c-09c3-3c19-a3e1-60003081442a | -1.28571 | -52.46565 | 2024-11-20 04:50:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 03283e3d-05f2-3cee-bfc0-413dfb4c72b7 | -0.90523 | -51.72651 | 2024-11-20 04:50:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ea5d56b2-e90f-3f7e-a8b7-0059f183ff46 | -3.78772 | -41.60709 | 2024-11-20 04:50:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| b5d9cf6b-3c41-389c-895e-c6cdb11260f6 | -1.4554 | -52.67438 | 2024-11-20 04:50:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| f2a3418a-d8e3-36dd-8aff-567473d8aa02 | -2.84924 | -46.68031 | 2024-11-20 04:50:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7208a5b4-1e8c-3f92-b789-6f91a195981c | -4.11023 | -51.05392 | 2024-11-20 04:50:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b60a6ba6-9aae-3815-81df-cf0b3307089e | -4.38593 | -47.76126 | 2024-11-20 04:50:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 0a7208fe-cfe5-3a8b-b4e4-dc32d6ee7b3d | -2.78669 | -51.72404 | 2024-11-20 04:50:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 68bc9490-5de5-3931-935b-e68e03231750 | -3.54563 | -54.57336 | 2024-11-20 04:50:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f195540f-ae1d-346c-8b3c-a8207989abce | -1.25161 | -53.36803 | 2024-11-20 04:50:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| fc7dd393-44dc-3a1f-b2f1-7101e6b539db | -3.3922 | -44.4355 | 2024-11-20 04:50:00 | NPP-375D | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6d9990db-7991-3d26-b30d-112bd7ea7eae | -3.2902 | -46.195 | 2024-11-20 04:50:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b2f940c5-0e23-370f-acf8-edf6b69de4c5 | -3.91115 | -52.40683 | 2024-11-20 04:50:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b89cb4ee-7341-3671-984f-2244ec92fd6a | -1.22664 | -51.79097 | 2024-11-20 04:50:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 9848c385-95d7-3a51-b178-83186e7e8008 | -1.22332 | -51.79045 | 2024-11-20 04:50:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 661688ac-2687-3d67-8d9b-4210d7f4624a | -3.55153 | -51.52956 | 2024-11-20 04:50:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ac917306-3e20-38d6-9f03-eee0f94a3f54 | -1.15122 | -53.79798 | 2024-11-20 04:50:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 318b1623-75d6-3a17-a546-67e289ed023f | -2.20969 | -50.76663 | 2024-11-20 04:50:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 12cfcd46-80e4-3c71-a0ba-f8953d85d6e7 | -2.38466 | -54.43388 | 2024-11-20 04:50:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 620f5a72-43a1-3974-afe5-a2490b793890 | -2.94085 | -48.33131 | 2024-11-20 04:50:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 21cc27e9-858f-348f-bc0a-da49eb1e9cf5 | -1.49601 | -49.68574 | 2024-11-20 04:50:00 | NPP-375D | SÃO SEBASTIÃO DA BOA VISTA | PARÁ | Brasil | 1507706 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7c8e5f99-5eaa-3500-a0d1-277e388a14c4 | -6.82854 | -43.28737 | 2024-11-20 04:50:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 675a07ed-baa1-3105-9461-6d72665efcfc | -1.25214 | -51.77723 | 2024-11-20 04:50:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ce64e5cf-ad2b-38d2-91ed-84f994141453 | -2.65734 | -46.55342 | 2024-11-20 04:50:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ab81d874-1ccd-342c-b306-03e9ab4f82ef | -2.95183 | -48.33298 | 2024-11-20 04:50:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 37ec2411-341c-39a2-a0f1-964d70ae6db3 | -1.47851 | -51.13457 | 2024-11-20 04:50:00 | NPP-375D | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |


[Clique aqui para ver as próximas entradas](README53.md)
