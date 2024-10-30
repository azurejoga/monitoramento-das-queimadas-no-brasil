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

## Dados Diários - Página 102

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 71fea24b-4849-3333-aece-f66756e23847 | -5.15394 | -45.02778 | 2024-10-30 12:53:00 | TERRA_M-T | SÃO RAIMUNDO DO DOCA BEZERRA | MARANHÃO | Brasil | 2111631 | 21 | 33 | nan | nan | nan | Cerrado | 22.7 |
| f94e5391-1ed9-382b-bf18-5092c0cb6c4b | -4.74071 | -44.09017 | 2024-10-30 12:53:00 | TERRA_M-T | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 21.2 |
| f386f7f7-1104-3726-9d5c-d61a6eb9d4ce | -4.59951 | -44.31679 | 2024-10-30 12:53:00 | TERRA_M-T | CAPINZAL DO NORTE | MARANHÃO | Brasil | 2102754 | 21 | 33 | nan | nan | nan | Cerrado | 17.6 |
| f1a1dbd4-ea3d-3b97-887f-858a0e4a76de | -9.89366 | -44.75951 | 2024-10-30 12:55:00 | TERRA_M-T | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 41.5 |
| cb4211fb-d1e9-3151-b0e4-f463eb0fe203 | -9.89135 | -44.77793 | 2024-10-30 12:55:00 | TERRA_M-T | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 21.7 |
| 3a7ca6ee-f273-3d52-b9ac-9709a1e0b050 | -9.69237 | -43.98326 | 2024-10-30 12:55:00 | TERRA_M-T | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 65.0 |
| 1c7887f3-fb31-3f20-8148-92bf36a89afd | -9.6896 | -44.00466 | 2024-10-30 12:55:00 | TERRA_M-T | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 123.2 |
| 99138f58-d20f-3a2e-9ce2-97734573cf3e | -9.68863 | -43.98951 | 2024-10-30 12:55:00 | TERRA_M-T | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 101.7 |
| a2053a4b-0241-342c-a4d8-859861600fd4 | -9.686 | -44.01118 | 2024-10-30 12:55:00 | TERRA_M-T | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 45.2 |
| b105da1e-7ab3-3967-b55b-80f371f0f94f | -9.01311 | -44.92347 | 2024-10-30 12:55:00 | TERRA_M-T | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 22.7 |
| 0a634bfc-96a8-38b1-981f-5246989982aa | -9.01094 | -44.94091 | 2024-10-30 12:55:00 | TERRA_M-T | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 37.8 |
| 246c7d6b-ed58-35eb-8ef9-52ae2617bccd | -9.00664 | -44.93373 | 2024-10-30 12:55:00 | TERRA_M-T | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 49.0 |
| 2b623f4e-fe47-300e-8d64-a14303907420 | -8.86241 | -45.48875 | 2024-10-30 12:55:00 | TERRA_M-T | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 28.3 |
| b76547ed-6be7-389a-97e1-cdc1bc017e96 | -8.77755 | -44.71414 | 2024-10-30 12:55:00 | TERRA_M-T | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 25.2 |
| 40abaf9c-1f48-3371-8af1-cf729a110330 | -8.66775 | -44.0243 | 2024-10-30 12:55:00 | TERRA_M-T | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 18.3 |
| 6b3548e3-fb3b-35cd-8bd1-f35d96bf695c | -8.54617 | -44.57382 | 2024-10-30 12:55:00 | TERRA_M-T | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 32.2 |
| 9ce80bcd-fefb-34e8-98f5-399c7dcdc301 | -8.53622 | -44.5531 | 2024-10-30 12:55:00 | TERRA_M-T | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 33.6 |
| e5bc94f6-ca03-352e-868b-c31d0eef5906 | -8.53386 | -44.57164 | 2024-10-30 12:55:00 | TERRA_M-T | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 220.7 |
| 431e491e-6b37-3a16-8a36-fe16eb75a74f | -8.37441 | -40.51338 | 2024-10-30 12:55:00 | TERRA_M-T | DORMENTES | PERNAMBUCO | Brasil | 2605152 | 26 | 33 | nan | nan | nan | Caatinga | 51.6 |
| 38a46e9a-54b9-37ff-8795-f8b36dd75966 | -8.3709 | -40.50748 | 2024-10-30 12:55:00 | TERRA_M-T | DORMENTES | PERNAMBUCO | Brasil | 2605152 | 26 | 33 | nan | nan | nan | Caatinga | 61.5 |
| 0c7f5953-2c60-3ac9-89d7-19ec4938a422 | -8.36914 | -44.72087 | 2024-10-30 12:55:00 | TERRA_M-T | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 25.6 |
| 6475e900-8325-3ba5-8cd9-e1f86aa6b990 | -8.35921 | -44.70186 | 2024-10-30 12:55:00 | TERRA_M-T | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 47.4 |
| f2c2eec3-2b1e-38c6-ac63-206b04ca14a9 | -8.35682 | -44.72031 | 2024-10-30 12:55:00 | TERRA_M-T | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 119.9 |
| f6c6cef4-de41-303a-986c-8e98cf65b64f | -8.26174 | -44.84174 | 2024-10-30 12:55:00 | TERRA_M-T | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 122.2 |
| 95fdb0e0-d5ec-3e42-9717-5f751fc3d781 | -8.25944 | -44.85923 | 2024-10-30 12:55:00 | TERRA_M-T | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 128.3 |
| e21e27ec-6e7e-3c66-b588-fe3b9295c759 | -7.89365 | -42.9663 | 2024-10-30 12:55:00 | TERRA_M-T | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 77.2 |
| 89654de3-4340-3c87-9e36-d2df4eaa7fe5 | -7.88804 | -42.94649 | 2024-10-30 12:55:00 | TERRA_M-T | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 30.4 |
| 5cf5dbf2-72d6-3a2e-8af9-581ca378e9a3 | -7.88512 | -42.97043 | 2024-10-30 12:55:00 | TERRA_M-T | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 63.7 |
| c990b2b2-ccbd-3ebe-bc71-ca0f5569699c | -7.40104 | -44.23418 | 2024-10-30 12:55:00 | TERRA_M-T | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 66.6 |
| c994a475-d1d8-3b92-8fa0-fb9d5efafeb1 | -7.06704 | -43.38762 | 2024-10-30 12:55:00 | TERRA_M-T | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 35.8 |
| 07a62061-82b5-3fde-ba28-3b25c923b476 | -6.83947 | -42.81303 | 2024-10-30 12:55:00 | TERRA_M-T | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 49.5 |
| c9526f4a-0f1c-36ca-993b-13bf9daca3fc | -6.83372 | -42.80654 | 2024-10-30 12:55:00 | TERRA_M-T | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 31.0 |
| 4fa57c1d-2ee9-3758-acca-5c55cd1a1428 | -6.67713 | -43.04475 | 2024-10-30 12:55:00 | TERRA_M-T | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 33.7 |
| 0bfa0b4d-fe1a-370d-9c4b-2c8d90e075cc | -6.63912 | -41.99797 | 2024-10-30 12:55:00 | TERRA_M-T | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 34.9 |
| fe29af60-62e7-394f-8ff1-5e0c894173e2 | -6.63906 | -41.99128 | 2024-10-30 12:55:00 | TERRA_M-T | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 34.0 |
| e7ddf74d-a4be-3066-99a7-64c368db4a42 | -9.71411 | -46.25228 | 2024-10-30 12:55:00 | TERRA_M-T | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 184.9 |
| f0fa1e49-1d48-35e1-8501-b6b0eb799910 | -9.71222 | -46.26665 | 2024-10-30 12:55:00 | TERRA_M-T | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 18.9 |
| 647d0834-95d9-3aff-9ae3-d05e8c6b2558 | -9.70308 | -46.2509 | 2024-10-30 12:55:00 | TERRA_M-T | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 39.6 |
| 99e6cdcb-0a8e-3c47-9d3a-596a142fa763 | -9.67188 | -46.23203 | 2024-10-30 12:55:00 | TERRA_M-T | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 51.6 |
| f2c5862a-86b6-33d1-9e7b-5a5692b4258f | -9.67004 | -46.24642 | 2024-10-30 12:55:00 | TERRA_M-T | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 153.4 |
| 957533ed-2799-3c34-a44c-2993aca5bf01 | -9.66875 | -46.24031 | 2024-10-30 12:55:00 | TERRA_M-T | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 181.1 |
| a723b6b7-2a66-398d-b5c4-ef5f9f72989c | -9.65902 | -46.24497 | 2024-10-30 12:55:00 | TERRA_M-T | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 23.8 |
| 32d7923f-6273-3fce-aebc-d6edf51cf4db | -9.37399 | -45.96306 | 2024-10-30 12:55:00 | TERRA_M-T | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 33.9 |
| e549436e-9258-3384-86c3-2877a432b1bf | -8.84423 | -49.84861 | 2024-10-30 12:55:00 | TERRA_M-T | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 23.4 |
| ac1c5535-06ae-3acd-b1d0-0958d6079864 | -7.8369 | -48.95817 | 2024-10-30 12:55:00 | TERRA_M-T | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 7.5 |
| ff85f3bc-aeee-346d-8304-18cc76590357 | -7.47325 | -50.7923 | 2024-10-30 12:55:00 | TERRA_M-T | BANNACH | PARÁ | Brasil | 1501253 | 15 | 33 | nan | nan | nan | Amazônia | 12.5 |
| a43e9eb9-c0ae-375a-923d-4c9e85c8a656 | -6.70545 | -44.15076 | 2024-10-30 12:55:00 | TERRA_M-T | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 17.1 |
| 2c11d3dd-b3c2-3067-bb55-c4fc1f693e0a | -6.26655 | -49.43515 | 2024-10-30 12:55:00 | TERRA_M-T | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 261a814d-656f-37fd-9d90-cbfb1b8a24c6 | -3.3891 | -41.6201 | 2024-10-30 12:55:25 | GOES-16 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 77.4 |
| 89284b40-556d-3b10-b9e6-24aacb860b11 | -3.4078 | -41.6192 | 2024-10-30 12:55:25 | GOES-16 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 99.8 |
| 02935a9f-8623-3111-80a2-353a0f532b3e | -3.3889 | -41.6441 | 2024-10-30 12:55:25 | GOES-16 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 88.7 |
| 005b5799-3c88-3ca7-b339-842dde9dcf75 | -3.6648 | -42.4384 | 2024-10-30 12:55:27 | GOES-16 | LUZILÂNDIA | PIAUÍ | Brasil | 2205805 | 22 | 33 | nan | nan | nan | Cerrado | 170.6 |
| d5b91154-656d-3795-89d5-b1a8352fe4b5 | -4.2749 | -43.4357 | 2024-10-30 12:55:30 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 97.9 |
| 55e716e3-15b5-36fe-9f32-0c95194ebac3 | -4.2563 | -43.4368 | 2024-10-30 12:55:30 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 164.7 |
| e4b8ed41-7551-30aa-ba50-0fd3281432ba | -17.7446 | -57.5344 | 2024-10-30 12:56:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 64.9 |
| 3a75f43a-f016-3f48-b06c-936752bc4f2c | -17.745 | -57.5138 | 2024-10-30 12:56:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 81.4 |
| 726d6833-7942-3172-a6e8-417535e04ba3 | -17.7252 | -57.5162 | 2024-10-30 12:56:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 70.8 |
| 82efd126-ac87-3fec-b3ca-5d6344f0dde1 | -19.4874 | -56.6437 | 2024-10-30 12:56:55 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 91.4 |
| ca16e791-62e0-3a13-8def-b2dcc11018a5 | -19.5087 | -56.5779 | 2024-10-30 12:56:55 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 77.0 |
| 72ae1fbc-a0d8-3612-aa59-637e459a8f60 | -19.487 | -56.6647 | 2024-10-30 12:56:55 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 88.0 |
| 0ff0561a-4eaa-3137-9fdc-499b9dc676fa | -19.5083 | -56.5989 | 2024-10-30 12:56:55 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 73.3 |
| f994ef80-262e-3d57-81dd-6f165ef038ca | -20.255 | -55.4318 | 2024-10-30 12:56:59 | GOES-16 | DOIS IRMÃOS DO BURITI | MATO GROSSO DO SUL | Brasil | 5003488 | 50 | 33 | nan | nan | nan | Cerrado | 60.9 |
| 20ebaf80-004f-3938-83ce-0126cc0172a0 | -15.72046 | -53.34335 | 2024-10-30 12:57:00 | TERRA_M-T | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 2bba9856-ed55-3cbb-9912-1ed8a69af340 | -15.71904 | -53.35281 | 2024-10-30 12:57:00 | TERRA_M-T | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 37.6 |
| d4358c11-d316-39a4-8c01-6249e257bf2c | -15.01083 | -55.66921 | 2024-10-30 12:57:00 | TERRA_M-T | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 5f5149de-ac9c-333c-a71a-ad14bb3fc69a | -12.06337 | -46.50882 | 2024-10-30 12:57:00 | TERRA_M-T | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 15.9 |
| c592593d-1a38-3b75-a7d7-fb441e1e63b2 | -10.37314 | -49.91858 | 2024-10-30 12:57:00 | TERRA_M-T | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 10.1 |
| e9ae1904-2edf-3cee-9b5b-99d424c5684f | -10.37185 | -49.92778 | 2024-10-30 12:57:00 | TERRA_M-T | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 6839c030-0bf4-3c63-866c-e55c9c100bde | -10.78468 | -44.83646 | 2024-10-30 12:57:00 | TERRA_M-T | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 52.4 |
| 35f1eb49-e1a5-38ff-938b-7a8be7f6b431 | -15.76033 | -51.81479 | 2024-10-30 12:57:00 | TERRA_M-T | MONTES CLAROS DE GOIÁS | GOIÁS | Brasil | 5213707 | 52 | 33 | nan | nan | nan | Cerrado | 9.0 |
| e21de665-1712-3c10-ab47-fbf94e42b37f | -15.75145 | -51.81347 | 2024-10-30 12:57:00 | TERRA_M-T | MONTES CLAROS DE GOIÁS | GOIÁS | Brasil | 5213707 | 52 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 3e75f058-babe-32e4-b242-aa73bd06e34a | -13.90752 | -43.94809 | 2024-10-30 12:57:00 | TERRA_M-T | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 39.1 |
| 9ed0d753-4726-3aa4-9e6a-57476c2eb507 | -13.53923 | -50.71786 | 2024-10-30 12:57:00 | TERRA_M-T | NOVA CRIXÁS | GOIÁS | Brasil | 5214838 | 52 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 87ef6aa2-c8db-3fab-91d3-93ff63c2ca68 | -13.48648 | -43.24293 | 2024-10-30 12:57:00 | TERRA_M-T | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 61.1 |
| 007a102b-23bd-35dd-b31b-12b97ae776be | -13.48606 | -43.24814 | 2024-10-30 12:57:00 | TERRA_M-T | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 83.0 |
| 96e6f9f1-815f-3d2f-bf4b-8c265103fdc5 | -13.48328 | -43.27105 | 2024-10-30 12:57:00 | TERRA_M-T | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 51.4 |
| 55c7bbcd-5d89-3494-9c04-8c61dc9c4257 | -13.07165 | -43.02816 | 2024-10-30 12:57:00 | TERRA_M-T | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 41.5 |
| 929e716b-1d60-396d-bd72-9d3b0e0065dd | -12.44896 | -43.57314 | 2024-10-30 12:57:00 | TERRA_M-T | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 80.0 |
| 72ef95b3-b16d-36ba-a3ee-c13e5e8a3906 | -12.32448 | -41.79262 | 2024-10-30 12:57:00 | TERRA_M-T | SEABRA | BAHIA | Brasil | 2929909 | 29 | 33 | nan | nan | nan | Caatinga | 78.8 |
| 6b43ee95-3d5e-316c-ad9e-2c88f804d04e | -12.31491 | -41.79862 | 2024-10-30 12:57:00 | TERRA_M-T | SEABRA | BAHIA | Brasil | 2929909 | 29 | 33 | nan | nan | nan | Caatinga | 56.1 |
| c609f4aa-8600-30ec-bb4d-a321a5b4d347 | -11.73195 | -45.30495 | 2024-10-30 12:57:00 | TERRA_M-T | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 20.0 |
| a372da34-f9f0-3513-b66b-5c12b0fff3f2 | -11.40851 | -45.16787 | 2024-10-30 12:57:00 | TERRA_M-T | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 42.7 |
| 160c7cc2-58bb-35fa-98a2-b733e81bb2a7 | -11.40623 | -45.18624 | 2024-10-30 12:57:00 | TERRA_M-T | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 31.3 |
| 267ed281-dd03-32bc-adc4-03c024feac78 | -11.39616 | -45.16632 | 2024-10-30 12:57:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 65.5 |
| bb6e2c3f-5608-35c6-9c84-3900de221d93 | -10.86853 | -42.99432 | 2024-10-30 12:57:00 | TERRA_M-T | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 27.9 |
| dbb814d1-fc3f-30ff-8440-0d01328d669e | -10.86718 | -42.98752 | 2024-10-30 12:57:00 | TERRA_M-T | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 27.4 |
| 9086b321-316e-3e40-a42a-94552c1ff4dd | -10.78235 | -44.85551 | 2024-10-30 12:57:00 | TERRA_M-T | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 38.2 |
| c18d7f75-3fb1-3919-a2f9-88b6ee6f4cf7 | -10.61504 | -44.93592 | 2024-10-30 12:57:00 | TERRA_M-T | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 32.3 |
| 2aeb0a41-a108-3d00-8dbe-6ef38a9e881b | -10.15596 | -45.33613 | 2024-10-30 12:57:00 | TERRA_M-T | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 27.2 |
| f39b1093-a185-38d8-b04c-d0d8084f4ae2 | -10.14979 | -45.3408 | 2024-10-30 12:57:00 | TERRA_M-T | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 135.2 |
| 71794d2b-65e3-31c3-9bfb-fca83e522873 | -10.14771 | -45.35757 | 2024-10-30 12:57:00 | TERRA_M-T | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 23.3 |
| 6c602af4-2789-3e4e-927c-d4aafd04a2d0 | -10.14407 | -45.33426 | 2024-10-30 12:57:00 | TERRA_M-T | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 69.0 |
| 000caa39-a6f7-3b80-8b6b-3e6ab8201e01 | -10.14187 | -45.35109 | 2024-10-30 12:57:00 | TERRA_M-T | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 79.0 |
| 2519d638-6406-383e-b08c-a5b837222243 | -23.9923 | -54.1106 | 2024-10-30 12:57:18 | GOES-16 | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 83.0 |
| d51e4ba6-897e-3307-8cf7-db96957515b0 | -17.72106 | -57.51867 | 2024-10-30 12:59:00 | TERRA_M-T | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 41.8 |
| 785a9a47-7300-334e-b8bd-76e9c267f840 | -17.71584 | -57.5493 | 2024-10-30 12:59:00 | TERRA_M-T | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 71.6 |
| 13938776-355f-3917-906d-e34f1aa00d8a | -27.77414 | -51.07551 | 2024-10-30 12:59:00 | TERRA_M-T | ANITA GARIBALDI | SANTA CATARINA | Brasil | 4201000 | 42 | 33 | nan | nan | nan | Mata Atlântica | 10.4 |
| 5934b17d-3ada-3280-9441-f2d4c1b3363b | -27.05661 | -52.75703 | 2024-10-30 12:59:00 | TERRA_M-T | GUATAMBÚ | SANTA CATARINA | Brasil | 4206652 | 42 | 33 | nan | nan | nan | Mata Atlântica | 7.0 |
| 1926670b-cb0a-32d7-94fa-fb73a9729efe | -27.03024 | -52.74187 | 2024-10-30 12:59:00 | TERRA_M-T | GUATAMBÚ | SANTA CATARINA | Brasil | 4206652 | 42 | 33 | nan | nan | nan | Mata Atlântica | 9.8 |
| 1a1d0a9f-3876-30e0-b71f-2397dc921657 | -26.81315 | -52.51181 | 2024-10-30 12:59:00 | TERRA_M-T | XANXERÊ | SANTA CATARINA | Brasil | 4219507 | 42 | 33 | nan | nan | nan | Mata Atlântica | 10.7 |


[Clique aqui para ver as próximas entradas](README103.md)
