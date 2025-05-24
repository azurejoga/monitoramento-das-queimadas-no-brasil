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

## Dados Diários - Página 10

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f2b878af-47da-348c-be79-e791c6716e0a | -14.06147 | -57.11342 | 2025-05-24 04:08:00 | NOAA-20 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 819d82eb-f7ea-3d69-a3b4-75152c634b4d | -11.74981 | -54.22742 | 2025-05-24 04:08:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 57c8a31b-1d71-330e-9d83-0797d4e4eece | -11.41743 | -54.30541 | 2025-05-24 04:08:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| db4a180a-6480-32fa-ae15-620f222b1e1a | -12.39187 | -49.97743 | 2025-05-24 04:08:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 46d6bade-012e-3405-99ea-f53e4c356de0 | -12.13361 | -54.65707 | 2025-05-24 04:08:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a93d96c7-bcdc-3607-b8e8-7321dd84ea26 | -10.72287 | -52.47142 | 2025-05-24 04:08:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 7dfd0b7e-b219-3f33-a0ac-9bc7d3c356df | -16.05599 | -42.25538 | 2025-05-24 04:08:00 | NOAA-20 | SALINAS | MINAS GERAIS | Brasil | 3157005 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| a6f0d7cc-6a83-3c5a-915f-abf9d8aa8b89 | -13.19217 | -53.57799 | 2025-05-24 04:08:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 9146d598-182a-3676-8329-62668bd5f55f | -10.52731 | -47.58277 | 2025-05-24 04:08:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 21fa35e9-9dfe-39e3-91cf-19fe89719560 | -12.13264 | -54.6619 | 2025-05-24 04:08:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| cfd4236d-f9af-3e55-9382-bbf08f1ae0df | -10.94641 | -48.15245 | 2025-05-24 04:08:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8dfe9563-ff37-3578-b417-03fe09afac46 | -14.02629 | -55.13477 | 2025-05-24 04:08:00 | NOAA-20 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2bc6bb01-13e3-315f-a142-01bba2323096 | -13.14535 | -56.81543 | 2025-05-24 04:08:00 | NOAA-20 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 07dfccfc-50a6-353b-994f-f02d6eeb0c30 | -12.37919 | -49.99519 | 2025-05-24 04:08:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 99bb6551-955b-39e0-bde2-7cdc59b25e74 | -15.0782 | -48.94325 | 2025-05-24 04:08:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 8f2eb29f-b82a-3956-85c8-5a2ebcfe330a | -12.34937 | -49.92469 | 2025-05-24 04:08:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c05368cc-354a-3852-b8a5-4bfa6267ee06 | -12.3756 | -49.98522 | 2025-05-24 04:08:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 42a2e012-5282-37a0-bd66-6702fa2c2e9a | -10.46924 | -47.94496 | 2025-05-24 04:08:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| a1453d0d-386d-3e23-a96f-0e3dd38187ed | -12.0677 | -47.34767 | 2025-05-24 04:08:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c75b19cb-10a9-3465-a547-3ac5985d6006 | -10.46295 | -47.94375 | 2025-05-24 04:08:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e28f3148-ff25-317a-9d2f-bff689c63e19 | -10.53434 | -55.72153 | 2025-05-24 04:08:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| ee9c9f3c-08b0-3a64-8afd-529bbfed79b5 | -13.45814 | -47.48233 | 2025-05-24 04:08:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 19efeb71-ce10-3bd4-aaf9-406954d2bc76 | -12.35765 | -49.93114 | 2025-05-24 04:08:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| dc883e53-93fa-383c-99ad-d7dc3136914f | -10.72218 | -52.47515 | 2025-05-24 04:08:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 08779fe0-1d71-34aa-accd-e01e2dd98220 | -10.46362 | -47.93999 | 2025-05-24 04:08:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 078d01ba-349f-34db-b3b9-d99a22731058 | -12.37433 | -47.32269 | 2025-05-24 04:08:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6a02c1f8-a827-3981-9447-0547b91d63d9 | -13.19277 | -53.58065 | 2025-05-24 04:08:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b03857dc-3841-39d8-97af-6b72d8b1fe2b | -17.56208 | -42.05276 | 2025-05-24 04:08:00 | NOAA-20 | NOVO CRUZEIRO | MINAS GERAIS | Brasil | 3145307 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| d8790828-3411-37bb-9ef4-1434e3d037ea | -12.35309 | -49.93024 | 2025-05-24 04:08:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 493f7ce1-7ac4-3275-9013-7164c09a574a | -10.71515 | -48.82704 | 2025-05-24 04:08:00 | NOAA-20 | OLIVEIRA DE FÁTIMA | TOCANTINS | Brasil | 1715507 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e0b4f561-458d-30d8-9d4e-ba24cbf15d74 | -11.47333 | -48.02666 | 2025-05-24 04:08:00 | NOAA-20 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0b120d13-dbda-3760-803c-44c4abd65beb | -13.45901 | -47.47731 | 2025-05-24 04:08:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7383be93-a6a8-3edd-9ad9-69597ca99a43 | -12.07505 | -48.45614 | 2025-05-24 04:08:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 87896015-1236-3313-a6c3-925b4c8bcd8b | -12.39101 | -49.98225 | 2025-05-24 04:08:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 04919599-4c20-3dfc-9bc9-22ea9b74036d | -10.36453 | -47.98138 | 2025-05-24 04:08:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 25236bba-fa7c-37ca-b75b-89c3c0c023ea | -13.19194 | -53.58469 | 2025-05-24 04:08:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 39f3cc58-a112-3c15-920a-2d3a38069684 | -13.19137 | -53.58204 | 2025-05-24 04:08:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 49d9acf1-d653-3b95-b3c4-58f270ed77d5 | -12.37636 | -49.9846 | 2025-05-24 04:08:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| df47632d-f494-3662-a723-f8168234d743 | -13.15083 | -56.82355 | 2025-05-24 04:08:00 | NOAA-20 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 2ae31e16-16ca-3076-86e6-bc5d5e75a0a7 | -17.78188 | -42.80698 | 2025-05-24 04:08:00 | NOAA-20 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4539811b-183d-3e22-91f2-dd5183358503 | -17.37958 | -42.48232 | 2025-05-24 04:08:00 | NOAA-20 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| eb7e0d9c-362b-35be-8537-036534bcc81b | -10.36799 | -47.98606 | 2025-05-24 04:08:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| dee3f493-c930-3338-b8f7-f8935d013643 | -12.39487 | -49.9837 | 2025-05-24 04:08:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f7dbe1f0-5e51-3db3-9773-b03023b7df23 | -14.06953 | -57.11355 | 2025-05-24 04:08:00 | NOAA-20 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 43ed2c5b-0362-3ab5-9724-ae63dd3d3775 | -12.07072 | -47.35339 | 2025-05-24 04:08:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| a5e4497e-6247-37e3-9e92-4d54e3b360e7 | -14.01293 | -55.13696 | 2025-05-24 04:08:00 | NOAA-20 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 25d2e298-935e-3631-aa9e-3e4b38417afd | -12.07159 | -47.34836 | 2025-05-24 04:08:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 9.6 |
| ebb69a75-38e8-37cc-a782-6c5ff686fa85 | -17.67665 | -42.74047 | 2025-05-24 04:08:00 | NOAA-20 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 9e913600-1b3f-3a43-af34-2b1d2c5194b4 | -12.37928 | -49.99091 | 2025-05-24 04:08:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f1e50e4c-de5f-32ed-b174-bd2d0218084a | -13.00507 | -46.66481 | 2025-05-24 04:08:00 | NOAA-20 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1bf1930a-f530-3a71-834d-793a6c5052e0 | -14.01909 | -55.13832 | 2025-05-24 04:08:00 | NOAA-20 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 50f7e463-2db0-3a69-8044-63a6a3676023 | -12.38095 | -49.98543 | 2025-05-24 04:08:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a93ec57d-c242-3103-babd-96341af46b35 | -14.06299 | -57.10664 | 2025-05-24 04:08:00 | NOAA-20 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 058162db-caa6-356c-8d38-42d6a2b30fc7 | -12.27565 | -44.60041 | 2025-05-24 04:08:00 | NOAA-20 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e3f157c3-28e8-3799-89c6-75b437776f3f | -15.62596 | -57.31292 | 2025-05-24 04:08:00 | NOAA-20 | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a8847d82-a38d-33ad-a54b-a2304da1653d | -14.6734 | -48.11427 | 2025-05-24 04:08:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ffd75e23-c3aa-3283-94cf-6032f32c0ce2 | -12.4058 | -49.97599 | 2025-05-24 04:08:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| c00f6197-0d9c-3e09-aa06-f82781b830ec | -15.11907 | -43.93755 | 2025-05-24 04:08:00 | NOAA-20 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e0ab3722-8ece-3cb2-8164-7dd7c4edbd67 | -14.06271 | -57.11163 | 2025-05-24 04:08:00 | NOAA-20 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| a4fa8a6c-f4cc-39c8-bd52-50977a4e0969 | -15.7469 | -43.48863 | 2025-05-24 04:08:00 | NOAA-20 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b79cb214-252b-390a-83bb-659ca33a85d6 | -12.34851 | -49.92941 | 2025-05-24 04:08:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 61c1c983-6114-39f9-8869-02cf0729db50 | -11.7939 | -44.28557 | 2025-05-24 04:08:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0412ee1f-393c-3345-b91f-ae52df416cd7 | -11.76247 | -54.22747 | 2025-05-24 04:08:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a826b5b5-fd7c-35c1-91bb-ec1326074ef9 | -13.77774 | -54.30772 | 2025-05-24 04:08:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b55eb07f-5666-3ad3-baa8-4be7bde61e1f | -12.83731 | -47.39085 | 2025-05-24 04:08:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 538bc572-5bd1-3ac4-b977-abb2e64f23dd | -12.35222 | -49.93499 | 2025-05-24 04:08:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f916ac95-c113-3eb2-aff9-e363e6bae8ac | -12.07548 | -47.34905 | 2025-05-24 04:08:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 3a006aa5-8428-345e-a4ba-37190b531afe | -12.84233 | -47.39294 | 2025-05-24 04:08:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a0e8bd77-3cba-357b-a612-bd59192ce8ff | -14.03347 | -55.13129 | 2025-05-24 04:08:00 | NOAA-20 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b73453c4-0660-36c1-af88-0318e17571d5 | -11.62107 | -47.99679 | 2025-05-24 04:08:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 24c18322-dfe7-305b-86ff-78bb2bdfa46a | -12.38467 | -49.99115 | 2025-05-24 04:08:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9fb312a6-7190-3209-8b3e-b105f441e9fb | -16.30225 | -42.77449 | 2025-05-24 04:08:00 | NOAA-20 | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 9403710e-9926-3f40-9cde-48e638a0760f | -15.62661 | -57.31315 | 2025-05-24 04:08:00 | NOAA-20 | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e64f7a4e-cf4a-377f-85c9-3c96ef0cd9eb | -10.95057 | -48.15325 | 2025-05-24 04:08:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 82f431cd-c177-33d2-96a5-8907f7bf817e | -13.20108 | -47.27954 | 2025-05-24 04:08:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| d6f393f2-c022-3251-ab90-03a754cf6384 | -11.47743 | -48.02742 | 2025-05-24 04:08:00 | NOAA-20 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6526d708-98d7-391c-91d3-476c08059fd1 | -12.13732 | -54.6594 | 2025-05-24 04:08:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 21f5d30a-0d1d-3808-aab9-e74ce8f2b9c1 | -10.36661 | -47.96973 | 2025-05-24 04:08:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c6005160-64c6-34d3-afd5-bca0b7526103 | -13.14673 | -56.80899 | 2025-05-24 04:08:00 | NOAA-20 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 8.0 |
| bfcf8964-41cc-3a62-a742-4fab4a848db6 | -12.35851 | -49.92643 | 2025-05-24 04:08:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 67538120-b38b-3569-9708-db215bbc51ec | -10.36523 | -47.97747 | 2025-05-24 04:08:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| eda278ac-3e83-3b52-a7d4-d0f90ec9ecd2 | -13.15359 | -56.81066 | 2025-05-24 04:08:00 | NOAA-20 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 8.0 |
| dfcf04b3-0d33-3204-b51d-3b9e686cb118 | -10.87768 | -45.07309 | 2025-05-24 04:08:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 133331bb-e076-3740-9dfd-93c4a3d15d93 | -13.15203 | -56.8135 | 2025-05-24 04:08:00 | NOAA-20 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 16.3 |
| 960b8350-5bd3-31b9-ba7d-67ace6f571cb | -10.36384 | -47.9853 | 2025-05-24 04:08:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 05f3fb51-355c-34c1-b9c5-01abfbf211e6 | -12.07937 | -47.34975 | 2025-05-24 04:08:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 64b77a77-94fb-34a8-a9ac-3332c1db3303 | -12.39029 | -49.98286 | 2025-05-24 04:08:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| dfcb1ec0-f438-3933-9cc4-df9ab929c51f | -13.67246 | -53.9386 | 2025-05-24 04:08:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| bd6cfc1c-15d1-3209-b414-09c3f6f32a59 | -17.86904 | -45.54485 | 2025-05-24 04:08:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c7b6f305-89e9-3abb-9eb5-7f8f6dcaa683 | -10.72144 | -52.47145 | 2025-05-24 04:08:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 10b7a8a1-4cb7-3cce-bc28-ee2279cbd1b5 | -14.06829 | -57.11527 | 2025-05-24 04:08:00 | NOAA-20 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 830c22db-c2aa-3142-a0e2-d87c899b335c | -12.07436 | -48.46 | 2025-05-24 04:08:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2a181c49-ffd0-369b-b8f5-ce24a427c663 | -10.7426 | -49.28525 | 2025-05-24 04:08:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d26b4d10-2bcd-39d0-8ba0-ecf632bd3d29 | -12.37549 | -49.98944 | 2025-05-24 04:08:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e88c5055-a6e5-3b63-a86b-db8ee11a13e7 | -13.78365 | -54.30895 | 2025-05-24 04:08:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 150cdfe5-63bc-36f6-906f-3fab5f2c7030 | -12.40491 | -49.98075 | 2025-05-24 04:08:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 68b31eb3-a5f9-30fc-bea9-2857b35e945f | -12.40403 | -49.98549 | 2025-05-24 04:08:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 3d0a008e-8e71-373d-9a17-bf9f1d0aac06 | -13.9875 | -56.01647 | 2025-05-24 04:08:00 | NOAA-20 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ec8cadbe-28b4-3cb2-b633-cdc6a9473a99 | -12.38182 | -49.98061 | 2025-05-24 04:08:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 25092eef-2f04-3e4e-886b-9c9d6d1430ea | -13.58108 | -47.35471 | 2025-05-24 04:08:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |


[Clique aqui para ver as próximas entradas](README11.md)
