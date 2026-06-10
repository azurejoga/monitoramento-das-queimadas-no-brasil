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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 385f427c-5e3d-33bd-b599-d6d8b897dae2 | -9.3234 | -45.4787 | 2026-06-10 00:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 107.7 |
| c7f50722-7028-3058-a421-49ed86c91b61 | -7.1092 | -46.5065 | 2026-06-10 00:00:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 106.4 |
| ea6350db-22af-3e6b-8b31-17f3e45513fc | -13.5084 | -54.3012 | 2026-06-10 00:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 51.2 |
| 12cf46ea-807b-35c2-abe3-e6d66c39bf6a | -9.3149 | -48.9815 | 2026-06-10 00:00:00 | GOES-19 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 67.3 |
| 02ce2901-3852-38f0-8bad-db3d0fca2c9e | -9.3152 | -48.9599 | 2026-06-10 00:00:00 | GOES-19 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 69.4 |
| d4c4668b-a923-39bc-bf8d-c5dbf6a78845 | -7.109 | -46.5287 | 2026-06-10 00:00:00 | GOES-19 | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 64.9 |
| fe306ad9-764f-3adc-b79f-c12c0ec9d05d | -9.3045 | -45.4809 | 2026-06-10 00:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 120.7 |
| e044ad01-e14c-35b8-9957-d7b5cc7ecd8c | -12.4277 | -58.4642 | 2026-06-10 00:00:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 57.6 |
| 6ec35019-07d1-337e-aa7b-f28e11ddad66 | -9.3048 | -45.4581 | 2026-06-10 00:00:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 64.9 |
| 9451d1eb-6a03-3f3c-900e-fe570b9090e8 | -7.0905 | -46.508 | 2026-06-10 00:00:00 | GOES-19 | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 65.8 |
| f2e23e40-5f4c-3856-88cc-6086bc79ed0f | -10.0112 | -48.212299 | 2026-06-10 00:05:00 | METOP-B | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 13cc98a2-5407-3343-ad13-73a6944d1973 | -9.3037 | -45.4799 | 2026-06-10 00:05:00 | METOP-B | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| a04645c1-5487-3978-95e8-92f53121c5d0 | -8.2949 | -48.224701 | 2026-06-10 00:05:00 | METOP-B | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 47aeaf9d-cd07-3f0c-bec1-85dbc8bf20f8 | -3.5011 | -48.033401 | 2026-06-10 00:05:00 | METOP-B | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b1f7796b-d74c-3ad4-be3b-a572a5f922a4 | -9.7518 | -47.8773 | 2026-06-10 00:05:00 | METOP-B | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| abdd6b3c-4cb3-3922-a911-87b2ad2a3571 | -9.2986 | -45.458099 | 2026-06-10 00:05:00 | METOP-B | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 0f9739a0-7b69-36b1-96a2-b588a7af54f3 | -9.4498 | -47.630402 | 2026-06-10 00:05:00 | METOP-B | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| c5b97724-857a-382e-a908-a125e078e7a7 | -9.3003 | -45.465401 | 2026-06-10 00:05:00 | METOP-B | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 2710538d-0335-37c3-a6f9-a31c59d9a950 | -7.1015 | -46.496399 | 2026-06-10 00:05:00 | METOP-B | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| eb435fc3-433e-3bbd-81cf-48c54ee26a4f | -9.3135 | -45.477699 | 2026-06-10 00:05:00 | METOP-B | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 3f37f1b4-ab69-38e4-b35e-eb34336c1fda | -7.0948 | -46.5126 | 2026-06-10 00:05:00 | METOP-B | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 31c755b6-1245-36cd-8cc7-61f5f4b8d2ae | -12.8542 | -44.356998 | 2026-06-10 00:05:00 | METOP-B | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| a6676031-13ba-3f43-9aa6-ee5fb354f563 | -9.779 | -49.7379 | 2026-06-10 00:05:00 | METOP-B | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 97dbf3d6-21bc-3251-ae6e-f6d42928bfcb | -12.4995 | -46.3391 | 2026-06-10 00:05:00 | METOP-B | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 90dcccfc-953d-367c-8c33-c264c6bf5129 | -21.3256 | -48.5373 | 2026-06-10 00:05:00 | METOP-B | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| d4c59de6-5133-32c8-a501-7031978125e5 | -11.3833 | -47.808601 | 2026-06-10 00:05:00 | METOP-B | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 7da0cf9d-0413-3639-ae95-4e3c7c885701 | -5.7278 | -49.0886 | 2026-06-10 00:05:00 | METOP-B | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8b402967-190c-3afb-9683-7495c75f0300 | -12.0278 | -47.792 | 2026-06-10 00:05:00 | METOP-B | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 9e532302-f402-390f-aa93-6290533e3afe | -6.5654 | -47.9081 | 2026-06-10 00:05:00 | METOP-B | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 6206cf61-1a07-3cf9-b3f5-ca791bed3086 | -11.9876 | -47.374901 | 2026-06-10 00:05:00 | METOP-B | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| dc19ac81-d67c-3221-8c16-a9c52087993b | -11.0421 | -44.6922 | 2026-06-10 00:05:00 | METOP-B | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| e85816ab-8ef0-3af8-8c9e-68ea548692e9 | -9.2662 | -50.119499 | 2026-06-10 00:05:00 | METOP-B | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 20d99204-dcfd-39a2-a500-1fa6a344c510 | -9.3249 | -45.482601 | 2026-06-10 00:05:00 | METOP-B | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 72bb8bc6-0994-32c7-bd41-fd8bb94c3d3e | -9.3229 | -48.964901 | 2026-06-10 00:05:00 | METOP-B | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 19bc6718-e0d5-351a-b047-ff8da2c7c33c | -9.3115 | -48.959702 | 2026-06-10 00:05:00 | METOP-B | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| e9b7402b-5b9f-326c-94a0-301b37e555c6 | -5.3009 | -47.240501 | 2026-06-10 00:05:00 | METOP-B | JOÃO LISBOA | MARANHÃO | Brasil | 2105500 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| e744332e-b682-3063-a270-383b9c230b31 | -12.2034 | -41.520401 | 2026-06-10 00:05:00 | METOP-B | IRAQUARA | BAHIA | Brasil | 2914406 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 97a4e17b-80d8-35e9-aa56-7dd77b54a85d | -12.4137 | -47.487499 | 2026-06-10 00:05:00 | METOP-B | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 6c7fae34-b448-36ac-ba3b-d95f1ac71f89 | -15.1831 | -43.8428 | 2026-06-10 00:05:00 | METOP-B | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 4eb01cfe-8393-3a7a-b684-8d2792549be2 | -11.3849 | -47.815701 | 2026-06-10 00:05:00 | METOP-B | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| aea47475-b19f-3b6d-8ea9-ecfa5e78c307 | -12.4054 | -47.496799 | 2026-06-10 00:05:00 | METOP-B | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 0e50a8ca-812e-395e-ac61-b2db207861b7 | -7.2074 | -44.093899 | 2026-06-10 00:05:00 | METOP-B | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| e7cf3a9b-5e18-3b4a-8aa8-1e298d36bca7 | -9.3118 | -45.470402 | 2026-06-10 00:05:00 | METOP-B | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 7d0a2b50-86f3-38e3-a48f-b3455f0e1bf4 | -15.175 | -43.852699 | 2026-06-10 00:05:00 | METOP-B | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 2dbc604b-0c3c-3aee-8baf-8ae250b1bdf3 | -23.032101 | -44.219799 | 2026-06-10 00:05:00 | METOP-B | ANGRA DOS REIS | RIO DE JANEIRO | Brasil | 3300100 | 33 | 33 | nan | nan | nan | Mata Atlântica | nan |
| f647792d-c407-3266-bb24-c7a437d68036 | -6.3984 | -44.163898 | 2026-06-10 00:05:00 | METOP-B | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| db3ba94b-eb2a-30ba-bfe2-4ec526614720 | -5.7393 | -49.093498 | 2026-06-10 00:05:00 | METOP-B | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cc104bcd-cb6e-3704-92f5-092f5f96e664 | -6.9512 | -44.5439 | 2026-06-10 00:05:00 | METOP-B | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 24147808-991b-32e6-9283-e25ca1b4d9ac | -5.2994 | -47.233601 | 2026-06-10 00:05:00 | METOP-B | JOÃO LISBOA | MARANHÃO | Brasil | 2105500 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 32ab75ad-3899-350b-80ca-ee6031c8b503 | -9.2251 | -48.567101 | 2026-06-10 00:05:00 | METOP-B | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 5bb1115e-4650-353d-b86a-32199fa40b53 | -7.2115 | -44.111099 | 2026-06-10 00:05:00 | METOP-B | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 8cbc55cd-514f-3608-be84-ea34045f39a1 | -15.1733 | -43.8452 | 2026-06-10 00:05:00 | METOP-B | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 39ac0da8-b41a-331a-a672-947a241e19d6 | -9.3131 | -48.967098 | 2026-06-10 00:05:00 | METOP-B | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 8a26ea19-ded5-3eea-9b6c-ddf703dc7835 | -11.992 | -45.142799 | 2026-06-10 00:05:00 | METOP-B | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 1dbec94d-4074-3eda-b98a-cc8420e99f5b | -12.8576 | -44.372002 | 2026-06-10 00:05:00 | METOP-B | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| ff049e6d-112f-3c04-b5a1-9e2e550a1c06 | -6.5752 | -47.905899 | 2026-06-10 00:05:00 | METOP-B | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 0a10a1a0-4a92-3cdb-9100-2264678669af | -9.2169 | -48.576401 | 2026-06-10 00:05:00 | METOP-B | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 9dce86a7-6c59-32d5-a960-c94abf11d4b0 | -5.6328 | -44.286301 | 2026-06-10 00:05:00 | METOP-B | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 69cc978e-11f9-32c2-b984-db64d3999793 | -7.2095 | -44.102501 | 2026-06-10 00:05:00 | METOP-B | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 656d1598-d0d9-3abf-ae1c-c18eb11fa3c8 | -8.981 | -47.976398 | 2026-06-10 00:05:00 | METOP-B | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 2965df35-b266-394d-a617-031d8eead359 | -5.7691 | -46.0378 | 2026-06-10 00:05:00 | METOP-B | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a51f5276-3687-3878-a545-6b083b4dc3fa | -9.1458 | -47.9762 | 2026-06-10 00:05:00 | METOP-B | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 31955d97-8c13-3e48-93ca-6acc3897a2b8 | -23.440901 | -47.7752 | 2026-06-10 00:05:00 | METOP-B | TATUÍ | SÃO PAULO | Brasil | 3554003 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 6c3fcf4e-4924-33d6-af6f-d329ce7c962c | -11.1631 | -44.679501 | 2026-06-10 00:05:00 | METOP-B | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| da2011b3-129a-371e-8971-40ab09d8a889 | -9.7503 | -47.8703 | 2026-06-10 00:05:00 | METOP-B | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 2e2d5edc-1b0c-3419-acee-35238f223405 | -15.1848 | -43.8503 | 2026-06-10 00:05:00 | METOP-B | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 11dc866e-ae1e-37a8-b9fa-15434367ff76 | -6.9629 | -44.549801 | 2026-06-10 00:05:00 | METOP-B | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| fe3cc5a6-88c2-3cbe-960b-6f377d23bf72 | -9.302 | -45.472599 | 2026-06-10 00:05:00 | METOP-B | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 07444e8e-5acf-3a34-b93e-261afa72c64d | -3.5109 | -48.0312 | 2026-06-10 00:05:00 | METOP-B | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| adb2ae85-9366-34a8-a726-a039c0b0485a | -12.4152 | -47.494598 | 2026-06-10 00:05:00 | METOP-B | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 6584a279-b3ff-3e2d-b403-c696c2cf707c | -7.7582 | -47.575802 | 2026-06-10 00:05:00 | METOP-B | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 78aedb44-6a6e-34ed-ad43-6e42bd7b4523 | -12.8559 | -44.364498 | 2026-06-10 00:05:00 | METOP-B | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| b1b8b874-2024-3372-a36c-6d1fdc517f5e | -6.3886 | -44.166199 | 2026-06-10 00:05:00 | METOP-B | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f23774d0-ec75-3388-9403-1bb25510fc85 | -14.3755 | -45.557201 | 2026-06-10 00:05:00 | METOP-B | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 41f77ce3-9890-3c29-bc60-cd23c51fa4bf | -9.2236 | -48.559898 | 2026-06-10 00:05:00 | METOP-B | RIO DOS BOIS | TOCANTINS | Brasil | 1718709 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| b049a964-12a8-3ad5-b2f0-c123404d380c | -10.4873 | -46.420601 | 2026-06-10 00:05:00 | METOP-B | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| e7984ca1-d02a-329d-9a08-d0d070a42eab | -7.1047 | -46.510399 | 2026-06-10 00:05:00 | METOP-B | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 0bdbab4e-a800-3644-900b-1ae69c3482b8 | -9.4416 | -47.6395 | 2026-06-10 00:05:00 | METOP-B | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| c01a23e5-19e9-3dfc-b2b5-18e586df4fa0 | -5.7593 | -46.040001 | 2026-06-10 00:05:00 | METOP-B | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 5f0ad155-45b8-3652-b58e-8ddc99c5cdba | -13.5034 | -54.2878 | 2026-06-10 00:05:00 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 97205d20-5060-3d98-9249-d7b1f64230fa | -5.7377 | -49.086498 | 2026-06-10 00:05:00 | METOP-B | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0ba9653d-898d-30a7-8d1b-03482b9f8bee | -12.0294 | -47.799198 | 2026-06-10 00:05:00 | METOP-B | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| c2b1a4ae-9eef-30f1-ab28-ab429cfb2e33 | -6.4005 | -44.1726 | 2026-06-10 00:05:00 | METOP-B | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d3dba6e8-ac65-3e85-a574-b9966a446be9 | -9.1473 | -47.9832 | 2026-06-10 00:05:00 | METOP-B | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 695d804a-83d1-36e4-b9cd-ecb77926ee20 | -9.3213 | -48.9575 | 2026-06-10 00:05:00 | METOP-B | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 23c65517-a82e-3cea-97b9-8649d66843b9 | -11.0404 | -44.6847 | 2026-06-10 00:05:00 | METOP-B | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| cad75a81-f9f0-3ea5-a55d-5a5ab771aa3a | -23.442699 | -47.784801 | 2026-06-10 00:05:00 | METOP-B | TATUÍ | SÃO PAULO | Brasil | 3554003 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 42d16933-7662-327c-bb18-b8c8d039ad23 | -3.5094 | -48.024399 | 2026-06-10 00:05:00 | METOP-B | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 85ae1290-5e51-367c-badb-85b7e725ec9c | -5.7294 | -49.0956 | 2026-06-10 00:05:00 | METOP-B | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| facacab8-bcd1-35dc-8329-a5da68ee8b08 | -7.1063 | -46.517502 | 2026-06-10 00:05:00 | METOP-B | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 95b729cf-1f03-39c6-b0a6-dd67c47557fc | -9.44 | -47.632599 | 2026-06-10 00:05:00 | METOP-B | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| d69bc13c-254a-3a6c-b298-fc3001099b1a | -5.6348 | -44.295101 | 2026-06-10 00:05:00 | METOP-B | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 704569ee-c9e2-319b-b38a-db3a3c78fde9 | -8.3063 | -48.2295 | 2026-06-10 00:05:00 | METOP-B | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 23c1ee63-1564-3d05-b91c-a3c156a2eb47 | -7.1603 | -44.0686 | 2026-06-10 00:05:00 | METOP-B | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 55771e4b-66a8-3d70-9431-f0c6ce3118ee | -6.3907 | -44.1749 | 2026-06-10 00:05:00 | METOP-B | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 0fef90b9-a110-3bd7-9304-cd77b491ebbb | -17.4244 | -43.799702 | 2026-06-10 00:05:00 | METOP-B | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| fbb85433-1c6a-3b0d-a5b3-dc7ebc1d521b | -21.3237 | -48.5275 | 2026-06-10 00:05:00 | METOP-B | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| c41ddcbc-6187-394b-bd2d-db8bcb2508bf | -7.1583 | -44.059898 | 2026-06-10 00:05:00 | METOP-B | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 8b206a7f-ab66-34b0-8792-5220eecf9b78 | -6.9531 | -44.552101 | 2026-06-10 00:05:00 | METOP-B | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 034bda40-e0e9-3665-95cc-205f9c7d9f2b | -11.1648 | -44.687 | 2026-06-10 00:05:00 | METOP-B | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README2.md)
