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

## Dados Diários - Página 99

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 600f4c6b-2dc9-3afb-8a1c-fd1b179f2b7d | -1.53025 | -54.5245 | 2026-10-10 05:04:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 35d683fb-4153-3da8-b107-73ebbac4b8c7 | -3.65191 | -59.71345 | 2026-10-10 05:04:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 8db2a788-9d49-3ff8-8ace-8b920c1b9979 | -3.02531 | -54.05226 | 2026-10-10 05:04:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b8f592be-f5a7-3b10-9f4a-ba47454e1ba3 | -7.23926 | -55.07467 | 2026-10-10 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 5f4f261c-1457-3754-b193-59a21cb51c63 | -3.95093 | -55.33979 | 2026-10-10 05:04:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 09b5b995-01e3-39b6-aa3a-06d39eec3e9a | -3.50172 | -54.19865 | 2026-10-10 05:04:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ff4cee46-32cc-3baa-955d-3c296a2b4672 | -3.72525 | -55.97373 | 2026-10-10 05:04:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f2ac32b5-aa0e-3be6-94ad-0d6cdd5cfdac | -3.29662 | -53.99274 | 2026-10-10 05:04:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| bb4cee55-986f-3f9e-acb5-3264fde99e84 | -3.01042 | -54.06051 | 2026-10-10 05:04:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d152ea6f-b125-398b-acff-f8c7bcb28fd5 | -0.87689 | -48.72028 | 2026-10-10 05:04:00 | NOAA-20 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 995859f5-777a-32bd-ae5a-42e301d93e52 | -3.88106 | -55.99 | 2026-10-10 05:04:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| d0dcde72-21b9-3d2e-a533-3954befca5b4 | -6.42811 | -60.04203 | 2026-10-10 05:04:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 608b959c-69bc-325a-a97b-ff9507dbde8e | -5.03939 | -49.35054 | 2026-10-10 05:04:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c1e8d799-42f8-3886-a33c-3e119bbf796b | -7.23208 | -55.07709 | 2026-10-10 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 29b9a8a1-9406-38e8-bd2e-8b295813cb7e | -6.80289 | -52.77608 | 2026-10-10 05:04:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 72dd3eed-b311-327a-be7f-4c2f76dc714f | -6.5512 | -61.41741 | 2026-10-10 05:04:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1d3b1431-a332-3abd-9999-cd2321ef4432 | -5.96332 | -55.34061 | 2026-10-10 05:04:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7f5f520b-9b34-3809-b8dc-29fba2f8c709 | -6.4858 | -53.61087 | 2026-10-10 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 80cff819-47be-3046-8bb1-f836b02a3696 | -2.62491 | -54.75048 | 2026-10-10 05:04:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3db9f93e-b3a7-3ea6-853b-134f46784fb1 | -3.51952 | -59.95021 | 2026-10-10 05:04:00 | NOAA-20 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7986dda7-abec-3fd9-8698-d4bac6d3aca5 | -2.99148 | -53.90218 | 2026-10-10 05:04:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4394ce36-07dd-3d02-99c4-497f2a8afd94 | -3.65368 | -54.52436 | 2026-10-10 05:04:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4f28b097-a496-311b-8919-6df10ee4f780 | -3.26205 | -54.25256 | 2026-10-10 05:04:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 965b8bb4-705f-3118-8a90-9c63e2a05bfd | -7.24361 | -55.21789 | 2026-10-10 05:04:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9ed8e418-ea45-3394-90cf-aece73043644 | -6.67213 | -55.0946 | 2026-10-10 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f7e234a5-669f-3799-85eb-9fe7622e27bb | -3.57467 | -54.70131 | 2026-10-10 05:04:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9ec40729-f1ac-3b08-b689-4f6bc1234f08 | -1.32394 | -55.44637 | 2026-10-10 05:04:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d9139c80-6d55-38e3-8f5b-e28985659057 | -3.0621 | -54.20648 | 2026-10-10 05:04:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d341dffa-f73f-354b-b74c-90c9a8ff0535 | -2.46701 | -56.08534 | 2026-10-10 05:04:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 75e64325-6250-3319-9b0b-5971297149f7 | -7.51653 | -48.02447 | 2026-10-10 05:04:00 | NOAA-20 | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| fd085f3b-b301-3a21-ae3f-adfbbf977d77 | -3.30851 | -53.70172 | 2026-10-10 05:04:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ea7f0465-a36e-38f7-819b-b4e18aab6093 | -5.88934 | -57.721 | 2026-10-10 05:04:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| e2f5a336-926b-3d0a-b5df-1f22f0075c72 | -3.82694 | -55.67191 | 2026-10-10 05:04:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3601594d-4d63-3e57-b2d3-ae22883b99f3 | -2.56373 | -57.41968 | 2026-10-10 05:04:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 4.9 |
| f1e9ffc1-9eb5-3453-885d-f9269dfcc0c9 | -7.50283 | -54.99934 | 2026-10-10 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 1d8045f0-0f5b-34f8-af34-9562e8f1a702 | -3.4853 | -50.49244 | 2026-10-10 05:04:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 408ffaf7-e812-3a70-80bd-7e7a5509e0ac | -4.13581 | -53.99163 | 2026-10-10 05:04:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7f5381e6-1950-32b7-a2c2-6d7a8799af6a | -4.58017 | -54.95734 | 2026-10-10 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 027c3380-58e9-316c-9fbe-41b31bb003ee | -2.62804 | -57.74131 | 2026-10-10 05:04:00 | NOAA-20 | URUCARÁ | AMAZONAS | Brasil | 1304302 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| e9323cf5-3ac9-3d70-91f2-2a28807dada1 | -5.22234 | -60.04311 | 2026-10-10 05:04:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2b836e83-92d0-351b-8921-43829444b5a9 | -3.04001 | -54.23848 | 2026-10-10 05:04:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0fb5a69e-8136-33d5-a3e4-1370e6120149 | -6.22898 | -60.03798 | 2026-10-10 05:04:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cd4051c1-69ca-300f-8c17-fc2178845faf | -3.28235 | -54.69864 | 2026-10-10 05:04:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 1496ef72-1680-34f1-bc0e-b794c408a2ff | -3.89187 | -52.19111 | 2026-10-10 05:04:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2157fede-6375-308f-ba89-2a8e4746eb26 | -4.63778 | -50.95813 | 2026-10-10 05:04:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5b358c10-3415-36c9-b032-1c7d0c454771 | -3.96307 | -59.99648 | 2026-10-10 05:04:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fdf81a33-5fbc-3037-aa77-43c189e2ce39 | -4.33853 | -55.12944 | 2026-10-10 05:04:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1cc4af57-9048-3ab2-bd33-663b0943b6d5 | -6.71796 | -55.04061 | 2026-10-10 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 83e0ce7c-974d-3edf-9e86-0f7ba3f9a8a1 | -2.06889 | -48.14658 | 2026-10-10 05:04:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7a6f2a6b-f1bb-34eb-84e1-20434fbb11b7 | -3.56911 | -54.69323 | 2026-10-10 05:04:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 04d0b27e-78bf-3aa7-9fc6-989b8062506b | -5.89229 | -57.72594 | 2026-10-10 05:04:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 63d62586-3803-36e5-bcb9-42f65239f9d6 | -3.26222 | -54.01513 | 2026-10-10 05:04:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cad61c11-c1ad-386e-a89e-9728b8a1b4a3 | -8.44874 | -47.98846 | 2026-10-10 05:04:00 | NOAA-20 | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 52af542d-aec8-3e86-9002-89a4f8ba3fc0 | -7.1846 | -52.61806 | 2026-10-10 05:04:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| dcf707f3-5253-36f5-9dfb-9986c843f2f9 | -3.1792 | -48.58556 | 2026-10-10 05:04:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 005e0792-37e9-3e8a-9f36-d43be7038ef6 | -3.29939 | -53.9967 | 2026-10-10 05:04:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b446e6a5-62dc-3c5c-935c-61d9c0ecfce1 | -2.97134 | -54.17833 | 2026-10-10 05:04:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 359d354d-7f81-3ade-ac32-2cb7aa5aefbf | -6.49372 | -55.29535 | 2026-10-10 05:04:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 16f47052-29f3-3afe-9815-83aa586648ca | -1.11336 | -54.17388 | 2026-10-10 05:04:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f2fc8471-7ab9-3899-8f63-6e486275bae0 | -3.35965 | -50.48282 | 2026-10-10 05:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7b412333-b5d0-32ba-b951-35c0b24ebb15 | 0.22501 | -60.38884 | 2026-10-10 05:04:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2047760f-2ff4-3a62-a088-8220347c5756 | -2.22216 | -50.4884 | 2026-10-10 05:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1439a256-ec8e-3e9e-961a-baa80f824de7 | -5.36066 | -48.56734 | 2026-10-10 05:04:00 | NOAA-20 | ESPERANTINA | TOCANTINS | Brasil | 1707405 | 17 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c8b3818b-35dc-3616-bec2-f572a762dc38 | -3.0732 | -54.28633 | 2026-10-10 05:04:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 1505c520-90e1-336f-acf5-d2afba47ff6d | -6.37523 | -55.16501 | 2026-10-10 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f9143576-c4e1-368d-b80d-34ab79d4e4bf | -7.57392 | -45.65487 | 2026-10-10 05:04:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2941bd7f-16d4-3eea-9c49-4526099b2a83 | -5.96024 | -49.40351 | 2026-10-10 05:04:00 | NOAA-20 | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 75a1ca10-f2b2-3820-8e9e-8815748d35a0 | -6.42324 | -60.0452 | 2026-10-10 05:04:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9d1af339-119e-34a0-b19d-c772effad2c0 | -5.74642 | -45.139 | 2026-10-10 05:04:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| d3c068c5-0aaf-3742-a694-b2aab4c93adb | -6.32101 | -54.80256 | 2026-10-10 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 068de8a2-418d-3954-943a-05ec516285aa | -7.18947 | -55.17381 | 2026-10-10 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 18ec8489-dcf2-39f1-8dbe-1c85058f112b | -3.7318 | -59.46157 | 2026-10-10 05:04:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 232416a0-dd28-3d7f-9ede-1190261f4162 | -6.31547 | -55.32788 | 2026-10-10 05:04:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 6f2d3ba6-201b-3369-a383-5ce713ffa510 | -6.20334 | -45.42728 | 2026-10-10 05:04:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 20b6a362-199c-34ec-ad28-280954df01ea | -5.88173 | -53.51966 | 2026-10-10 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 539bf525-b019-3af7-95b6-8e2dabd2a84b | -1.52244 | -54.50873 | 2026-10-10 05:04:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fa9759e2-3dec-3d34-9dd1-b3a3fa888e6a | -4.41284 | -49.78278 | 2026-10-10 05:04:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cddc008e-4e30-3a23-b908-ce82b4a0aa64 | -4.36437 | -54.75481 | 2026-10-10 05:04:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f8850947-4b77-3283-82d2-402f6ed282e4 | -3.36243 | -58.22034 | 2026-10-10 05:04:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0dab13d1-7ad9-3e2c-9491-84c358532ddd | -3.31928 | -54.04217 | 2026-10-10 05:04:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 18fc4276-5811-3ca1-a702-97ad3d080f44 | -1.8906 | -54.69018 | 2026-10-10 05:04:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| e618fa9d-af7b-306c-9314-12ec17f43f26 | -6.46121 | -55.05343 | 2026-10-10 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9ac1cb60-64e1-3855-953e-93a3802bd4ec | -3.89016 | -52.19549 | 2026-10-10 05:04:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| fc4a438a-87b2-3f3a-97e0-57a3ce678865 | -2.73107 | -54.15068 | 2026-10-10 05:04:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| f9a8d0fd-d084-36f6-b0b5-45de3fc48720 | -6.71409 | -55.04353 | 2026-10-10 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 211093d6-d292-32ca-8272-354bcc530e3e | -2.5141 | -56.26651 | 2026-10-10 05:04:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 67277505-178a-350f-a698-22ac6d621e11 | -3.28513 | -53.87067 | 2026-10-10 05:04:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 11.8 |
| c5077e0e-19a0-3401-aea5-98f4de231ce9 | -2.85104 | -59.12088 | 2026-10-10 05:04:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ebb72494-ff29-3863-b5d8-0de77abbaa20 | -1.19662 | -54.14025 | 2026-10-10 05:04:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4e25a0d7-6125-3431-83c8-c12dc7d9057c | -3.18561 | -50.59712 | 2026-10-10 05:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2c32fef6-8c2b-34ad-8613-b2507ec26632 | -4.66631 | -56.21333 | 2026-10-10 05:04:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f5b20467-938f-3a73-b372-8863dc338c5f | -6.22189 | -60.02884 | 2026-10-10 05:04:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7dbd9290-8dfc-3941-a438-c48ea2152531 | -6.0428 | -59.9079 | 2026-10-10 05:04:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| afea7fb8-2fc7-33da-8578-3930388b3406 | -3.70412 | -57.20005 | 2026-10-10 05:04:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a2447388-d3f2-36bd-93b1-2ed509f3db52 | -4.11119 | -54.61805 | 2026-10-10 05:04:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 61b72d25-62c3-36a0-89f7-8ad2d388b729 | -3.59911 | -54.59042 | 2026-10-10 05:04:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 104cbb4b-3743-3a64-84ae-1cb50e0e1de7 | -4.58184 | -54.94688 | 2026-10-10 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| e13339c0-8cfe-3d4f-844e-07a7ef01aa9e | -3.23405 | -50.18314 | 2026-10-10 05:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 71fb46e5-279d-3428-b968-fe1d46bbe05b | -3.43314 | -54.54341 | 2026-10-10 05:04:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3d70a202-7709-3c67-8423-5b63d937d27f | -6.48978 | -55.31994 | 2026-10-10 05:04:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |


[Clique aqui para ver as próximas entradas](README100.md)
