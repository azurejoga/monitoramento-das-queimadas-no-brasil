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
| 1be12e0a-f741-387d-9171-594320f835ef | -9.30601 | -45.49715 | 2026-05-21 04:04:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 16.2 |
| 5052ef9b-58ff-3119-8f15-fd1d833fb818 | -9.30675 | -45.4929 | 2026-05-21 04:04:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 23.1 |
| d8cbdb9d-9f3b-340c-a018-47d3eae3a4c1 | -8.32155 | -48.00918 | 2026-05-21 04:04:00 | NPP-375D | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 81aaa04d-4b6e-3760-b0e2-e7264c01f757 | -6.11092 | -44.74263 | 2026-05-21 04:04:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b256c46b-c3b0-35ec-8e8b-9213da6de861 | -8.55878 | -45.98594 | 2026-05-21 04:04:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| b35928a8-44c6-3626-8f86-5455cb09a7c8 | -10.6468 | -42.30436 | 2026-05-21 04:04:00 | NPP-375D | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 59b0728d-72a8-36f0-8a74-64f8883c7dd3 | -8.60074 | -45.95684 | 2026-05-21 04:04:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3c01ed75-4709-340d-a60a-82beccae6d44 | -10.6546 | -42.30152 | 2026-05-21 04:04:00 | NPP-375D | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| c8605185-493c-357b-81e1-707e48f0ddf4 | -10.42109 | -44.95768 | 2026-05-21 04:04:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 0.4 |
| a5741f03-5f1e-3821-a991-96aa5ad2a01c | -8.55422 | -45.985 | 2026-05-21 04:04:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 1f76eefe-1b9b-3bca-9dfd-3ae37a123145 | -4.66115 | -42.42168 | 2026-05-21 04:04:00 | NPP-375D | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 03417b50-d1c0-3a17-a6af-d775c69e9ac8 | -8.60653 | -45.95583 | 2026-05-21 04:04:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9c023acb-7651-3642-8790-94b652dd649e | -10.64749 | -42.3003 | 2026-05-21 04:04:00 | NPP-375D | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 70e40b46-8d1c-304a-a7bd-ebd092fabb56 | -4.36896 | -37.89758 | 2026-05-21 04:04:00 | NPP-375D | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 3ffa3f8d-1ab6-3db3-af8c-dc27ef16bb4a | -6.75261 | -45.01522 | 2026-05-21 04:04:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 39b4715b-da45-32cb-8803-61c53ae57975 | -8.62488 | -45.98012 | 2026-05-21 04:04:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 8b7bc44d-dbcf-3421-b72d-2a7cb01bc543 | -11.01838 | -42.86409 | 2026-05-21 04:04:00 | NPP-375D | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 3fc91de7-7e1b-30da-9b3a-063d6c7e7f21 | -9.32902 | -40.21334 | 2026-05-21 04:04:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 566dd8ff-9e5b-37a7-bedd-9c5cf9063c3f | -10.65104 | -42.30091 | 2026-05-21 04:04:00 | NPP-375D | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| d66f7e8e-8c69-32ca-9368-ed290b92201d | -8.60161 | -45.95204 | 2026-05-21 04:04:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b04ad6fb-370e-3c63-972d-7d8b6c1788ec | -4.47686 | -37.81526 | 2026-05-21 04:04:00 | NPP-375D | FORTIM | CEARÁ | Brasil | 2304459 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 7ed41ddb-6e1f-350b-b1cb-c74120ed2320 | -10.0938 | -46.53919 | 2026-05-21 04:04:00 | NPP-375D | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 9b5b2f56-1bcc-3ce4-8322-400fd229715b | -7.0164 | -45.41307 | 2026-05-21 04:04:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7f6a61f2-7de7-3430-94b8-a5e14e184daa | -9.30238 | -45.49207 | 2026-05-21 04:04:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 23.1 |
| 48083b3b-f202-3ea4-bcbe-722a0299199b | -9.33238 | -40.21389 | 2026-05-21 04:04:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 2c462448-48f0-31f3-8aa9-6dd2b44f108e | -9.31039 | -45.49799 | 2026-05-21 04:04:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 0031a2a6-71d2-3b1a-9180-5f244a9769ca | -4.47632 | -37.81873 | 2026-05-21 04:04:00 | NPP-375D | FORTIM | CEARÁ | Brasil | 2304459 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 5f07da3e-a990-3c4d-a3ab-b546b8c1783a | -6.3022 | -43.6383 | 2026-05-21 04:04:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 365ecf1b-f0ad-32ff-af8a-4f6c2444d9dd | -5.94939 | -43.48941 | 2026-05-21 04:04:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c5a69bfd-d80d-302e-a25a-c8f6d523be27 | -6.7563 | -45.02021 | 2026-05-21 04:04:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9eb52903-1198-3cb0-bb2c-42e4841bd31a | -5.95345 | -43.49006 | 2026-05-21 04:04:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 9e910296-5a8c-3c45-ae34-d1a7dbf7066a | -11.02202 | -42.86471 | 2026-05-21 04:04:00 | NPP-375D | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| d8fb27d3-cfed-3837-b8f9-721d677053a3 | -15.06936 | -42.37767 | 2026-05-21 04:06:00 | NPP-375D | MORTUGABA | BAHIA | Brasil | 2921807 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 66fb6a35-ef97-3216-92df-8e91562c21aa | -12.2295 | -44.26023 | 2026-05-21 04:06:00 | NPP-375D | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d908d06b-e8d2-397f-8ab2-ba3a40062b67 | -12.00019 | -45.13992 | 2026-05-21 04:06:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 7.9 |
| c253d6e7-e296-3151-9c50-28f2fee0d786 | -12.22819 | -46.60905 | 2026-05-21 04:06:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b225bae2-fd07-3151-80f3-f7726f5baec6 | -12.81192 | -44.87132 | 2026-05-21 04:06:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 875b5b14-d5d8-3914-89af-a68d01efcad6 | -9.96087 | -52.45304 | 2026-05-21 04:06:00 | NPP-375D | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c43c6c8d-5205-303c-9a5d-4328210b36a5 | -11.33724 | -48.00827 | 2026-05-21 04:06:00 | NPP-375D | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| bab71e5c-21e1-34a4-bc07-ae2339f08c56 | -16.89675 | -46.787 | 2026-05-21 04:06:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5da43b09-be0d-34ef-bbc5-7e5f946fe89d | -13.02728 | -49.94469 | 2026-05-21 04:06:00 | NPP-375D | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| eab744d8-c356-350a-a4e3-73027d95dafb | -11.03814 | -48.91547 | 2026-05-21 04:06:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b782cc2d-6731-3a16-af30-9adc9bbb2f39 | -11.48163 | -52.9227 | 2026-05-21 04:06:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6b13d056-71a2-34c7-a8cb-d3a830c5ba4c | -14.90083 | -47.74505 | 2026-05-21 04:06:00 | NPP-375D | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 52d71640-f985-3667-adba-32f6413cd997 | -11.65333 | -47.59073 | 2026-05-21 04:06:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 75813c31-a8c1-39f3-b5b8-179d92e95ac1 | -14.9054 | -47.74616 | 2026-05-21 04:06:00 | NPP-375D | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 42e8d994-b668-3b08-a5af-9573c0fa9ee7 | -13.02485 | -49.93344 | 2026-05-21 04:06:00 | NPP-375D | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a19f918e-0a1e-355c-9bcf-26fd228cbec3 | -16.35463 | -43.87766 | 2026-05-21 04:06:00 | NPP-375D | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 4.4 |
| daad9cf4-649d-3f7a-a49a-78cd00473724 | -12.05837 | -45.28952 | 2026-05-21 04:06:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4237b3a3-eded-3cd0-bc1e-1f54172da6b1 | -13.28472 | -50.2848 | 2026-05-21 04:06:00 | NPP-375D | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bc40a70c-548c-31fb-8289-eeaae7c61e27 | -14.90448 | -47.75092 | 2026-05-21 04:06:00 | NPP-375D | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 36d02055-e21c-33e0-b00c-a6bcbd58f3af | -11.32371 | -47.56441 | 2026-05-21 04:06:00 | NPP-375D | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a858ee3d-ab9f-3a67-bfc0-b2826bdd0c98 | -11.4749 | -52.92115 | 2026-05-21 04:06:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c0e100d2-de65-3f19-b74b-4450aab7eb90 | -10.49362 | -49.36342 | 2026-05-21 04:06:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| d3d0ed33-996b-3706-9580-32a804d1f99e | -10.48809 | -49.36225 | 2026-05-21 04:06:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 46c90a62-2c91-3935-a1b2-206868ba60fd | -13.03438 | -49.94323 | 2026-05-21 04:06:00 | NPP-375D | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 23f6eda4-d4d7-3d64-bcda-60208f89d905 | -10.3981 | -49.44999 | 2026-05-21 04:06:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7bf6b662-30a1-388f-8c4c-66a18dda75ba | -11.34331 | -48.00345 | 2026-05-21 04:06:00 | NPP-375D | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b1e2119f-b969-37d6-a9f6-0423bab268fd | -14.00934 | -47.50768 | 2026-05-21 04:06:00 | NPP-375D | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fe377337-b091-37c9-8d71-cb45c7075d73 | -10.48737 | -49.36597 | 2026-05-21 04:06:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 2f1467fb-8429-3ae2-a942-de87b4b70937 | -14.01398 | -47.50846 | 2026-05-21 04:06:00 | NPP-375D | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e6f348ab-08fb-3714-85b8-d8162d866f04 | -11.46938 | -52.9211 | 2026-05-21 04:06:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b71f1fbb-3c39-3e9b-9377-27888e767b48 | -11.46816 | -52.91962 | 2026-05-21 04:06:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| aacfb3bc-4736-38fd-b3fb-80550ea71ff4 | -11.03279 | -48.91449 | 2026-05-21 04:06:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| db6013f0-d9bc-34ac-b39e-994f0c04331c | -13.03352 | -49.94213 | 2026-05-21 04:06:00 | NPP-375D | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9cd8abec-2dd3-3dc5-b607-56094ef9cd5b | -10.49432 | -49.35979 | 2026-05-21 04:06:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 7e9f559f-8203-3787-858d-e3b176b9064b | -10.39252 | -49.44883 | 2026-05-21 04:06:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d7b46f8f-05fa-3066-a286-6340d4277543 | -9.95334 | -52.46054 | 2026-05-21 04:06:00 | NPP-375D | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9e0bc8c5-21ce-334f-876c-a9aa07a67241 | -13.03035 | -49.93457 | 2026-05-21 04:06:00 | NPP-375D | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ff00e097-c086-39c5-909e-b8ac9a99f305 | -13.02557 | -49.92976 | 2026-05-21 04:06:00 | NPP-375D | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 43f5b857-f2b6-36ad-b45a-dcd13c7dbb59 | -12.0577 | -45.29328 | 2026-05-21 04:06:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6a82acc8-0afa-3aa0-b694-32e71689cc7a | -11.65456 | -47.59513 | 2026-05-21 04:06:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e2ec99c4-e6e8-3028-8b60-0c4569c8441a | -11.9614 | -43.38555 | 2026-05-21 04:06:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ec835681-d1f4-31e4-952d-5a8249f08490 | -11.47611 | -52.92262 | 2026-05-21 04:06:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5d999fd6-2751-3e57-8940-ba0cd04ee2de | -11.95696 | -43.38931 | 2026-05-21 04:06:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d3e833c3-4138-3846-ac79-01b123d8a236 | -11.76223 | -48.28587 | 2026-05-21 04:06:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 303a9b39-6085-356f-988a-7d5ba60c9507 | -9.94656 | -52.45931 | 2026-05-21 04:06:00 | NPP-375D | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e6233d70-d0b0-3824-bb8a-5395b67ce594 | -14.22755 | -43.65492 | 2026-05-21 04:06:00 | NPP-375D | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b7d7ec98-3264-3eb4-b5a7-1bc6324ed1df | -15.09089 | -41.15765 | 2026-05-21 04:06:00 | NPP-375D | BELO CAMPO | BAHIA | Brasil | 2903508 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| f71b7737-d27c-3c25-9a55-0f5a0aa5335d | -10.45639 | -47.93686 | 2026-05-21 04:06:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 967bd7c7-fcc2-3432-b6b4-d32213370db6 | -10.49292 | -49.36708 | 2026-05-21 04:06:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 3d026afd-e81e-3300-b58e-6e018872abc1 | -14.69387 | -41.35848 | 2026-05-21 04:06:00 | NPP-375D | CARAÍBAS | BAHIA | Brasil | 2906899 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| f623906b-8446-34b1-a49a-e0fdae98211f | -9.94613 | -52.45652 | 2026-05-21 04:06:00 | NPP-375D | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 891d4a88-603b-3660-a538-a41f19b2dc2d | -14.62844 | -48.0337 | 2026-05-21 04:06:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2117969c-54b6-38ce-9f27-085ed5baaf27 | -14.63405 | -48.03 | 2026-05-21 04:06:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| fe2a2330-f0cf-3eff-9024-11ac8443a6b9 | -14.89991 | -47.74979 | 2026-05-21 04:06:00 | NPP-375D | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| bc272793-0886-3460-a825-ecfbf732cfb4 | -10.39883 | -49.44614 | 2026-05-21 04:06:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a7ea1843-1920-3549-a57b-b63f20b34360 | -14.62946 | -48.02842 | 2026-05-21 04:06:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6cb482ed-ba8c-3183-afd4-b3400cbaddb1 | -10.32877 | -53.5821 | 2026-05-21 04:06:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 78cd1ea2-49d2-3bdb-8031-0161ca45ceff | -12.43891 | -47.41716 | 2026-05-21 04:06:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e458399a-65f8-3b69-9291-be2a43d3049e | -11.46263 | -52.91966 | 2026-05-21 04:06:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c31e0a36-dd32-3d82-a971-8af223e471b1 | -9.9529 | -52.4578 | 2026-05-21 04:06:00 | NPP-375D | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 05a4c6c0-1c2c-33b1-96a3-665896823b7a | -15.06999 | -42.37384 | 2026-05-21 04:06:00 | NPP-375D | MORTUGABA | BAHIA | Brasil | 2921807 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| b0685c93-8310-3671-ac4f-2b7e966d45f3 | -13.02954 | -49.93354 | 2026-05-21 04:06:00 | NPP-375D | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 307562d4-93f3-36cc-9e4f-4c9794f37d11 | -9.96134 | -52.45581 | 2026-05-21 04:06:00 | NPP-375D | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9c69647e-3555-3a7b-a993-3133e59b9dab | -11.96067 | -43.38988 | 2026-05-21 04:06:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 69f871ef-f0cd-31c9-bbb5-851bd9d93fde | -14.70971 | -39.58948 | 2026-05-21 04:06:00 | NPP-375D | ALMADINA | BAHIA | Brasil | 2900900 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 99a1e924-b3ab-39e3-a3cc-712892488139 | -13.2911 | -50.28199 | 2026-05-21 04:06:00 | NPP-375D | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 26a2a1a6-a601-3651-94c5-dcc7030f5720 | -12.22864 | -44.26517 | 2026-05-21 04:06:00 | NPP-375D | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 537d3b0e-1de6-338e-b032-9a0853e0da68 | -12.06249 | -45.29029 | 2026-05-21 04:06:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |


[Clique aqui para ver as próximas entradas](README5.md)
