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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0ff9d1c4-10ca-3f43-8390-781d86d755e7 | -5.10092 | -44.80209 | 2025-05-17 03:47:00 | NOAA-21 | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 22.3 |
| 71397e3a-7ca3-3399-9c85-e3248d14c427 | -6.7885 | -47.59981 | 2025-05-17 03:47:00 | NOAA-21 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2fd3cb62-b46d-3df7-bbcd-aa1f4bd58511 | -7.90734 | -44.4808 | 2025-05-17 03:47:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d9d44792-ee1a-3ebb-9217-e976b7651b87 | -6.84944 | -42.79847 | 2025-05-17 03:47:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 378f8a02-53ff-3ac3-9127-96280c4c17ed | -7.90177 | -44.48507 | 2025-05-17 03:47:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 4fab6b9d-9389-338d-8e6d-fc0774dd0c54 | -6.71388 | -42.13658 | 2025-05-17 03:47:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 9576babc-c443-3159-a05c-b55684afd9fe | -6.17393 | -48.06588 | 2025-05-17 03:47:00 | NOAA-21 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 986d2590-9ab6-3a72-be7b-fb9e2c98340a | -5.10143 | -44.7991 | 2025-05-17 03:47:00 | NOAA-21 | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 22.3 |
| bf1c0405-c47d-3e45-85b3-cee06889aea1 | -9.79705 | -47.74173 | 2025-05-17 03:49:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5736ae4f-4209-31b8-a462-f52a1839b8a7 | -13.30255 | -45.36741 | 2025-05-17 03:49:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 3a68261d-f9b2-31c5-8d6b-d686f76409e9 | -13.50375 | -47.40057 | 2025-05-17 03:49:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 17729588-049a-3d4c-beba-4efb923f1999 | -13.3113 | -45.37638 | 2025-05-17 03:49:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 1fd4032a-ef41-3bd3-a421-9632f5b99a33 | -13.32225 | -45.39314 | 2025-05-17 03:49:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1d350a22-4989-38e7-b304-fa34c37d21c8 | -10.6372 | -48.08637 | 2025-05-17 03:49:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 49136e89-85c1-3578-9227-9030c3b7b5b8 | -12.99273 | -46.32302 | 2025-05-17 03:49:00 | NOAA-21 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 84b304b3-eebc-3ff4-92f9-5ec3f6a59fa2 | -13.30587 | -45.38028 | 2025-05-17 03:49:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 5.4 |
| bf8fdb13-dc4d-3924-9d13-14635cf35eb5 | -12.99115 | -46.31526 | 2025-05-17 03:49:00 | NOAA-21 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c1d23b93-4351-3b1a-88d3-4f37d53fee76 | -11.57973 | -47.87115 | 2025-05-17 03:49:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| acbb3f89-d93a-3834-acc0-2965b4b61a63 | -9.80032 | -47.73911 | 2025-05-17 03:49:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 705c6f17-33d6-32ef-b8a3-5b96c7a2c146 | -11.16462 | -48.67862 | 2025-05-17 03:49:00 | NOAA-21 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 6c5f1b4a-22c6-3d09-bfca-41c6d4c6d679 | -13.32313 | -45.38844 | 2025-05-17 03:49:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 50e82f22-69e6-30d1-99a7-40080abeb9fb | -11.41705 | -44.70862 | 2025-05-17 03:49:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| aaf165b2-b921-3e2c-905b-ffd61ccdcec3 | -13.50012 | -47.25519 | 2025-05-17 03:49:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 05555474-47c2-37a7-9b33-ecbe00ef69f4 | -15.04997 | -43.88316 | 2025-05-17 03:49:00 | NOAA-21 | MATIAS CARDOSO | MINAS GERAIS | Brasil | 3140852 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9363b27d-3e17-3d2b-80a3-ac1e9c6510a9 | -9.14287 | -41.00198 | 2025-05-17 03:49:00 | NOAA-21 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 1f54c556-a373-3c5c-9d04-6de7f061d370 | -13.30169 | -45.37214 | 2025-05-17 03:49:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 7185b629-38d2-35bb-84fd-7ca1e0291e1d | -13.31495 | -45.38197 | 2025-05-17 03:49:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 2b8f97de-2c07-33b0-ad35-1b635cb7c199 | -13.32591 | -45.39873 | 2025-05-17 03:49:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 286c9b98-99c4-3549-becb-8c7f12e0f23f | -8.54079 | -45.89976 | 2025-05-17 03:49:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7f01a1cc-62a6-3c61-a2f3-2ef64d6b668f | -13.32679 | -45.39402 | 2025-05-17 03:49:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 296ab6db-fbc8-378a-babd-352d40ca99fb | -13.32035 | -45.37817 | 2025-05-17 03:49:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c4e02501-9880-3e15-b973-541fdbbe5865 | -13.05571 | -47.82866 | 2025-05-17 03:49:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 09aec726-d68e-3463-b606-d8166e469488 | -11.63946 | -48.03278 | 2025-05-17 03:49:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 824595a5-d883-3f79-8101-4f412512641f | -13.30312 | -45.36997 | 2025-05-17 03:49:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 552eebf3-d48f-3d57-a370-37f68dc57509 | -9.30716 | -44.82969 | 2025-05-17 03:49:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3506371b-6c21-3100-a8d3-6d2052dc3300 | -11.1606 | -48.67297 | 2025-05-17 03:49:00 | NOAA-21 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 4fea8c6d-fe2a-3acf-8801-229be0896062 | -11.57722 | -47.62046 | 2025-05-17 03:49:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 165db583-d859-3255-adca-6abe7d493d46 | -10.63641 | -48.09043 | 2025-05-17 03:49:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0e2838be-3dd4-3c5f-96cd-cc533e660716 | -11.69444 | -44.62423 | 2025-05-17 03:49:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f35fdb1f-51e8-30c5-94c7-8b2e38b84ab4 | -12.10476 | -44.74351 | 2025-05-17 03:49:00 | NOAA-21 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3e3917da-d8be-3c95-906a-297b091cc4be | -14.06521 | -45.42251 | 2025-05-17 03:49:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 79cae577-cfd2-377c-b07e-099dc323ee1d | -11.78882 | -47.3444 | 2025-05-17 03:49:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 060fb867-91b5-32d5-bc48-719613ea8c86 | -13.30677 | -45.37553 | 2025-05-17 03:49:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 1337abd6-e8be-332a-bfc7-07d59c6018ce | -12.35543 | -49.96728 | 2025-05-17 03:49:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bcdbf85b-a485-3e79-9d19-1fee4cfe0513 | -11.57862 | -47.61329 | 2025-05-17 03:49:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 8e538406-fc55-3efd-9de8-c151dbefeed6 | -12.83981 | -47.40806 | 2025-05-17 03:49:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0fd06c50-0cda-3056-a906-b2bb82d5d308 | -12.34923 | -49.96612 | 2025-05-17 03:49:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7963bdcd-7ddb-3c73-98a8-c205fa536d1f | -11.57701 | -47.61292 | 2025-05-17 03:49:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 92d2f505-486a-350e-b75d-0cf5705f735e | -13.3123 | -45.39613 | 2025-05-17 03:49:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b3aead00-3253-3924-ba49-2f1c3cb51243 | -13.30222 | -45.37473 | 2025-05-17 03:49:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 3326a37c-f96e-3fa5-ba99-cf960a7a17e0 | -13.30765 | -45.37081 | 2025-05-17 03:49:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| e815922d-d0dd-347f-8d8d-7059d013e7bb | -12.995 | -46.32159 | 2025-05-17 03:49:00 | NOAA-21 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9061f26f-67d3-3441-846c-91c96a522fa4 | -13.31131 | -47.46763 | 2025-05-17 03:49:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f11c228c-df84-3eb8-a8ec-9ed5b90f6a8e | -14.06608 | -45.4179 | 2025-05-17 03:49:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 9587b9a8-821d-330e-b588-f1b155d7de6b | -11.79905 | -47.40662 | 2025-05-17 03:49:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5e933c34-39f6-31b5-a0dd-77ba0f755547 | -10.0271 | -48.7002 | 2025-05-17 03:49:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| e1ba6479-df81-3488-8d83-49aac8ac81dd | -13.31583 | -45.37727 | 2025-05-17 03:49:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 2b717a9a-8975-3a33-b55f-c0284a0ed2e7 | -8.54023 | -45.90284 | 2025-05-17 03:49:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1e8bd8a9-e099-3c3c-8cf9-47bb2da4614a | -15.56813 | -47.85483 | 2025-05-17 03:49:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8b4f77f6-0669-355c-b794-4b99e0b87a3f | -12.10754 | -44.74678 | 2025-05-17 03:49:00 | NOAA-21 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 092ff05e-1817-3dd2-b231-d2d1cb0923a2 | -11.78687 | -47.3546 | 2025-05-17 03:49:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 855327aa-5d6c-3d4d-b8ee-d9b2883fd971 | -11.79632 | -44.28797 | 2025-05-17 03:49:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0057d9d5-bc32-3820-b8df-614247665304 | -11.42153 | -44.70943 | 2025-05-17 03:49:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 81d36258-93d6-3001-b726-37b7c88f8682 | -8.54589 | -45.90075 | 2025-05-17 03:49:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a5d71eab-eae3-3428-9865-2de300bdc997 | -13.32137 | -45.39785 | 2025-05-17 03:49:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e8322462-409b-3a8e-b018-be395b319b47 | -12.35442 | -49.97226 | 2025-05-17 03:49:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f9a4d5ea-447a-3b6e-8a0e-6efab7a76a4d | -11.58262 | -47.62162 | 2025-05-17 03:49:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f79f1677-0af5-3aa6-9033-9929fec8fc98 | -13.29857 | -45.36921 | 2025-05-17 03:49:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6ee446a0-5153-33d6-8f83-ec61cd7c4fd1 | -11.64726 | -48.0223 | 2025-05-17 03:49:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 84d049e3-d9e7-3b04-958a-82b46866430f | -13.30083 | -45.37694 | 2025-05-17 03:49:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0f6bbb60-7746-3e4d-b280-ee60ecb13ab5 | -11.79829 | -47.38149 | 2025-05-17 03:49:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| abd37e17-3cf5-3e44-9d57-57a551684773 | -13.3186 | -45.38755 | 2025-05-17 03:49:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5586df02-3098-3eef-becc-06b70a6fb55b | -13.30863 | -45.39059 | 2025-05-17 03:49:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8adc778b-7705-39cf-b847-088882ceebf5 | -13.31407 | -45.38668 | 2025-05-17 03:49:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 96adc784-20af-3f69-a7a0-ce50209daa60 | -13.31684 | -45.39698 | 2025-05-17 03:49:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e0d943b1-24ad-3c47-a7f8-d143298419f5 | -9.79959 | -47.74306 | 2025-05-17 03:49:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c5cbccd6-9ade-38a1-8237-2b050cdf25d0 | -11.58195 | -47.62508 | 2025-05-17 03:49:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 17b560cf-57f4-3f84-9c8b-dba3ddbcdfcf | -13.31042 | -45.3811 | 2025-05-17 03:49:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| ce15c537-cc91-38bb-a882-6271918dfcc9 | -13.05435 | -47.82007 | 2025-05-17 03:49:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| dfd894e9-14a6-3dad-8523-abf3f1fad668 | -11.43785 | -44.72186 | 2025-05-17 03:49:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 252f90c9-b096-3e98-b5a3-1a3fa12ccba2 | -13.32401 | -45.38374 | 2025-05-17 03:49:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 594de3c6-f61a-3111-bc22-623df547dabb | -11.79841 | -47.41003 | 2025-05-17 03:49:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 24c33f43-9bc6-3ef1-87a6-f609936e6de7 | -13.06191 | -47.82542 | 2025-05-17 03:49:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a9ae2b92-f5b4-3c49-9c65-4018b7eaeeb0 | -12.83521 | -47.4038 | 2025-05-17 03:49:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 636111c3-cb15-393e-a31c-3278a9cfdb57 | -13.31772 | -45.39226 | 2025-05-17 03:49:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8c7833bb-ea5f-36b9-96ff-d3ecc3cfa66b | -12.99379 | -46.31755 | 2025-05-17 03:49:00 | NOAA-21 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| df591ced-a18a-3b1f-a9d9-deaf681ee9bb | -13.3114 | -45.4009 | 2025-05-17 03:49:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 75c8fd4b-bedd-3eaf-8b4c-2c076fb3c44c | -11.15963 | -48.67319 | 2025-05-17 03:49:00 | NOAA-21 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 438dab7c-9ddb-344e-9a2c-c551e458e3e3 | -7.94864 | -49.76177 | 2025-05-17 03:49:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| f42cfc4b-750f-33a1-b600-0ebe67731067 | -12.83459 | -47.40701 | 2025-05-17 03:49:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2ddeb310-ac77-3048-ae24-f37944556b52 | -13.31948 | -45.38286 | 2025-05-17 03:49:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5acc72f4-d790-3b15-9863-011abd991c7f | -13.31595 | -45.40173 | 2025-05-17 03:49:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1e9d65e1-0b41-3c89-8d74-9513894b57d8 | -11.57769 | -47.60927 | 2025-05-17 03:49:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| c9c461a8-51c8-3db9-9806-dbfb9c35501b | -11.15977 | -48.67732 | 2025-05-17 03:49:00 | NOAA-21 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 11.5 |
| e9d95c9f-f962-30b0-8aa4-d5d8e2d6550a | -11.69599 | -44.62186 | 2025-05-17 03:49:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2a5ef4fe-88b8-39ab-af09-72478a00fdb3 | -11.78907 | -47.40101 | 2025-05-17 03:49:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4ed1daa3-15eb-3e3f-b3ed-ea95c53bd68c | -13.30853 | -45.36615 | 2025-05-17 03:49:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 4c27c674-a9e4-3560-b166-216319625b4d | -11.64651 | -48.02617 | 2025-05-17 03:49:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 2ba6e205-51cb-3198-adb9-6fd23cded632 | -11.79894 | -47.37807 | 2025-05-17 03:49:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5206e356-9958-3dd4-baff-9efb9d0d2fac | -11.64503 | -48.03381 | 2025-05-17 03:49:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |


[Clique aqui para ver as próximas entradas](README4.md)
