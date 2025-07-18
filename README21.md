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

## Dados Diários - Página 21

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3dcd92e4-eea1-32d2-983e-e34b98e3d1bb | -5.53157 | -43.88279 | 2025-07-18 04:51:00 | NPP-375D | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a1fa9651-0323-3a52-a488-0409e2d9888d | -2.64064 | -47.3049 | 2025-07-18 04:51:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ace429bb-ebf4-31af-9cf3-c462f7e2726d | -3.98433 | -48.40503 | 2025-07-18 04:51:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a640769e-2fdc-3c16-be9a-023c47a4222a | -5.79722 | -43.62906 | 2025-07-18 04:51:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 56152715-8971-3fff-a637-f56b0e35d44a | -5.65695 | -43.71214 | 2025-07-18 04:51:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 6ab696b9-2e57-38c7-ba28-ef8025dc9531 | -5.53114 | -43.88575 | 2025-07-18 04:51:00 | NPP-375D | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6a500c1b-d9dc-380f-aabe-432f22673bab | -4.80489 | -43.22062 | 2025-07-18 04:51:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| becab6d0-b497-3f1d-9d09-3dd8a04f7ff0 | -4.58886 | -43.31079 | 2025-07-18 04:51:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| dd56da1d-4b50-3e65-af36-ddfab0e91a8a | -3.72365 | -53.98322 | 2025-07-18 04:51:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 827fabf0-69be-37c4-978d-1e0ab9dd231e | -2.90989 | -48.24635 | 2025-07-18 04:51:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| dc7459f0-6ce6-3569-80fd-3f0bd790a5da | -1.68956 | -50.34159 | 2025-07-18 04:51:00 | NPP-375D | BREVES | PARÁ | Brasil | 1501808 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5c23e8ba-0303-35e5-9be0-3b78b2371bda | -5.85687 | -44.97526 | 2025-07-18 04:51:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 54d3e2da-91ea-37cf-902c-85aa7a2f8df7 | -7.05862 | -42.98964 | 2025-07-18 04:51:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 228d625f-b8a9-3f71-a846-b1dce90e8ab9 | -5.65174 | -43.71134 | 2025-07-18 04:51:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 9.1 |
| b826f049-8dc2-33c0-999b-f606931e7314 | -4.47943 | -46.07516 | 2025-07-18 04:51:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 17e67f5a-fa2d-371a-be72-78871a22d23d | -5.48229 | -43.07838 | 2025-07-18 04:51:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 059609e7-b777-39d0-8079-dc94dafdd72c | -5.83552 | -44.10603 | 2025-07-18 04:51:00 | NPP-375D | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 995e5246-5d5e-3d31-9723-e16dd937976f | -6.27102 | -45.27774 | 2025-07-18 04:51:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 191a6a30-83d7-3194-95b3-2cb507ba3dd9 | -2.65233 | -48.80789 | 2025-07-18 04:51:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ee2a0c9d-7e9b-3fa9-9f50-443485c88dd8 | -5.78326 | -45.07944 | 2025-07-18 04:51:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| d2d3f396-ef71-3aab-b2f1-c7b9e4ce0d14 | -4.48379 | -46.07567 | 2025-07-18 04:51:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 45180fb8-64a6-3deb-9ad2-43d1bc6decdf | -6.72924 | -44.33272 | 2025-07-18 04:51:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| fe7c18dc-57f8-3e4c-a4d6-149b80eeb99c | -3.19388 | -60.60945 | 2025-07-18 04:51:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 45b0b947-2d3b-38a7-95b5-2e5096ba62a6 | -3.20151 | -54.58915 | 2025-07-18 04:51:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 7fc47ca9-4216-30e3-a286-5ca6fc09a4e3 | -2.44108 | -47.32926 | 2025-07-18 04:51:00 | NPP-375D | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e01cd76d-cabb-3b72-9640-0b2af267bfa0 | -4.3116 | -48.10476 | 2025-07-18 04:51:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 11.7 |
| 6e227b47-6dd0-3c16-ac93-a71a54b8c202 | -5.85764 | -44.97004 | 2025-07-18 04:51:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 74886b69-58a8-3fd8-aa42-89ef70aba6c5 | -3.60988 | -43.54308 | 2025-07-18 04:51:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b08abb4c-bd16-3e9f-ab3d-50e5bed3d7e3 | -4.10659 | -48.20675 | 2025-07-18 04:51:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 28768035-d902-3376-ba85-1b76449de2a1 | -3.39594 | -47.48421 | 2025-07-18 04:51:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 12.7 |
| 5b1c73a0-b37d-3c47-b149-78b6fc92b2be | -2.92299 | -48.23498 | 2025-07-18 04:51:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cdfec0ef-0fd1-3061-a49e-802d888a4b32 | -6.39935 | -46.54687 | 2025-07-18 04:51:00 | NPP-375D | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 083b8f20-4afe-39a8-83c2-1ad66943cbf4 | -6.45625 | -45.07277 | 2025-07-18 04:51:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3ee49971-232c-39ca-a898-d1fb73a69386 | -5.36299 | -45.12183 | 2025-07-18 04:51:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| a1339201-046c-3fca-bf5e-3095f75fd021 | -3.57048 | -49.90505 | 2025-07-18 04:51:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 86ff107a-2405-3c05-8fc9-e9e9ccad9a2d | -5.72763 | -44.50618 | 2025-07-18 04:51:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d4604095-41cb-373b-be8f-b119751296d9 | -6.71089 | -44.32653 | 2025-07-18 04:51:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| bd5eecd6-3a96-3b25-b26c-67b6969fc97e | -3.29936 | -49.19232 | 2025-07-18 04:51:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| bc544157-26c9-31cd-823f-af01256020b2 | -3.38425 | -47.48248 | 2025-07-18 04:51:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 12.9 |
| 888d164e-cf89-36d3-9718-8bfc25f8eff9 | -4.10995 | -47.93628 | 2025-07-18 04:51:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 991a8a9c-825e-3d84-8030-0534fe1ae784 | -2.91056 | -48.24198 | 2025-07-18 04:51:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| b715030b-b883-3efc-8bf9-d29a895adab4 | -6.37103 | -44.744 | 2025-07-18 04:51:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 79074174-e7b5-3829-b7ef-ab64f5d9f168 | -3.48417 | -51.62093 | 2025-07-18 04:51:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b93af871-cfbb-303b-9477-1c4331ebe312 | -6.72883 | -44.33571 | 2025-07-18 04:51:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4e62437b-f8c9-32cf-a3b1-bec109d957a8 | -2.995 | -49.31652 | 2025-07-18 04:51:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d3c89200-d722-338c-a36a-1eea631d6ee2 | -9.4629 | -62.19994 | 2025-07-18 04:53:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 41575f36-aea7-3328-9c9d-8fdd5cd4dbbb | -12.47692 | -44.50284 | 2025-07-18 04:53:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ba3a5381-8275-301f-a1a5-cdf0d5828368 | -9.24181 | -48.5644 | 2025-07-18 04:53:00 | NPP-375D | RIO DOS BOIS | TOCANTINS | Brasil | 1718709 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 26f41b20-cbe8-39fd-a9ca-12d9185c0e6e | -11.7392 | -48.18762 | 2025-07-18 04:53:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 6de07ca1-284e-3055-9162-5b15ba9acf3e | -7.18835 | -43.09915 | 2025-07-18 04:53:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 0c7912d3-0536-358a-a4d8-b9bdb8083223 | -11.56885 | -47.07989 | 2025-07-18 04:53:00 | NPP-375D | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 8b199901-9bba-385d-ad9e-cdd0d24e7632 | -9.80561 | -47.73417 | 2025-07-18 04:53:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c62b5253-586b-360b-a492-4fff5148f484 | -10.71685 | -49.48977 | 2025-07-18 04:53:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 4c9550b9-d03d-3348-a9ed-554c7fdea51c | -7.70709 | -47.28887 | 2025-07-18 04:53:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 2b32ea79-9204-3226-a523-2bb639ea63bf | -11.35994 | -48.70603 | 2025-07-18 04:53:00 | NPP-375D | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5d6e610e-64e8-35b2-8644-04d9efc418e9 | -8.87716 | -50.15719 | 2025-07-18 04:53:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 1b45d55a-b1e2-3efe-bfdb-a5848b3fd9d5 | -9.43524 | -48.85666 | 2025-07-18 04:53:00 | NPP-375D | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f344011c-a2da-36b7-8162-60d646a0fad7 | -8.08801 | -43.15389 | 2025-07-18 04:53:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 6.2 |
| b63eee59-82a7-340f-b558-2466fed84c28 | -12.70515 | -46.81249 | 2025-07-18 04:53:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 49fc2c50-9d25-304b-a070-4c3e2d6df602 | -11.74228 | -48.19607 | 2025-07-18 04:53:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 66b3375e-d429-3831-abe1-a2c41a90fbc0 | -7.94425 | -43.85957 | 2025-07-18 04:53:00 | NPP-375D | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| bf1e9b29-41b4-3a8c-970d-5c944b279f04 | -9.27205 | -49.63939 | 2025-07-18 04:53:00 | NPP-375D | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a363bee7-3af0-332d-90de-10c9a79359b7 | -9.02322 | -61.22274 | 2025-07-18 04:53:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 34251f10-78e0-3426-85e8-f358bd27342a | -9.49889 | -47.5642 | 2025-07-18 04:53:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 9.3 |
| aa4a4a1f-d086-3ccf-a19c-5300007dbbf4 | -11.71831 | -47.7728 | 2025-07-18 04:53:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0d3c9a75-2cf1-380f-85d8-1c2e5e2e437e | -11.73809 | -48.1955 | 2025-07-18 04:53:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 25.5 |
| 2e9b11a5-f18c-3ace-99f1-90a3fe3f530f | -10.6614 | -49.36821 | 2025-07-18 04:53:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 937183e4-1910-3c6c-9f18-1be554f73c6f | -11.56417 | -47.07257 | 2025-07-18 04:53:00 | NPP-375D | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3bf3804c-ca7a-3200-b00c-5ed1e63bd49e | -11.73902 | -48.19442 | 2025-07-18 04:53:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 30.7 |
| 504173e4-fa66-3972-a59d-4c2794e663bf | -9.84967 | -48.06811 | 2025-07-18 04:53:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d5988fa5-33ce-3f60-99e3-c5c81718fc24 | -12.47745 | -46.92091 | 2025-07-18 04:53:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 63b70294-3a64-3f99-8c00-fb8b0a88826e | -7.61348 | -45.55357 | 2025-07-18 04:53:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 244f3b51-22bd-3542-8057-78003164e975 | -8.09972 | -43.15173 | 2025-07-18 04:53:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 6fe1d7f8-839d-35bc-ba42-c014e8a13dd8 | -10.71818 | -49.48038 | 2025-07-18 04:53:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 14.1 |
| 316e17e7-5b8f-3eec-921a-ddec09c16477 | -11.57065 | -47.09221 | 2025-07-18 04:53:00 | NPP-375D | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| d9034193-4b9f-3a69-bbf1-cb367de99e55 | -11.46456 | -48.15767 | 2025-07-18 04:53:00 | NPP-375D | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e6f96218-cf63-3d44-8ade-33569509bfb0 | -9.76447 | -48.75883 | 2025-07-18 04:53:00 | NPP-375D | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 28447430-1c04-306f-ba58-04f3cfa1f208 | -9.0148 | -59.5415 | 2025-07-18 04:53:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4b797780-dd83-3283-aee8-edabf83849a3 | -12.66378 | -47.09727 | 2025-07-18 04:53:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 8bc32ad3-4915-3417-8ae1-c09bf542c9c6 | -8.38485 | -44.03454 | 2025-07-18 04:53:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 01ed3b07-287a-3631-a21a-2676a617137c | -7.93605 | -43.8586 | 2025-07-18 04:53:00 | NPP-375D | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 83975f77-e17d-3514-ac60-b24c54a2be6d | -9.3889 | -48.40333 | 2025-07-18 04:53:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 7ec5be42-d771-34f2-9e1d-67ab5b8ab31e | -7.18975 | -43.10072 | 2025-07-18 04:53:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 694eecd8-65f6-3d57-86e4-cee6e1833669 | -9.44405 | -50.5614 | 2025-07-18 04:53:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 847446c5-8dba-31f3-b03a-8055dd29e1ba | -11.36043 | -48.70249 | 2025-07-18 04:53:00 | NPP-375D | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ab45c00d-5092-359b-82d6-d4bbf43ce17e | -11.85747 | -46.75609 | 2025-07-18 04:53:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7dbba22e-469b-33b2-aba2-0d9d523ec8a7 | -11.56806 | -47.07775 | 2025-07-18 04:53:00 | NPP-375D | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 12.3 |
| fd5e66c7-990d-3224-ba13-4cafe6a57a79 | -7.18616 | -44.07419 | 2025-07-18 04:53:00 | NPP-375D | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b65c30a7-8988-399d-8ea6-e5d95975bdf3 | -6.76911 | -45.51206 | 2025-07-18 04:53:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f0e284f4-8246-3f66-a7b6-861ede0e0c8f | -11.45984 | -48.16099 | 2025-07-18 04:53:00 | NPP-375D | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 61e6b6dc-f975-3049-b2e4-829534376c9c | -12.03758 | -48.76577 | 2025-07-18 04:53:00 | NPP-375D | SUCUPIRA | TOCANTINS | Brasil | 1720853 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 74d11471-d6d1-39fa-a749-5d1d0a220c29 | -9.25709 | -47.90629 | 2025-07-18 04:53:00 | NPP-375D | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d6d80e65-99b7-3967-a444-d3fcf9d80639 | -7.16636 | -43.59366 | 2025-07-18 04:53:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9f6ac2cd-c355-3af9-8ca5-77c45ce80201 | -7.59291 | -46.30651 | 2025-07-18 04:53:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0cd465a3-c0cd-34df-a26e-7b255df2e8e1 | -8.87962 | -50.15411 | 2025-07-18 04:53:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 5eaaef33-bf26-34fe-844c-37ddfffb2028 | -11.57002 | -47.09681 | 2025-07-18 04:53:00 | NPP-375D | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 9a76088f-105d-354e-8a73-dd99f87d12ba | -12.56936 | -44.7467 | 2025-07-18 04:53:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 98611abf-d956-37a9-8c70-cee70b6f7e74 | -9.16124 | -49.67197 | 2025-07-18 04:53:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 565baf88-e9e2-316a-8189-7d26b5443225 | -7.60892 | -46.32223 | 2025-07-18 04:53:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 36d786ce-6be8-302a-8a24-3ee32bebf339 | -11.73954 | -48.19048 | 2025-07-18 04:53:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 30.7 |


[Clique aqui para ver as próximas entradas](README22.md)
