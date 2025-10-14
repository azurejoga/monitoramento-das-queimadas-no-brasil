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

## Dados Diários - Página 20

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| bf4e5f7b-6c67-34dc-9d71-7d55029eb882 | -10.04002 | -43.80699 | 2025-10-14 04:06:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 621626cd-f5a6-39ff-9237-d93371b726b6 | -12.82402 | -50.65675 | 2025-10-14 04:06:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a81f141a-511f-3977-96df-58d73ffd2277 | -12.81618 | -50.64768 | 2025-10-14 04:06:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ae88cb53-67b8-3dca-8203-a9aeceb16f88 | -12.85099 | -50.65884 | 2025-10-14 04:06:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 5.2 |
| bb25a773-9b8f-3dcd-b689-27dbbdb10a31 | -12.8378 | -50.64239 | 2025-10-14 04:06:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3e50b436-0ecc-33c0-a169-66496d8e189d | -12.84637 | -50.65445 | 2025-10-14 04:06:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 824d3bfd-fc55-3943-8fb7-37917489230c | -12.73332 | -50.65131 | 2025-10-14 04:06:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5024d72e-2155-3bcc-bd8d-375489ea74ce | -12.8437 | -50.64017 | 2025-10-14 04:06:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 13.6 |
| bb95da2b-3319-3996-b50a-5fd53644bf4b | -12.83909 | -50.63579 | 2025-10-14 04:06:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 117fbfdd-29c3-3ca3-95c5-c608e14bf6c6 | -11.52308 | -43.50475 | 2025-10-14 04:06:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 09b8bba4-b053-34a3-8881-7e2b5c0ee864 | -13.68769 | -42.41298 | 2025-10-14 04:06:00 | NPP-375D | CAETITÉ | BAHIA | Brasil | 2905206 | 29 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 0029beb8-e54c-30f1-bc0e-52048cc17fa2 | -13.96733 | -42.52179 | 2025-10-14 04:06:00 | NPP-375D | CAETITÉ | BAHIA | Brasil | 2905206 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| f8161b80-dbd4-37a4-a544-6ec5117e05ff | -14.47874 | -41.45617 | 2025-10-14 04:06:00 | NPP-375D | ARACATU | BAHIA | Brasil | 2902005 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 8e4b7c2e-7f46-339a-8cff-daa459a8b5c5 | -14.73913 | -42.39361 | 2025-10-14 04:06:00 | NPP-375D | JACARACI | BAHIA | Brasil | 2917409 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 9774bfbb-cf0c-3f7c-9a21-36276d968ab9 | -11.56135 | -44.05025 | 2025-10-14 04:06:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ab0705a5-4226-3b50-9a5f-43385ec33175 | -13.97635 | -42.50848 | 2025-10-14 04:06:00 | NPP-375D | CAETITÉ | BAHIA | Brasil | 2905206 | 29 | 33 | nan | nan | nan | Caatinga | 5.1 |
| e5c21543-2f02-3d89-8726-71ab267912ea | -12.85883 | -50.64671 | 2025-10-14 04:06:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 410f3cbe-119e-3a75-b39b-80a97807c8f0 | -12.62581 | -44.12154 | 2025-10-14 04:06:00 | NPP-375D | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ffb5bd09-2f84-3fe8-8b91-c146e257b67b | -12.81662 | -42.16538 | 2025-10-14 04:06:00 | NPP-375D | NOVO HORIZONTE | BAHIA | Brasil | 2923035 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 795adb67-01b2-3ec4-b132-1a6a5414fa44 | -13.33026 | -40.90374 | 2025-10-14 04:06:00 | NPP-375D | IRAMAIA | BAHIA | Brasil | 2914307 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| c5309bad-0bc4-3bd3-b055-93013db77f3e | -12.66238 | -43.42747 | 2025-10-14 04:06:00 | NPP-375D | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 01d29959-87f2-32f1-a0f9-be7863d2cac8 | -11.51894 | -43.50806 | 2025-10-14 04:06:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 50271781-d802-3615-9f24-a34224b6047d | -12.84572 | -50.65775 | 2025-10-14 04:06:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8246cf87-ec2c-3aef-86a4-3fac7cb5bbe3 | -12.82863 | -50.66114 | 2025-10-14 04:06:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 77feb42d-35f4-319c-b389-84368c3690dc | -12.78667 | -50.65883 | 2025-10-14 04:06:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5f69b74e-9fd2-37e8-91b1-564ae9536c0e | -12.80888 | -50.65021 | 2025-10-14 04:06:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a56f91dc-6417-3071-9ef7-6a3df0751ff6 | -10.36301 | -44.98008 | 2025-10-14 04:06:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 52a45386-b76f-31c7-858a-37c2b694d37a | -12.79848 | -50.65437 | 2025-10-14 04:06:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 7bf3d3f0-0d39-30a8-8b2b-fb739cd9cf0f | -14.08344 | -44.09068 | 2025-10-14 04:06:00 | NPP-375D | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 250346d9-57d5-3a83-925b-5bccd9f6f4e7 | -12.8267 | -50.64987 | 2025-10-14 04:06:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6c31a72a-01fa-37bb-86db-a8753a4ffc63 | -12.63289 | -44.12278 | 2025-10-14 04:06:00 | NPP-375D | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 074aa2f0-9438-3cd5-a8c2-0ad84b1fceb7 | -11.74497 | -43.29205 | 2025-10-14 04:06:00 | NPP-375D | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 15.3 |
| 15a1e688-823f-3813-92e1-da56968dd502 | -12.84766 | -50.64785 | 2025-10-14 04:06:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 61416cfe-5fdb-3dba-8d9d-f467526780ce | -12.82607 | -50.65318 | 2025-10-14 04:06:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3aa13efa-8ae2-3f95-b5b0-78d3128e3387 | -12.82928 | -50.65783 | 2025-10-14 04:06:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 796cc21b-cdaf-3695-89f6-264f06b3553e | -15.31715 | -43.09597 | 2025-10-14 04:06:00 | NPP-375D | CATUTI | MINAS GERAIS | Brasil | 3115474 | 31 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 4d247506-e67c-3829-8e79-261523102c4c | -12.24138 | -49.36279 | 2025-10-14 04:06:00 | NPP-375D | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | 9.6 |
| fe4e7a87-c235-39df-9cce-c45ffc038d76 | -12.22694 | -51.03147 | 2025-10-14 04:06:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| adaf4431-f1ed-3d89-b4b4-a737de0fb813 | -12.81028 | -50.6499 | 2025-10-14 04:06:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 8be50c31-ee73-34ff-914c-627cb9ba8256 | -12.83319 | -50.63801 | 2025-10-14 04:06:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7c5b45c4-abba-3eca-959f-41bd30dfe398 | -12.82006 | -50.64906 | 2025-10-14 04:06:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5b3d0a7a-cb69-31ee-80f9-ad11c353eee1 | -13.27155 | -42.49905 | 2025-10-14 04:06:00 | NPP-375D | BOTUPORÃ | BAHIA | Brasil | 2904209 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 27ba30f4-ade9-3972-8c61-a50b3d814bc8 | -11.50079 | -43.48183 | 2025-10-14 04:06:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 37b15eea-b574-30d7-ba48-84a34f629cda | -12.67775 | -43.39872 | 2025-10-14 04:06:00 | NPP-375D | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a0a87ec3-e090-351d-9691-bd3dc7bf4c4e | -12.8496 | -50.63795 | 2025-10-14 04:06:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 7b84059b-0c05-37bb-a5fb-c77e2b6f2172 | -12.73266 | -50.65464 | 2025-10-14 04:06:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1e7b7982-5976-324c-b054-790a1ccceade | -12.79911 | -50.65106 | 2025-10-14 04:06:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| c1a236a8-d07d-300d-aee9-9463637afaaf | -12.84176 | -50.65007 | 2025-10-14 04:06:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 79e644d8-dd5b-31e6-a159-d0c58028b675 | -12.01817 | -47.80033 | 2025-10-14 04:06:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d2d62e2b-3608-3a84-8b0e-9857b4ca47ca | -12.83844 | -50.63909 | 2025-10-14 04:06:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5ddacf6a-adc4-3223-9b79-f398185eac4d | -12.82662 | -50.64354 | 2025-10-14 04:06:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 727df71a-872f-3e5e-a7bf-f3ab4dd5dfe9 | -10.81991 | -43.97255 | 2025-10-14 04:06:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 9b7c7f98-fd80-3e9f-97b9-3646eb319528 | -12.67712 | -43.40253 | 2025-10-14 04:06:00 | NPP-375D | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 557ed229-fe18-36d4-980a-4ef92ea85d38 | -11.5233 | -43.52489 | 2025-10-14 04:06:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 89d8b3db-280c-353b-9ae5-0312747b534c | -12.20453 | -51.03173 | 2025-10-14 04:06:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 43002958-15d2-3cf1-b0f6-1fdb268ca64e | -15.82316 | -41.89665 | 2025-10-14 04:06:00 | NPP-375D | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 33db7f4b-8761-36c4-8860-166a83b3a9a3 | -11.53168 | -49.27773 | 2025-10-14 04:06:00 | NPP-375D | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| f70fe73b-e3fb-35e2-9145-7b0671d55795 | -12.84507 | -50.66106 | 2025-10-14 04:06:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1f4372e7-0b8c-3ffb-bc20-5ceca0897a24 | -12.84443 | -50.66436 | 2025-10-14 04:06:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 72bbaac7-390b-3738-8bff-f09cd301827b | -14.39344 | -40.76612 | 2025-10-14 04:06:00 | NPP-375D | CAETANOS | BAHIA | Brasil | 2905156 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 84e6d138-0f62-3c18-a674-1969ea7a6de7 | -10.81197 | -43.95398 | 2025-10-14 04:06:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 0c35507f-79a3-369e-a80f-ebc8ea226eb2 | -12.80965 | -50.65322 | 2025-10-14 04:06:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 69495d55-8e1d-303d-8b53-b415ea082273 | -12.83585 | -50.65229 | 2025-10-14 04:06:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4ac0e25d-2088-34d8-a28a-2aebeee6a8aa | -15.3761 | -43.0379 | 2025-10-14 04:06:00 | NPP-375D | CATUTI | MINAS GERAIS | Brasil | 3115474 | 31 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 2504aad5-1c6c-31da-afee-c8f47ecd63b0 | -14.4793 | -41.4526 | 2025-10-14 04:06:00 | NPP-375D | ARACATU | BAHIA | Brasil | 2902005 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 0a119642-88fd-3a91-be45-1a9f10d8b16d | -12.83455 | -50.65889 | 2025-10-14 04:06:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| fc90df7c-c4fa-3bed-b56e-c5b3fbfc38d3 | -12.8194 | -50.65237 | 2025-10-14 04:06:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4ef2f247-4bfe-31a3-acb9-6ebd4173e95e | -11.50428 | -43.48243 | 2025-10-14 04:06:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f2585b97-ab11-3ab6-8b38-e7c853e0c758 | -13.6849 | -44.37612 | 2025-10-14 04:06:00 | NPP-375D | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 41c0cc1e-76da-3ad2-adcd-2191c2e1cbed | -12.85422 | -50.64233 | 2025-10-14 04:06:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 3c4ade63-a014-3f48-bdaa-d04ea0f9e6ac | -12.84896 | -50.64125 | 2025-10-14 04:06:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 13.6 |
| 21b119b3-d99a-3699-a958-e44aabf8287e | -12.80953 | -50.64691 | 2025-10-14 04:06:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 18d8434d-2a67-3974-a86e-f8be81d142f5 | -12.82532 | -50.65014 | 2025-10-14 04:06:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1c20a8b8-c644-3510-b6d0-b4370eedf324 | -12.82993 | -50.65452 | 2025-10-14 04:06:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9d40640c-c3dd-3493-9f32-e2a0651e4c01 | -13.33292 | -41.36819 | 2025-10-14 04:06:00 | NPP-375D | IBICOARA | BAHIA | Brasil | 2912202 | 29 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 27d25812-ebce-388d-89a8-363774e02552 | -12.82481 | -50.65981 | 2025-10-14 04:06:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f68c6bcc-750a-3030-bd1c-09e77dd5a011 | -12.85809 | -43.81642 | 2025-10-14 04:06:00 | NPP-375D | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| de922f9f-846a-31f1-9907-7ca0e0442bf5 | -12.80375 | -50.65546 | 2025-10-14 04:06:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| cb24590d-b7e7-3c3d-b810-ecd1003da8c9 | -12.77549 | -50.65997 | 2025-10-14 04:06:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3ff42e4e-f7e7-357b-af61-5fbb9866c36e | -12.84046 | -50.65667 | 2025-10-14 04:06:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 173d0dbd-a099-39dc-9c2a-d4c310fd5cb3 | -12.63792 | -43.44681 | 2025-10-14 04:06:00 | NPP-375D | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 96e63d69-b952-3aad-af3c-9cb33be9a04c | -12.84702 | -50.65115 | 2025-10-14 04:06:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| baf358d9-d198-33cd-bf05-b6b9ee1c9705 | -15.80415 | -41.45756 | 2025-10-14 04:06:00 | NPP-375D | ÁGUAS VERMELHAS | MINAS GERAIS | Brasil | 3101003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| a7512e06-4259-3c0f-b838-b7d0fc8b0566 | -12.99367 | -43.99822 | 2025-10-14 04:06:00 | NPP-375D | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 0b496311-2706-38aa-bb77-60c4f18d5a27 | -12.81414 | -50.65129 | 2025-10-14 04:06:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e8006475-2a34-3ca1-8e0b-bc5b9b2ac37e | -14.0895 | -44.14046 | 2025-10-14 04:06:00 | NPP-375D | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 66567bfd-88d2-34b4-b308-b8856687ab89 | -12.80438 | -50.65215 | 2025-10-14 04:06:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 6cc76281-bec2-3c61-81ed-c0720de19744 | -13.9965 | -43.87523 | 2025-10-14 04:06:00 | NPP-375D | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 09b28345-6123-368d-b15c-43ee74dfcb6a | -12.84378 | -50.66767 | 2025-10-14 04:06:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9a8473a5-21ed-3aa5-92de-cd207e57d262 | -15.61102 | -41.37419 | 2025-10-14 04:06:00 | NPP-375D | ÁGUAS VERMELHAS | MINAS GERAIS | Brasil | 3101003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 11ec7cad-bc82-33b6-9855-91332808736d | -10.36681 | -44.98077 | 2025-10-14 04:06:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4bf37705-e9e4-34d4-a8bd-9eeaf80c1601 | -12.85228 | -50.65223 | 2025-10-14 04:06:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 10.1 |
| e55c5245-5672-3d68-aec2-e4e3610b70c3 | -13.53843 | -43.0113 | 2025-10-14 04:06:00 | NPP-375D | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 7.2 |
| 030c3b5e-c84e-3cc0-bb18-064daefe1d23 | -12.83254 | -50.64131 | 2025-10-14 04:06:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1861b3c5-7f21-370a-9c55-f52393111941 | -12.99718 | -43.99881 | 2025-10-14 04:06:00 | NPP-375D | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 78fa0994-2b67-3272-b74f-25ac71b5eec6 | -12.45909 | -38.47932 | 2025-10-14 04:06:00 | NPP-375D | SÃO SEBASTIÃO DO PASSÉ | BAHIA | Brasil | 2929503 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| bb564060-6b8d-3637-882f-0ed44155c422 | -12.81091 | -50.6466 | 2025-10-14 04:06:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a4839a91-b881-3c0a-b1a8-d0e6290305b3 | -12.79975 | -50.64774 | 2025-10-14 04:06:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 0421f1e2-e45c-3e34-b1eb-e72c6be5b291 | -12.82081 | -50.65208 | 2025-10-14 04:06:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 393bf8e7-142f-3d61-b8af-08f25ba266cc | -11.01962 | -44.53265 | 2025-10-14 04:06:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |


[Clique aqui para ver as próximas entradas](README21.md)
