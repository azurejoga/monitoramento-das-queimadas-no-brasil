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

## Dados Diários - Página 25

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 50fed468-d2ad-354a-9e40-f7d696b9e7af | -10.02922 | -54.32125 | 2025-06-21 05:23:00 | NOAA-20 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 40c0e2eb-83af-3b87-b7b7-dcef7e5b0dfb | -9.25558 | -57.53288 | 2025-06-21 05:23:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 3dfebc0f-a59a-3866-9414-8654a5c16635 | -9.4615 | -57.83677 | 2025-06-21 05:23:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f9e0e294-5a85-3a53-bb59-4753aac67956 | -9.46945 | -57.83355 | 2025-06-21 05:23:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 7a4a496d-538a-3b51-8516-8781e06710d9 | -9.9199 | -59.90825 | 2025-06-21 05:23:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| cdf2f71d-ce1c-3408-b249-390d70bb103d | -9.24881 | -57.52732 | 2025-06-21 05:23:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f4867e09-e5e7-3732-9844-c56ca105403e | -9.026 | -61.22366 | 2025-06-21 05:23:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b5e63f0e-9514-3725-bce6-801cd8bd4c08 | -9.01829 | -61.22955 | 2025-06-21 05:23:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 28b01236-9b64-3c33-8f40-719256dacea5 | -9.02655 | -61.22018 | 2025-06-21 05:23:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 116b8f82-4fcc-3ca1-a35b-08005162fdf0 | -5.30345 | -55.97262 | 2025-06-21 05:23:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4db5bea1-7384-3906-bbc1-b17e36ab6437 | -9.47136 | -57.82061 | 2025-06-21 05:23:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 5a0ac29f-554d-3e2c-a4db-a60c64c0900d | -11.14021 | -53.91825 | 2025-06-21 05:23:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e8597b12-d378-3ddd-9b58-3dfd8202223b | -9.48642 | -56.0842 | 2025-06-21 05:23:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 75682b2d-2d46-32d7-a0c5-caa1c11f9c7e | -11.13949 | -53.92359 | 2025-06-21 05:23:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 602a7a12-0fcf-3485-953d-419198ad1dba | -9.01884 | -61.22607 | 2025-06-21 05:23:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8cda68e0-c08f-3cea-b1fb-48d802516ffe | -7.94341 | -61.81182 | 2025-06-21 05:23:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.3 |
| cc86b3bf-a072-35d3-b460-ca63b2783c4d | -8.73363 | -47.99357 | 2025-06-21 05:23:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 852c7af0-1022-36aa-b47a-a72a6c55f424 | -10.88637 | -56.45679 | 2025-06-21 05:23:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 53f101d8-4026-3d31-9ede-308fde9cd004 | -10.68109 | -56.55366 | 2025-06-21 05:23:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1b4c231a-3851-333f-9b61-5c9a405db0cb | -8.02407 | -47.65875 | 2025-06-21 05:23:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 21a680e8-238b-3f7b-bff8-4f2bb3c2e2f1 | -9.46881 | -57.83786 | 2025-06-21 05:23:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| ec3b1d8b-7e07-3e45-8e39-ebb3c024335e | -9.24817 | -57.53173 | 2025-06-21 05:23:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| dc738ba4-560a-3db4-9b35-97ad5924cbe2 | -9.47803 | -57.82598 | 2025-06-21 05:23:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| dd98f20b-c83f-3d2d-b7a2-fe351a7ea77e | -9.3538 | -57.01293 | 2025-06-21 05:23:00 | NOAA-20 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 03b10717-934f-3236-8818-16160cb63fb3 | -11.14219 | -53.93689 | 2025-06-21 05:23:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 34a86844-0aa8-3019-af1a-052a9f1d8a16 | -9.47485 | -57.84747 | 2025-06-21 05:23:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a7320153-2eaf-368d-bf69-d3b388d623f3 | -7.90162 | -61.52159 | 2025-06-21 05:23:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 227b2b12-86f2-3f0f-8846-cab69ec46a56 | -9.02986 | -61.22071 | 2025-06-21 05:23:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e76cc9bf-7f37-3146-a53e-26b5ba7b7ed2 | -9.47565 | -57.81685 | 2025-06-21 05:23:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2cd87c36-8d70-3603-a256-6cb34eaff04a | -10.15425 | -48.99046 | 2025-06-21 05:23:00 | NOAA-20 | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 17b3870e-e3c3-3e3c-8184-be1a7a762f15 | -9.2661 | -57.81947 | 2025-06-21 05:23:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f1974fe6-c962-3e0a-ab82-51e305663fea | -9.91969 | -52.44512 | 2025-06-21 05:23:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3619a5c2-53f7-36f2-a35d-5e1cc0e9c993 | -8.03066 | -47.65993 | 2025-06-21 05:23:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 35577076-04a3-3696-80f3-07f48e97c141 | -9.91446 | -52.44442 | 2025-06-21 05:23:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d63033c2-189d-339a-9469-71b100046042 | -9.45722 | -57.84048 | 2025-06-21 05:23:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 70438896-48c2-3e7f-8f09-23bc21ba9789 | -9.25622 | -57.52843 | 2025-06-21 05:23:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 7c6b7235-8e4c-3647-b664-41886847aed5 | -9.4731 | -57.83407 | 2025-06-21 05:23:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| f879b7ae-2ef5-3db7-9ee6-5df1b987b441 | -9.0216 | -61.23008 | 2025-06-21 05:23:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d0b132ae-e201-3621-920e-02fd9eaa2d96 | -9.47612 | -57.83888 | 2025-06-21 05:23:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| acbeda74-6c63-382c-ba95-c2f02881f79a | -9.12311 | -49.66291 | 2025-06-21 05:23:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| de2ab338-1045-3e5b-9214-a79fe952ee94 | -9.4817 | -57.33209 | 2025-06-21 05:23:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8ef2a0e4-9076-3ae2-aca7-9d157fe61a95 | -9.46754 | -57.84642 | 2025-06-21 05:23:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 2eecf1f7-ac41-3a0b-8406-9f0148b40af8 | -10.13342 | -58.22188 | 2025-06-21 05:23:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 35bf16d5-aee7-3f02-aa49-043a97ebe4b0 | -11.13613 | -53.91217 | 2025-06-21 05:23:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 90c267e6-bb83-3d7a-a547-0e27af448217 | -11.13527 | -53.91426 | 2025-06-21 05:23:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ed4e8053-4bec-3e9e-8d46-018aa88ad0c7 | -10.05309 | -59.35735 | 2025-06-21 05:23:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4b09d5f4-bab6-3d96-82e3-269b47e6c7c0 | -9.73677 | -48.33034 | 2025-06-21 05:23:00 | NOAA-20 | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f63f8702-dc0e-3f28-8c38-b896fc0c0c0b | -6.01993 | -48.20666 | 2025-06-21 05:23:00 | NOAA-20 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5b1d5118-d1c5-3a5c-9797-0045cdcd2509 | -9.02491 | -61.2306 | 2025-06-21 05:23:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d5a8bd8e-b7cf-3e52-b41d-e82b068bb3ba | -9.47867 | -57.8217 | 2025-06-21 05:23:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 82aef599-dbda-308c-bf18-297e9980d8d5 | -7.89227 | -61.47355 | 2025-06-21 05:23:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 43d8a453-70b5-39a2-a187-22fb15b34ab0 | -6.01922 | -48.21205 | 2025-06-21 05:23:00 | NOAA-20 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bce4f84d-7f21-388d-b9cb-ad9d936c1ce8 | -12.15881 | -48.68163 | 2025-06-21 05:23:00 | NOAA-20 | SUCUPIRA | TOCANTINS | Brasil | 1720853 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| de184313-0f9c-3b38-a7c3-4d7459f56154 | -9.47676 | -57.83458 | 2025-06-21 05:23:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| cdd12c16-b49a-39d7-8655-efbfbd4547d4 | -9.47056 | -57.85122 | 2025-06-21 05:23:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 015fc6c0-5acd-3768-8506-bdc123390727 | -10.88938 | -56.46462 | 2025-06-21 05:23:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| f3f9fccb-3096-3f4f-9fe1-11d6b83b7672 | -9.17401 | -61.40367 | 2025-06-21 05:23:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 765c504e-ec39-3a62-a321-d6a7723e63f2 | -8.01686 | -47.65784 | 2025-06-21 05:23:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 824171f4-5b79-3b4d-a750-e54ba1eca034 | -10.52195 | -53.62162 | 2025-06-21 05:23:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| e11df182-fb3c-36cf-873e-18d7f0215b9a | -10.03003 | -54.31863 | 2025-06-21 05:23:00 | NOAA-20 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 8.8 |
| c0a3bdb1-f836-37eb-a0cd-6bdf534f305e | -8.00862 | -47.66944 | 2025-06-21 05:23:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| bb8f00b1-7bf5-352a-b469-b2efcbcd8bfb | -9.47183 | -57.84267 | 2025-06-21 05:23:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 8740d160-8968-3e92-a175-36994485f035 | -10.3047 | -57.13963 | 2025-06-21 05:23:00 | NOAA-20 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a1b3d36b-921e-3e36-bb7a-1bd55a7012ed | -7.27988 | -49.99409 | 2025-06-21 05:23:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b0a76ffe-39d1-361b-a858-54708eec5149 | -9.02931 | -61.22418 | 2025-06-21 05:23:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3515470f-bb04-33cd-9922-c9a951ce1f3d | -10.15549 | -48.98972 | 2025-06-21 05:23:00 | NOAA-20 | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 25908709-f0e0-37c5-a659-3ed704d43523 | -9.25992 | -57.52904 | 2025-06-21 05:23:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| f41f9580-fa42-3d65-9f34-8425f9b6cf74 | -10.14894 | -48.98886 | 2025-06-21 05:23:00 | NOAA-20 | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| a2d990c4-37ac-34aa-8cf9-60644f42c1b5 | -10.89342 | -56.46518 | 2025-06-21 05:23:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 9388b16f-1eb4-3423-a20d-c0ce31b205a9 | -8.00918 | -47.66318 | 2025-06-21 05:23:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 296b09b6-3d44-3193-bc33-b90e500bb232 | -9.4774 | -57.83027 | 2025-06-21 05:23:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 8314b232-26d7-3a98-99ff-1176a259b579 | -9.01278 | -61.22155 | 2025-06-21 05:23:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bea0846a-9dcf-3b12-a997-9f5781b846bf | -10.37154 | -57.50738 | 2025-06-21 05:23:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 439ed811-75aa-3ff8-afdd-d8f25ed9fd0f | -9.25686 | -57.52398 | 2025-06-21 05:23:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 4e74fd06-0baa-3c2e-bf50-864bfb88de27 | -9.26056 | -57.52459 | 2025-06-21 05:23:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 05628598-54ef-36d1-83e1-21d7f18014c9 | -9.01994 | -61.21913 | 2025-06-21 05:23:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d1fff546-2c21-316c-a590-2f189eb7907f | -8.02325 | -47.66503 | 2025-06-21 05:23:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2f213545-a658-388c-984e-288e4c4771f7 | -10.52121 | -53.62711 | 2025-06-21 05:23:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| f25b122b-a97e-3852-a500-1992d6cb5e26 | -9.0172 | -61.2365 | 2025-06-21 05:23:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c77765a1-4aba-39d5-abbd-41d00bf74a56 | -9.01554 | -61.22555 | 2025-06-21 05:23:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 99faa82b-edc8-3fdd-9c1e-6d37c6de76a8 | -10.2977 | -57.13371 | 2025-06-21 05:23:00 | NOAA-20 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0475ba8f-b7ed-318e-afad-818db324552e | -5.12377 | -56.11604 | 2025-06-21 05:23:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 38af337c-700e-3926-aa30-c1ada062780b | -8.33601 | -55.09592 | 2025-06-21 05:23:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 492f5e94-8ef5-3253-9490-f59086731d89 | -9.47438 | -57.82545 | 2025-06-21 05:23:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 11f66c62-efc9-3cd2-9889-3a6ae6bed850 | -8.98531 | -49.87027 | 2025-06-21 05:23:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 57ecde3c-64e3-32a6-8ac6-867776eac603 | -7.94008 | -61.81129 | 2025-06-21 05:23:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 63186ee9-29d3-3267-9d86-dfc858d9c83b | -11.13541 | -53.91752 | 2025-06-21 05:23:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| dd03a3b2-44b5-3d96-bfc1-2a8927463bbf | -10.88534 | -56.46404 | 2025-06-21 05:23:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| dbee935c-fb3e-3594-9a40-95b104759099 | -9.01223 | -61.22502 | 2025-06-21 05:23:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ed0d9687-d04e-3139-bf32-ccc3753458f9 | -9.73604 | -48.33619 | 2025-06-21 05:23:00 | NOAA-20 | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 810f3d80-9ae3-35b8-9aab-155027f7b72d | -10.03383 | -54.32192 | 2025-06-21 05:23:00 | NOAA-20 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 0b371d64-9095-3181-84b2-21b90b7a2de9 | -10.30086 | -57.13909 | 2025-06-21 05:23:00 | NOAA-20 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 75e473fd-f713-37b8-8cf7-7aea53be2553 | -9.47501 | -57.82116 | 2025-06-21 05:23:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 59f9f7b6-213d-342d-accf-4ae3b5ef7897 | -8.98546 | -49.8684 | 2025-06-21 05:23:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| f2285381-434c-3eca-9659-b83bfffc6862 | -8.73254 | -47.99154 | 2025-06-21 05:23:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| b4b72755-ef44-308f-a007-63b0e393148f | -7.28048 | -49.98974 | 2025-06-21 05:23:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 119d002f-369e-3a0f-abae-e9e008735198 | -10.77409 | -58.45956 | 2025-06-21 05:23:00 | NOAA-20 | CASTANHEIRA | MATO GROSSO | Brasil | 5102850 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| df0df25d-2f54-3cb4-b17b-7004a5f59eec | -9.47422 | -57.85175 | 2025-06-21 05:23:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 21342f51-aa1e-34f1-9183-8c14881103f0 | -9.46087 | -57.84106 | 2025-06-21 05:23:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 56c2ef59-6bc7-3453-b6a8-bbc215206a81 | -8.03097 | -47.65975 | 2025-06-21 05:23:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |


[Clique aqui para ver as próximas entradas](README26.md)
