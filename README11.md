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
| 77d611a9-bf58-34b2-ad4e-6cca0084eb88 | -2.1954 | -47.938999 | 2024-10-29 00:28:54 | METOP-C | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5774fc2f-3376-3b69-86d0-cc07d5aa7180 | -2.4404 | -49.019402 | 2024-10-29 00:28:54 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 76305382-d86e-36d7-831a-48a7b08fe0cb | -2.4427 | -49.029598 | 2024-10-29 00:28:54 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c9fbe213-a0b8-373a-b2fa-c79adc49fcb5 | -2.1837 | -47.932499 | 2024-10-29 00:28:54 | METOP-C | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c659de8d-a5c5-3e63-96c1-53aeef0215d6 | -2.1856 | -47.9412 | 2024-10-29 00:28:54 | METOP-C | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0f2a8118-f0d9-335c-88b8-d6cca0c47035 | -2.1877 | -47.9501 | 2024-10-29 00:28:54 | METOP-C | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e9cdf425-65e1-3510-83ab-41c152a61e7f | -2.2904 | -48.4935 | 2024-10-29 00:28:54 | METOP-C | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 41e3a081-ebb1-3871-8fdd-098849eb8d25 | -2.3495 | -48.890202 | 2024-10-29 00:28:55 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b150eb4b-b7b7-3f53-a3f6-3027937ed868 | -2.3518 | -48.900299 | 2024-10-29 00:28:55 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d525e3e4-c1e9-35d7-9704-05046beb4417 | -2.3541 | -48.910301 | 2024-10-29 00:28:55 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| afb5cdd7-c976-34a9-bedc-feba6ebceb5d | -2.342 | -48.9025 | 2024-10-29 00:28:55 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e8774f10-88ee-36f0-ac72-ff39785a4938 | -2.3443 | -48.912498 | 2024-10-29 00:28:55 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fc08214c-74bd-3dda-845a-dd9f0400b3ae | -2.9213 | -51.746799 | 2024-10-29 00:28:56 | METOP-C | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1635c5ad-5dfa-363b-851e-e8c03bede393 | -2.0488 | -48.017799 | 2024-10-29 00:28:56 | METOP-C | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e53ed206-07ae-3318-93f8-54afd8cb57cc | -2.1851 | -48.7085 | 2024-10-29 00:28:57 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 31a734e7-1604-3a40-a7f6-10f0b3268bbc | -2.1873 | -48.718201 | 2024-10-29 00:28:57 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 95242d4a-0b6e-352b-b8eb-cde20eff6f96 | -2.2095 | -48.816399 | 2024-10-29 00:28:57 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8eae6144-b095-37db-8eaf-57b948dfbac0 | -2.2118 | -48.826302 | 2024-10-29 00:28:57 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9f7c2156-cdc2-3abe-ad8b-0b48e72f3bfc | -2.1975 | -48.808601 | 2024-10-29 00:28:57 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 024ed131-f9a8-3db8-b7d0-799dc18502f1 | -2.1997 | -48.818501 | 2024-10-29 00:28:57 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bc510463-3525-393c-9412-e991673afcd6 | -2.202 | -48.8284 | 2024-10-29 00:28:57 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1df72404-65bc-3676-8eb5-4cd2e540d7b2 | -1.8444 | -47.436501 | 2024-10-29 00:28:57 | METOP-C | IRITUIA | PARÁ | Brasil | 1503507 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 239e6bfd-43b5-3e38-940f-06f595a78457 | -1.8463 | -47.444698 | 2024-10-29 00:28:57 | METOP-C | IRITUIA | PARÁ | Brasil | 1503507 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f8510b15-1285-342e-8296-4fa1e4161992 | -1.6867 | -47.376999 | 2024-10-29 00:29:00 | METOP-C | IRITUIA | PARÁ | Brasil | 1503507 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a0e71105-07e0-3b4f-9a61-31239cbe5a8f | -1.6886 | -47.385101 | 2024-10-29 00:29:00 | METOP-C | IRITUIA | PARÁ | Brasil | 1503507 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 852385c8-47f6-34db-ae60-3852ef521ce2 | -1.7894 | -47.8279 | 2024-10-29 00:29:00 | METOP-C | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0ca92d61-66f2-312d-9999-296a0b3ef0f4 | -1.7914 | -47.836498 | 2024-10-29 00:29:00 | METOP-C | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ae5050d5-220b-3e34-a9be-1d08b4b38a15 | -1.6769 | -47.379101 | 2024-10-29 00:29:00 | METOP-C | IRITUIA | PARÁ | Brasil | 1503507 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 55c74887-f12a-3e29-95c0-8e7f60105eed | -1.6788 | -47.387199 | 2024-10-29 00:29:00 | METOP-C | IRITUIA | PARÁ | Brasil | 1503507 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cc5c2419-4ee1-36de-a3d0-fb5afe5014dd | -2.6504 | -51.722801 | 2024-10-29 00:29:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| df1f1b30-d934-3a42-b7d6-4eed6d0e74e5 | -2.6539 | -51.738499 | 2024-10-29 00:29:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 06d24e76-d616-386e-9521-a35fe6bf3134 | -2.6407 | -51.724899 | 2024-10-29 00:29:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d78f9dd6-f66d-3fa4-aa00-3ded26f9c8b7 | -2.6442 | -51.740601 | 2024-10-29 00:29:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2209ae6c-f357-361a-a2c8-e81f03684199 | -3.1315 | -54.239399 | 2024-10-29 00:29:01 | METOP-C | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5b8a2308-2cfa-3ff3-a775-bdf25880162a | -1.4564 | -46.864101 | 2024-10-29 00:29:02 | METOP-C | SANTA LUZIA DO PARÁ | PARÁ | Brasil | 1506559 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4c7a4cc1-69b5-306b-9f5e-8b879a9ee24c | -1.4581 | -46.871799 | 2024-10-29 00:29:02 | METOP-C | SANTA LUZIA DO PARÁ | PARÁ | Brasil | 1506559 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a973ff5b-2303-34de-98aa-22830dce8019 | -1.5312 | -47.192001 | 2024-10-29 00:29:02 | METOP-C | OURÉM | PARÁ | Brasil | 1505403 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b2e1fd0d-234e-3c10-8f8e-58cf13443e2e | -1.533 | -47.199902 | 2024-10-29 00:29:02 | METOP-C | OURÉM | PARÁ | Brasil | 1505403 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9ca8eefc-6e17-3924-8b0d-c8ee44647d74 | -1.5349 | -47.207901 | 2024-10-29 00:29:02 | METOP-C | OURÉM | PARÁ | Brasil | 1505403 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 15fb30ae-32c7-3b74-a90b-dace152a0b7c | -3.1218 | -54.241501 | 2024-10-29 00:29:02 | METOP-C | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d476a907-ee1b-35ed-83a9-18a37ddf42b1 | -3.1271 | -54.265499 | 2024-10-29 00:29:02 | METOP-C | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4c7bf61a-d7fc-3716-9e68-5bcbc4f011a9 | -3.1121 | -54.243599 | 2024-10-29 00:29:02 | METOP-C | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f721ae82-7a39-3293-a8ad-c3a33c1dc9c2 | -3.1174 | -54.267502 | 2024-10-29 00:29:02 | METOP-C | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 28470f39-b739-3c67-aabc-3044e66f1c80 | -1.5134 | -47.2043 | 2024-10-29 00:29:02 | METOP-C | OURÉM | PARÁ | Brasil | 1505403 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6839cc3c-2d2f-31c2-aaec-8bcb0f254aba | -3.1024 | -54.245602 | 2024-10-29 00:29:02 | METOP-C | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0664a27d-3033-3a34-960f-3b025fe10af0 | -3.1078 | -54.2696 | 2024-10-29 00:29:02 | METOP-C | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4dcc5d91-57ba-3de5-a810-2d2ec908b183 | -3.0927 | -54.2477 | 2024-10-29 00:29:02 | METOP-C | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d0479810-4132-35ab-bda7-65ee66223549 | -2.876 | -53.321301 | 2024-10-29 00:29:02 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 81fad531-69d7-3d81-8949-847f73d39a52 | -2.8618 | -53.302898 | 2024-10-29 00:29:02 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a6eff7bb-cacc-3dc1-bcda-2983c755a5f3 | -2.8663 | -53.323399 | 2024-10-29 00:29:02 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e8b6bb41-e92f-38b2-9a6b-78a9260cd3ba | -2.8709 | -53.3438 | 2024-10-29 00:29:02 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0b0821c5-36d5-3527-98ae-80cce18b91b0 | -2.8566 | -53.3255 | 2024-10-29 00:29:03 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 65cb95d1-242c-37c6-b2cd-3411fc08f9d7 | -2.9813 | -54.475601 | 2024-10-29 00:29:05 | METOP-C | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a84c214d-48e1-324a-8a3d-f4f63b589db1 | -2.9868 | -54.500401 | 2024-10-29 00:29:05 | METOP-C | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d3072fa9-58de-373e-8947-7df17cdbc26a | -1.1706 | -46.5158 | 2024-10-29 00:29:05 | METOP-C | AUGUSTO CORRÊA | PARÁ | Brasil | 1500909 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 93543fa1-bf98-3192-9f03-348d7f3be15b | -1.1723 | -46.523201 | 2024-10-29 00:29:05 | METOP-C | AUGUSTO CORRÊA | PARÁ | Brasil | 1500909 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4c54c2bc-5bbe-3f94-8e1a-9864dd592397 | -2.9661 | -54.452999 | 2024-10-29 00:29:05 | METOP-C | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 41d9ff59-ac99-3ab8-af7a-c7e0ea265136 | -2.9716 | -54.477699 | 2024-10-29 00:29:05 | METOP-C | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e171bbe4-ca41-3b88-95dd-b5e0990a8779 | -2.9772 | -54.502499 | 2024-10-29 00:29:05 | METOP-C | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6ab02ab1-1f93-37f0-9d96-bc1669caba55 | -2.9827 | -54.527401 | 2024-10-29 00:29:05 | METOP-C | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| dd2b0ca5-4d0a-3809-a9fb-22b8e22c86b5 | -2.962 | -54.479801 | 2024-10-29 00:29:05 | METOP-C | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 87955557-16bd-3616-82fd-04861d7c94f7 | -2.9675 | -54.504601 | 2024-10-29 00:29:05 | METOP-C | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 924b0ae9-d280-33f3-a003-98dc8508b886 | -1.3468 | -47.512199 | 2024-10-29 00:29:06 | METOP-C | SANTA MARIA DO PARÁ | PARÁ | Brasil | 1506609 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 844b0fb4-4b87-3d2e-9d76-351634b41d94 | -1.3487 | -47.520401 | 2024-10-29 00:29:06 | METOP-C | SANTA MARIA DO PARÁ | PARÁ | Brasil | 1506609 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2fc37792-5e29-3040-bc56-512745c62866 | -1.3389 | -47.522598 | 2024-10-29 00:29:06 | METOP-C | SANTA MARIA DO PARÁ | PARÁ | Brasil | 1506609 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ddad750d-ac45-34a6-91bf-82604a2e749e | -1.1164 | -46.819302 | 2024-10-29 00:29:07 | METOP-C | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 366d81ef-6398-3117-bdb9-daa852e20053 | -1.1182 | -46.8269 | 2024-10-29 00:29:07 | METOP-C | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1410065f-537f-3859-b9f3-6de01726f426 | -1.0006 | -47.0788 | 2024-10-29 00:29:10 | METOP-C | PRIMAVERA | PARÁ | Brasil | 1506104 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 85817a18-aa78-362d-abcd-ad87b0cc0766 | -1.0024 | -47.086498 | 2024-10-29 00:29:10 | METOP-C | PRIMAVERA | PARÁ | Brasil | 1506104 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 40282910-b35d-3eab-85f4-936d9e1a44e3 | -1.064 | -47.626701 | 2024-10-29 00:29:11 | METOP-C | MARAPANIM | PARÁ | Brasil | 1504406 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| eafaf39c-6e5f-33e6-8a79-6b16eae9f097 | -1.0659 | -47.634899 | 2024-10-29 00:29:11 | METOP-C | IGARAPÉ-AÇU | PARÁ | Brasil | 1503200 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a401e7b1-04f5-3d28-a885-bfeabc439dd8 | -1.5494 | -52.0965 | 2024-10-29 00:29:19 | METOP-C | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 791fc373-7220-35ad-84f2-129a1f0b4e89 | -1.7121 | -54.472401 | 2024-10-29 00:29:26 | METOP-C | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0862a91f-f50c-341f-93b3-c7e46afc3ac4 | -1.7175 | -54.495998 | 2024-10-29 00:29:26 | METOP-C | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 10d29d37-1b12-3e54-b759-ef16075cc6cb | -1.7229 | -54.519798 | 2024-10-29 00:29:26 | METOP-C | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 08e2eb79-1be3-31e7-b2bb-a0b88923c566 | -1.7079 | -54.4981 | 2024-10-29 00:29:26 | METOP-C | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6e102112-1b95-38c2-97fb-24bccfc052e5 | -1.7133 | -54.5219 | 2024-10-29 00:29:26 | METOP-C | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 28a0d347-c180-3850-b4ff-05647038f43c | -1.454 | -54.052399 | 2024-10-29 00:29:28 | METOP-C | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| dd1176a3-ea52-3f4e-aa8b-f41475b08607 | -0.9801 | -53.6717 | 2024-10-29 00:29:35 | METOP-C | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b4667a60-908e-3f2d-ae25-8e65a62fc06c | -0.9847 | -53.692001 | 2024-10-29 00:29:35 | METOP-C | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 810487b0-0f75-3776-a940-50f974d62fec | 1.377 | -50.875301 | 2024-10-29 00:30:02 | METOP-C | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| dfa8c4f3-7d5a-310a-bd84-4223832ef004 | -1.714 | -54.5335 | 2024-10-29 00:35:15 | GOES-16 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 88.4 |
| 8c10bba1-cc88-3c4b-8b37-cec16da03004 | -2.3353 | -48.9137 | 2024-10-29 00:35:19 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 102.3 |
| 8fce4edb-3035-3b1d-a42a-5284001b0af5 | -2.3537 | -48.9133 | 2024-10-29 00:35:19 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 75.2 |
| 2df7cdb0-b90e-346a-bd73-8bc825929d52 | -2.5251 | -47.442 | 2024-10-29 00:35:20 | GOES-16 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 74.8 |
| 6a39e978-9efc-3798-9503-a9e99805d4f6 | -2.6398 | -51.758 | 2024-10-29 00:35:21 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 55.7 |
| 997378fc-4b53-3e32-bb32-0a4b1f003e98 | -2.8555 | -53.3459 | 2024-10-29 00:35:22 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 72.6 |
| 500e7461-1d3a-388d-8638-354c15117ee4 | -2.8739 | -53.3454 | 2024-10-29 00:35:22 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 65.4 |
| e6b44b92-74af-3250-b405-708f2a852e22 | -2.9619 | -54.5304 | 2024-10-29 00:35:23 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 89.7 |
| 433a5305-8f52-3304-8894-ec151463e8d9 | -2.962 | -54.5104 | 2024-10-29 00:35:23 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 131.5 |
| bc1296a5-b9a9-3866-bd2b-1dae67711786 | -2.9803 | -54.5299 | 2024-10-29 00:35:23 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 144.8 |
| cbeb9c40-fe6d-3419-8855-388ef7fd2d24 | -2.9804 | -54.5099 | 2024-10-29 00:35:23 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 231.7 |
| 5d42a892-7ecf-3bc2-a390-a62edd76f0c7 | -3.0734 | -54.167 | 2024-10-29 00:35:23 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 55.8 |
| aaa845e2-8697-310e-ab83-f2eab13cc0ca | -3.1097 | -54.2865 | 2024-10-29 00:35:23 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 145.1 |
| ae7a0a7f-e3b6-36e0-918e-3d9989a1435b | -3.1098 | -54.2665 | 2024-10-29 00:35:23 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 97.9 |
| 9edf6c50-568c-3dc8-89af-c500e4ea911f | -3.1281 | -54.286 | 2024-10-29 00:35:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 60.2 |
| 1c163ba9-9d49-3c6e-9cae-b8baa891fb60 | -3.1281 | -54.266 | 2024-10-29 00:35:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 72.3 |
| 401abafa-be72-33be-ad33-3014c064f6f8 | -3.1794 | -50.3922 | 2024-10-29 00:35:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 58.1 |
| 8d68fb7a-d2bf-3050-a437-85ccae33f058 | -3.2503 | -46.8709 | 2024-10-29 00:35:24 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 57.5 |
| 7d12f47c-e6a2-3bf0-b148-7c6533c7e818 | -3.2548 | -45.9186 | 2024-10-29 00:35:24 | GOES-16 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 65.2 |


[Clique aqui para ver as próximas entradas](README12.md)
