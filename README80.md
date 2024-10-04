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

## Dados Diários - Página 80

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a5f24486-a82e-3dd3-8e59-724e0d15297c | -20.18918 | -47.46737 | 2024-10-04 04:12:00 | NOAA-21 | PEDREGULHO | SÃO PAULO | Brasil | 3537008 | 35 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 9dc81a69-4af1-3a55-b44e-4d89fc428a61 | -20.31476 | -46.85347 | 2024-10-04 04:12:00 | NOAA-21 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 21.5 |
| aeed049d-800d-3001-9600-24d1e2e27284 | -20.31409 | -46.85741 | 2024-10-04 04:12:00 | NOAA-21 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 21.5 |
| af26d99c-6be2-313b-be39-d755b5dbc35b | -20.27463 | -46.88226 | 2024-10-04 04:12:00 | NOAA-21 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c128ffd9-f2c0-3301-b39a-408319589688 | -20.72218 | -46.8998 | 2024-10-04 04:12:00 | NOAA-21 | CÁSSIA | MINAS GERAIS | Brasil | 3115102 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| eb0b9ff9-e56a-376e-be35-63654fc5784d | -22.36786 | -47.94109 | 2024-10-04 04:12:00 | NOAA-21 | ITIRAPINA | SÃO PAULO | Brasil | 3523602 | 35 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c80d4778-faa3-3ef8-b8f5-f3a74df9ff25 | -22.3475 | -47.95448 | 2024-10-04 04:12:00 | NOAA-21 | BROTAS | SÃO PAULO | Brasil | 3507902 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 25994ca8-0b73-32e1-8e14-aa897f2cbf1f | -21.93126 | -48.21045 | 2024-10-04 04:12:00 | NOAA-21 | RIBEIRÃO BONITO | SÃO PAULO | Brasil | 3542909 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1411d0b9-008c-30ab-af51-2e57510eb4c6 | -21.92438 | -48.40939 | 2024-10-04 04:12:00 | NOAA-21 | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 32fa1852-9afa-3cdb-bb0e-16ed71590dbd | -21.92357 | -48.41387 | 2024-10-04 04:12:00 | NOAA-21 | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f5216027-9e06-3fa9-aa0a-ee62e0f60e2e | -21.92001 | -48.41312 | 2024-10-04 04:12:00 | NOAA-21 | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7e6ae7cb-623b-3f8b-970f-b67af55661aa | -21.9196 | -48.436 | 2024-10-04 04:12:00 | NOAA-21 | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 51767903-be39-3eb9-98de-9549e9f171c7 | -21.91645 | -48.41236 | 2024-10-04 04:12:00 | NOAA-21 | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e732c10c-119e-3a62-bfd7-a273abd4e2d3 | -21.91604 | -48.43524 | 2024-10-04 04:12:00 | NOAA-21 | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 744e0965-2dca-31c5-8594-f7de52218f2a | -21.91424 | -48.41367 | 2024-10-04 04:12:00 | NOAA-21 | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c1d3e2c1-1372-3676-8ae1-38081e1489ca | -21.91209 | -48.41605 | 2024-10-04 04:12:00 | NOAA-21 | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f62dad52-e3a5-30a8-92e6-0a9b66db4a3c | -21.90991 | -48.41733 | 2024-10-04 04:12:00 | NOAA-21 | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8eba5a9c-25b1-3dc2-a7e2-744af793e692 | -21.90933 | -48.41082 | 2024-10-04 04:12:00 | NOAA-21 | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1fc40827-3966-34e4-af4d-2f01a8b0646a | -21.90854 | -48.41524 | 2024-10-04 04:12:00 | NOAA-21 | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 548c4a8e-5a2b-3de2-afa6-59c731dd9fda | -21.89985 | -48.47488 | 2024-10-04 04:12:00 | NOAA-21 | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| eb60c0d0-73a3-3e5c-ba09-0c1e9e8e56ac | -21.89969 | -48.43346 | 2024-10-04 04:12:00 | NOAA-21 | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6ab83721-307d-358a-92b7-ab95ecb700bc | -21.89819 | -48.47263 | 2024-10-04 04:12:00 | NOAA-21 | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0ddf1583-bf33-39d9-818c-0784c980981f | -21.89738 | -48.47711 | 2024-10-04 04:12:00 | NOAA-21 | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ba08944a-0004-3084-b7cd-3ae10c4022d3 | -21.89629 | -48.47401 | 2024-10-04 04:12:00 | NOAA-21 | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ac6c7cb5-1bcc-3d74-8b1a-9247e4cc5ca7 | -21.89613 | -48.43267 | 2024-10-04 04:12:00 | NOAA-21 | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 46b6fe6c-dfaf-317d-b023-cc856f11514e | -21.8955 | -48.47854 | 2024-10-04 04:12:00 | NOAA-21 | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7e7d1f69-1c4f-36ef-9c87-c6f7a1bd883e | -21.88758 | -48.48139 | 2024-10-04 04:12:00 | NOAA-21 | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 96d8d364-64a4-3f16-bd1a-0860725566d0 | -21.88694 | -48.42175 | 2024-10-04 04:12:00 | NOAA-21 | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 1bc855c3-dd5c-335e-a259-80300d374e83 | -21.88336 | -48.42105 | 2024-10-04 04:12:00 | NOAA-21 | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c168bce2-5f54-3efc-bdaf-4af71f901013 | -21.87979 | -48.42033 | 2024-10-04 04:12:00 | NOAA-21 | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 10d89556-5769-3ba0-9b33-39445f8c8a1d | -21.87622 | -48.41962 | 2024-10-04 04:12:00 | NOAA-21 | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a26a04ea-c733-3813-982c-21078dd535fd | -21.87544 | -48.42402 | 2024-10-04 04:12:00 | NOAA-21 | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 86d2570b-54c6-352c-af58-81f93044bb5e | -21.86628 | -48.41306 | 2024-10-04 04:12:00 | NOAA-21 | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 04e4200b-a35f-3993-92ba-f005921cb3b9 | -21.85756 | -48.42052 | 2024-10-04 04:12:00 | NOAA-21 | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0921defc-68da-38c7-a775-0e8f98c88b06 | -21.8547 | -48.20826 | 2024-10-04 04:12:00 | NOAA-21 | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8142ba8b-029a-3203-b46b-f95635caebd4 | -21.85398 | -48.41982 | 2024-10-04 04:12:00 | NOAA-21 | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 3.7 |
| b2aeada2-2f41-3c60-b960-55a2c7e48be1 | -21.85259 | -48.36512 | 2024-10-04 04:12:00 | NOAA-21 | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 250ae107-3898-3cae-8126-0545b13807f6 | -21.8524 | -48.4287 | 2024-10-04 04:12:00 | NOAA-21 | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 23939203-7d1d-37c5-b493-e387daca1ccf | -21.85182 | -48.36948 | 2024-10-04 04:12:00 | NOAA-21 | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4500141e-af5f-3367-907d-36a89107125f | -21.85118 | -48.20747 | 2024-10-04 04:12:00 | NOAA-21 | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3fe70ab6-56ef-3867-9c84-10d38eb89985 | -21.8504 | -48.41912 | 2024-10-04 04:12:00 | NOAA-21 | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 3.7 |
| aee2dc63-5be6-3f1e-9e94-a2351bda2e72 | -21.85006 | -48.44188 | 2024-10-04 04:12:00 | NOAA-21 | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 247c0658-4dd7-315f-aff6-15dbe90ea2f9 | -21.84962 | -48.42354 | 2024-10-04 04:12:00 | NOAA-21 | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 3.9 |
| e3996aab-5941-304b-848a-906545d0514c | -21.84928 | -48.44631 | 2024-10-04 04:12:00 | NOAA-21 | GAVIÃO PEIXOTO | SÃO PAULO | Brasil | 3516853 | 35 | 33 | nan | nan | nan | Cerrado | 4.4 |
| a6f0b087-99ec-30ed-8ed5-87982f2ef498 | -21.84905 | -48.36427 | 2024-10-04 04:12:00 | NOAA-21 | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a59bc654-9d70-337f-8f15-5829e996154e | -21.84883 | -48.42797 | 2024-10-04 04:12:00 | NOAA-21 | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 3.9 |
| c3bbcd70-f398-3f6b-b915-ac365ba7ea1f | -21.84871 | -48.387 | 2024-10-04 04:12:00 | NOAA-21 | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 08578d8f-8d38-3648-931a-0d65e3f75f10 | -21.84827 | -48.36864 | 2024-10-04 04:12:00 | NOAA-21 | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | 2.6 |
| cae512b3-b4af-360b-aed4-1c40f030f6ac | -21.84805 | -48.43238 | 2024-10-04 04:12:00 | NOAA-21 | GAVIÃO PEIXOTO | SÃO PAULO | Brasil | 3516853 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fb1eaf33-3c28-3876-a741-9b2be96c92c9 | -21.84749 | -48.37303 | 2024-10-04 04:12:00 | NOAA-21 | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 1fb242e7-49c3-3d69-9aca-8a72a32f3d1c | -21.84726 | -48.43678 | 2024-10-04 04:12:00 | NOAA-21 | GAVIÃO PEIXOTO | SÃO PAULO | Brasil | 3516853 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e9b151a5-669e-38a4-9e61-f4c52736154c | -21.84604 | -48.42284 | 2024-10-04 04:12:00 | NOAA-21 | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 67b84f3f-c506-3e4a-a4fb-fbf59f943d23 | -21.8457 | -48.44559 | 2024-10-04 04:12:00 | NOAA-21 | GAVIÃO PEIXOTO | SÃO PAULO | Brasil | 3516853 | 35 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 03effd39-1259-350a-87e6-24316161ca4a | -21.84525 | -48.42725 | 2024-10-04 04:12:00 | NOAA-21 | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 4b2b4632-3bfa-3923-8bed-a7d38aafe127 | -21.84514 | -48.38625 | 2024-10-04 04:12:00 | NOAA-21 | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | 7.3 |
| a3ad057b-55cc-3fdf-ba32-b4e9e53d0cab | -21.84473 | -48.36782 | 2024-10-04 04:12:00 | NOAA-21 | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 359171dc-cc77-3954-a8b4-1942f2d06102 | -21.84437 | -48.39059 | 2024-10-04 04:12:00 | NOAA-21 | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 6e9d8b32-7f1e-35f6-b7ff-691bd2d6003e | -21.84394 | -48.37223 | 2024-10-04 04:12:00 | NOAA-21 | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 78c473d1-0924-38d5-9439-9de3d1188dca | -21.84369 | -48.43602 | 2024-10-04 04:12:00 | NOAA-21 | GAVIÃO PEIXOTO | SÃO PAULO | Brasil | 3516853 | 35 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 622a7990-b871-373e-9c6a-11d6a589ee92 | -21.84214 | -48.44477 | 2024-10-04 04:12:00 | NOAA-21 | GAVIÃO PEIXOTO | SÃO PAULO | Brasil | 3516853 | 35 | 33 | nan | nan | nan | Cerrado | 4.8 |
| e71f21e0-20c0-3737-8a9d-690ade5a1cd8 | -21.84168 | -48.42653 | 2024-10-04 04:12:00 | NOAA-21 | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 28912618-0027-3f55-a561-a3efbe5e25d1 | -21.84135 | -48.4492 | 2024-10-04 04:12:00 | NOAA-21 | GAVIÃO PEIXOTO | SÃO PAULO | Brasil | 3516853 | 35 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ac4bb789-61ad-362a-b6e6-919222fdbf8e | -21.8408 | -48.38985 | 2024-10-04 04:12:00 | NOAA-21 | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 55d76ff8-b5cc-3601-8467-b33541dfecb7 | -21.84056 | -48.45364 | 2024-10-04 04:12:00 | NOAA-21 | GAVIÃO PEIXOTO | SÃO PAULO | Brasil | 3516853 | 35 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a6139be1-fe6c-3117-b5c9-b55c2542f770 | -21.84039 | -48.37146 | 2024-10-04 04:12:00 | NOAA-21 | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 3c2ab0b9-1c27-3964-8236-f9cb1af2d2c2 | -21.84004 | -48.39416 | 2024-10-04 04:12:00 | NOAA-21 | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | 14.8 |
| c8ca328d-adbe-37c0-a85f-150c10f7ca4d | -21.8381 | -48.4258 | 2024-10-04 04:12:00 | NOAA-21 | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 466fb7c8-5ee4-3093-90b6-f397a6678a4d | -21.83724 | -48.38911 | 2024-10-04 04:12:00 | NOAA-21 | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | 5.7 |
| a75e6783-374d-384f-8945-90038d060708 | -21.83699 | -48.45286 | 2024-10-04 04:12:00 | NOAA-21 | GAVIÃO PEIXOTO | SÃO PAULO | Brasil | 3516853 | 35 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d0ddc054-1e89-315d-a670-0dce82643a5f | -21.83648 | -48.39341 | 2024-10-04 04:12:00 | NOAA-21 | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | 27.2 |
| 91344a12-b164-32f8-8b7e-72ce81f65451 | -21.8357 | -48.39775 | 2024-10-04 04:12:00 | NOAA-21 | GAVIÃO PEIXOTO | SÃO PAULO | Brasil | 3516853 | 35 | 33 | nan | nan | nan | Cerrado | 27.2 |
| f03a73c9-7f09-352f-9252-c349b7a94928 | -21.83524 | -48.37958 | 2024-10-04 04:12:00 | NOAA-21 | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | 2.3 |
| dd0559d0-7265-38e1-bf04-d3c694f099c6 | -21.83446 | -48.38397 | 2024-10-04 04:12:00 | NOAA-21 | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 05d3caa2-4bee-3aa9-bffb-488148cf7330 | -21.83368 | -48.38834 | 2024-10-04 04:12:00 | NOAA-21 | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | 5.7 |
| fae3f7a9-002c-3968-b2bd-0d7d508a547e | -21.83342 | -48.45208 | 2024-10-04 04:12:00 | NOAA-21 | GAVIÃO PEIXOTO | SÃO PAULO | Brasil | 3516853 | 35 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8fffcec3-c04c-3e4a-ad9d-cc85eb78aeb4 | -21.83291 | -48.39266 | 2024-10-04 04:12:00 | NOAA-21 | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | 27.2 |
| 26807d13-625e-3df6-8443-a4381f11b62d | -21.83263 | -48.45652 | 2024-10-04 04:12:00 | NOAA-21 | GAVIÃO PEIXOTO | SÃO PAULO | Brasil | 3516853 | 35 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 568f5739-451a-3215-a8c4-1437b17246eb | -21.83213 | -48.39702 | 2024-10-04 04:12:00 | NOAA-21 | GAVIÃO PEIXOTO | SÃO PAULO | Brasil | 3516853 | 35 | 33 | nan | nan | nan | Cerrado | 27.2 |
| 8c9fbec5-9cb3-3f2d-8462-8ab0b8a50a5c | -21.83168 | -48.37884 | 2024-10-04 04:12:00 | NOAA-21 | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 366b23ad-37ff-3bb2-9cfd-8d098f169576 | -21.82935 | -48.39191 | 2024-10-04 04:12:00 | NOAA-21 | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | 4.8 |
| f94c318c-4333-319e-9308-7472c7d5e7a8 | -21.82906 | -48.45576 | 2024-10-04 04:12:00 | NOAA-21 | GAVIÃO PEIXOTO | SÃO PAULO | Brasil | 3516853 | 35 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b9f35df6-71d4-339e-94f7-dda8467cbd0d | -21.82889 | -48.37374 | 2024-10-04 04:12:00 | NOAA-21 | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | 4.9 |
| ac16e511-ef83-3226-9e76-bc64e8f275be | -21.82857 | -48.39628 | 2024-10-04 04:12:00 | NOAA-21 | GAVIÃO PEIXOTO | SÃO PAULO | Brasil | 3516853 | 35 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 128fd186-5639-3c22-9cb4-5765eacb4e1d | -21.82827 | -48.46014 | 2024-10-04 04:12:00 | NOAA-21 | GAVIÃO PEIXOTO | SÃO PAULO | Brasil | 3516853 | 35 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 19d4016c-640d-3d38-884f-455ca685f7f1 | -21.82777 | -48.40072 | 2024-10-04 04:12:00 | NOAA-21 | GAVIÃO PEIXOTO | SÃO PAULO | Brasil | 3516853 | 35 | 33 | nan | nan | nan | Cerrado | 8.3 |
| c42060ad-3169-352f-9969-6c344246c6c9 | -21.82548 | -48.45502 | 2024-10-04 04:12:00 | NOAA-21 | GAVIÃO PEIXOTO | SÃO PAULO | Brasil | 3516853 | 35 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 0f1720e0-7359-311c-97c9-6ca535acbda0 | -21.82533 | -48.37302 | 2024-10-04 04:12:00 | NOAA-21 | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b8686d17-dc77-37c4-97c9-a1355f9df7a1 | -21.8247 | -48.45938 | 2024-10-04 04:12:00 | NOAA-21 | GAVIÃO PEIXOTO | SÃO PAULO | Brasil | 3516853 | 35 | 33 | nan | nan | nan | Cerrado | 2.6 |
| aacc8fcf-8c70-3069-9e09-5a9e846fafbe | -21.82176 | -48.37228 | 2024-10-04 04:12:00 | NOAA-21 | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2e6989d4-f979-3037-be9c-ebab9128fe4a | -21.8215 | -48.43583 | 2024-10-04 04:12:00 | NOAA-21 | GAVIÃO PEIXOTO | SÃO PAULO | Brasil | 3516853 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4c6927a5-3b25-3641-90da-87fc7f2dda7b | -21.81792 | -48.43509 | 2024-10-04 04:12:00 | NOAA-21 | GAVIÃO PEIXOTO | SÃO PAULO | Brasil | 3516853 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 24bf1be4-d9f5-3c9a-8912-5dd40a770116 | -22.22349 | -48.612 | 2024-10-04 04:12:00 | NOAA-21 | JAÚ | SÃO PAULO | Brasil | 3525300 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| fdbf5285-a5d5-33a8-aaa4-7a160712b487 | -21.81269 | -48.40229 | 2024-10-04 04:12:00 | NOAA-21 | GAVIÃO PEIXOTO | SÃO PAULO | Brasil | 3516853 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a8f75898-aff0-34e4-ab49-65c2cd148585 | -21.81185 | -48.36573 | 2024-10-04 04:12:00 | NOAA-21 | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 388cacc7-1cb2-3271-9c38-ce31cec835a0 | -21.80997 | -48.38518 | 2024-10-04 04:12:00 | NOAA-21 | GAVIÃO PEIXOTO | SÃO PAULO | Brasil | 3516853 | 35 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2b7e79b5-cb71-3943-9ecb-cc09c4cf51d6 | -21.80945 | -48.367 | 2024-10-04 04:12:00 | NOAA-21 | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | 4.2 |
| f339006a-8c15-30c6-9376-8f73211f1428 | -21.8092 | -48.38962 | 2024-10-04 04:12:00 | NOAA-21 | GAVIÃO PEIXOTO | SÃO PAULO | Brasil | 3516853 | 35 | 33 | nan | nan | nan | Cerrado | 9.3 |
| dacf42b4-23e4-3468-97e4-bc4280b7daca | -21.80912 | -48.40152 | 2024-10-04 04:12:00 | NOAA-21 | GAVIÃO PEIXOTO | SÃO PAULO | Brasil | 3516853 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8c82dd2a-cc37-34e8-b295-cda754c8a406 | -21.80829 | -48.365 | 2024-10-04 04:12:00 | NOAA-21 | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 77a53266-f067-3d83-8849-0cdf92ef0db6 | -21.80794 | -48.38752 | 2024-10-04 04:12:00 | NOAA-21 | GAVIÃO PEIXOTO | SÃO PAULO | Brasil | 3516853 | 35 | 33 | nan | nan | nan | Cerrado | 8.2 |


[Clique aqui para ver as próximas entradas](README81.md)
