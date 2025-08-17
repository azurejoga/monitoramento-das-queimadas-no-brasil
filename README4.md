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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a3650f5f-7e6a-324b-b50f-a9181664c7b1 | -27.33076 | -51.30138 | 2025-08-17 01:05:00 | TERRA_M-M | ERVAL VELHO | SANTA CATARINA | Brasil | 4205209 | 42 | 33 | nan | nan | nan | Mata Atlântica | 7.5 |
| 62091621-3fb6-3dbc-9f2e-d74ebba40d9e | -18.75542 | -45.08249 | 2025-08-17 01:05:00 | TERRA_M-M | FELIXLÂNDIA | MINAS GERAIS | Brasil | 3125705 | 31 | 33 | nan | nan | nan | Cerrado | 99.2 |
| 1d4d4d9e-4241-3591-bac3-c15992e2a8fa | -22.28281 | -55.9618 | 2025-08-17 01:05:00 | TERRA_M-M | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 6.5 |
| a4d9650e-def2-3a9a-807f-9052a2e14188 | -24.48932 | -50.22821 | 2025-08-17 01:05:00 | TERRA_M-M | TIBAGI | PARANÁ | Brasil | 4127502 | 41 | 33 | nan | nan | nan | Cerrado | 9.6 |
| f7ad439e-ab20-392c-9fc1-9f56620e76ab | -22.17216 | -56.11585 | 2025-08-17 01:05:00 | TERRA_M-M | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 9e7ddf6f-c542-3873-b8cd-7912f0c4a877 | -19.31544 | -49.31092 | 2025-08-17 01:05:00 | TERRA_M-M | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 53.1 |
| b97a886a-d9e9-374b-afa6-e4c88234acfa | -19.31277 | -49.2953 | 2025-08-17 01:05:00 | TERRA_M-M | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 41.4 |
| 03a43ae7-5e5c-3130-84dc-ca0bd72a1be7 | -14.59788 | -47.95414 | 2025-08-17 01:07:00 | TERRA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 22.1 |
| cc81faae-5c3e-3c5d-94db-0b300b428cf2 | -13.15618 | -55.71358 | 2025-08-17 01:07:00 | TERRA_M-M | SORRISO | MATO GROSSO | Brasil | 5107925 | 51 | 33 | nan | nan | nan | Cerrado | 14.7 |
| e06dab95-a02f-3122-9c3a-6bd9bc388569 | -14.62643 | -54.89064 | 2025-08-17 01:07:00 | TERRA_M-M | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 15.5 |
| 5b20294f-0144-3bdc-89a7-98b687822633 | -11.35237 | -55.39548 | 2025-08-17 01:07:00 | TERRA_M-M | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| c113184c-a686-3f5d-89b2-b2955ae5a395 | -10.53265 | -50.3902 | 2025-08-17 01:07:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 25.4 |
| 04b53df8-a5ea-3f72-bfae-23e6d2fcf0b2 | -14.93078 | -54.70392 | 2025-08-17 01:07:00 | TERRA_M-M | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 12.5 |
| e01406e7-2cc5-3ea8-837f-a1207e14b760 | -11.36127 | -55.39413 | 2025-08-17 01:07:00 | TERRA_M-M | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 45.6 |
| 2b7adb30-1bb7-3078-a1f6-8aa5a24bfdea | -13.5714 | -46.99559 | 2025-08-17 01:07:00 | TERRA_M-M | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 44.7 |
| b789f78c-afd0-33fd-8735-3229e58f5f17 | -14.96526 | -54.7551 | 2025-08-17 01:07:00 | TERRA_M-M | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 19.2 |
| bf2cede7-2d49-3d21-9151-745645f139a8 | -10.53919 | -50.37611 | 2025-08-17 01:07:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 20.3 |
| ebd409c5-65f1-3bf0-8dfb-89260eab7647 | -14.92689 | -54.67645 | 2025-08-17 01:07:00 | TERRA_M-M | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 23.0 |
| e4edc8aa-7f52-34da-a7c5-0fa04ce9c737 | -16.84197 | -48.92094 | 2025-08-17 01:07:00 | TERRA_M-M | BELA VISTA DE GOIÁS | GOIÁS | Brasil | 5203302 | 52 | 33 | nan | nan | nan | Cerrado | 15.4 |
| dde9b17c-e3a7-33be-b014-d656b15f9768 | -11.3664 | -55.43057 | 2025-08-17 01:07:00 | TERRA_M-M | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 415e0485-32f6-3b84-b7a6-2dd95b79a882 | -14.6366 | -54.89841 | 2025-08-17 01:07:00 | TERRA_M-M | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 12.8 |
| d275c631-f7dc-3fb9-9e4c-6f84e72a108c | -16.83319 | -48.91674 | 2025-08-17 01:07:00 | TERRA_M-M | BELA VISTA DE GOIÁS | GOIÁS | Brasil | 5203302 | 52 | 33 | nan | nan | nan | Cerrado | 23.1 |
| e59caac4-386e-3756-bb4d-fd442cb98736 | -13.60161 | -47.76945 | 2025-08-17 01:07:00 | TERRA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 21.6 |
| 1723ad75-c7d4-31f0-891a-56357dd3aa50 | -13.67311 | -53.71491 | 2025-08-17 01:07:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| a74df2ec-7dd3-3ed5-a279-f7a3803b4f36 | -10.542 | -50.39429 | 2025-08-17 01:07:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 17.7 |
| 08f4ca6e-1fb1-307a-9de2-866521e267fa | -13.15743 | -55.72261 | 2025-08-17 01:07:00 | TERRA_M-M | SORRISO | MATO GROSSO | Brasil | 5107925 | 51 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 86b1a899-a2dc-33b8-96ed-f34ef7632fbc | -11.35365 | -55.40459 | 2025-08-17 01:07:00 | TERRA_M-M | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 853bac1c-ad4e-3886-868f-38d2b85e85ac | -11.43038 | -52.21266 | 2025-08-17 01:07:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 8.3 |
| e397aae9-992b-3349-8587-d23f5d3c1251 | -14.96656 | -54.76426 | 2025-08-17 01:07:00 | TERRA_M-M | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 19.5 |
| ec2b53b0-4693-3073-aec3-620c04054d7c | -13.42718 | -45.88176 | 2025-08-17 01:07:00 | TERRA_M-M | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 59.6 |
| 00d53752-a7da-3d7d-9113-861da90d2f2f | -14.93838 | -54.69342 | 2025-08-17 01:07:00 | TERRA_M-M | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 9.5 |
| a64df772-bd47-34e5-827c-c08f91b5e9a8 | -13.42868 | -57.03267 | 2025-08-17 01:07:00 | TERRA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 8ad1594c-3faf-3747-9ccc-7e272d5e921c | -15.17429 | -48.7811 | 2025-08-17 01:07:00 | TERRA_M-M | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 25.2 |
| 5ce4786b-ef7c-36ed-ba7e-62fc81803d5e | -14.95637 | -54.75643 | 2025-08-17 01:07:00 | TERRA_M-M | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 16.5 |
| 8c705e9a-9b8b-343f-bb77-8785e7dec218 | -13.42741 | -57.02325 | 2025-08-17 01:07:00 | TERRA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 300a4844-187b-3703-b0bc-6b4c6339667e | -11.35999 | -55.38501 | 2025-08-17 01:07:00 | TERRA_M-M | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 182c16c9-5ec7-345e-bbee-6cd24739343f | -11.34859 | -55.43322 | 2025-08-17 01:07:00 | TERRA_M-M | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| f4f25e1d-10a1-3d19-86b8-17e48ec542af | -14.92818 | -54.68559 | 2025-08-17 01:07:00 | TERRA_M-M | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 39.9 |
| 484ba57b-2935-3ea3-a85b-93885f14730d | -13.15244 | -57.16748 | 2025-08-17 01:07:00 | TERRA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 5.7 |
| ae94bb61-8778-3999-8178-1225ac91c0ca | -15.18351 | -48.75835 | 2025-08-17 01:07:00 | TERRA_M-M | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 15.2 |
| 176c8763-80be-301c-922a-bf6757006a78 | -14.97593 | -54.75657 | 2025-08-17 01:07:00 | TERRA_M-M | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 24332187-c4da-34f2-9cae-c56277754c60 | -11.36255 | -55.40324 | 2025-08-17 01:07:00 | TERRA_M-M | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 11.3 |
| 6384e78b-71ed-350a-8b75-acfc419d3183 | -13.43392 | -45.91787 | 2025-08-17 01:07:00 | TERRA_M-M | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 56.2 |
| be168797-f96a-31ad-83d8-2c138b1daa14 | -13.5872 | -47.77079 | 2025-08-17 01:07:00 | TERRA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 22.6 |
| a85c4dfb-4772-3350-8f9d-c267be05e138 | -13.57358 | -47.00152 | 2025-08-17 01:07:00 | TERRA_M-M | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 27.3 |
| 5aefb847-39ea-3040-8df5-fbfbd95d2d6f | -14.98355 | -54.7462 | 2025-08-17 01:07:00 | TERRA_M-M | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 5.6 |
| e51e6017-46f1-3265-9bf0-9134efccb16b | -15.05212 | -56.04497 | 2025-08-17 01:07:00 | TERRA_M-M | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 8.8 |
| f065425c-b12b-3e5f-a358-27bcb1c6f8d8 | -11.36512 | -55.42147 | 2025-08-17 01:07:00 | TERRA_M-M | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 12.4 |
| 1b44e3cf-be46-31c4-b09b-daa7a4c4f9a2 | -14.97465 | -54.74747 | 2025-08-17 01:07:00 | TERRA_M-M | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 20.1 |
| 07aebd89-5c13-3202-a2c0-7eeb4af6f7f8 | -13.59858 | -47.77534 | 2025-08-17 01:07:00 | TERRA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 28.9 |
| 42a664e9-01a7-302a-8802-cbb7a2f1c63d | -15.18691 | -48.77824 | 2025-08-17 01:07:00 | TERRA_M-M | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 25.8 |
| dbd9a0bd-d83d-35da-a02b-6e8e2c69fa4f | -14.62772 | -54.89979 | 2025-08-17 01:07:00 | TERRA_M-M | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 34.4 |
| 40aef3e1-fe11-3393-9e69-9e3c0c7df11b | -14.93709 | -54.68429 | 2025-08-17 01:07:00 | TERRA_M-M | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 20.3 |
| 9937469d-6a82-305c-9bad-82d6fef3bf86 | -9.50912 | -60.53048 | 2025-08-17 01:09:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 47.8 |
| 5ff27458-c7e9-3392-a7c5-c3d4611d25b7 | -10.31834 | -54.16347 | 2025-08-17 01:09:00 | TERRA_M-M | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 39.2 |
| 9d72f452-a89e-3b07-9be7-10cd02f1eb62 | -9.5124 | -60.55644 | 2025-08-17 01:09:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 23.8 |
| 871de254-ebfd-3623-b3be-fd58d6eac958 | -6.14163 | -57.93347 | 2025-08-17 01:09:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 24.3 |
| 8d696cd9-6c50-3cee-a08d-220320a92a11 | -9.17778 | -59.69918 | 2025-08-17 01:09:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 16.5 |
| 2f36a9ca-6416-36bf-a095-78a5093abb47 | -8.98752 | -60.50561 | 2025-08-17 01:09:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 19.7 |
| ae86d360-4ab4-3940-a4ba-6ab7b315d9c1 | -9.1802 | -59.64187 | 2025-08-17 01:09:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 10.7 |
| d3c73964-71e5-332e-925b-4471b1da3bba | -8.98589 | -60.49303 | 2025-08-17 01:09:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 23.2 |
| 718c5cc9-7cff-32be-bf79-91c60a8cb483 | -9.51076 | -60.54345 | 2025-08-17 01:09:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 32.5 |
| 098cf5e2-a82b-38d6-a170-675b7256711d | -9.50185 | -60.55785 | 2025-08-17 01:09:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 24.5 |
| 65d865b4-2900-35c6-9aea-5c75ef861151 | -10.30689 | -52.56333 | 2025-08-17 01:09:00 | TERRA_M-M | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 12.2 |
| c93d5391-32a0-3aed-8fc3-4587dac35362 | -5.80252 | -59.22407 | 2025-08-17 01:09:00 | TERRA_M-M | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 3c7d4175-a6b5-3750-8726-e36867e7b89c | -6.63769 | -55.54989 | 2025-08-17 01:09:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 01c500fe-60ea-3c77-b580-eb7dd41905f1 | -8.9771 | -60.50697 | 2025-08-17 01:09:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 44.5 |
| f0414d4f-a0a1-3dda-8e62-0bf4dc1122f7 | -3.82165 | -47.74364 | 2025-08-17 01:09:00 | TERRA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 62.4 |
| 093d23f7-a50a-3c2a-8b80-b63f96074f03 | -9.5213 | -60.54206 | 2025-08-17 01:09:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 13.2 |
| 90706940-3a72-3906-9f61-d088eb288c23 | -6.13275 | -57.9347 | 2025-08-17 01:09:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 45.3 |
| 35bbeabe-780e-312c-a0d0-1baf6060d615 | -5.81042 | -59.21306 | 2025-08-17 01:09:00 | TERRA_M-M | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 49dcaa25-b496-35ef-b561-071a6b73f6f6 | -9.22333 | -59.65253 | 2025-08-17 01:09:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 14.3 |
| de198626-b77e-3a75-a647-f95384f712c5 | -9.20071 | -59.63264 | 2025-08-17 01:09:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 29.4 |
| 7336230f-4acf-3b60-a1fe-aca635efa8cc | -9.17629 | -59.68797 | 2025-08-17 01:09:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 3c065ec2-578b-3c08-a2b7-3bf749387411 | -5.44645 | -60.1305 | 2025-08-17 01:09:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 6.7 |
| f118c689-0551-3291-8a7b-d91c65677492 | -3.82456 | -47.73627 | 2025-08-17 01:09:00 | TERRA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 60.7 |
| 419e27a3-2445-3a00-a63b-98a6cb4307ed | -9.7659 | -48.74519 | 2025-08-17 01:09:00 | TERRA_M-M | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 19.5 |
| c171b328-3615-3da1-b759-421eee727db6 | -9.19151 | -59.6515 | 2025-08-17 01:09:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 7ec6375e-2fb0-34e6-8cb9-35f8358725f8 | -9.22187 | -59.64128 | 2025-08-17 01:09:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 11.1 |
| ce0888f0-33ad-3eb4-98c4-a11d3413f9f1 | -9.50748 | -60.51756 | 2025-08-17 01:09:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 14.2 |
| 544be763-85fd-314a-8146-3e6ab46ba092 | -6.13398 | -57.94364 | 2025-08-17 01:09:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 8fbe02b7-e0e6-386d-9e78-f2e9631118c6 | -10.31686 | -54.1533 | 2025-08-17 01:09:00 | TERRA_M-M | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 28.3 |
| 4d3434d5-12fc-38d3-afed-1ab4ab4f2a52 | -8.97547 | -60.49436 | 2025-08-17 01:09:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 70.1 |
| 7193563c-93f7-3c84-80fb-ffe0356a485c | -10.11397 | -57.76435 | 2025-08-17 01:09:00 | TERRA_M-M | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 25.5 |
| 9fa59b13-e594-380e-90ac-81ebe4cf5fc9 | -9.18767 | -59.69789 | 2025-08-17 01:09:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.0 |
| affb3d43-cc12-39be-a92e-d7b4455187ea | -9.18168 | -59.65299 | 2025-08-17 01:09:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 27.9 |
| 3894a97b-3342-33a7-b77e-9cc982e17fa2 | -9.51965 | -60.52913 | 2025-08-17 01:09:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 19.7 |
| c25a11c1-664e-355e-83fb-1b074e73e001 | -6.07687 | -59.95882 | 2025-08-17 01:09:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 4b20da97-8a1b-3b5d-b74e-0fdd162c477a | -9.4991 | -60.5663 | 2025-08-17 01:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 48.7 |
| 89855564-a74f-3508-9b52-bc8b34373813 | -9.518 | -60.5268 | 2025-08-17 01:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 73.0 |
| 5380c29c-37e5-381b-875a-5db2bf86ab78 | -8.034 | -47.6639 | 2025-08-17 01:10:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 43.5 |
| fae0006e-184e-3ef7-9615-446299988507 | -9.1709 | -59.6374 | 2025-08-17 01:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 44.0 |
| a6b8d2b2-8f42-3297-a6eb-c8e59d0917c9 | -13.0122 | -42.3321 | 2025-08-17 01:10:00 | GOES-19 | IBIPITANGA | BAHIA | Brasil | 2912509 | 29 | 33 | nan | nan | nan | Caatinga | 72.4 |
| 378a7a0f-0b20-35c1-a0f9-f6b758f6e881 | -6.545 | -43.0373 | 2025-08-17 01:10:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 86.9 |
| 0c7aabb0-7d18-33e2-8f43-40c34042fc97 | -13.4421 | -45.8898 | 2025-08-17 01:10:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 52.3 |
| e7bf1bf2-16be-3bd2-92c8-555d297c88e5 | -18.7771 | -45.1059 | 2025-08-17 01:10:00 | GOES-19 | FELIXLÂNDIA | MINAS GERAIS | Brasil | 3125705 | 31 | 33 | nan | nan | nan | Cerrado | 72.0 |
| b1c7e3ff-9841-323c-bcd0-daf23b500e3f | -9.1708 | -59.6568 | 2025-08-17 01:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 45.9 |
| c29f9be6-4206-3ee0-a0f2-b338e0996bbb | -4.9118 | -43.257 | 2025-08-17 01:10:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 89.7 |
| 8e7b46c7-08f8-3cfa-a95f-f1e3b379a1b8 | -9.1895 | -59.6364 | 2025-08-17 01:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 53.3 |
| 8de1a346-f555-30c6-abdd-40a07b6258df | -4.9305 | -43.2558 | 2025-08-17 01:10:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 101.7 |


[Clique aqui para ver as próximas entradas](README5.md)
