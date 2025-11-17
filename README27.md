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

## Dados Diários - Página 27

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9c887af7-07f0-3382-a6a4-6b9f7afe1996 | -6.61717 | -41.46532 | 2025-11-17 04:38:00 | NOAA-21 | SÃO JOÃO DA CANABRAVA | PIAUÍ | Brasil | 2209856 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 2fad1786-cfb9-3089-b304-d898f2333633 | -2.86095 | -51.27699 | 2025-11-17 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3adc7d63-4e07-37a1-a512-c790e3af1d25 | -4.69222 | -46.31575 | 2025-11-17 04:38:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e876b2d3-d2a6-3b0d-8480-691fe0c00929 | -6.7083 | -40.79964 | 2025-11-17 04:38:00 | NOAA-21 | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 32a61535-072b-3fda-98ba-53f7369886bb | -4.00904 | -49.10434 | 2025-11-17 04:38:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| f87d5852-0b83-38cc-911c-6137750d67c9 | -3.56008 | -49.88165 | 2025-11-17 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c9bb8bc6-e96b-314d-b4f3-145e470b5379 | -3.35035 | -43.49303 | 2025-11-17 04:38:00 | NOAA-21 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 62c5ba96-3d1c-3610-81dd-0d97a914768e | -3.39039 | -54.33511 | 2025-11-17 04:38:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2048fe99-ac57-3c56-ad72-bbeecd9a388a | -4.94001 | -44.52694 | 2025-11-17 04:38:00 | NOAA-21 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 4c32dc47-99e3-3b24-b3b2-413039215aca | -5.33669 | -43.03088 | 2025-11-17 04:38:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | 6.4 |
| 55d6da7b-a8de-34a6-9066-29e081e595c5 | -2.94058 | -51.7592 | 2025-11-17 04:38:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 71166cf0-c5dc-38d5-ba08-8174f7819ebf | -3.18927 | -50.65144 | 2025-11-17 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 97c2b3e8-cc09-3a50-b488-8275caa97e91 | -4.75361 | -45.65446 | 2025-11-17 04:38:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3b5db8bf-1648-3434-9599-e5ea5fc529cd | -3.52829 | -42.37716 | 2025-11-17 04:38:00 | NOAA-21 | LUZILÂNDIA | PIAUÍ | Brasil | 2205805 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 4572549a-4c67-3e49-9ade-afa29722ee76 | -3.23389 | -50.50279 | 2025-11-17 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f6523d13-7036-3ee0-abab-5f87c136ab90 | -1.98341 | -52.00024 | 2025-11-17 04:38:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 5f34fb0a-b689-3004-a715-82dd36e0e778 | -4.29591 | -49.74635 | 2025-11-17 04:38:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6720fe84-4493-3e65-b7b9-b6c8f5fedadb | -4.94955 | -48.24606 | 2025-11-17 04:38:00 | NOAA-21 | ABEL FIGUEIREDO | PARÁ | Brasil | 1500131 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 2c109c6c-35f8-3a4e-bfc4-7abe31787d5d | -5.84066 | -48.83656 | 2025-11-17 04:38:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| f4251cdf-44b6-36cc-9927-aaa89635a25e | -3.60184 | -50.15464 | 2025-11-17 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c183b72b-c082-3516-933a-294725e8c024 | -4.91863 | -47.41423 | 2025-11-17 04:38:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 10.0 |
| f0aa38ad-bfc7-393d-be65-3d33cedc413d | -4.02129 | -48.81052 | 2025-11-17 04:38:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4c42e093-e018-3dec-9339-f9cae57a1089 | -4.97665 | -47.80854 | 2025-11-17 04:38:00 | NOAA-21 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 83e676f8-531f-343f-80ce-1d7a8eb0c81a | -5.47865 | -40.96511 | 2025-11-17 04:38:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 0d718376-ce02-3135-a693-4af80c4b62f3 | -2.8904 | -53.29185 | 2025-11-17 04:38:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 61e458ce-bfca-3588-8c77-12b6fdc3efe2 | -3.47823 | -49.68872 | 2025-11-17 04:38:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 5669160e-3dce-33b9-919c-f1b249573a98 | -3.32338 | -50.17736 | 2025-11-17 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| dd8c719f-4328-30da-a537-0f88dc05e880 | -3.23955 | -50.51121 | 2025-11-17 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b56d813e-af17-3215-93a0-f8d2c185e6fa | -3.18643 | -50.6472 | 2025-11-17 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 37400044-299b-3401-ac52-5819ab825513 | -3.30364 | -50.21496 | 2025-11-17 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| dfb5aeb2-2f14-344b-82bc-6a250999f54f | -3.38765 | -50.132 | 2025-11-17 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5ef84695-fe29-3b9d-bd20-6efbe527ebf8 | -2.93679 | -51.07185 | 2025-11-17 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0f88c36a-423f-3834-b71a-393a4f3afec4 | -3.42332 | -50.37422 | 2025-11-17 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| adf22b8f-9cd0-3b46-8eed-07703471f1cd | -6.6042 | -44.26578 | 2025-11-17 04:38:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ff0de107-ac60-3da4-b011-de59ca80ac41 | -3.68687 | -50.54647 | 2025-11-17 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| bcd2b0f6-4366-3081-b830-8338a7684452 | -3.16426 | -50.16746 | 2025-11-17 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| ae0c8cac-0fe1-3392-b225-ef19ba52280a | -3.52009 | -51.23985 | 2025-11-17 04:38:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b0e97991-ff03-3e89-b965-6764e00c17c3 | -5.5786 | -47.09187 | 2025-11-17 04:38:00 | NOAA-21 | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| db39deec-8348-3aff-8cb9-862a5bb7ebf4 | -2.06736 | -45.38689 | 2025-11-17 04:38:00 | NOAA-21 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 8c3cd2f5-8bb9-3ba6-81f1-3d7cdfae7e32 | -5.38193 | -46.2589 | 2025-11-17 04:38:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2945dfb2-da09-3ad8-ab30-925dcdee9257 | -2.70825 | -46.97854 | 2025-11-17 04:38:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 891d4ce3-f0b8-3937-8bf8-24f8e9300998 | -3.28539 | -53.82091 | 2025-11-17 04:38:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a0321132-99dd-33c5-a16f-b73e3464b668 | -7.63965 | -48.22038 | 2025-11-17 04:38:00 | NOAA-21 | NOVA OLINDA | TOCANTINS | Brasil | 1714880 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 73a8b01f-188c-3688-ad92-7f6863867b84 | -3.24354 | -50.50807 | 2025-11-17 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5d930497-81f4-3db5-b84c-5c334158d7c4 | -3.75576 | -50.42588 | 2025-11-17 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 976ce225-8d47-3cff-b960-106265814787 | -4.27045 | -49.67032 | 2025-11-17 04:38:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c4991908-4ba6-3cd6-a5db-2aff77441d4c | -4.18544 | -50.41931 | 2025-11-17 04:38:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ee9f8711-07da-326b-a971-b32859f6a9d8 | -3.90852 | -45.80175 | 2025-11-17 04:38:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 9bf70c12-518b-3e65-9513-1fb4cb97fb44 | -2.99832 | -51.01011 | 2025-11-17 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 18081871-e053-3a86-ac37-7eef54f31994 | -2.66329 | -49.07283 | 2025-11-17 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 513de6de-79cd-3de5-85cf-6155a70c86b2 | -3.23447 | -50.49913 | 2025-11-17 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7d9d80f7-3222-322a-8607-9fbf537889e6 | -6.71268 | -42.93675 | 2025-11-17 04:38:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.7 |
| f7cd35b5-cb8f-35ea-9425-ad71b0c4f036 | -3.2373 | -50.50333 | 2025-11-17 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9c94d1c5-1e62-3188-88cf-c9cf30ed10e8 | -7.13355 | -47.12687 | 2025-11-17 04:38:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c991a938-290f-3400-b44c-da462d893c3a | -4.40089 | -45.83029 | 2025-11-17 04:38:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0b85620f-5f49-3dba-bc83-2a13b4f86c0f | -5.15592 | -46.12904 | 2025-11-17 04:38:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b681148e-3b18-34e8-869e-c43bc663732f | -2.96257 | -53.21761 | 2025-11-17 04:38:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f06e8ad1-27b9-3e6f-a544-54ed72d3947c | -7.26484 | -48.01911 | 2025-11-17 04:38:00 | NOAA-21 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e4ac0d91-4dcc-3c3b-a90a-c94bb7ec3dd1 | -4.11116 | -49.0822 | 2025-11-17 04:38:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4f2c39c2-9932-31d1-81b3-6214132eeb4b | -3.48016 | -50.25681 | 2025-11-17 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| aa4c895e-fc5c-3963-ab13-69542f759b44 | -4.10312 | -47.10527 | 2025-11-17 04:38:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 7150b3f8-13be-31c1-b32d-d10d7d6c9568 | -4.57539 | -50.94572 | 2025-11-17 04:38:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 06ca1cd0-7929-3feb-bfc6-337b48b6e0c3 | -4.6743 | -50.3668 | 2025-11-17 04:38:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 69b1ae35-786d-35de-9039-87c2ceef1382 | -1.5281 | -55.51733 | 2025-11-17 04:38:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 6a58de9a-ca5c-37c7-9154-5747418abb28 | -2.91566 | -54.16253 | 2025-11-17 04:38:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 65cee3d0-ca07-3359-8788-aa197f844936 | -3.37697 | -50.13403 | 2025-11-17 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7ac354dd-0473-394a-be4d-b55d3a22dc5e | -4.69343 | -46.30793 | 2025-11-17 04:38:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 48f8adeb-36e4-312a-8adc-309bd764255e | -5.09595 | -50.65067 | 2025-11-17 04:38:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 791cc983-264c-387d-bc5c-41088da19a04 | -3.77996 | -49.2627 | 2025-11-17 04:38:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3a9f3998-74fe-31c4-bb5c-1e12f3b6d90a | -3.14697 | -51.32471 | 2025-11-17 04:38:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d130b886-32ba-3f96-8385-e0a903fddff9 | -6.86713 | -47.07553 | 2025-11-17 04:38:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 670a58ac-fd89-314d-b8d7-7e6274f6d57d | -5.75585 | -42.7164 | 2025-11-17 04:38:00 | NOAA-21 | AGRICOLÂNDIA | PIAUÍ | Brasil | 2200103 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 062c2e59-74f1-319a-9cf2-c98dbfaa98cc | -3.77914 | -47.74579 | 2025-11-17 04:38:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 353beb49-7d02-3327-a742-9161a5f377cb | -2.46331 | -47.08734 | 2025-11-17 04:38:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d5e795dc-ded9-31ca-a20b-0691c4b62d38 | -1.12227 | -54.11573 | 2025-11-17 04:38:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2d58dad6-1463-3496-8c6c-cb0f989a745b | -7.6236 | -42.57803 | 2025-11-17 04:38:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| f97d4d35-51d0-30d7-a5ca-a9573d934609 | -7.26821 | -48.01964 | 2025-11-17 04:38:00 | NOAA-21 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2f3185b9-e7b7-3450-819e-1c3d33e98620 | -8.05758 | -45.66142 | 2025-11-17 04:38:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6a929143-3df3-3ab5-b962-dfa690442d66 | -4.74787 | -46.40334 | 2025-11-17 04:38:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 631ae76e-8c90-310a-b825-3e23b33f4ec8 | -5.38782 | -45.22713 | 2025-11-17 04:38:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 41c63385-2b99-37b9-ad71-14ed996a36b1 | -3.11441 | -51.03162 | 2025-11-17 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4433b5c2-e567-3697-bdad-5e1aec6954ad | -4.02075 | -48.81395 | 2025-11-17 04:38:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2d2ee563-d9bf-36b4-bb9d-39cd3898e659 | -4.46063 | -45.65743 | 2025-11-17 04:38:00 | NOAA-21 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| db6f042e-61c5-39e9-afa5-a24cc1908650 | -4.40742 | -45.83558 | 2025-11-17 04:38:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 5c120e92-b4a7-3127-afe4-72decf821fe2 | -2.58486 | -51.8273 | 2025-11-17 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2e747c91-c873-30e4-94d2-fd81cc133226 | -4.68309 | -46.93923 | 2025-11-17 04:38:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b7cf0397-12e2-39ec-b021-677f8bb612d3 | -3.22932 | -50.5096 | 2025-11-17 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 13c9b0e1-1814-3750-a413-8e2046770583 | -3.14817 | -51.31994 | 2025-11-17 04:38:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3f65f5aa-f328-38b4-b5e5-5e8eec8e6723 | -2.88727 | -53.28616 | 2025-11-17 04:38:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 50ca522a-a96b-33b6-9576-717dd6e8a9d6 | -2.9363 | -51.76284 | 2025-11-17 04:38:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 04a86696-9c10-32e6-bb26-9db1e6e36d88 | -3.39885 | -44.17993 | 2025-11-17 04:38:00 | NOAA-21 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 6628be05-7ee8-334f-9cb0-96f8bdfadafb | -7.43717 | -48.93489 | 2025-11-17 04:38:00 | NOAA-21 | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d3c5f0f3-c6c8-38b0-9e75-86af1dd4717b | -1.9797 | -51.99972 | 2025-11-17 04:38:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 1fe5e65c-2227-3a4d-871d-b23005aa6a86 | -3.20774 | -51.42295 | 2025-11-17 04:38:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d7cf1187-b42a-337c-9bc4-379673def6a9 | -5.54306 | -41.76554 | 2025-11-17 04:38:00 | NOAA-21 | SÃO JOÃO DA SERRA | PIAUÍ | Brasil | 2209906 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 6f6b53c8-4e5e-3e26-80db-dfc88a40c61c | -4.33807 | -46.50889 | 2025-11-17 04:38:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7e6497cf-7162-3862-b231-308c1579f64c | -2.80688 | -48.67943 | 2025-11-17 04:38:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 15a91d9c-169e-33f1-ae3a-1fe1ad22c666 | -4.72217 | -46.38372 | 2025-11-17 04:38:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 96da1d37-1d36-3722-b326-acf1c6b309ad | -2.8915 | -50.4044 | 2025-11-17 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 55896400-72c2-3f1e-85a3-26fa3650bc28 | -3.75518 | -50.42952 | 2025-11-17 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |


[Clique aqui para ver as próximas entradas](README28.md)
