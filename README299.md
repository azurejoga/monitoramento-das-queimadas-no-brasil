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

## Dados Diários - Página 299

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 342233ed-6806-3409-8e5d-774dd84d9e50 | -5.18146 | -38.45098 | 2026-10-08 16:20:00 | NPP-375 | MORADA NOVA | CEARÁ | Brasil | 2308708 | 23 | 33 | nan | nan | nan | Caatinga | 4.7 |
| ec4cb4eb-ce5d-30db-8680-19eecfa9debc | -5.68004 | -42.59669 | 2026-10-08 16:20:00 | NPP-375 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 4.9 |
| 0d81a6ef-3993-362f-acb3-d65c1aadb8cd | -5.70976 | -41.67231 | 2026-10-08 16:20:00 | NPP-375 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 7.4 |
| 37c65f70-2d97-3a8c-8062-29e70432ed54 | -5.70675 | -41.72343 | 2026-10-08 16:20:00 | NPP-375 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 13.0 |
| 075b51db-31e3-3f00-847a-42ecd5d72b00 | -2.08497 | -46.57652 | 2026-10-08 16:20:00 | NPP-375 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 102.4 |
| 404aa11d-e0de-31c3-9391-5b93d7ece5b7 | -7.20571 | -46.53724 | 2026-10-08 16:20:00 | NPP-375 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 9154eca4-a605-3470-8208-6898af405a6f | -6.92607 | -45.26503 | 2026-10-08 16:20:00 | NPP-375 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 23.9 |
| f1f81c60-4547-361b-bee9-86c9280465a1 | -7.20975 | -46.53154 | 2026-10-08 16:20:00 | NPP-375 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 13.8 |
| bd425a56-3fab-36dd-a29c-1f0e6045af6d | -5.78484 | -50.10255 | 2026-10-08 16:20:00 | NPP-375 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 0f24a581-0c4a-3a2b-8502-4759c8505c49 | -5.75229 | -42.07815 | 2026-10-08 16:20:00 | NPP-375 | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 11.8 |
| 0c9ede12-4808-3f1f-b443-347b3df63e6a | -5.74526 | -42.05502 | 2026-10-08 16:20:00 | NPP-375 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 17.6 |
| 338ece3f-2662-32f0-b896-86414f9597a8 | -3.66396 | -45.40895 | 2026-10-08 16:20:00 | NPP-375 | SANTA INÊS | MARANHÃO | Brasil | 2109908 | 21 | 33 | nan | nan | nan | Amazônia | 5.0 |
| e6ea7bdf-7ab4-36f8-8614-d1de9b37fe8e | -7.24816 | -44.52904 | 2026-10-08 16:20:00 | NPP-375 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 6a7df4a3-26ca-3996-9bbe-d20743006a4d | -6.14695 | -43.3769 | 2026-10-08 16:20:00 | NPP-375 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| e70e706e-e267-3cd6-b7bb-bad755c78216 | -5.4722 | -45.70759 | 2026-10-08 16:20:00 | NPP-375 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 9fea5fb7-2ebe-3d05-a542-1eb338df8b29 | -7.05709 | -44.33004 | 2026-10-08 16:20:00 | NPP-375 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| f3f9e11b-a55a-3781-816b-c66fabe56b98 | -6.66673 | -45.36211 | 2026-10-08 16:20:00 | NPP-375 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| e59856dc-b216-3b82-aa59-05c7c78a9eeb | -3.36411 | -50.47174 | 2026-10-08 16:20:00 | NPP-375 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 85fa75c9-c950-3659-be7b-a79fab1b4c8d | -4.15797 | -43.19853 | 2026-10-08 16:20:00 | NPP-375 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 73119f49-98fd-3e68-9898-a0b46f9101c8 | -6.84331 | -45.1235 | 2026-10-08 16:20:00 | NPP-375 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 15.2 |
| dddb5694-7eb0-3ebd-b25e-0a0dde81eaad | -2.98744 | -54.07652 | 2026-10-08 16:20:00 | NPP-375 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 25.4 |
| df825a71-5c67-305d-a3c5-c2b20b104772 | -4.84922 | -44.08746 | 2026-10-08 16:20:00 | NPP-375 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 31a2ba8b-082c-36a2-8aeb-3c040bd4108c | -4.34488 | -47.76628 | 2026-10-08 16:20:00 | NPP-375 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 0cd0b522-b353-37d9-874e-16e2772dfc3a | -4.35869 | -43.80507 | 2026-10-08 16:20:00 | NPP-375 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 22407c10-8259-3083-804c-7628c89a1630 | -7.85676 | -44.96175 | 2026-10-08 16:20:00 | NPP-375 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 5.6 |
| d4648930-bfbc-39d5-95ed-585bcb3e2a59 | -4.58018 | -40.65737 | 2026-10-08 16:20:00 | NPP-375 | IPUEIRAS | CEARÁ | Brasil | 2305902 | 23 | 33 | nan | nan | nan | Caatinga | 17.6 |
| 79164c41-af91-3bb6-8b32-2eacdd2bbeab | -7.0576 | -44.33367 | 2026-10-08 16:20:00 | NPP-375 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 9c915f02-c06b-3c5b-b47b-9f0aa8ca6ef2 | -5.70482 | -53.46686 | 2026-10-08 16:20:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 70.2 |
| 9d5f15f2-49f5-3728-bbf6-a9cd11eee161 | -2.7552 | -54.11473 | 2026-10-08 16:20:00 | NPP-375 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| a35ad6cd-679b-3b34-a89b-06b3499c4136 | -6.33512 | -35.12705 | 2026-10-08 16:20:00 | NPP-375 | CANGUARETAMA | RIO GRANDE DO NORTE | Brasil | 2402204 | 24 | 33 | nan | nan | nan | Mata Atlântica | 7.2 |
| 2a70592f-eb8b-326a-b503-4c5d9e0f5244 | -5.48557 | -45.04102 | 2026-10-08 16:20:00 | NPP-375 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 8ae18a61-3661-313f-8afa-72010c334a0f | -5.71484 | -41.73004 | 2026-10-08 16:20:00 | NPP-375 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 28.4 |
| 51f1d132-8883-3a5c-b586-f94f9db85064 | -6.40726 | -44.95715 | 2026-10-08 16:20:00 | NPP-375 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 34.4 |
| c2b3c4f6-ccd4-30a8-82dc-bfb5765df585 | -8.34708 | -47.66956 | 2026-10-08 16:20:00 | NPP-375 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 7a7660ed-490e-318f-864d-03e6947f4b1a | -6.12685 | -47.93666 | 2026-10-08 16:20:00 | NPP-375 | CACHOEIRINHA | TOCANTINS | Brasil | 1703826 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| aee60cca-1d20-38ac-9da1-f14f55a17755 | -3.00416 | -54.08903 | 2026-10-08 16:20:00 | NPP-375 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 21.7 |
| f1374a25-2b27-3044-b850-a90b9021fe2c | -5.30829 | -45.71994 | 2026-10-08 16:20:00 | NPP-375 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| a9f19a1a-3940-3dac-b06f-4f4a64991a35 | -7.11937 | -40.56322 | 2026-10-08 16:20:00 | NPP-375 | FRONTEIRAS | PIAUÍ | Brasil | 2204303 | 22 | 33 | nan | nan | nan | Caatinga | 7.0 |
| 7ab5b752-6163-3222-93ac-cd2feb154734 | -7.21085 | -46.53413 | 2026-10-08 16:20:00 | NPP-375 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 8.3 |
| b898fb20-764d-3e2a-bbec-784eb91f977e | -6.15141 | -43.38094 | 2026-10-08 16:20:00 | NPP-375 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 15.2 |
| 1d328950-9aab-33f8-9ce1-9504443dec40 | -2.37837 | -45.70813 | 2026-10-08 16:20:00 | NPP-375 | PRESIDENTE MÉDICI | MARANHÃO | Brasil | 2109239 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| eecfac79-46fc-3e42-ba6c-12a27be6ba9c | -3.261 | -54.04186 | 2026-10-08 16:20:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 618cf96c-3c11-3473-aeed-0001520dce7f | -7.18576 | -52.62353 | 2026-10-08 16:20:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 38.8 |
| 8e8b3f7f-2e27-350e-bbbc-17f831db66f7 | -6.39353 | -52.72451 | 2026-10-08 16:20:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 25.2 |
| 720df966-8915-3cef-8363-1fd4e62bb377 | -2.99346 | -51.56092 | 2026-10-08 16:20:00 | NPP-375 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 4e2f0244-db22-3c2c-961e-eb19e8d49be2 | -5.95908 | -40.94378 | 2026-10-08 16:20:00 | NPP-375 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 52.6 |
| 210c8f02-036d-3d98-8b2c-ff12f4e6b418 | -3.19944 | -43.40911 | 2026-10-08 16:20:00 | NPP-375 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 5f6fbaab-b6e2-313a-89be-e27e7f388299 | -6.93413 | -43.66639 | 2026-10-08 16:20:00 | NPP-375 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 57.1 |
| 90fcb10c-2a4b-3337-a965-a849303d0fed | -7.14966 | -45.61468 | 2026-10-08 16:20:00 | NPP-375 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 961a445b-0e0c-376f-a63f-df45c4b2f4f0 | -7.4902 | -42.79444 | 2026-10-08 16:20:00 | NPP-375 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 15.4 |
| ada92635-f992-31b9-be54-eba5bebc6a59 | -3.78484 | -41.78401 | 2026-10-08 16:20:00 | NPP-375 | SÃO JOSÉ DO DIVINO | PIAUÍ | Brasil | 2210052 | 22 | 33 | nan | nan | nan | Caatinga | 7.6 |
| a763c450-ee50-3c82-a20a-a2885b43e82c | -5.48108 | -41.21822 | 2026-10-08 16:20:00 | NPP-375 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 7.4 |
| 998e5540-127e-3ed8-8e88-b2f7012cfb7a | -4.08088 | -44.10819 | 2026-10-08 16:20:00 | NPP-375 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 32.4 |
| 43ed45bc-186d-339f-90b0-76841aa3dc4e | -7.07214 | -47.39525 | 2026-10-08 16:20:00 | NPP-375 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 26.0 |
| 7363615f-2db2-3a4a-bf75-6dfa5efd221f | -7.47615 | -42.85577 | 2026-10-08 16:20:00 | NPP-375 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 73.7 |
| a5b95d44-f5aa-3277-96b1-b3e1753a4687 | -3.39543 | -40.24848 | 2026-10-08 16:20:00 | NPP-375 | SANTANA DO ACARAÚ | CEARÁ | Brasil | 2312007 | 23 | 33 | nan | nan | nan | Caatinga | 9.1 |
| 78f0d9c0-e63b-3c96-bf9e-3c93b483d660 | -2.08182 | -46.58572 | 2026-10-08 16:20:00 | NPP-375 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| a6534533-d08f-37a5-886d-03429bdbf3cc | -6.1346 | -47.94007 | 2026-10-08 16:20:00 | NPP-375 | CACHOEIRINHA | TOCANTINS | Brasil | 1703826 | 17 | 33 | nan | nan | nan | Cerrado | 14.0 |
| ba926332-34f2-351a-84ab-6c5326ce0ab5 | -6.09811 | -53.49678 | 2026-10-08 16:20:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 14.5 |
| 9558bc5d-6c08-3e70-b06c-b1bfd5e70a11 | -3.17422 | -50.58567 | 2026-10-08 16:20:00 | NPP-375 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 17.7 |
| 03f8d89b-df4d-3e50-96cb-eacd5ea5e3e9 | -7.34099 | -45.2924 | 2026-10-08 16:20:00 | NPP-375 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 01ce4dc4-b3bd-3ab2-ab5f-4bd61d08d547 | -3.08172 | -53.95169 | 2026-10-08 16:20:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 21.6 |
| 7ec0ea89-71c1-3c30-a38d-962755cf7ee4 | -7.71699 | -44.7365 | 2026-10-08 16:20:00 | NPP-375 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 273da2d7-d56b-3d9e-b33b-7dff051cc06d | -7.38374 | -50.34492 | 2026-10-08 16:20:00 | NPP-375 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 323fcc2b-2555-3b56-a376-7114279f857f | -7.45701 | -43.1999 | 2026-10-08 16:20:00 | NPP-375 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 17.1 |
| 3b40212f-10c5-3c84-9473-8a6a22264e39 | -3.94578 | -44.71674 | 2026-10-08 16:20:00 | NPP-375 | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Amazônia | 8.7 |
| bae3a257-fa06-3003-be0b-28951cfccd41 | -4.03359 | -38.84776 | 2026-10-08 16:20:00 | NPP-375 | MARANGUAPE | CEARÁ | Brasil | 2307700 | 23 | 33 | nan | nan | nan | Caatinga | 3.5 |
| f29ab8d8-e788-3d0d-a54d-4a2b80f02266 | -3.29739 | -40.09122 | 2026-10-08 16:20:00 | NPP-375 | MORRINHOS | CEARÁ | Brasil | 2308906 | 23 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 0d461c0d-edb0-33de-be2a-c1172241b58e | -7.90347 | -44.17403 | 2026-10-08 16:20:00 | NPP-375 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 9adfd549-b590-3418-8783-7c3fb2b6fd14 | -1.0241 | -48.89366 | 2026-10-08 16:20:00 | NPP-375 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a8855a1b-2ecd-3889-92bf-d8d113b33f36 | -2.42092 | -50.45575 | 2026-10-08 16:20:00 | NPP-375 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 76b1735d-d43a-372f-a82f-52076d516530 | -6.43231 | -37.09869 | 2026-10-08 16:20:00 | NPP-375 | CAICÓ | RIO GRANDE DO NORTE | Brasil | 2402006 | 24 | 33 | nan | nan | nan | Caatinga | 14.7 |
| 4bac3318-755c-3265-8f26-282d0dde0600 | -6.15785 | -39.42973 | 2026-10-08 16:20:00 | NPP-375 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 14.3 |
| 4b9d3297-342a-3d3b-9146-ff15d5877a93 | -6.77143 | -44.12312 | 2026-10-08 16:20:00 | NPP-375 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 15.4 |
| e4dcf59d-6170-34c6-824f-001920e012ec | -6.99549 | -44.1287 | 2026-10-08 16:20:00 | NPP-375 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 4d4b8edc-aae1-3eb8-8574-cecf68692766 | -3.25885 | -54.02251 | 2026-10-08 16:20:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 15.1 |
| 8cb67cd1-aaa8-387c-b492-f01e19f0ea52 | -7.87538 | -44.15217 | 2026-10-08 16:20:00 | NPP-375 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 671d5031-d759-30e9-b816-d07d2083157b | -6.96529 | -45.26081 | 2026-10-08 16:20:00 | NPP-375 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 9831846b-a384-3c50-a984-d58b7361b517 | -6.33819 | -35.12167 | 2026-10-08 16:20:00 | NPP-375 | CANGUARETAMA | RIO GRANDE DO NORTE | Brasil | 2402204 | 24 | 33 | nan | nan | nan | Mata Atlântica | 11.0 |
| 61a361f6-053f-3fef-8d62-c33a6a8204b7 | -6.86369 | -44.90184 | 2026-10-08 16:20:00 | NPP-375 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 1c6adc54-4900-39b1-900e-5da2301b3c55 | -6.22424 | -44.85395 | 2026-10-08 16:20:00 | NPP-375 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 23.8 |
| f7e03391-4592-33bf-b996-35f60fb3c7b4 | -7.40886 | -44.74743 | 2026-10-08 16:20:00 | NPP-375 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 17.0 |
| f88c32c1-5e6c-300f-b820-61f1afacc90f | -5.71022 | -41.72292 | 2026-10-08 16:20:00 | NPP-375 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 7.3 |
| 4d9375ca-fb9f-3013-a4e5-de9f4bc94061 | -6.04516 | -53.48955 | 2026-10-08 16:20:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 6f80c526-62e8-36af-aa0e-4da5f9fae1ef | -6.50781 | -42.02978 | 2026-10-08 16:20:00 | NPP-375 | NOVO ORIENTE DO PIAUÍ | PIAUÍ | Brasil | 2206902 | 22 | 33 | nan | nan | nan | Caatinga | 17.9 |
| be5352dc-3baa-33f5-9936-cc3226254986 | -2.33599 | -50.48013 | 2026-10-08 16:20:00 | NPP-375 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 13.9 |
| 8038daeb-75cc-3404-9af8-f393683c05bf | -4.98144 | -36.8835 | 2026-10-08 16:20:00 | NPP-375 | PORTO DO MANGUE | RIO GRANDE DO NORTE | Brasil | 2410256 | 24 | 33 | nan | nan | nan | Caatinga | 7.0 |
| f07ba083-29c7-3322-88c9-a4874353759e | -7.0321 | -45.29413 | 2026-10-08 16:20:00 | NPP-375 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 11.5 |
| f6df4906-3678-385b-bf09-2f79128b8800 | -2.98798 | -54.06799 | 2026-10-08 16:20:00 | NPP-375 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 18.8 |
| d188574d-05d5-39e2-a042-4fd4307ece4d | -5.29403 | -42.70592 | 2026-10-08 16:20:00 | NPP-375 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 9ebecdf8-b6bb-3f7d-8c45-037a77ffdfa6 | -5.75135 | -41.71287 | 2026-10-08 16:20:00 | NPP-375 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 52.2 |
| aa1488e7-03d7-392e-a8f0-efc2c37e4ee5 | -4.38333 | -43.95586 | 2026-10-08 16:20:00 | NPP-375 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 848e30ec-9845-3714-adde-03c9442d2bb8 | -3.07858 | -40.1642 | 2026-10-08 16:20:00 | NPP-375 | BELA CRUZ | CEARÁ | Brasil | 2302305 | 23 | 33 | nan | nan | nan | Caatinga | 7.1 |
| 1373b372-4349-3b2b-8d9f-abb4b1135cac | -6.36275 | -42.56098 | 2026-10-08 16:20:00 | NPP-375 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 10.6 |
| e3aa5d94-d794-337c-bc07-ce1c9ad72007 | -6.53681 | -45.39272 | 2026-10-08 16:20:00 | NPP-375 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 35.0 |
| 586e26cc-06a5-34d4-aa37-0ebe02cb00b0 | -2.0725 | -46.5819 | 2026-10-08 16:20:00 | NPP-375 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 7e6fde70-59c0-3b4a-a1b6-d662a3fc1869 | -5.39189 | -42.96367 | 2026-10-08 16:20:00 | NPP-375 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | 8.1 |
| 0cfa931b-d748-3f9f-9cac-d62005dbcd40 | -7.53264 | -42.09243 | 2026-10-08 16:20:00 | NPP-375 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 80.0 |
| 3f2fd924-eef8-3b7f-bd75-747150dc3627 | -4.50927 | -42.88713 | 2026-10-08 16:20:00 | NPP-375 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 7b972b7f-6e13-353c-b07a-2076e7f83917 | -5.7237 | -41.62358 | 2026-10-08 16:20:00 | NPP-375 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 6.3 |


[Clique aqui para ver as próximas entradas](README300.md)
