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

## Dados Diários - Página 11

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b647a5e0-22e2-3947-bc97-abb91ae30edf | -10.06049 | -59.09744 | 2025-07-23 04:34:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 4c7adfb9-2569-38c4-b9e2-3256876902ed | -10.64034 | -45.22908 | 2025-07-23 04:34:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 33c5bb43-e5ca-3760-af7d-a105d6ce4432 | -13.70156 | -45.70139 | 2025-07-23 04:34:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1194fc9a-4ea5-3d19-936c-0b83ee84d932 | -9.06816 | -45.06297 | 2025-07-23 04:34:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 52036284-92d5-38e7-81b8-bdd1494ec5ae | -11.25962 | -47.82101 | 2025-07-23 04:34:00 | NOAA-21 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| fa56b997-b754-325e-9302-562f8d50feef | -13.54376 | -43.70931 | 2025-07-23 04:34:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 7fd1d52d-19e1-39e8-9a78-4b921dd48338 | -13.71416 | -45.69376 | 2025-07-23 04:34:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| b63cc44b-60ed-308d-a333-b8bf42332217 | -8.09157 | -50.09172 | 2025-07-23 04:34:00 | NOAA-21 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c2508dce-d68d-3786-b4bb-801c1a197a0b | -8.73353 | -49.48402 | 2025-07-23 04:34:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2b56ce74-faba-3c43-90db-ca5a26391bb4 | -7.23555 | -44.78821 | 2025-07-23 04:34:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| bf1e64e0-0959-3dc5-8b47-8253bee3d15c | -7.25833 | -44.30374 | 2025-07-23 04:34:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 75113df9-6f20-3b4f-8bb0-d0d0ffe4c745 | -13.6775 | -44.22342 | 2025-07-23 04:34:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b11a8870-1f67-3f21-ab4f-7fc4ce541386 | -12.30105 | -50.99973 | 2025-07-23 04:34:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a7d0900c-66b2-3f84-b755-0496b0b2af18 | -7.22277 | -49.59251 | 2025-07-23 04:34:00 | NOAA-21 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| fb601f9a-0565-3874-b88a-2b1c95c51a8a | -7.281 | -47.53315 | 2025-07-23 04:34:00 | NOAA-21 | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 78cbd8e3-4ca1-386f-98d7-0009574a9ddb | -10.43265 | -54.37547 | 2025-07-23 04:34:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 15fe6ff3-1d89-3ffd-92d4-8c48b2dc0d39 | -7.25899 | -44.29923 | 2025-07-23 04:34:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 402d382f-eb0c-3fb2-9748-66ce894e62ad | -9.7345 | -48.02158 | 2025-07-23 04:34:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8aacb454-4063-31c2-bca1-4d023a79c9d8 | -7.6157 | -49.49365 | 2025-07-23 04:34:00 | NOAA-21 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| ac4d02fb-eca2-3dd0-8b60-a98174ce0cb8 | -8.91571 | -47.36007 | 2025-07-23 04:34:00 | NOAA-21 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1e048f17-f925-359c-b959-5fcbc244e26b | -7.76355 | -44.02633 | 2025-07-23 04:34:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 4.8 |
| f05ca318-a2aa-3d9d-936e-50880651af26 | -8.08935 | -50.08392 | 2025-07-23 04:34:00 | NOAA-21 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6539e08d-9543-37db-877e-58b1dff49db5 | -14.20939 | -43.95367 | 2025-07-23 04:34:00 | NOAA-21 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| efb14bc9-5cf4-3327-ab43-e7dfc4ddb9f6 | -7.04928 | -45.85263 | 2025-07-23 04:34:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| b5ee95d1-9aed-37f4-9261-7ae37038f5be | -7.74576 | -44.0136 | 2025-07-23 04:34:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 744f6cd9-d7a9-382a-a532-6d22cc4eefb0 | -7.14559 | -46.09663 | 2025-07-23 04:34:00 | NOAA-21 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 60441837-ec28-33eb-96b6-67708b42cdd1 | -10.64405 | -45.22967 | 2025-07-23 04:34:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 0a945086-ff6e-3e2d-b58d-5e0dd50c8c4e | -12.50087 | -57.77226 | 2025-07-23 04:34:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 59b06675-177a-3532-95dd-a1ce1ceb0e66 | -9.33346 | -49.8395 | 2025-07-23 04:34:00 | NOAA-21 | CASEARA | TOCANTINS | Brasil | 1703909 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f7f3c515-fb0b-3531-8a82-ea26d5b20e87 | -9.85801 | -44.59777 | 2025-07-23 04:34:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 85f97f8a-8a89-3376-82d7-34c62b937e4e | -13.6532 | -45.71783 | 2025-07-23 04:34:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 85006d34-2eab-393b-a7cd-fa0824e0975d | -7.26182 | -60.18252 | 2025-07-23 04:34:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 689d5d73-3803-35b3-ae45-a437373ab428 | -10.26384 | -48.31416 | 2025-07-23 04:34:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| e4aab7d7-c2c1-37c5-b41f-e83f9b62de40 | -10.68509 | -47.20868 | 2025-07-23 04:34:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 92cd535c-17f0-30d0-b784-ab84b0381ff7 | -8.28957 | -44.97045 | 2025-07-23 04:34:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6a2838cc-1c97-37c6-bb2a-17df598da6a0 | -7.91536 | -49.64812 | 2025-07-23 04:34:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ec5e306a-116d-34fa-8286-63af37830763 | -7.75517 | -44.02989 | 2025-07-23 04:34:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 25010d3c-5a6e-3bf8-8627-a0227f5b9638 | -13.70598 | -45.69728 | 2025-07-23 04:34:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 3f184d70-6503-37f3-9ea7-69b8640bbecd | -7.7496 | -44.0143 | 2025-07-23 04:34:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 6.7 |
| fc365688-b1b8-3d83-a0ff-51eaf690c1e9 | -7.5227 | -45.37661 | 2025-07-23 04:34:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cc64f61d-816c-3623-964a-4ccea75019c4 | -9.60966 | -43.8737 | 2025-07-23 04:34:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| c6f77661-a4b6-378c-b98c-b34f1cb040c1 | -10.3642 | -48.23618 | 2025-07-23 04:34:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 43fb9881-249b-3ad6-bf7e-1bdf9b60488a | -9.74405 | -48.57567 | 2025-07-23 04:34:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 7fdd425e-7b83-3211-872a-b6bc30945d2b | -7.04698 | -45.84436 | 2025-07-23 04:34:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| afd76800-54f5-3ef6-ae25-30d6d5b4e373 | -7.74889 | -44.01911 | 2025-07-23 04:34:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 1af32197-5160-3f89-a42c-a36d1818b978 | -7.27967 | -44.54517 | 2025-07-23 04:34:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3cc98f66-fa1b-3fc2-987b-dc425fccba31 | -12.68259 | -46.82936 | 2025-07-23 04:34:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 75dfd62a-af5b-30c2-b7c7-f1375cb4e849 | -9.20739 | -49.6728 | 2025-07-23 04:34:00 | NOAA-21 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4811ba8a-2850-3a6c-87c4-34790fa21c65 | -7.75657 | -44.02038 | 2025-07-23 04:34:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 6.8 |
| b90cfa9f-ebf0-3d9e-b602-81726b317d1c | -10.06122 | -59.09353 | 2025-07-23 04:34:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 2d2daeb9-9f80-3d3c-847d-b1362d98e941 | -14.21309 | -43.95829 | 2025-07-23 04:34:00 | NOAA-21 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 44c3a824-8110-3d98-b8a7-6bdf0899ede9 | -13.69779 | -45.70083 | 2025-07-23 04:34:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 202f4d4d-aa38-3c6a-93ac-9afa71186857 | -12.32659 | -49.99656 | 2025-07-23 04:34:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 24030aec-df1a-3830-9fcf-d1f5842fdc68 | -13.09759 | -46.83566 | 2025-07-23 04:34:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f23b7792-0e76-3bd2-8241-2202e054d083 | -7.53934 | -45.36274 | 2025-07-23 04:34:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1e3787e5-5202-35ad-9bf2-d856e8a9b77a | -10.6329 | -45.22796 | 2025-07-23 04:34:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1845f5f3-47cf-3c4c-aec5-37ad6ea28c4f | -9.11695 | -60.75031 | 2025-07-23 04:34:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 8.4 |
| d67eed50-7e67-39f0-9566-76351359ad63 | -8.20111 | -46.98952 | 2025-07-23 04:34:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 24df2b20-8e69-35c8-81ba-ade02a2dec26 | -10.04277 | -59.09831 | 2025-07-23 04:34:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ef9fee62-02ca-337e-94cd-b06e90ccc8c9 | -7.25038 | -44.27926 | 2025-07-23 04:34:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 1bd74ed6-af31-30fb-a438-663e29906058 | -10.88902 | -44.36906 | 2025-07-23 04:34:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1655fecb-72f1-37fd-a01b-2191247c54d3 | -9.1151 | -60.74839 | 2025-07-23 04:34:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| d8e81c12-91c8-33ac-b098-851a4b56e46b | -10.43975 | -56.62717 | 2025-07-23 04:34:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e933c588-9069-38b7-80e7-912c82e43b3b | -10.62918 | -45.22742 | 2025-07-23 04:34:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c81efc40-f0d6-37f8-a580-81669b79d847 | -9.06385 | -45.0668 | 2025-07-23 04:34:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| aa88b604-04a8-3701-8c36-568673ddf14a | -7.27215 | -44.366 | 2025-07-23 04:34:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 010b8d9b-82fd-339e-9ced-a666a500f937 | -13.72169 | -45.69487 | 2025-07-23 04:34:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e0bcc9d6-8769-3ab4-98d8-65f4867e384d | -12.49445 | -57.77553 | 2025-07-23 04:34:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 87ab7a3e-028f-357f-8191-e49d0995728d | -7.26909 | -60.17858 | 2025-07-23 04:34:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 42387c30-2608-3817-8495-3ba2cf5a3e12 | -8.05777 | -49.97024 | 2025-07-23 04:34:00 | NOAA-21 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 95a05a63-4923-3a84-98c1-0228113695ea | -12.50194 | -57.7667 | 2025-07-23 04:34:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 3711cbd6-0cd2-3518-9acc-955159df7c7a | -7.88752 | -45.55231 | 2025-07-23 04:34:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| dfe3bbb3-2798-3bc0-b375-6e64d01deac2 | -7.14501 | -46.1004 | 2025-07-23 04:34:00 | NOAA-21 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 8165d824-e387-30c3-a528-5bc85e3754be | -9.06448 | -45.06241 | 2025-07-23 04:34:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 5.9 |
| bd7732e0-2658-324c-8dd0-8b6f26611599 | -12.49551 | -57.76984 | 2025-07-23 04:34:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 7b2e32bb-324f-3336-bc60-ae980f1b9b90 | -13.69093 | -45.69504 | 2025-07-23 04:34:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| aebf8b80-857d-32be-9238-05266bc0fca2 | -7.02155 | -45.84815 | 2025-07-23 04:34:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 68cc6fcf-d3d5-3d5d-a388-0eef9cfe7164 | -7.27927 | -43.09566 | 2025-07-23 04:34:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| effd0962-b04d-3ed4-a3da-36dfef6ad3c0 | -7.8934 | -45.55993 | 2025-07-23 04:34:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 138b188f-a00e-3235-9196-8867c1859f72 | -6.94844 | -51.63913 | 2025-07-23 04:34:00 | NOAA-21 | TUCUMÃ | PARÁ | Brasil | 1508084 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 06f0b436-fef6-3b59-989c-4099ccc9f183 | -9.67593 | -43.72475 | 2025-07-23 04:34:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 151e345a-494b-314e-9997-f4032cbd89c2 | -12.66131 | -45.04359 | 2025-07-23 04:34:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e6b6cc99-0f53-39e6-9183-2364739ad630 | -14.18481 | -45.34024 | 2025-07-23 04:34:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ec8f3c8f-16d3-3c6f-b241-1f6af94ead9d | -8.19477 | -50.21383 | 2025-07-23 04:34:00 | NOAA-21 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| b8bc2a35-d5ce-3b63-bf4a-8f4537bbb51c | -7.94113 | -44.84775 | 2025-07-23 04:34:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 09a0d42a-6916-35b4-8864-b5dc5c39b005 | -7.20389 | -45.33157 | 2025-07-23 04:34:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| df9291a6-10e4-30d8-ab39-3a92f1f13592 | -7.7976 | -44.78403 | 2025-07-23 04:34:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 6757fd8b-73d1-38dc-bf64-a33a3e52133d | -12.67907 | -46.82882 | 2025-07-23 04:34:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c914567d-624a-39d6-86da-b1d86d2d1dcd | -7.02965 | -45.84158 | 2025-07-23 04:34:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4511aa90-b769-3c97-91b3-3423c2e0e7b6 | -13.74822 | -43.45981 | 2025-07-23 04:34:00 | NOAA-21 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 659d5b01-ddfb-3d8c-9731-373e91f78d92 | -7.04581 | -45.85206 | 2025-07-23 04:34:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 2d6b6b30-18f1-33eb-9e29-490f3a36ac60 | -7.19617 | -45.33461 | 2025-07-23 04:34:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 3e027a87-ddc2-3baa-8135-f7e273e44e43 | -8.29021 | -44.96611 | 2025-07-23 04:34:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 40d348f5-5152-33d9-bc7b-c7de8db2fad8 | -7.75971 | -44.02574 | 2025-07-23 04:34:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 20274e22-ada6-3961-95f8-8c2bc3d37a2f | -7.2362 | -44.78391 | 2025-07-23 04:34:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a205d125-43b6-367e-bb23-d32cada78801 | -11.81115 | -44.27114 | 2025-07-23 04:34:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d072db4b-dd3c-3677-97f3-8343495c23a1 | -13.7135 | -45.69842 | 2025-07-23 04:34:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 76b1c3fd-ca4c-3569-bd05-9b600f57c64c | -12.73193 | -46.61765 | 2025-07-23 04:34:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 75f9bd05-6967-37e0-8cd8-e1a4e736b009 | -12.49591 | -57.77128 | 2025-07-23 04:34:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| d292f233-fe41-3fde-ae0f-2e35bd9d61e5 | -9.26672 | -48.55996 | 2025-07-23 04:34:00 | NOAA-21 | RIO DOS BOIS | TOCANTINS | Brasil | 1718709 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |


[Clique aqui para ver as próximas entradas](README12.md)
