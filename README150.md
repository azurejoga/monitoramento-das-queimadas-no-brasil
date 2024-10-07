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

## Dados Diários - Página 150

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8d395d98-2cda-313e-8fa8-774b08b01c36 | -21.58529 | -47.7379 | 2024-10-07 12:21:00 | TERRA_M-T | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 33.2 |
| 7c12d290-275e-3900-b200-7af463e9e1a7 | -21.58754 | -47.72435 | 2024-10-07 12:21:00 | TERRA_M-T | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 28.9 |
| 88fb2ed5-a605-3498-8c54-8b2893d8b279 | -21.59604 | -47.96717 | 2024-10-07 12:21:00 | TERRA_M-T | RINCÃO | SÃO PAULO | Brasil | 3543709 | 35 | 33 | nan | nan | nan | Cerrado | 57.5 |
| 9f2e05ae-241c-3e52-83a7-628c659b4abd | -21.59777 | -47.72674 | 2024-10-07 12:21:00 | TERRA_M-T | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 23.3 |
| 6ca4d328-41fc-3f21-998b-9bfdd204c043 | -21.59834 | -47.95368 | 2024-10-07 12:21:00 | TERRA_M-T | RINCÃO | SÃO PAULO | Brasil | 3543709 | 35 | 33 | nan | nan | nan | Cerrado | 79.3 |
| 20bd6952-1c27-3ef9-baf6-38da8fd28b30 | -19.2087 | -46.5804 | 2024-10-07 12:21:00 | TERRA_M-T | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 22.3 |
| 42c3876c-f5ff-3fef-a13c-2c9623658252 | -21.60652 | -47.96909 | 2024-10-07 12:21:00 | TERRA_M-T | RINCÃO | SÃO PAULO | Brasil | 3543709 | 35 | 33 | nan | nan | nan | Cerrado | 23.1 |
| e1c7c4cf-5540-3632-8d86-d49d32e5b419 | -21.60883 | -47.95551 | 2024-10-07 12:21:00 | TERRA_M-T | RINCÃO | SÃO PAULO | Brasil | 3543709 | 35 | 33 | nan | nan | nan | Cerrado | 57.4 |
| c8d90cca-cf24-3b05-bb16-74e83f633581 | -18.88972 | -54.49558 | 2024-10-07 12:21:00 | TERRA_M-T | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 62.0 |
| ac5bc443-793d-370e-b178-a40befb60a0a | -17.66581 | -53.10041 | 2024-10-07 12:21:00 | TERRA_M-T | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 112.8 |
| 9aecbbca-6b90-38e3-a5d8-7e4b6df2e30f | -17.67337 | -53.06282 | 2024-10-07 12:21:00 | TERRA_M-T | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 83.4 |
| 1841982a-f9d8-3f06-8dd0-14fd51e7d3bc | -17.67783 | -53.09489 | 2024-10-07 12:21:00 | TERRA_M-T | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 620.1 |
| a4a8ebad-bb70-3d40-b500-4b4bf340b943 | -17.68235 | -53.10347 | 2024-10-07 12:21:00 | TERRA_M-T | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 309.6 |
| a5134147-ed63-3e8b-a5e7-c7f8052df589 | -17.68502 | -53.05769 | 2024-10-07 12:21:00 | TERRA_M-T | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 177.7 |
| 069fbc91-335f-30e5-9cef-e7ed2a0abc03 | -17.68981 | -53.06616 | 2024-10-07 12:21:00 | TERRA_M-T | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 211.9 |
| 87733b0d-c83b-3a24-a5b7-369c7b0455c2 | -17.77696 | -53.09191 | 2024-10-07 12:21:00 | TERRA_M-T | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 61.8 |
| 03224267-7456-37dd-b59d-e0a06c7096e4 | -20.77809 | -51.52301 | 2024-10-07 12:21:00 | TERRA_M-T | CASTILHO | SÃO PAULO | Brasil | 3511003 | 35 | 33 | nan | nan | nan | Mata Atlântica | 45.6 |
| 342e8e6f-451c-3b06-afd5-eebd34691570 | -20.79186 | -51.52606 | 2024-10-07 12:21:00 | TERRA_M-T | CASTILHO | SÃO PAULO | Brasil | 3511003 | 35 | 33 | nan | nan | nan | Mata Atlântica | 23.8 |
| 0d0d7460-8993-3291-a550-a503085eef8e | -17.12765 | -51.70877 | 2024-10-07 12:21:00 | TERRA_M-T | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 31.6 |
| 55b82847-67a1-39c2-8427-6dc0b706cf73 | -19.87212 | -50.37126 | 2024-10-07 12:21:00 | TERRA_M-T | OUROESTE | SÃO PAULO | Brasil | 3534757 | 35 | 33 | nan | nan | nan | Mata Atlântica | 21.3 |
| 6c876d69-a91c-32a9-b7ee-2b02cc216427 | -20.1994 | -50.03194 | 2024-10-07 12:21:00 | TERRA_M-T | PARISI | SÃO PAULO | Brasil | 3536257 | 35 | 33 | nan | nan | nan | Mata Atlântica | 22.9 |
| ebb740d9-8420-3dd3-a2c6-92789a0ee265 | -16.08032 | -50.20827 | 2024-10-07 12:21:00 | TERRA_M-T | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | 36.7 |
| 50b0643c-81ad-333f-97b8-0c9c77cfe0a2 | -23.04511 | -49.85674 | 2024-10-07 12:21:00 | TERRA_M-T | OURINHOS | SÃO PAULO | Brasil | 3534708 | 35 | 33 | nan | nan | nan | Mata Atlântica | 30.0 |
| 10c175a5-bf1c-3bea-8966-41899833445c | -15.70167 | -47.15691 | 2024-10-07 12:21:00 | TERRA_M-T | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 16.3 |
| d09a43af-7268-308f-8ccd-51aec4798324 | -15.70398 | -47.14265 | 2024-10-07 12:21:00 | TERRA_M-T | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 25.9 |
| baa045a4-075c-35bf-9d46-5721cce52d50 | -15.70497 | -47.14873 | 2024-10-07 12:21:00 | TERRA_M-T | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 36.1 |
| 817aa214-b2b6-3061-89a2-39b39eac6247 | -15.71595 | -47.15067 | 2024-10-07 12:21:00 | TERRA_M-T | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 34.2 |
| 84f14569-48b9-317a-94ed-91b1ac9edc89 | -21.65735 | -47.73157 | 2024-10-07 12:21:00 | TERRA_M-T | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 18.5 |
| 33b90987-f8f8-3c05-87e4-8348131e583c | -20.48281 | -47.69957 | 2024-10-07 12:21:00 | TERRA_M-T | GUARÁ | SÃO PAULO | Brasil | 3517703 | 35 | 33 | nan | nan | nan | Cerrado | 66.1 |
| 087fac6d-95db-3c3c-a1de-f3982ae60f1c | -15.71834 | -47.13644 | 2024-10-07 12:21:00 | TERRA_M-T | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 15.3 |
| 7a314f72-4ff7-3d24-8acf-4fb7a9545c3f | -20.48509 | -47.68586 | 2024-10-07 12:21:00 | TERRA_M-T | GUARÁ | SÃO PAULO | Brasil | 3517703 | 35 | 33 | nan | nan | nan | Cerrado | 14.8 |
| fbb7e3f7-d366-3441-a667-a4951098ce51 | -25.09987 | -49.36227 | 2024-10-07 12:23:00 | TERRA_M-T | RIO BRANCO DO SUL | PARANÁ | Brasil | 4122206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 47.6 |
| f391577c-1bfd-3609-9642-061458d6f6e2 | -11.7561 | -44.513 | 2024-10-07 12:26:12 | GOES-16 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 106.9 |
| 35ecc307-983f-3b45-af9c-6052ad0f1e43 | -11.7566 | -44.4897 | 2024-10-07 12:26:12 | GOES-16 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 134.2 |
| a4758590-602b-3e08-bc26-fe4ec7484464 | -13.8359 | -44.6162 | 2024-10-07 12:26:24 | GOES-16 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 106.3 |
| 5d757f7f-e1ed-3e7a-a9d7-93a9f3e57a89 | -13.8549 | -44.6363 | 2024-10-07 12:26:24 | GOES-16 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 92.0 |
| 2040d992-e14c-3da2-9858-957382882ac1 | -14.1268 | -45.5439 | 2024-10-07 12:26:25 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 89.3 |
| e9e2d6ea-832b-35c6-83f8-0c4c25a1d3a6 | -14.0703 | -45.4611 | 2024-10-07 12:26:25 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 105.3 |
| 2019afa3-9647-3dd8-9123-66cc8dd857d2 | -14.1258 | -45.5904 | 2024-10-07 12:26:25 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 181.4 |
| 55fbf502-f93d-3c4a-969e-4f391ce40eb1 | -14.1083 | -45.5008 | 2024-10-07 12:26:25 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 101.9 |
| 7c023679-a31e-3bfa-a3ea-4f46b432774f | -14.1273 | -45.5207 | 2024-10-07 12:26:25 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 139.1 |
| 9924833a-c25f-3822-97c3-4b15cacd2ae2 | -14.0898 | -45.4577 | 2024-10-07 12:26:25 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 102.9 |
| 20bd7bf4-1507-39b2-864a-5c0e196c5208 | -16.9098 | -47.1493 | 2024-10-07 12:26:40 | GOES-16 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 124.7 |
| dcd5d61d-badf-30d3-b965-5989ce85f819 | -16.8894 | -47.1763 | 2024-10-07 12:26:40 | GOES-16 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 120.5 |
| 305cefed-0114-3b9a-b853-93a76fc7cb5f | -16.8899 | -47.1532 | 2024-10-07 12:26:40 | GOES-16 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 159.0 |
| ad187774-627f-307e-b1a5-fc27564c8146 | -17.6679 | -53.0819 | 2024-10-07 12:26:45 | GOES-16 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 268.9 |
| 219e92f1-6474-3a56-a914-aaee6fa0e319 | -17.6675 | -53.1033 | 2024-10-07 12:26:45 | GOES-16 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 147.1 |
| bd9ab424-cc4a-3efa-9d51-a0b8943f8264 | -17.6882 | -53.0573 | 2024-10-07 12:26:45 | GOES-16 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 80.8 |
| b392c0d7-6326-3607-8a3b-211c3a5d077e | -17.6873 | -53.1003 | 2024-10-07 12:26:45 | GOES-16 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 144.1 |
| 617b2b01-6019-3066-aeea-d1cb8668235b | -17.6688 | -53.0389 | 2024-10-07 12:26:45 | GOES-16 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 131.0 |
| 5a957e81-3b75-3807-a21d-cd8c17aade4f | -17.6684 | -53.0604 | 2024-10-07 12:26:45 | GOES-16 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 110.1 |
| bd42bf7b-dd73-3c2f-acea-ff3c1a0755a9 | -17.8319 | -53.7829 | 2024-10-07 12:26:46 | GOES-16 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 79.8 |
| cf423382-c4e9-3cc3-ab22-d312f2ab9714 | -18.8886 | -54.5587 | 2024-10-07 12:26:52 | GOES-16 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 100.5 |
| 272193d3-ee98-3a89-8793-87b3384d4ffd | -18.8882 | -54.58 | 2024-10-07 12:26:52 | GOES-16 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 78.1 |
| cfb62559-2618-3121-a90b-924d2d7c6edc | -19.1995 | -46.5714 | 2024-10-07 12:26:52 | GOES-16 | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 126.2 |
| 6817a355-a1f3-3a71-b18b-a6b8d0f5d732 | -11.7566 | -44.4897 | 2024-10-07 12:36:12 | GOES-16 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 175.3 |
| 659b7b6a-e8c2-3de7-b614-8d05be43b7f0 | -11.7373 | -44.4926 | 2024-10-07 12:36:12 | GOES-16 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 79.9 |
| ad8dffe5-fdb6-3171-b59e-f131b9a50364 | -11.7561 | -44.513 | 2024-10-07 12:36:12 | GOES-16 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 120.6 |
| 7170ced0-a5eb-3e6e-8756-a4578b5214b9 | -14.0694 | -45.5076 | 2024-10-07 12:36:25 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 85.3 |
| 8078560a-54b3-3bbe-86bb-e288f979a4b4 | -14.1068 | -45.5705 | 2024-10-07 12:36:25 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 83.1 |
| f03bc9d7-0149-3a03-bd45-a2c71a2115e1 | -14.1258 | -45.5904 | 2024-10-07 12:36:25 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 161.2 |
| ba9b43e0-311b-3bc6-a483-9874f793d626 | -14.0689 | -45.5308 | 2024-10-07 12:36:25 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 86.2 |
| 2b58da53-e39c-3292-b16b-d9af5fd7d0fa | -15.71 | -47.1463 | 2024-10-07 12:36:34 | GOES-16 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 87.6 |
| 89bdccd5-ff75-3b63-9565-72a313bf14b9 | -16.8899 | -47.1532 | 2024-10-07 12:36:40 | GOES-16 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 243.9 |
| 8b082e62-fe79-3bd4-9a74-da02b02e237c | -16.9098 | -47.1493 | 2024-10-07 12:36:40 | GOES-16 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 171.0 |
| beeccd92-e7e4-38df-a633-c18982abf17f | -16.8894 | -47.1763 | 2024-10-07 12:36:40 | GOES-16 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 124.0 |
| cdef00b0-dc50-304e-9910-f7ef8bca2c20 | -17.6464 | -53.1708 | 2024-10-07 12:36:45 | GOES-16 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 211.8 |
| 2e6c9de0-b836-3285-8d39-ca19251bd864 | -17.6873 | -53.1003 | 2024-10-07 12:36:45 | GOES-16 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 151.2 |
| dd70beaa-8e59-3681-be89-0bd38253d281 | -17.6882 | -53.0573 | 2024-10-07 12:36:45 | GOES-16 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 89.7 |
| 0322c9ad-76e6-3e80-ad6a-de300c091f24 | -17.6679 | -53.0819 | 2024-10-07 12:36:45 | GOES-16 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 168.5 |
| 0e2b393d-c401-3b77-aefc-7e7d1a9fed1d | -17.6877 | -53.0788 | 2024-10-07 12:36:45 | GOES-16 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 290.8 |
| ea8c8620-f1ee-32d4-87d8-5c5aa8cf852a | -17.6675 | -53.1033 | 2024-10-07 12:36:45 | GOES-16 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 105.7 |
| 0eeabe02-71e3-32db-a7c4-984827b942a4 | -19.1995 | -46.5714 | 2024-10-07 12:36:52 | GOES-16 | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 92.4 |
| 5dc22d5e-2840-36ab-b6a1-fecaa6c04957 | -18.8882 | -54.58 | 2024-10-07 12:36:52 | GOES-16 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 98.8 |
| 8e31b2c4-4b1d-3b87-bcb6-707c02404044 | -18.8886 | -54.5587 | 2024-10-07 12:36:52 | GOES-16 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 129.3 |
| 76631b74-7636-3950-ac31-090edad47a4e | -11.7369 | -44.5159 | 2024-10-07 12:46:12 | GOES-16 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 83.7 |
| a47db338-b234-3f77-bfbf-89e1e0dd0cdd | -11.7373 | -44.4926 | 2024-10-07 12:46:12 | GOES-16 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 83.0 |
| 9d28a408-da20-37cc-8e4a-227b54eccf54 | -11.7561 | -44.513 | 2024-10-07 12:46:12 | GOES-16 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 260.0 |
| 9a09c735-9a75-334a-827e-44d5dee0e840 | -11.7566 | -44.4897 | 2024-10-07 12:46:12 | GOES-16 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 296.2 |
| 47466d1e-d2be-34c9-83ae-1d24580fa80a | -14.1258 | -45.5904 | 2024-10-07 12:46:25 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 125.2 |
| 1052c1ef-6534-3684-bed3-fe8c7c15243e | -14.0694 | -45.5076 | 2024-10-07 12:46:25 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 95.2 |
| 09d4a0d3-6c71-376f-b92f-1194b216bd2f | -14.0689 | -45.5308 | 2024-10-07 12:46:25 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 91.1 |
| 98a97d98-07bc-331a-8d73-ad2dab2dfd30 | -14.1068 | -45.5705 | 2024-10-07 12:46:25 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 90.5 |
| dcd34d1d-5ec0-3995-be0d-acebb8c77326 | -14.1064 | -45.5938 | 2024-10-07 12:46:25 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 80.8 |
| e0151595-7313-3748-839d-46fec9f14747 | -15.71 | -47.1463 | 2024-10-07 12:46:34 | GOES-16 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 109.4 |
| eabcd8b5-4609-3cc1-97cf-d09c84bdf389 | -16.8899 | -47.1532 | 2024-10-07 12:46:40 | GOES-16 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 238.9 |
| f96a13bb-5499-300a-bd84-af2309c52a32 | -16.9098 | -47.1493 | 2024-10-07 12:46:40 | GOES-16 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 198.3 |
| e5248b59-b189-3710-96a8-758bfc542721 | -16.8894 | -47.1763 | 2024-10-07 12:46:40 | GOES-16 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 112.2 |
| 4f1dfc5c-ae53-37f1-8b04-60b8149ea09a | -16.6063 | -55.2168 | 2024-10-07 12:46:40 | GOES-16 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 80.2 |
| 9fc01c9c-9601-3fb1-898b-d397c874b466 | -17.6877 | -53.0788 | 2024-10-07 12:46:45 | GOES-16 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 148.3 |
| e31e4afd-273f-3e0c-a168-07f8bf054e56 | -17.6873 | -53.1003 | 2024-10-07 12:46:45 | GOES-16 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 88.0 |
| ab1dd208-bdea-3de0-88ef-84c5c481fd75 | -18.8886 | -54.5587 | 2024-10-07 12:46:52 | GOES-16 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 113.2 |
| 208b1989-2258-3376-b4d8-b9ed1c4aa40d | -19.1995 | -46.5714 | 2024-10-07 12:46:52 | GOES-16 | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 289.5 |
| bb91c6e9-331a-3ce1-9712-220953fbff7d | -11.7566 | -44.4897 | 2024-10-07 12:56:12 | GOES-16 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 368.7 |
| 10d931c9-ea59-3e3c-84a7-697dd1247918 | -11.7369 | -44.5159 | 2024-10-07 12:56:12 | GOES-16 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 86.6 |
| 4b7a628d-ff01-3177-9c90-dd952a0765e9 | -11.7373 | -44.4926 | 2024-10-07 12:56:12 | GOES-16 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 92.2 |
| 385eae91-c19f-3be0-b477-4704ccbebb36 | -11.7561 | -44.513 | 2024-10-07 12:56:12 | GOES-16 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 276.3 |
| 211bce8d-3a4b-3f43-b4cd-86e9308cb6ac | -13.8559 | -44.5892 | 2024-10-07 12:56:24 | GOES-16 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 99.2 |
| a54c2559-8fad-315c-aa4e-5eaba39c5945 | -13.8359 | -44.6162 | 2024-10-07 12:56:24 | GOES-16 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 109.1 |
| 135a9133-965b-3539-b991-8924981614e4 | -13.8549 | -44.6363 | 2024-10-07 12:56:24 | GOES-16 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 85.5 |


[Clique aqui para ver as próximas entradas](README151.md)
