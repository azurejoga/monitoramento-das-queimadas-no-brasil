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

## Dados Diários - Página 88

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 930155d5-cd48-3f80-9acd-dbca9509304e | -10.65975 | -44.49932 | 2024-10-03 04:27:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 6f28c91b-4a2b-3cf3-9f14-972cc8831702 | -10.65915 | -44.50334 | 2024-10-03 04:27:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 058fe7e7-c0a0-35c4-993e-b8b8384563c5 | -10.65623 | -44.49879 | 2024-10-03 04:27:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 6.0 |
| d3d3f72f-222a-3b99-877d-4e6aaed7c70b | -10.63628 | -45.1933 | 2024-10-03 04:27:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 910fc17f-ee89-3a98-8f01-3bf7fb3213a9 | -10.43363 | -44.90631 | 2024-10-03 04:27:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b0473c3a-9d12-3c7e-8035-e613a2b7018c | -10.89064 | -45.98611 | 2024-10-03 04:27:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a20bf603-3ff8-3560-a35a-dab59c8b8ca5 | -10.89009 | -45.98971 | 2024-10-03 04:27:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6ef5bef2-3149-3d0b-94af-0b37f98dc439 | -10.8884 | -45.97838 | 2024-10-03 04:27:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| cf155bf3-3b96-3ca0-a510-8881c4c4b665 | -10.88336 | -45.96652 | 2024-10-03 04:27:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 95cc0de9-5ec2-3c5c-9756-f0d95e9eb213 | -13.16383 | -46.31571 | 2024-10-03 04:27:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 7d234399-0d36-34b5-b3fa-17671bb51324 | -13.16329 | -46.31928 | 2024-10-03 04:27:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f2e5f568-2359-3fc6-84bc-099083493498 | -12.27255 | -45.96748 | 2024-10-03 04:27:00 | NOAA-21 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 1f9d13ed-f5fd-3377-bcc7-c6222c3b5284 | -12.26917 | -45.96695 | 2024-10-03 04:27:00 | NOAA-21 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 8c99e442-a582-3ca4-b1b9-09a9ccca2943 | -12.26579 | -45.9664 | 2024-10-03 04:27:00 | NOAA-21 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 9d5c2cb3-b544-347d-b5f0-b8a239d09cc5 | -13.18587 | -45.45721 | 2024-10-03 04:27:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2d543c1b-a29f-32cd-9d47-bae0f3939bd3 | -13.18297 | -45.45277 | 2024-10-03 04:27:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c6bad2b2-c733-3684-ae38-21b2f2bc6ef3 | -13.18008 | -45.44831 | 2024-10-03 04:27:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4f172715-16c6-33c7-94aa-2f0c6fd3ebaa | -13.17661 | -45.44779 | 2024-10-03 04:27:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 272f66c7-10b3-3d2c-b203-aa561d641a28 | -13.17314 | -45.44727 | 2024-10-03 04:27:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a4ca6486-519f-3247-b0c2-155aa0a59e4b | -13.16217 | -45.44955 | 2024-10-03 04:27:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ec9fe278-7834-3927-80d7-91d86feff28c | -13.15992 | -45.45018 | 2024-10-03 04:27:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e17a3667-d357-3474-bcde-3b5bd086e467 | -12.74482 | -45.45585 | 2024-10-03 04:27:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 058acf72-1946-39ec-ad9d-f8fd95f9bb4f | -15.18189 | -45.48075 | 2024-10-03 04:27:00 | NOAA-21 | CHAPADA GAÚCHA | MINAS GERAIS | Brasil | 3116159 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0797d84e-bd6f-3e68-a769-e02bc831998f | -14.69398 | -45.45658 | 2024-10-03 04:27:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4f1f2b8d-c308-3867-a79c-01b59eb42eaf | -14.68989 | -45.46005 | 2024-10-03 04:27:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ae95d4df-8837-36b7-9662-be7a86c878ae | -14.44013 | -45.71315 | 2024-10-03 04:27:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 749018e0-0b79-3978-9818-e84381b0af39 | -14.43667 | -45.7126 | 2024-10-03 04:27:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8d040910-3bbc-3cee-9c43-8bbe93ff8805 | -14.19949 | -46.46064 | 2024-10-03 04:27:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5d9f6667-ca53-312e-87ca-6e1485f93108 | -14.19893 | -46.46432 | 2024-10-03 04:27:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 2e31fb21-7ff7-3adf-9b83-df2994db682f | -14.19837 | -46.46799 | 2024-10-03 04:27:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| a97a6e19-57e0-33b8-b251-0f4b84fddbe0 | -14.19555 | -46.46383 | 2024-10-03 04:27:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0e931901-b26b-31ca-bf73-4be2ac42269b | -14.19499 | -46.46748 | 2024-10-03 04:27:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 144a3775-8751-3cfb-88bc-ba414373e189 | -14.19444 | -46.47113 | 2024-10-03 04:27:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 3cbd15fd-4975-36ea-8d61-a2ad29f0b9b6 | -14.19273 | -46.45959 | 2024-10-03 04:27:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 1847f76b-84a5-330e-9967-bcdafb46fc85 | -14.19107 | -46.47058 | 2024-10-03 04:27:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| ff1e45d5-5e72-37e4-bef8-587a2673d01f | -14.1877 | -46.47002 | 2024-10-03 04:27:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8d70c627-1ca1-3168-833b-d2e7e9640ebb | -14.18094 | -46.46903 | 2024-10-03 04:27:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 87f46ef9-04dd-3b1a-95e0-987074f7be5c | -14.17756 | -46.46853 | 2024-10-03 04:27:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b8a72ee1-946e-3574-9e68-4f77eed8d8a8 | -14.1629 | -46.45113 | 2024-10-03 04:27:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 217ad795-1ca7-3aae-82ec-b80592c2bcaa | -14.03451 | -45.46798 | 2024-10-03 04:27:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fd148587-5b95-3ecb-9d5e-544e427b7986 | -7.72731 | -45.42192 | 2024-10-03 04:27:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ed9c5391-8879-335f-93a2-58b8caebc168 | -7.72453 | -45.41782 | 2024-10-03 04:27:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a2594184-76fe-3d25-80bf-b95364e28579 | -7.72397 | -45.42139 | 2024-10-03 04:27:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b1a38214-493c-30c3-a67f-d07e2d68884e | -7.72119 | -45.41729 | 2024-10-03 04:27:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| b4caac8d-6cd0-353e-9e8e-e0a57ed45389 | -7.72064 | -45.42086 | 2024-10-03 04:27:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 8a4ad639-01fb-343b-8819-f2993bff7b72 | -7.71397 | -45.41977 | 2024-10-03 04:27:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 0484f3ef-1e2a-3a44-9b8d-82395b3d2b8d | -7.71341 | -45.42335 | 2024-10-03 04:27:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 4.4 |
| bb3648a9-f969-34df-a180-584ed969476a | -7.91178 | -46.42415 | 2024-10-03 04:27:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ee076ef4-a180-3c64-9f16-1819a98d4e99 | -7.90848 | -46.42363 | 2024-10-03 04:27:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 539492f2-40e2-30ae-b3b6-92b611cf4682 | -7.85624 | -46.25534 | 2024-10-03 04:27:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 845d2bf9-e7dd-33da-b978-c0039a4a19ff | -7.8557 | -46.2588 | 2024-10-03 04:27:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5d6eb9bd-fd49-3556-9c4d-3fd0b22a4bdc | -14.8114 | -48.09386 | 2024-10-03 04:27:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 250d3da8-7183-3362-9508-956c1aa4cda1 | -7.85294 | -46.25482 | 2024-10-03 04:27:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a3cfd872-1699-3276-aefb-c0056e91dc81 | -7.8524 | -46.25828 | 2024-10-03 04:27:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| eb10756c-a2fa-34cd-ae02-82db6cbc5e37 | -7.74554 | -46.65591 | 2024-10-03 04:27:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 284dfa97-4759-3d22-9ebe-f8da8f16031a | -7.74278 | -46.65194 | 2024-10-03 04:27:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ecf50562-20b0-3006-8081-288ed40949ca | -7.74267 | -46.15593 | 2024-10-03 04:27:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| acc4e686-15b3-37fa-9abf-d80ebed99de0 | -7.74044 | -46.14847 | 2024-10-03 04:27:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bd50bc77-5014-30a8-b6c6-7ae13bc84841 | -7.73768 | -46.14448 | 2024-10-03 04:27:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6c0f7a1f-d8ff-35ec-9c97-cf4bc1055734 | -7.73714 | -46.14795 | 2024-10-03 04:27:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0b72e828-11f7-3446-915f-b5609c1ee61a | -7.73215 | -46.13648 | 2024-10-03 04:27:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f577743d-8f33-31e0-88bc-026eea9f8f70 | -7.72885 | -46.13596 | 2024-10-03 04:27:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b41cfb88-4ea0-3170-b38f-027407697245 | -7.72831 | -46.13943 | 2024-10-03 04:27:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cb97478b-9797-3d9f-8230-bd4e82bcd3d1 | -7.72437 | -46.13883 | 2024-10-03 04:27:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 25f81dd3-ad17-3b7e-8c88-c15712c0056b | -7.71559 | -46.15167 | 2024-10-03 04:27:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 42440460-a77d-3651-a64f-0ff91ee8a8cb | -7.70791 | -46.15755 | 2024-10-03 04:27:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e42c18f1-ecc0-393c-88c3-53fe5724dcc5 | -7.70737 | -46.16102 | 2024-10-03 04:27:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c9d991df-adf8-395e-bc0f-e6930c44f664 | -14.75587 | -48.08103 | 2024-10-03 04:27:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 02c4479a-620e-31c8-a04d-024acaee710b | -8.93017 | -45.64495 | 2024-10-03 04:27:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 7d1026e4-939c-3968-a186-69b0fa1b9c11 | -9.33807 | -46.56963 | 2024-10-03 04:27:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 5b51b16a-9ab3-3758-8b54-f265e2f91b75 | -9.10213 | -46.90169 | 2024-10-03 04:27:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 959bd50d-6633-34bf-bd3a-3bf013bd8b65 | -9.02461 | -46.59423 | 2024-10-03 04:27:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bc1043a2-009d-3918-8d59-871aa9c27418 | -8.72728 | -47.10089 | 2024-10-03 04:27:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2fe5843a-100f-3395-99ae-ed82e4f60cf4 | -8.72673 | -47.10436 | 2024-10-03 04:27:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6f178bef-5c04-35ec-92ba-acbb3cedb528 | -8.72343 | -47.10384 | 2024-10-03 04:27:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6c036703-0d33-3ba3-9d2f-88d86deaceb4 | -8.62993 | -46.52788 | 2024-10-03 04:27:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ff9d0160-f288-3156-bb62-8a471f066c21 | -8.62938 | -46.53134 | 2024-10-03 04:27:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 196e1b04-7920-3673-9dc0-25b0ab3d08dc | -8.62717 | -46.52388 | 2024-10-03 04:27:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| aa3d9484-8f28-3074-bf1f-d5c82aba0845 | -8.62663 | -46.52735 | 2024-10-03 04:27:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| dd0e110c-456d-3161-8e44-e865ada13585 | -8.62387 | -46.52337 | 2024-10-03 04:27:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| c0c527b7-1010-3a36-977d-26ef16608222 | -8.61343 | -46.52528 | 2024-10-03 04:27:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0cdb8cf4-7dbb-3ffc-a767-7b7163ed18f5 | -8.60959 | -46.52822 | 2024-10-03 04:27:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ba4b5b6e-ccc5-3e60-986b-130e94b87286 | -8.60629 | -46.5277 | 2024-10-03 04:27:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7359fc83-36ea-3c1d-b27a-cc125d03ed91 | -8.60575 | -46.53117 | 2024-10-03 04:27:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0388249e-9060-3155-a122-6c8052d3facd | -8.60299 | -46.52718 | 2024-10-03 04:27:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| fd4cd9de-d5ea-3701-8dc5-439db9c0b70f | -8.59969 | -46.52667 | 2024-10-03 04:27:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| fbeaa35e-109d-305c-a412-6dc067ad91e5 | -8.59639 | -46.52615 | 2024-10-03 04:27:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| da75395e-2242-3cbf-a691-03ad88ef8619 | -8.59309 | -46.52563 | 2024-10-03 04:27:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| eea50b7c-a132-31c7-aba1-2acd53c4e6f3 | -8.58979 | -46.52512 | 2024-10-03 04:27:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 750ea889-a480-38d4-8c6c-109fd3c28b84 | -8.58925 | -46.52858 | 2024-10-03 04:27:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| be332bd1-2000-315a-8217-536b6613309a | -8.4948 | -46.85072 | 2024-10-03 04:27:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a2c4801b-2532-35ea-b9e3-9f963a6ec196 | -8.49425 | -46.85419 | 2024-10-03 04:27:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cce59b08-60a6-39f8-9272-ac8516e092f3 | -8.43302 | -46.30793 | 2024-10-03 04:27:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b9adefc0-a8cb-3dc1-a379-e1e0894d6917 | -8.43134 | -46.29699 | 2024-10-03 04:27:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| bdfd3eeb-0d87-3a74-890a-5a77c0638589 | -8.4308 | -46.30046 | 2024-10-03 04:27:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 88f364e6-bc65-313c-9690-16aa00f5170d | -8.43026 | -46.30394 | 2024-10-03 04:27:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8bae8519-5aa4-3a97-b5c9-1467da53a299 | -8.4298 | -46.85053 | 2024-10-03 04:27:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a95f197d-585d-3d48-add6-8853334806a7 | -8.42971 | -46.30742 | 2024-10-03 04:27:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 22e727c9-816f-3a6b-afc1-eacea619b598 | -8.42926 | -46.85399 | 2024-10-03 04:27:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| def12cc9-5e28-346c-b48f-4730835b84a9 | -8.42804 | -46.29647 | 2024-10-03 04:27:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |


[Clique aqui para ver as próximas entradas](README89.md)
