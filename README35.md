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

## Dados Diários - Página 35

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c37f905e-9ebf-3e13-a30f-83bf2df0b102 | -13.42986 | -47.36416 | 2025-10-30 04:06:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 852e2c2e-305b-39e7-9ee6-f524e5c6ad4d | -13.98872 | -40.44276 | 2025-10-30 04:06:00 | NPP-375D | MANOEL VITORINO | BAHIA | Brasil | 2920403 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| dc643314-a604-3d09-9c54-3f0af8e7a442 | -13.0738 | -48.20936 | 2025-10-30 04:06:00 | NPP-375D | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 4ba71e9f-2d55-3469-beb2-b0d6a580a667 | -14.16125 | -43.40189 | 2025-10-30 04:06:00 | NPP-375D | PALMAS DE MONTE ALTO | BAHIA | Brasil | 2923407 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d1cb3b16-f993-33a7-ac31-dc265c7605b1 | -13.56705 | -47.1536 | 2025-10-30 04:06:00 | NPP-375D | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| fd24ff0e-91ef-3f2c-a0c4-5054368d875d | -12.81291 | -43.4553 | 2025-10-30 04:06:00 | NPP-375D | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d73d2906-1ef5-3000-b47c-dc3e3d4ceabc | -9.86131 | -47.69117 | 2025-10-30 04:06:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3793fedc-391a-3dcd-a8ba-ddd370f62be6 | -12.31354 | -48.06235 | 2025-10-30 04:06:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 79582672-680c-37a4-aca5-c8a9ef0cc4dd | -12.36696 | -50.15418 | 2025-10-30 04:06:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 48b11eb7-77ad-3a62-b7d7-14bd37ab15fb | -13.71695 | -48.76864 | 2025-10-30 04:08:00 | NPP-375D | CAMPINORTE | GOIÁS | Brasil | 5204706 | 52 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 84c80233-65e0-3c83-aa50-ff55f2f8a03f | -17.78452 | -42.93761 | 2025-10-30 04:08:00 | NPP-375D | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 0.3 |
| d23e6154-e596-3557-b1ef-06361aee7c22 | -15.24335 | -43.12897 | 2025-10-30 04:08:00 | NPP-375D | MONTE AZUL | MINAS GERAIS | Brasil | 3142908 | 31 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 0dd4ecd2-0592-34ce-8300-1d24a8793b09 | -13.92982 | -48.48924 | 2025-10-30 04:08:00 | NPP-375D | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 220b029c-0e97-31bb-bbb0-1ad4a4ea2724 | -15.2512 | -43.11107 | 2025-10-30 04:08:00 | NPP-375D | MONTE AZUL | MINAS GERAIS | Brasil | 3142908 | 31 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 89ae058c-0100-36a1-9759-972d539c8640 | -20.78541 | -47.20967 | 2025-10-30 04:08:00 | NPP-375D | SÃO TOMÁS DE AQUINO | MINAS GERAIS | Brasil | 3165107 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6b4e0df3-86d3-3032-9df9-b6fc68095ef8 | -16.05277 | -41.47307 | 2025-10-30 04:08:00 | NPP-375D | CACHOEIRA DE PAJEÚ | MINAS GERAIS | Brasil | 3102704 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| 12af4da1-15f3-3c1b-8cf6-f77d24ad00ec | -18.776 | -42.42278 | 2025-10-30 04:08:00 | NPP-375D | SARDOÁ | MINAS GERAIS | Brasil | 3165503 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 91037c88-530b-3c4d-af31-2b2a226246d1 | -16.8113 | -41.22766 | 2025-10-30 04:08:00 | NPP-375D | MONTE FORMOSO | MINAS GERAIS | Brasil | 3143153 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| aa3214e5-e348-3c35-b26b-75d71e0d9502 | -15.24485 | -43.12878 | 2025-10-30 04:08:00 | NPP-375D | MONTE AZUL | MINAS GERAIS | Brasil | 3142908 | 31 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 73ba901f-e658-34e5-beec-a073426e7dfb | -19.3313 | -43.0647 | 2025-10-30 04:08:00 | NPP-375D | SANTA MARIA DE ITABIRA | MINAS GERAIS | Brasil | 3158003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 4ef69550-8239-3025-939c-565b79f5df37 | -15.02757 | -46.30961 | 2025-10-30 04:08:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c7e5f102-6706-394d-bb9d-95fce95014f1 | -14.77419 | -44.97856 | 2025-10-30 04:08:00 | NPP-375D | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5f2b48f5-0c0c-3ed6-8e39-059ab116a718 | -13.94019 | -48.45838 | 2025-10-30 04:08:00 | NPP-375D | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e7a5a088-9242-347b-aa46-db414ef04069 | -19.46948 | -41.5592 | 2025-10-30 04:08:00 | NPP-375D | POCRANE | MINAS GERAIS | Brasil | 3151909 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 04c9d2eb-477a-39bf-906b-8cab7af2afc7 | -15.9012 | -48.59533 | 2025-10-30 04:08:00 | NPP-375D | CORUMBÁ DE GOIÁS | GOIÁS | Brasil | 5205802 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a7e4fda9-09d5-3ecd-89ae-fbaefbbf5e0a | -13.93066 | -48.48473 | 2025-10-30 04:08:00 | NPP-375D | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f3c48be5-8fea-3287-86b0-804e18d955f2 | -19.33968 | -43.0549 | 2025-10-30 04:08:00 | NPP-375D | SANTA MARIA DE ITABIRA | MINAS GERAIS | Brasil | 3158003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 5117fd01-520d-3e1c-91d3-cc9f12d4951f | -20.88103 | -43.68317 | 2025-10-30 04:08:00 | NPP-375D | CARANAÍBA | MINAS GERAIS | Brasil | 3113107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| d50d1d12-9039-3553-bf08-cf4129e28a70 | -14.90252 | -43.10091 | 2025-10-30 04:08:00 | NPP-375D | GAMELEIRAS | MINAS GERAIS | Brasil | 3127339 | 31 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 37a78031-58ba-3c19-bc89-3df6e52fd51f | -13.94459 | -48.45963 | 2025-10-30 04:08:00 | NPP-375D | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 2381453f-cf2d-38ca-a873-9b6fe5eb269a | -14.48289 | -51.51987 | 2025-10-30 04:08:00 | NPP-375D | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b0a81b7b-6073-3159-ad00-64110dc554bc | -14.68098 | -46.84064 | 2025-10-30 04:08:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ee7ba1ff-4765-3ba4-b767-59fdfaf8fa81 | -18.32552 | -42.14044 | 2025-10-30 04:08:00 | NPP-375D | SÃO JOSÉ DA SAFIRA | MINAS GERAIS | Brasil | 3163003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| c8904f8a-83f0-3ec7-b3e7-2d976d478fca | -15.21074 | -43.13839 | 2025-10-30 04:08:00 | NPP-375D | MONTE AZUL | MINAS GERAIS | Brasil | 3142908 | 31 | 33 | nan | nan | nan | Caatinga | 0.8 |
| c069e359-4b2f-3bb0-9467-7faed0f75ef4 | -18.2295 | -42.3723 | 2025-10-30 04:08:00 | NPP-375D | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| a3064513-54e0-3653-a558-db1b88edb6c6 | -15.02769 | -46.31622 | 2025-10-30 04:08:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d19cb568-a17d-3f97-b55a-b0c953023903 | -16.59055 | -43.51335 | 2025-10-30 04:08:00 | NPP-375D | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 153016e4-8d1d-337b-a1bb-8831a4d0d881 | -14.71334 | -45.09457 | 2025-10-30 04:08:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0f7aa7b1-cffb-3c8c-8f9d-9acee0fe3de9 | -19.3352 | -43.06163 | 2025-10-30 04:08:00 | NPP-375D | SANTA MARIA DE ITABIRA | MINAS GERAIS | Brasil | 3158003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 12ca4fd5-9cdc-34aa-a732-c77d12b667a7 | -14.4902 | -51.50742 | 2025-10-30 04:08:00 | NPP-375D | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a6dee769-baaa-31a5-8b9f-ac2901f5c57f | -19.16144 | -43.30234 | 2025-10-30 04:08:00 | NPP-375D | MORRO DO PILAR | MINAS GERAIS | Brasil | 3143708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 75393439-81ea-3a96-b31f-056a7e356849 | -14.48342 | -51.51334 | 2025-10-30 04:08:00 | NPP-375D | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f92620ae-495a-367d-a555-53fcdf14effd | -18.77658 | -42.41912 | 2025-10-30 04:08:00 | NPP-375D | SARDOÁ | MINAS GERAIS | Brasil | 3165503 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| dc78dce2-f8ce-33ed-b40d-e0ce62addc95 | -16.59296 | -42.83533 | 2025-10-30 04:08:00 | NPP-375D | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fd892bbc-7f4e-3b61-a880-b30768266d12 | -18.04299 | -43.14629 | 2025-10-30 04:08:00 | NPP-375D | SENADOR MODESTINO GONÇALVES | MINAS GERAIS | Brasil | 3165909 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| f69c7d6a-a239-3acf-9b7f-dce29aa2c988 | -19.33795 | -43.06587 | 2025-10-30 04:08:00 | NPP-375D | SANTA MARIA DE ITABIRA | MINAS GERAIS | Brasil | 3158003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 9dbe8cb8-3198-30e3-9ffb-e275f7130f98 | -19.33188 | -43.06105 | 2025-10-30 04:08:00 | NPP-375D | SANTA MARIA DE ITABIRA | MINAS GERAIS | Brasil | 3158003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 33b3f660-0b80-31ec-b74a-ea71c00205ad | -18.54713 | -41.57792 | 2025-10-30 04:08:00 | NPP-375D | NOVA MÓDICA | MINAS GERAIS | Brasil | 3144904 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 9047e6dd-640e-3819-a5d3-4844ee3d1c39 | -15.02474 | -46.31063 | 2025-10-30 04:08:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b8cf11d7-48c0-3c43-8257-90f8d714b2c8 | -17.68119 | -42.37363 | 2025-10-30 04:08:00 | NPP-375D | CAPELINHA | MINAS GERAIS | Brasil | 3112307 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 4a6a178d-758c-3b7d-8b23-b6c6e122877d | -15.29744 | -43.909 | 2025-10-30 04:08:00 | NPP-375D | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 50bf4f4b-f759-378b-a1d6-03e145a7e4fb | -14.78351 | -44.989 | 2025-10-30 04:08:00 | NPP-375D | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9c021405-67a8-390b-979b-8050cb8d36ec | -20.9004 | -42.146 | 2025-10-30 04:08:00 | NPP-375D | TOMBOS | MINAS GERAIS | Brasil | 3169208 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| cba5c97e-3d15-3ece-b60e-dd049f859767 | -17.38444 | -41.03508 | 2025-10-30 04:08:00 | NPP-375D | PAVÃO | MINAS GERAIS | Brasil | 3148509 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 0e92ace0-12f2-3a3c-8fba-bb01c45c9a1f | -14.48202 | -51.52044 | 2025-10-30 04:08:00 | NPP-375D | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3410546e-00ed-3b12-ae5a-e4cabca90909 | -15.20152 | -43.72876 | 2025-10-30 04:08:00 | NPP-375D | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 0.4 |
| f8e3ea70-1688-3224-9e18-9e01e2b36236 | -20.88436 | -43.68378 | 2025-10-30 04:08:00 | NPP-375D | CARANAÍBA | MINAS GERAIS | Brasil | 3113107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 0afdcf90-75c4-3d07-812c-18c66a3c32ee | -14.48361 | -51.51633 | 2025-10-30 04:08:00 | NPP-375D | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f8eae2df-dc7d-38c2-8e4a-9071b70b004a | -15.09144 | -41.98611 | 2025-10-30 04:08:00 | NPP-375D | CORDEIROS | BAHIA | Brasil | 2909000 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 17f5d4f6-2851-3c83-8a34-375995178db8 | -15.02211 | -46.31822 | 2025-10-30 04:08:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e871372a-7261-3090-bd7a-7906cb798e04 | -15.85922 | -44.8906 | 2025-10-30 04:08:00 | NPP-375D | SÃO FRANCISCO | MINAS GERAIS | Brasil | 3161106 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6ff0e5a7-d259-3895-9c8e-8961d667dded | -14.77061 | -44.9779 | 2025-10-30 04:08:00 | NPP-375D | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 03100ab7-8c94-3f86-a13e-cce6794d8b35 | -16.86387 | -42.36996 | 2025-10-30 04:08:00 | NPP-375D | VIRGEM DA LAPA | MINAS GERAIS | Brasil | 3171600 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bf60754f-7422-3d0f-b5f4-71d626379afa | -18.35902 | -42.56212 | 2025-10-30 04:08:00 | NPP-375D | SÃO PEDRO DO SUAÇUÍ | MINAS GERAIS | Brasil | 3164100 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 1a0ff08b-2ea3-3a9e-adf3-cb0bb5045eac | -18.04387 | -42.0864 | 2025-10-30 04:08:00 | NPP-375D | FRANCISCÓPOLIS | MINAS GERAIS | Brasil | 3126752 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 3c1ea22e-d433-307c-89bf-b9761b063fd4 | -17.96551 | -44.07881 | 2025-10-30 04:08:00 | NPP-375D | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| d399c2bf-e73f-30fd-b592-a9c66b9093cc | -20.40071 | -41.5266 | 2025-10-30 04:08:00 | NPP-375D | IÚNA | ESPÍRITO SANTO | Brasil | 3203007 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 63c1faf8-17c2-39ef-9df7-4245d04092d3 | -15.11265 | -43.26871 | 2025-10-30 04:08:00 | NPP-375D | GAMELEIRAS | MINAS GERAIS | Brasil | 3127339 | 31 | 33 | nan | nan | nan | Caatinga | 1.6 |
| b9c0bbc8-a25a-3857-9de2-5c5c1b3f2038 | -15.98704 | -45.64566 | 2025-10-30 04:08:00 | NPP-375D | URUCUIA | MINAS GERAIS | Brasil | 3170529 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d15b6ff7-df6d-34ce-9715-24ed67ba7848 | -15.21647 | -43.34321 | 2025-10-30 04:08:00 | NPP-375D | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 3c3f8a88-61cc-3caa-b4d4-287a75c68599 | -15.72531 | -43.15806 | 2025-10-30 04:08:00 | NPP-375D | PORTEIRINHA | MINAS GERAIS | Brasil | 3152204 | 31 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 8fe203a3-b822-3f0f-836e-2b20bf455cee | -16.58906 | -43.51751 | 2025-10-30 04:08:00 | NPP-375D | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bef7d4a3-d6c2-3966-a138-5e91874e0676 | -17.38104 | -41.03455 | 2025-10-30 04:08:00 | NPP-375D | PAVÃO | MINAS GERAIS | Brasil | 3148509 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| e8047fde-1ede-3985-a3cc-396ce886cf63 | -18.24449 | -42.6252 | 2025-10-30 04:08:00 | NPP-375D | SÃO JOSÉ DO JACURI | MINAS GERAIS | Brasil | 3163508 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 4ed6e557-89be-39f4-ab22-208843cc88fb | -16.58558 | -40.9256 | 2025-10-30 04:08:00 | NPP-375D | JEQUITINHONHA | MINAS GERAIS | Brasil | 3135803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| f69d9a69-2478-36c0-b204-7c1c92bf9153 | -13.93048 | -48.4608 | 2025-10-30 04:08:00 | NPP-375D | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1a419f32-8840-3111-bcd5-913d1c95f778 | -16.85244 | -42.8868 | 2025-10-30 04:08:00 | NPP-375D | BOTUMIRIM | MINAS GERAIS | Brasil | 3108503 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 7a365d1c-e613-30f9-94a5-b183210f23be | -14.76201 | -44.96333 | 2025-10-30 04:08:00 | NPP-375D | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f8dc4a6a-2afd-31ef-9370-62ce349b2bca | -15.02592 | -46.31911 | 2025-10-30 04:08:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9954e20a-ee30-345e-81c6-2afa757dd822 | -16.45729 | -43.85452 | 2025-10-30 04:08:00 | NPP-375D | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2762a2d6-4548-3310-8221-8cbcf8f25b5b | -15.02389 | -46.31534 | 2025-10-30 04:08:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2a9689f6-220d-35ea-ac41-21fe77e1eb53 | -18.56519 | -42.40961 | 2025-10-30 04:08:00 | NPP-375D | COROACI | MINAS GERAIS | Brasil | 3119203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| cc71348f-8555-3daa-9bf5-63bfd4177b46 | -14.92935 | -42.23783 | 2025-10-30 04:08:00 | NPP-375D | MORTUGABA | BAHIA | Brasil | 2921807 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 7022a1c9-7f30-32c1-9d69-411295c824cf | -14.48506 | -51.50924 | 2025-10-30 04:08:00 | NPP-375D | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 01bc7831-9b1f-3b58-a4d5-b9717ea02a8d | -15.01921 | -46.31927 | 2025-10-30 04:08:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 02c0cf31-3da4-360b-ae3a-f4ce3ee902cb | -17.96275 | -44.07445 | 2025-10-30 04:08:00 | NPP-375D | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| b75f2e84-b297-325c-806e-eb8688fbc110 | -15.41285 | -44.28214 | 2025-10-30 04:08:00 | NPP-375D | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 39902f0f-8729-31ac-af8a-aa698e5219ca | -15.26602 | -43.69662 | 2025-10-30 04:08:00 | NPP-375D | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 2563a138-d156-3ac7-8581-8f9db1d10770 | -19.45246 | -41.53362 | 2025-10-30 04:08:00 | NPP-375D | CONSELHEIRO PENA | MINAS GERAIS | Brasil | 3118403 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 41fd452a-16c6-380f-925b-73eae6d10d01 | -15.02889 | -46.32478 | 2025-10-30 04:08:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b6293562-1657-3ff2-846c-0cc97c54aa55 | -15.02557 | -46.30598 | 2025-10-30 04:08:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a324e05a-a752-3104-81d5-eacc80cf1a7d | -14.4862 | -51.49917 | 2025-10-30 04:08:00 | NPP-375D | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5c66b241-a061-3537-9d9a-fdead4fd1367 | -14.48951 | -51.51097 | 2025-10-30 04:08:00 | NPP-375D | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f80e1176-ab0c-3647-84d9-55e73cb4da60 | -15.02508 | -46.32392 | 2025-10-30 04:08:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 7.0 |
| d08b5ed8-f071-3df7-9ac2-e3e3bac44446 | -21.44566 | -43.4053 | 2025-10-30 04:08:00 | NPP-375D | SANTOS DUMONT | MINAS GERAIS | Brasil | 3160702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| dc2f5686-57ec-354c-bbd9-bca9dce02b7c | -14.48132 | -51.524 | 2025-10-30 04:08:00 | NPP-375D | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9a7cacac-6d36-31b4-86c6-985643ebd2f9 | -14.7162 | -45.09956 | 2025-10-30 04:08:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 83460120-d2f8-3c58-b749-380aefdfba74 | -18.24781 | -42.62577 | 2025-10-30 04:08:00 | NPP-375D | SÃO JOSÉ DO JACURI | MINAS GERAIS | Brasil | 3163508 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| f684c5c4-d160-38bc-bf5d-ba3f5993bf18 | -14.78263 | -44.35355 | 2025-10-30 04:08:00 | NPP-375D | MIRAVÂNIA | MINAS GERAIS | Brasil | 3142254 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e0d72f58-b49a-3651-b257-7ea1c667d870 | -14.90588 | -43.10147 | 2025-10-30 04:08:00 | NPP-375D | GAMELEIRAS | MINAS GERAIS | Brasil | 3127339 | 31 | 33 | nan | nan | nan | Caatinga | 0.6 |


[Clique aqui para ver as próximas entradas](README36.md)
