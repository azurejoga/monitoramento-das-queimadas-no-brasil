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

## Dados Diários - Página 96

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 84deddae-ad30-37be-a68b-7fd82e587317 | -10.51907 | -49.10802 | 2024-10-09 04:17:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 33244020-f2d1-333e-9b10-da3de8f7d61c | -11.69753 | -49.95956 | 2024-10-09 04:17:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b926a67f-3e2e-395a-a9d5-2a27d9e339b5 | -11.69685 | -49.96341 | 2024-10-09 04:17:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4334cef3-a97e-37c4-8b6f-9795ccf00560 | -11.55931 | -49.90758 | 2024-10-09 04:17:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 32739419-e94c-3d06-bd3c-643fa22e9fe8 | -11.55516 | -49.90683 | 2024-10-09 04:17:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| baaef1a6-b09e-3a50-8913-c1af1b3af648 | -11.55447 | -49.91067 | 2024-10-09 04:17:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 78d3dd56-c980-3067-80e1-7ed1a12f107b | -11.47407 | -49.49124 | 2024-10-09 04:17:00 | NOAA-21 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 05591776-7b86-3ef3-a5d1-1885c1f615bc | -11.47066 | -49.48687 | 2024-10-09 04:17:00 | NOAA-21 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b9ed0808-f19f-3fe1-969a-ce46f846e5ff | -11.47003 | -49.4905 | 2024-10-09 04:17:00 | NOAA-21 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 02bd67d3-3887-3202-9f0c-cf9ca7c83957 | -11.15061 | -49.7317 | 2024-10-09 04:17:00 | NOAA-21 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| eb8326be-9b51-3d1c-9dee-5bf810d8f23e | -12.22576 | -50.44079 | 2024-10-09 04:17:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 534a0349-6fb6-3089-8a59-3dfe0081c21e | -12.19531 | -50.58348 | 2024-10-09 04:17:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a3f47655-d5ed-344d-9eeb-f7302f83c91d | -12.19455 | -50.58763 | 2024-10-09 04:17:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7bb75cf4-0ed1-3905-a89a-58f8bec2a98f | -13.70177 | -49.85686 | 2024-10-09 04:17:00 | NOAA-21 | AMARALINA | GOIÁS | Brasil | 5200829 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a3942bfc-5b80-35f2-955b-27b1c888af76 | -13.18483 | -51.17555 | 2024-10-09 04:17:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7b8cf19f-a4b9-3788-8ad6-dcdcc3102691 | -12.32401 | -50.94434 | 2024-10-09 04:17:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| f7fc27d3-26bd-38c6-8831-00aaab394d6e | -12.32245 | -50.95308 | 2024-10-09 04:17:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 4168fc9e-70d9-3fc6-82cb-57bcd6d10ff0 | -12.31807 | -50.95225 | 2024-10-09 04:17:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| f6ff6fd7-d6de-3a88-b597-95ed4b8a5f05 | -12.31602 | -50.93835 | 2024-10-09 04:17:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d68a2bf8-08ef-3791-b27e-1d40e6f7eab1 | -14.03415 | -50.56004 | 2024-10-09 04:17:00 | NOAA-21 | NOVA CRIXÁS | GOIÁS | Brasil | 5214838 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1a71edaa-b690-3fd6-9610-61c4b5af4163 | -14.10825 | -51.09065 | 2024-10-09 04:17:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 76f8417a-b974-3d36-81ef-0a080d152341 | -14.10473 | -51.08565 | 2024-10-09 04:17:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 29.6 |
| bde7b3e8-c330-31db-b93f-88fbcbec5f7f | -14.10396 | -51.08984 | 2024-10-09 04:17:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 27.5 |
| 9fd46b54-20a7-32af-8c8d-876ebf939e6c | -14.10044 | -51.08485 | 2024-10-09 04:17:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 29.6 |
| 85a7611f-6d1a-3574-8cd3-0268055fd84a | -14.09967 | -51.08903 | 2024-10-09 04:17:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 27.5 |
| 9d2028fe-8a88-3a5d-8deb-deef0d41f0ae | -14.0989 | -51.09321 | 2024-10-09 04:17:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 27.5 |
| ea9b042b-fb46-3ac9-aa5b-b6de18a05d49 | -14.09813 | -51.09739 | 2024-10-09 04:17:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e7d0d26f-1a77-382e-810c-59aaf0f2441b | -14.09538 | -51.08821 | 2024-10-09 04:17:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 14.9 |
| 141c0fb8-785f-3e0a-82fb-9ebcf99d89d1 | -14.09461 | -51.09239 | 2024-10-09 04:17:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 14.9 |
| 85d9171a-0276-391c-8da7-c39a97264fcb | -14.09384 | -51.09658 | 2024-10-09 04:17:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 94faba67-7556-3b97-b00d-00bfe3d736f0 | -14.09307 | -51.10077 | 2024-10-09 04:17:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 13.2 |
| de647e5c-70c1-32a4-8973-cf74111a1ef4 | -14.0923 | -51.10495 | 2024-10-09 04:17:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 86a4075f-4f9c-396f-ade5-b33c75945b14 | -14.09152 | -51.10915 | 2024-10-09 04:17:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 165f6168-6a2f-3c5d-932a-4ad09f133612 | -14.09075 | -51.11335 | 2024-10-09 04:17:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| dd1fdb87-9178-33d3-904e-a6ddfacc6e49 | -14.08877 | -51.09995 | 2024-10-09 04:17:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 13.2 |
| a0134544-bef8-30eb-bda3-46ff39b240fa | -14.088 | -51.10414 | 2024-10-09 04:17:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 71fb6dcb-6ed9-332d-bdcd-0d2fd86a70b7 | -15.08526 | -51.23238 | 2024-10-09 04:17:00 | NOAA-21 | BRITÂNIA | GOIÁS | Brasil | 5203807 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 39c51997-8e7f-3b82-aefe-877db16fd2ba | -15.08176 | -51.22745 | 2024-10-09 04:17:00 | NOAA-21 | BRITÂNIA | GOIÁS | Brasil | 5203807 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 54200f29-84fc-349b-8ceb-34b3a7880eed | -19.81652 | -52.24029 | 2024-10-09 04:17:00 | NOAA-21 | INOCÊNCIA | MATO GROSSO DO SUL | Brasil | 5004403 | 50 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 85bbc76f-3692-3446-b753-0122010863de | -19.81159 | -52.24343 | 2024-10-09 04:17:00 | NOAA-21 | INOCÊNCIA | MATO GROSSO DO SUL | Brasil | 5004403 | 50 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 2157ad73-7b63-3b16-b833-1c6676ce1eae | -20.9973 | -51.79443 | 2024-10-09 04:17:00 | NOAA-21 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 3e9cba9d-4260-347c-8d5a-3657a0dc1671 | -19.81574 | -52.24443 | 2024-10-09 04:17:00 | NOAA-21 | INOCÊNCIA | MATO GROSSO DO SUL | Brasil | 5004403 | 50 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 2cb05dc1-77c2-3745-940e-b4d58d7b0316 | -9.03267 | -51.51824 | 2024-10-09 04:17:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b14dc6a3-e7ce-3e2a-a0bb-bd19697df2d3 | -8.5415 | -51.37 | 2024-10-09 04:17:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 20e55e71-e38c-3e94-bbc0-032bb99545ba | -9.25115 | -50.36229 | 2024-10-09 04:17:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d2716b42-5b5e-33d2-955d-0786a68507b3 | -9.25037 | -50.36678 | 2024-10-09 04:17:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 492b860d-c02c-31ec-bb66-7f2103a7d484 | -8.56503 | -50.53304 | 2024-10-09 04:17:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 32dbd23e-7fbf-35b1-9edb-e22fbbb6a613 | -8.5613 | -50.5276 | 2024-10-09 04:17:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1fea13b8-261c-3d94-a47d-a920173846d2 | -8.56048 | -50.53224 | 2024-10-09 04:17:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7510659c-b291-3861-9d42-eb280f654eed | -10.66838 | -51.53227 | 2024-10-09 04:17:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| aeab17ae-48bb-3507-858e-8c17cd65a031 | -10.66664 | -51.81507 | 2024-10-09 04:17:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| dcedbfdb-3f8e-3aff-b5fe-f1b52b543e1a | -10.66621 | -51.81696 | 2024-10-09 04:17:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 7e58a3cd-ac19-3124-bcb4-3d9bdacd1f48 | -10.66125 | -50.91466 | 2024-10-09 04:17:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 51330e61-5ea9-3eb7-b4e5-ed7deacc21b9 | -10.66042 | -50.91925 | 2024-10-09 04:17:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 5.1 |
| f158047b-f363-30d7-953c-914f828aa37d | -10.65592 | -50.91844 | 2024-10-09 04:17:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 9b178098-ac6e-3a07-bffa-b4525d163ec1 | -10.65059 | -50.92222 | 2024-10-09 04:17:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c44a69d7-276e-3357-a259-79bd35c0ec3a | -10.64608 | -50.9214 | 2024-10-09 04:17:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a148ef74-6ccd-3c18-bcec-b1a0bcdcf778 | -10.61821 | -50.92112 | 2024-10-09 04:17:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6a1bb81c-fb30-34dd-9a0e-3e6c1a9fc875 | -12.0208 | -51.0649 | 2024-10-09 04:17:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 97d928ad-ed7f-39e5-b3e3-1150e9ae7407 | -12.01636 | -51.06409 | 2024-10-09 04:17:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a8581d2d-02b7-3188-9fcd-3365494ae773 | -12.01077 | -51.04457 | 2024-10-09 04:17:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| fed957a4-381a-3ee8-a655-3bf5ed8b2a44 | -18.10911 | -56.3955 | 2024-10-09 04:17:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 93fbef87-2ad4-359e-b8a3-a799fbba8377 | -18.10826 | -56.39947 | 2024-10-09 04:17:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 4517a921-d5a5-3e9f-8d1c-911778116014 | -12.00994 | -51.04905 | 2024-10-09 04:17:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| a4ab7d11-61fa-376e-85ac-a5bd89f96888 | -12.00633 | -51.04377 | 2024-10-09 04:17:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| de1eb479-6b74-3e2c-bdd0-2e8fe73e463d | -12.005 | -51.0759 | 2024-10-09 04:17:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 8009e59b-e4c1-3983-9898-893c296f80d2 | -12.00418 | -51.08038 | 2024-10-09 04:17:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 0b3aa24d-7bdc-37ef-b73d-5e567db1c513 | -12.00189 | -51.04295 | 2024-10-09 04:17:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f4ca24be-86f3-3f2d-ab3c-266de1077697 | -12.00107 | -51.0474 | 2024-10-09 04:17:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| f6c589d1-e98a-3928-9351-06ee451bf511 | -12.00056 | -51.07507 | 2024-10-09 04:17:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 11.6 |
| b17593c1-ffa9-3c9a-84a1-a558b738238a | -11.99973 | -51.07955 | 2024-10-09 04:17:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 99eef7f5-9826-35a7-a90f-05ca61dbed38 | -11.99699 | -51.05202 | 2024-10-09 04:17:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 2056bbbf-59c2-3c06-8bdb-6ac7fcbbea1e | -11.9962 | -51.0565 | 2024-10-09 04:17:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ef16cf2d-20e0-3b18-ab89-1e01a03da480 | -11.99581 | -51.05104 | 2024-10-09 04:17:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 484a5ede-c2f7-3110-9786-18585bebf95a | -11.99498 | -51.05552 | 2024-10-09 04:17:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| c07462c2-8849-3a33-a43a-e661bc776e56 | -11.99096 | -51.06016 | 2024-10-09 04:17:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c1f02e9a-6e24-3d8d-be6d-e27445b3117b | -11.98891 | -51.0459 | 2024-10-09 04:17:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a736da25-5d84-39e6-a3fd-854c4842bf2f | -11.98693 | -51.04942 | 2024-10-09 04:17:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 128b6494-1eed-309b-94d6-d33cf15eb255 | -11.98367 | -51.04955 | 2024-10-09 04:17:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 85e1b9a7-2a8d-32f4-b656-c042135d19c5 | -11.98128 | -51.06298 | 2024-10-09 04:17:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 268eea63-b7f1-3bf0-bddb-5805e85f24d9 | -11.98048 | -51.06747 | 2024-10-09 04:17:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 47f943a1-4cb6-389f-8b78-a22f67636a75 | -11.98 | -51.062 | 2024-10-09 04:17:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 642cef03-7916-3f3e-98e1-5985eb8c0e2b | -11.97968 | -51.07196 | 2024-10-09 04:17:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 19.4 |
| 65e63c90-304c-34e6-8dbd-e61ef45102ee | -11.97916 | -51.06649 | 2024-10-09 04:17:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 9.0 |
| cc0b9134-fbd0-3403-a7b0-5eacb6328e91 | -11.97888 | -51.07645 | 2024-10-09 04:17:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 19.4 |
| 2c88413b-c691-3ed9-9b8b-9264997f92ba | -11.97833 | -51.07097 | 2024-10-09 04:17:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 22.4 |
| 7dbda60d-d0ca-3d3b-b9f3-ff244f8ee44c | -11.9775 | -51.07545 | 2024-10-09 04:17:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 22.4 |
| 6214a8b7-7372-34c4-b8d3-97baffd5551d | -11.97684 | -51.06216 | 2024-10-09 04:17:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| dedbcfb4-1729-393b-ae74-1a4c3e1de4da | -11.97604 | -51.06665 | 2024-10-09 04:17:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e4f0bec9-916c-3377-8f5a-14d6638d766d | -11.97523 | -51.07113 | 2024-10-09 04:17:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4d13ebbc-b46d-3276-95fe-bd8c0e7c61fa | -11.35509 | -51.00739 | 2024-10-09 04:17:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 09374e40-aeaf-3886-969e-17501504a665 | -11.35425 | -51.01194 | 2024-10-09 04:17:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2c795712-c607-3eb6-9311-8b7bc60e5f6d | -11.3519 | -51.01216 | 2024-10-09 04:17:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ada2fb1d-9918-3cc4-96d2-97d75db29a30 | -11.35109 | -51.01672 | 2024-10-09 04:17:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0af88a82-f059-324f-a2ab-b3416d6d7a93 | -11.34893 | -51.01568 | 2024-10-09 04:17:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 66e29a5c-8439-3bea-b927-8d48cc84af1e | -11.32784 | -50.96548 | 2024-10-09 04:17:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d8f0d8ef-4f1a-3e54-a90f-0d4ac6a6adef | -11.32704 | -50.97001 | 2024-10-09 04:17:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b27e1d86-a4a7-3e13-923a-e954abb7e190 | -11.32338 | -50.96466 | 2024-10-09 04:17:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 195323c8-9a19-3d20-a4d4-1d59bc5dc355 | -11.31757 | -51.3133 | 2024-10-09 04:17:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3db67366-9a52-36bb-b109-cfe89430b2f7 | -11.31669 | -51.3181 | 2024-10-09 04:17:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |


[Clique aqui para ver as próximas entradas](README97.md)
