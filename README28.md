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

## Dados Diários - Página 28

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 242928e5-d0f7-3855-8c3c-895765bdd2d1 | -13.56261 | -44.45565 | 2025-08-19 04:27:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6c774402-7f18-3848-a2d2-768e03292f37 | -13.63232 | -46.88997 | 2025-08-19 04:27:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f4a5fe90-b539-3189-9e61-4cd546d318f3 | -13.01715 | -56.82791 | 2025-08-19 04:27:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| fddb225a-27a5-37a8-8017-b3a0d90d35cc | -12.95429 | -46.12556 | 2025-08-19 04:27:00 | NOAA-21 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5d5a48d2-1dd5-368f-ba7c-a827f6574a12 | -12.98188 | -56.86203 | 2025-08-19 04:27:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 7e1d55a5-a109-36bd-a11a-7e22e9fd776a | -13.00208 | -56.85061 | 2025-08-19 04:27:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1097515e-a41b-3daf-b950-5b6055c40a48 | -12.64501 | -45.80421 | 2025-08-19 04:27:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e55f0f4e-2d7a-3e66-a33b-e76c7e1442f6 | -8.23583 | -47.85764 | 2025-08-19 04:27:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9b197822-ebc9-3c10-af07-6be4766d4bcb | -6.63372 | -55.27404 | 2025-08-19 04:27:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3c3999d4-dc72-3934-bdef-03c899dd7efe | -13.1369 | -57.16025 | 2025-08-19 04:27:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 2f06f97b-19a7-3968-9001-d0c097697278 | -13.25862 | -50.813 | 2025-08-19 04:27:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 3d899bda-996d-31c1-8cec-e03b21590912 | -13.1333 | -57.15034 | 2025-08-19 04:27:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| dd226484-9be3-36e3-b9f9-88dc2dae8ec8 | -13.00226 | -45.19749 | 2025-08-19 04:27:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0e1db3fb-1b8d-3fbe-a2bd-5538018c987b | -8.81683 | -52.03552 | 2025-08-19 04:27:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 0772e4e9-223f-3cf3-ac1f-c126628f1a74 | -12.98612 | -56.85046 | 2025-08-19 04:27:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f3965c38-05a6-3b68-b388-0436f96b0906 | -12.73288 | -45.0602 | 2025-08-19 04:27:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4a091608-1833-3e16-8b03-d7c6c27560e5 | -12.99182 | -45.19328 | 2025-08-19 04:27:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 7d1a09e3-e544-38d3-ade0-3a7180cc724e | -8.22652 | -47.29204 | 2025-08-19 04:27:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3828b220-da85-3ce1-9ee9-f7e287ffcdab | -12.99247 | -56.84527 | 2025-08-19 04:27:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| dab3e093-1f34-3e83-8de1-2a1d02e4b664 | -8.23817 | -47.86147 | 2025-08-19 04:27:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 758892fc-ebf8-3fcd-ac37-c3c76fd6b9fc | -13.16959 | -54.93246 | 2025-08-19 04:27:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 281c7217-0e0e-3f26-bd20-1253bb76e4a4 | -12.51088 | -45.59561 | 2025-08-19 04:27:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2747d150-3403-3df6-9be7-ba2aea8f6370 | -12.96519 | -46.14965 | 2025-08-19 04:27:00 | NOAA-21 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d470209e-c600-36ac-a88c-5c220268b170 | -13.47945 | -47.06877 | 2025-08-19 04:27:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d3dbdd81-e613-392f-953b-3ee3866c3d80 | -12.4295 | -48.70087 | 2025-08-19 04:27:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 51b63c50-06cf-376f-9ee3-b4c0b67ca68d | -14.86607 | -48.04326 | 2025-08-19 04:27:00 | NOAA-21 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1d81ee3f-ad4e-3730-bc8e-c20f77682f61 | -12.09815 | -47.91344 | 2025-08-19 04:27:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6638d321-4a52-3734-ab95-4e6c062c782d | -13.22831 | -50.82031 | 2025-08-19 04:27:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8386abd8-f255-322f-bdf8-cd7ba9ad1fbb | -13.46849 | -47.05618 | 2025-08-19 04:27:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| df898d11-309e-3cab-81a3-10f6d5c35fc1 | -12.96079 | -46.17942 | 2025-08-19 04:27:00 | NOAA-21 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 1ecbadf3-ea4f-3cd2-9be8-17ee1b0c6225 | -12.0093 | -44.79088 | 2025-08-19 04:27:00 | NOAA-21 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 39da37b8-fad5-3f2c-8b80-0e81a99c8f19 | -11.58057 | -44.85547 | 2025-08-19 04:27:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 95076225-20f3-3abd-88fd-c5eb364ca0d3 | -13.29881 | -50.8116 | 2025-08-19 04:27:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 878809b7-4db6-36ff-a9c4-9b47efd94805 | -13.15693 | -54.92526 | 2025-08-19 04:27:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3abe3c1e-fc3c-3ab1-92bd-06af16de6cdf | -13.16697 | -54.94659 | 2025-08-19 04:27:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d63881ad-bfc8-3e82-9758-52d82f74e08a | -11.57704 | -44.85492 | 2025-08-19 04:27:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 390c4761-7190-3fe8-98b3-c94c1642a973 | -13.13888 | -57.1503 | 2025-08-19 04:27:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8c127726-f36e-300c-aa4a-bb529fb93339 | -13.14892 | -57.15374 | 2025-08-19 04:27:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0ccc1f12-cb70-384c-b114-5a08025cbd32 | -14.17054 | -45.31677 | 2025-08-19 04:27:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7b665beb-1979-38f2-ab02-e03d0e6c0ff5 | -12.63955 | -46.89659 | 2025-08-19 04:27:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 096103e6-0766-3b70-8469-7b4ea2a70407 | -9.17206 | -59.61483 | 2025-08-19 04:27:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| d7323101-53de-3778-a328-10e62033a15c | -13.62508 | -46.89252 | 2025-08-19 04:27:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 54bd3037-58dd-3eec-ad13-298e5393d1af | -7.44383 | -48.95026 | 2025-08-19 04:27:00 | NOAA-21 | PAU D'ARCO | TOCANTINS | Brasil | 1716307 | 17 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c18c9268-1d79-3cbe-b1ee-3e0272d6bce8 | -12.9864 | -56.86631 | 2025-08-19 04:27:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5b594cb0-74bf-3f18-86a1-3a3b59fafbce | -12.7791 | -41.25014 | 2025-08-19 04:27:00 | NOAA-21 | ANDARAÍ | BAHIA | Brasil | 2901304 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| eae5d366-67b8-36bb-8403-e5069568dbcd | -12.99051 | -45.20399 | 2025-08-19 04:27:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 3cb8ce1d-e848-3ba6-9471-3a8f764ad87d | -13.01144 | -56.8299 | 2025-08-19 04:27:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0861eab1-554a-3700-8616-ce93b0a7989e | -13.22899 | -50.81624 | 2025-08-19 04:27:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8a2cfc91-c30e-3783-9079-41d31b59064d | -15.40271 | -43.06804 | 2025-08-19 04:27:00 | NOAA-21 | CATUTI | MINAS GERAIS | Brasil | 3115474 | 31 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 9bec0e21-6d66-382a-85ad-1401b1fbaa9e | -9.34225 | -48.50894 | 2025-08-19 04:27:00 | NOAA-21 | RIO DOS BOIS | TOCANTINS | Brasil | 1718709 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a0b15f0e-ca25-3bae-b49b-83f3593600d4 | -12.6622 | -45.80681 | 2025-08-19 04:27:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| bbe6af0c-3434-31fa-8b33-f32c5d9f86ce | -14.51088 | -45.94063 | 2025-08-19 04:27:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 968828a3-837f-3b5e-bebe-6c09f87852e4 | -11.85931 | -51.58392 | 2025-08-19 04:27:00 | NOAA-21 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 29e9d192-96b8-333c-a72d-2157206cb825 | -13.16333 | -54.94103 | 2025-08-19 04:27:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 14.1 |
| 87704acb-fca2-3747-a9f3-0b00fec1ff26 | -13.58892 | -47.0014 | 2025-08-19 04:27:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e8cca96a-ea36-364e-8166-34ec18a2cc4c | -12.1009 | -47.91749 | 2025-08-19 04:27:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 96ae7770-bf87-3950-9450-b68b99459b4a | -13.59109 | -46.98716 | 2025-08-19 04:27:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c6755bff-ed05-36fb-8b5c-9c99c74d5383 | -6.63318 | -55.27716 | 2025-08-19 04:27:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b60131b5-33f1-3d3c-ab73-4317f187a2ad | -14.50483 | -45.94482 | 2025-08-19 04:27:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| dadf6d9c-963b-359c-92e5-8c757309d28c | -14.52326 | -42.21269 | 2025-08-19 04:27:00 | NOAA-21 | CACULÉ | BAHIA | Brasil | 2905008 | 29 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 166e531a-6c39-3d26-9291-b96a661e67d8 | -8.8277 | -52.04449 | 2025-08-19 04:27:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a1e72cb4-d32d-34b3-8e47-6c8fd936b4aa | -12.9957 | -56.84519 | 2025-08-19 04:27:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2aee09fb-d963-392d-bf75-e85f7a276bed | -12.77762 | -41.24826 | 2025-08-19 04:27:00 | NOAA-21 | ANDARAÍ | BAHIA | Brasil | 2901304 | 29 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 803feeb5-d367-39e1-a5e4-4174e7ae9bb3 | -13.81119 | -44.19648 | 2025-08-19 04:27:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 726b9753-4b74-3126-abc6-1099966280f8 | -12.97913 | -56.84835 | 2025-08-19 04:27:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 2cceaa63-43ac-3ba0-a434-fb2960b200e2 | -11.85262 | -51.57798 | 2025-08-19 04:27:00 | NOAA-21 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7ca0584c-605c-3f02-a8af-ddf11f97ec7a | -9.17875 | -59.64602 | 2025-08-19 04:27:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 6629a093-db7e-3119-a40f-548c47b97759 | -13.14212 | -57.1613 | 2025-08-19 04:27:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 78576f88-c938-34ec-8711-309aedaee1a2 | -13.43101 | -45.90908 | 2025-08-19 04:27:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c8b6d066-25d0-36a3-80df-7ef532d745b5 | -14.86222 | -48.06816 | 2025-08-19 04:27:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 4b2fabf1-2c6a-3ba1-8230-61120ad467ac | -12.11689 | -47.90205 | 2025-08-19 04:27:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 08236365-a927-3801-947d-40db282e211b | -13.00841 | -56.84546 | 2025-08-19 04:27:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8182dc4d-3e18-3e61-a5a6-d3efda60f2f4 | -14.50541 | -45.94089 | 2025-08-19 04:27:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b92041e8-ee13-3981-8dc0-51458203ff10 | -13.56779 | -47.00526 | 2025-08-19 04:27:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f7787cad-0a99-3a35-add6-03a40a762f6a | -11.44792 | -47.32996 | 2025-08-19 04:27:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5028a1ed-3b2e-3dd9-9724-02925711b483 | -10.03376 | -59.35833 | 2025-08-19 04:27:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 015a09f4-8e93-396c-914f-0010e86619d0 | -14.17892 | -45.32982 | 2025-08-19 04:27:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3662c58a-1291-3d69-a501-8c9272cc214c | -12.9785 | -56.86209 | 2025-08-19 04:27:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9c0d2fbb-2ee2-36ca-9aec-e9e86000b4a9 | -14.84678 | -48.05833 | 2025-08-19 04:27:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 99b3ec8c-a8ab-3e1c-bfe7-aed1c49e1ea6 | -14.86167 | -48.07172 | 2025-08-19 04:27:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 94991306-cd83-3d1d-890e-410ad349f7c0 | -14.17118 | -45.30752 | 2025-08-19 04:27:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9b85c297-fe83-33c9-b1ca-62a2ab38f945 | -13.15416 | -54.91507 | 2025-08-19 04:27:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 519fe4ab-6afb-3f2c-84d3-2882ea2d7e35 | -11.58981 | -49.01254 | 2025-08-19 04:27:00 | NOAA-21 | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a511c288-06a7-3e0d-a44a-7b7a1647f79e | -13.14472 | -57.14818 | 2025-08-19 04:27:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 91c8cab5-f04e-388c-9a80-3e1995f07665 | -12.99282 | -45.18776 | 2025-08-19 04:27:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d3a8c3ac-637c-3d63-9284-7c29ad15dc12 | -14.86939 | -48.0657 | 2025-08-19 04:27:00 | NOAA-21 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 765837e5-7a59-3999-96a6-ec52fb3065a8 | -12.51031 | -45.59947 | 2025-08-19 04:27:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7ba961d4-9bc6-30a5-9f6b-1242e59f06c3 | -11.45287 | -47.31996 | 2025-08-19 04:27:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 21c7579d-22f9-31bb-957b-2039f0633c26 | -13.14927 | -57.15259 | 2025-08-19 04:27:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9f8215bb-4550-3ecf-9ad5-feac16beeda8 | -13.62229 | -46.88817 | 2025-08-19 04:27:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e9118935-1b68-3e57-b75e-a1188268f425 | -13.60942 | -46.8896 | 2025-08-19 04:27:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 20811aa7-5cb6-320c-8768-96124ca871fa | -12.64789 | -45.04867 | 2025-08-19 04:27:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d6619061-d145-346b-ae9b-628950ee99fa | -10.03477 | -59.35309 | 2025-08-19 04:27:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1f41d6d5-4bde-31f9-8f16-927fc5d43dc6 | -12.8867 | -46.08795 | 2025-08-19 04:27:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a061eaf4-7b72-358c-930e-1dc956f325f9 | -12.99815 | -45.20102 | 2025-08-19 04:27:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2b53b1ad-ae87-3e1f-8895-564e6a1dbd1c | -8.71519 | -47.85827 | 2025-08-19 04:27:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a47a1241-920f-3f38-b227-f370d20821f9 | -14.87214 | -48.04788 | 2025-08-19 04:27:00 | NOAA-21 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 219371b9-560a-376f-bab9-61092387a084 | -13.25645 | -50.80426 | 2025-08-19 04:27:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| bd90d509-d591-3736-bb4d-993d00dd4804 | -9.20066 | -59.63803 | 2025-08-19 04:27:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| eefa0a64-83b1-3fee-8aa8-6f40b220ee65 | -13.31695 | -50.7897 | 2025-08-19 04:27:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |


[Clique aqui para ver as próximas entradas](README29.md)
