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

## Dados Diários - Página 81

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2482771a-9efb-35e3-bf8d-a9727f757862 | -21.80752 | -48.3693 | 2024-10-04 04:12:00 | NOAA-21 | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | 5.3 |
| a37dbe3e-3d7c-37d2-8dcb-3e8ed955537d | -21.80714 | -48.39196 | 2024-10-04 04:12:00 | NOAA-21 | GAVIÃO PEIXOTO | SÃO PAULO | Brasil | 3516853 | 35 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 01038f78-aea8-366a-b11f-9cff8d2d7c01 | -21.8064 | -48.38445 | 2024-10-04 04:12:00 | NOAA-21 | GAVIÃO PEIXOTO | SÃO PAULO | Brasil | 3516853 | 35 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6ca422ad-55c5-3045-b96e-303ef48487c2 | -21.80588 | -48.36626 | 2024-10-04 04:12:00 | NOAA-21 | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 884cf140-9ba1-3d2c-88ee-ccae4c312a9b | -21.80563 | -48.38888 | 2024-10-04 04:12:00 | NOAA-21 | GAVIÃO PEIXOTO | SÃO PAULO | Brasil | 3516853 | 35 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 7a66dbec-d819-3157-8ff9-c4bd9dcd9dea | -21.80513 | -48.37058 | 2024-10-04 04:12:00 | NOAA-21 | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 09c60caf-253e-3852-8cfe-7d426afd0b75 | -21.80357 | -48.39124 | 2024-10-04 04:12:00 | NOAA-21 | GAVIÃO PEIXOTO | SÃO PAULO | Brasil | 3516853 | 35 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 89979ce8-5e1a-3ddc-9f89-5538a36693ce | -21.80206 | -48.38817 | 2024-10-04 04:12:00 | NOAA-21 | GAVIÃO PEIXOTO | SÃO PAULO | Brasil | 3516853 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c57626e8-af59-3694-bc74-1e63127f5f51 | -21.80157 | -48.36985 | 2024-10-04 04:12:00 | NOAA-21 | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 250969b6-db3f-3cf4-b695-25a616721410 | -21.80128 | -48.3926 | 2024-10-04 04:12:00 | NOAA-21 | GAVIÃO PEIXOTO | SÃO PAULO | Brasil | 3516853 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a35ff30a-64ac-3e4b-b0e4-897b496c223a | -21.80124 | -48.44542 | 2024-10-04 04:12:00 | NOAA-21 | GAVIÃO PEIXOTO | SÃO PAULO | Brasil | 3516853 | 35 | 33 | nan | nan | nan | Cerrado | 24.3 |
| 0b5289f6-bda6-3f0b-a193-1bc972cdeb4a | -21.79921 | -48.44685 | 2024-10-04 04:12:00 | NOAA-21 | GAVIÃO PEIXOTO | SÃO PAULO | Brasil | 3516853 | 35 | 33 | nan | nan | nan | Cerrado | 2.8 |
| ad76e40a-fcf8-39ee-8894-6c89e59f2fdb | -21.79848 | -48.38747 | 2024-10-04 04:12:00 | NOAA-21 | GAVIÃO PEIXOTO | SÃO PAULO | Brasil | 3516853 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e148c112-2143-3033-a305-9837a080849e | -21.79771 | -48.39188 | 2024-10-04 04:12:00 | NOAA-21 | GAVIÃO PEIXOTO | SÃO PAULO | Brasil | 3516853 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d16b5616-9bc9-3718-8944-07b6cfcabfba | -21.79687 | -48.44905 | 2024-10-04 04:12:00 | NOAA-21 | GAVIÃO PEIXOTO | SÃO PAULO | Brasil | 3516853 | 35 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 667fc5a3-7b7f-38ad-a8f5-57d49ab36946 | -21.79646 | -48.37791 | 2024-10-04 04:12:00 | NOAA-21 | GAVIÃO PEIXOTO | SÃO PAULO | Brasil | 3516853 | 35 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 525ca75c-bc24-32ad-b99e-9beca394ddc2 | -21.79568 | -48.38234 | 2024-10-04 04:12:00 | NOAA-21 | GAVIÃO PEIXOTO | SÃO PAULO | Brasil | 3516853 | 35 | 33 | nan | nan | nan | Cerrado | 4.3 |
| dfd89557-5651-3704-9143-e8f0aaac2f67 | -21.79563 | -48.44611 | 2024-10-04 04:12:00 | NOAA-21 | GAVIÃO PEIXOTO | SÃO PAULO | Brasil | 3516853 | 35 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d069a1bb-4554-3621-8fb6-06c8f4eef80e | -21.79491 | -48.38676 | 2024-10-04 04:12:00 | NOAA-21 | GAVIÃO PEIXOTO | SÃO PAULO | Brasil | 3516853 | 35 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 150ff44b-85ed-3341-a230-ba90faaa85d2 | -21.79487 | -48.45048 | 2024-10-04 04:12:00 | NOAA-21 | GAVIÃO PEIXOTO | SÃO PAULO | Brasil | 3516853 | 35 | 33 | nan | nan | nan | Cerrado | 6.8 |
| ae9a05cb-4431-302b-813f-4137333c01d3 | -21.79329 | -48.44832 | 2024-10-04 04:12:00 | NOAA-21 | GAVIÃO PEIXOTO | SÃO PAULO | Brasil | 3516853 | 35 | 33 | nan | nan | nan | Cerrado | 2.7 |
| fb8caf5c-149d-3d34-9e8c-7ed791d2a2b4 | -21.79289 | -48.37717 | 2024-10-04 04:12:00 | NOAA-21 | GAVIÃO PEIXOTO | SÃO PAULO | Brasil | 3516853 | 35 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 6ccff01d-9741-328c-aed4-de2680ecea4a | -21.79251 | -48.45269 | 2024-10-04 04:12:00 | NOAA-21 | GAVIÃO PEIXOTO | SÃO PAULO | Brasil | 3516853 | 35 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 31cc83e7-de85-395f-8462-c9a0fb72745b | -21.79212 | -48.3816 | 2024-10-04 04:12:00 | NOAA-21 | GAVIÃO PEIXOTO | SÃO PAULO | Brasil | 3516853 | 35 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 02bef280-79f1-39c1-b159-81cbaa184856 | -21.79134 | -48.38603 | 2024-10-04 04:12:00 | NOAA-21 | GAVIÃO PEIXOTO | SÃO PAULO | Brasil | 3516853 | 35 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a02e18a2-cdb4-33ac-9686-5a41bcd90546 | -21.78855 | -48.38085 | 2024-10-04 04:12:00 | NOAA-21 | GAVIÃO PEIXOTO | SÃO PAULO | Brasil | 3516853 | 35 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 1a40b662-2b14-3f2a-bf4e-5c3908ae4037 | -21.78778 | -48.38529 | 2024-10-04 04:12:00 | NOAA-21 | GAVIÃO PEIXOTO | SÃO PAULO | Brasil | 3516853 | 35 | 33 | nan | nan | nan | Cerrado | 23.9 |
| 03d4af4b-1d9b-344e-952c-95c60b3e0b2d | -21.787 | -48.3897 | 2024-10-04 04:12:00 | NOAA-21 | GAVIÃO PEIXOTO | SÃO PAULO | Brasil | 3516853 | 35 | 33 | nan | nan | nan | Cerrado | 23.9 |
| 181ed697-c79c-38e7-bb2c-519156baef74 | -21.78421 | -48.38453 | 2024-10-04 04:12:00 | NOAA-21 | GAVIÃO PEIXOTO | SÃO PAULO | Brasil | 3516853 | 35 | 33 | nan | nan | nan | Cerrado | 23.9 |
| 71237b53-7290-37a4-a69d-c41b9aa9c4dc | -21.78343 | -48.38895 | 2024-10-04 04:12:00 | NOAA-21 | GAVIÃO PEIXOTO | SÃO PAULO | Brasil | 3516853 | 35 | 33 | nan | nan | nan | Cerrado | 23.9 |
| 326b0beb-f428-3f8b-98c0-1cbfc328cbc0 | -21.78266 | -48.39335 | 2024-10-04 04:12:00 | NOAA-21 | GAVIÃO PEIXOTO | SÃO PAULO | Brasil | 3516853 | 35 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 4a44dbc1-8758-3cf6-86f2-42f60b641419 | -21.77987 | -48.3882 | 2024-10-04 04:12:00 | NOAA-21 | GAVIÃO PEIXOTO | SÃO PAULO | Brasil | 3516853 | 35 | 33 | nan | nan | nan | Cerrado | 15.0 |
| de28949c-7930-3cd7-ad93-6d8a09d81f5e | -21.77909 | -48.39262 | 2024-10-04 04:12:00 | NOAA-21 | GAVIÃO PEIXOTO | SÃO PAULO | Brasil | 3516853 | 35 | 33 | nan | nan | nan | Cerrado | 17.5 |
| 83786b71-860c-316f-8c3f-b5ee4651548f | -21.77552 | -48.39189 | 2024-10-04 04:12:00 | NOAA-21 | GAVIÃO PEIXOTO | SÃO PAULO | Brasil | 3516853 | 35 | 33 | nan | nan | nan | Cerrado | 17.5 |
| b9d36a23-aafd-390b-8962-3773206da66a | -21.77475 | -48.39628 | 2024-10-04 04:12:00 | NOAA-21 | GAVIÃO PEIXOTO | SÃO PAULO | Brasil | 3516853 | 35 | 33 | nan | nan | nan | Cerrado | 17.5 |
| c95d16a0-3b60-302b-b169-a809b25dd68e | -21.77195 | -48.39117 | 2024-10-04 04:12:00 | NOAA-21 | GAVIÃO PEIXOTO | SÃO PAULO | Brasil | 3516853 | 35 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 8fe6e56f-eeb7-38bb-b306-508f4fd68543 | -21.75886 | -48.50747 | 2024-10-04 04:12:00 | NOAA-21 | NOVA EUROPA | SÃO PAULO | Brasil | 3532900 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8fa14c7f-4bd0-30f9-aac0-f9c54a7c0b5f | -21.60208 | -47.80231 | 2024-10-04 04:12:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 04a482e2-2988-3acb-b9ae-5f9ff9233b70 | -21.38375 | -47.62941 | 2024-10-04 04:12:00 | NOAA-21 | SÃO SIMÃO | SÃO PAULO | Brasil | 3550902 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 01139d0e-a002-3024-9fc6-a088041b8d84 | -21.313 | -47.60218 | 2024-10-04 04:12:00 | NOAA-21 | SERRA AZUL | SÃO PAULO | Brasil | 3551405 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f4a418a2-39ea-3b54-9e6f-d577953ad97a | -21.31226 | -47.6064 | 2024-10-04 04:12:00 | NOAA-21 | SERRA AZUL | SÃO PAULO | Brasil | 3551405 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6e4f633d-5db7-32d9-a325-390c89a94c89 | -21.3088 | -47.60566 | 2024-10-04 04:12:00 | NOAA-21 | SERRA AZUL | SÃO PAULO | Brasil | 3551405 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| af935c52-a082-3aad-8097-b189cb61377c | -21.30239 | -47.62176 | 2024-10-04 04:12:00 | NOAA-21 | SERRA AZUL | SÃO PAULO | Brasil | 3551405 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 341518a6-0711-3adc-a0ce-de5121f8c8e1 | -21.30164 | -47.62606 | 2024-10-04 04:12:00 | NOAA-21 | SERRA AZUL | SÃO PAULO | Brasil | 3551405 | 35 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5a3fd211-b7e0-3c4f-9b76-053b7b696200 | -21.29965 | -47.61688 | 2024-10-04 04:12:00 | NOAA-21 | SERRA AZUL | SÃO PAULO | Brasil | 3551405 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| aa73e8be-8c6d-309f-8d15-b891b6aeaa68 | -21.2989 | -47.62114 | 2024-10-04 04:12:00 | NOAA-21 | SERRA AZUL | SÃO PAULO | Brasil | 3551405 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 090ae498-06bc-332e-bed0-55f4af8214f0 | -21.29815 | -47.6254 | 2024-10-04 04:12:00 | NOAA-21 | SERRA AZUL | SÃO PAULO | Brasil | 3551405 | 35 | 33 | nan | nan | nan | Cerrado | 1.6 |
| bc214c3a-5ee4-3958-b3a3-464e8f07e28c | -21.29272 | -47.61539 | 2024-10-04 04:12:00 | NOAA-21 | SERRA AZUL | SÃO PAULO | Brasil | 3551405 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 27ff87d2-2c74-3fc4-852f-fbcb45b51b77 | -21.29197 | -47.61967 | 2024-10-04 04:12:00 | NOAA-21 | SERRA AZUL | SÃO PAULO | Brasil | 3551405 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b4ae69f8-3f03-3cd0-bb25-cf906716a640 | -22.3905 | -47.89367 | 2024-10-04 04:12:00 | NOAA-21 | ITIRAPINA | SÃO PAULO | Brasil | 3523602 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c0460bb7-ee9c-3039-9791-28fc7a94354c | -22.38978 | -47.8978 | 2024-10-04 04:12:00 | NOAA-21 | ITIRAPINA | SÃO PAULO | Brasil | 3523602 | 35 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 66de3d4d-3a71-3ce7-81b5-e13acf59927d | -23.70777 | -47.48058 | 2024-10-04 04:12:00 | NOAA-21 | PIEDADE | SÃO PAULO | Brasil | 3537800 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 6ea8b9d6-ee5f-3d6c-ae1b-b327b6155b0c | -23.48931 | -47.587 | 2024-10-04 04:12:00 | NOAA-21 | ARAÇOIABA DA SERRA | SÃO PAULO | Brasil | 3502903 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| dc16f2ad-c9c7-3b35-b26f-ca0354eaf9f0 | -22.48109 | -47.46945 | 2024-10-04 04:12:00 | NOAA-21 | CORDEIRÓPOLIS | SÃO PAULO | Brasil | 3512407 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| fe69ac35-3fc0-30db-9951-edfe9c981bee | -22.47903 | -47.44001 | 2024-10-04 04:12:00 | NOAA-21 | CORDEIRÓPOLIS | SÃO PAULO | Brasil | 3512407 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 055369a0-b7c3-3b98-854a-645b98c958cf | -19.20752 | -48.38506 | 2024-10-04 04:12:00 | NOAA-21 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 46532d63-02e5-3213-bb65-d1feee3cac1c | -19.20668 | -48.3897 | 2024-10-04 04:12:00 | NOAA-21 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 18268002-9557-3c53-b57d-519d94e667e3 | -19.13407 | -48.29149 | 2024-10-04 04:12:00 | NOAA-21 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 49ce0246-23b5-304b-80fb-86eb67080248 | -20.8063 | -49.25084 | 2024-10-04 04:12:00 | NOAA-21 | GUAPIAÇU | SÃO PAULO | Brasil | 3517505 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| bfce2aaa-95ac-3ffc-9e0d-8d4f12e21003 | -20.01326 | -48.69981 | 2024-10-04 04:12:00 | NOAA-21 | PLANURA | MINAS GERAIS | Brasil | 3151602 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 9b566e2f-6140-3f7f-87b8-8e82eb19b0fc | -19.53856 | -48.64434 | 2024-10-04 04:12:00 | NOAA-21 | CAMPO FLORIDO | MINAS GERAIS | Brasil | 3111408 | 31 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 12b952d3-6a47-3bd5-99ce-f2f06b42bb96 | -19.53771 | -48.6491 | 2024-10-04 04:12:00 | NOAA-21 | CAMPO FLORIDO | MINAS GERAIS | Brasil | 3111408 | 31 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 7073bd81-765d-385b-afae-ded628efca62 | -20.63393 | -48.75521 | 2024-10-04 04:12:00 | NOAA-21 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| fcac379f-d1a9-309b-9414-1813ac20f0d8 | -20.51827 | -48.7488 | 2024-10-04 04:12:00 | NOAA-21 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 5a36cd5a-1f4f-3c45-bfcd-71c95810f31f | -20.51743 | -48.75353 | 2024-10-04 04:12:00 | NOAA-21 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| f5730842-964f-3329-a9c8-03f2caa38b5c | -20.51457 | -48.74807 | 2024-10-04 04:12:00 | NOAA-21 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 0b21be6f-7247-3a87-bed4-ecdd42603173 | -22.34851 | -49.23247 | 2024-10-04 04:12:00 | NOAA-21 | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a55a3cd1-56cf-325c-bcea-517f97c313f3 | -22.3745 | -49.04832 | 2024-10-04 04:12:00 | NOAA-21 | BAURU | SÃO PAULO | Brasil | 3506003 | 35 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 6282d598-8d0a-3f42-a0c8-afbbc4a607e8 | -22.23698 | -49.70882 | 2024-10-04 04:12:00 | NOAA-21 | GARÇA | SÃO PAULO | Brasil | 3516705 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| dc5fa187-682d-3e45-9af5-1fb359e81521 | -22.23416 | -49.70286 | 2024-10-04 04:12:00 | NOAA-21 | GARÇA | SÃO PAULO | Brasil | 3516705 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| de7106ee-ae23-3c21-b912-61ba6bc510da | -22.23322 | -49.70785 | 2024-10-04 04:12:00 | NOAA-21 | GARÇA | SÃO PAULO | Brasil | 3516705 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 0db3e69f-4218-3cda-a36d-5b50b27c5b0f | -21.80903 | -48.77723 | 2024-10-04 04:12:00 | NOAA-21 | IBITINGA | SÃO PAULO | Brasil | 3519600 | 35 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0686aa70-5dbf-3ab1-a55e-7de3d975181a | -21.80864 | -48.75836 | 2024-10-04 04:12:00 | NOAA-21 | IBITINGA | SÃO PAULO | Brasil | 3519600 | 35 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 526e49a9-27c3-3b3c-a383-3fcc7cdccbdd | -21.80501 | -48.75758 | 2024-10-04 04:12:00 | NOAA-21 | IBITINGA | SÃO PAULO | Brasil | 3519600 | 35 | 33 | nan | nan | nan | Cerrado | 4.6 |
| a984841b-10d1-302b-bad3-72022f61f32b | -21.8042 | -48.76209 | 2024-10-04 04:12:00 | NOAA-21 | IBITINGA | SÃO PAULO | Brasil | 3519600 | 35 | 33 | nan | nan | nan | Cerrado | 4.6 |
| c9d55191-1901-301c-b727-40bf033cd6a4 | -21.79978 | -48.76575 | 2024-10-04 04:12:00 | NOAA-21 | IBITINGA | SÃO PAULO | Brasil | 3519600 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| baee8b0f-a554-339a-a080-0b2a29c6dfc4 | -21.5594 | -48.67756 | 2024-10-04 04:12:00 | NOAA-21 | ITÁPOLIS | SÃO PAULO | Brasil | 3522703 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e1cd78e8-f06c-3fe3-8668-dedc93f31ed3 | -21.3971 | -48.88493 | 2024-10-04 04:12:00 | NOAA-21 | ITÁPOLIS | SÃO PAULO | Brasil | 3522703 | 35 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 71831c2f-9f30-3944-9bc5-7be612075e3d | -21.3497 | -48.90149 | 2024-10-04 04:12:00 | NOAA-21 | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 1c1f08f0-a842-30c1-98ec-48feab3bdae7 | -21.34686 | -48.89603 | 2024-10-04 04:12:00 | NOAA-21 | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Cerrado | 15.7 |
| 53db2519-5931-37c5-98d1-2f0149d7e5ba | -21.34319 | -48.89524 | 2024-10-04 04:12:00 | NOAA-21 | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Cerrado | 15.7 |
| 4159e987-d426-36da-a7c6-b18b41536103 | -21.3327 | -48.86885 | 2024-10-04 04:12:00 | NOAA-21 | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 57fa89c7-c70b-372c-aef7-147de1be6316 | -21.32819 | -48.87271 | 2024-10-04 04:12:00 | NOAA-21 | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Cerrado | 4.1 |
| da17f11c-5933-3d8c-9425-1ad4ac4eedac | -21.32198 | -48.88593 | 2024-10-04 04:12:00 | NOAA-21 | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 11eba660-8953-3aca-9b46-398d1236b28c | -21.31461 | -48.88446 | 2024-10-04 04:12:00 | NOAA-21 | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Cerrado | 12.8 |
| 6a789b72-a08d-3f7a-a4e5-e6a3f58c7fc9 | -21.31403 | -48.90872 | 2024-10-04 04:12:00 | NOAA-21 | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Cerrado | 8.6 |
| c868c4b3-162d-3cc6-896a-9fceef3e5e56 | -21.31346 | -48.86981 | 2024-10-04 04:12:00 | NOAA-21 | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 6400fd35-d009-35a2-b792-5644fc8fed18 | -21.31093 | -48.88372 | 2024-10-04 04:12:00 | NOAA-21 | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Cerrado | 23.8 |
| cbee770d-6ad8-3ebd-9c10-6b998db4b251 | -21.30752 | -48.90247 | 2024-10-04 04:12:00 | NOAA-21 | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Cerrado | 19.4 |
| b39494eb-3a98-3533-8a46-6ec656791d36 | -21.30127 | -48.9158 | 2024-10-04 04:12:00 | NOAA-21 | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Cerrado | 22.0 |
| 251d4fec-ac66-3472-9069-ef0cfd482336 | -21.29819 | -48.89082 | 2024-10-04 04:12:00 | NOAA-21 | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 9fdfc684-c6c2-3ddd-85fe-8a4c6b796367 | -21.29758 | -48.91505 | 2024-10-04 04:12:00 | NOAA-21 | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Cerrado | 117.1 |
| 6e804795-631b-3daf-b1bf-45ee573974b0 | -21.29649 | -48.90012 | 2024-10-04 04:12:00 | NOAA-21 | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 0e72a0a5-b0f9-36ec-8237-5d7e472cfe61 | -21.29536 | -48.88538 | 2024-10-04 04:12:00 | NOAA-21 | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 898861a1-d4fc-3c47-9af9-aeaaee59b313 | -21.29107 | -48.90883 | 2024-10-04 04:12:00 | NOAA-21 | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Cerrado | 16.1 |
| 472ddc11-a72e-39ba-a706-e36e113fd93e | -21.28001 | -48.90662 | 2024-10-04 04:12:00 | NOAA-21 | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Cerrado | 7.6 |
| a7691964-3eea-3d2d-a5ee-12bd9a79826b | -21.82155 | -48.77039 | 2024-10-04 04:12:00 | NOAA-21 | IBITINGA | SÃO PAULO | Brasil | 3519600 | 35 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7d23684c-9db1-3593-9c5a-23b5bae68ed8 | -21.80783 | -48.76287 | 2024-10-04 04:12:00 | NOAA-21 | IBITINGA | SÃO PAULO | Brasil | 3519600 | 35 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 17cada76-5a46-36cf-b930-d6530eaf7305 | -21.8046 | -48.78095 | 2024-10-04 04:12:00 | NOAA-21 | IBITINGA | SÃO PAULO | Brasil | 3519600 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2ee74434-f8d0-3b56-a896-55b5c750c242 | -21.80014 | -48.78477 | 2024-10-04 04:12:00 | NOAA-21 | IBITINGA | SÃO PAULO | Brasil | 3519600 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |


[Clique aqui para ver as próximas entradas](README82.md)
