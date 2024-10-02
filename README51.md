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

## Dados Diários - Página 51

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d41913d2-90fe-3609-bd31-b960facb7c35 | -5.20612 | -37.62321 | 2024-10-02 03:28:00 | NPP-375D | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 7f90b40c-2e8b-3aca-82e9-a936a68eb1cf | -5.20544 | -37.62726 | 2024-10-02 03:28:00 | NPP-375D | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 1.9 |
| e4873926-1969-397c-b049-057344924e96 | -5.16892 | -38.14341 | 2024-10-02 03:28:00 | NPP-375D | LIMOEIRO DO NORTE | CEARÁ | Brasil | 2307601 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| bcb5ae2a-ab9d-33b2-98e0-a05021f1cd59 | -5.16445 | -38.1427 | 2024-10-02 03:28:00 | NPP-375D | LIMOEIRO DO NORTE | CEARÁ | Brasil | 2307601 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 37372312-f879-32cb-b0ec-d65e9840092f | -4.66543 | -43.7603 | 2024-10-02 03:28:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f2e03546-8439-311f-82a1-f051b2a50af9 | -4.66461 | -43.7614 | 2024-10-02 03:28:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 63d7c94f-3e59-3867-984e-532a486d26d8 | -4.65891 | -43.75922 | 2024-10-02 03:28:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ad86f44a-5435-3410-8f5a-90bd53001717 | -4.46367 | -42.89153 | 2024-10-02 03:28:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 9f158ff6-022e-3b62-ab3e-c30d7b1b284b | -4.45747 | -42.89051 | 2024-10-02 03:28:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 38224305-6da4-3df0-bdc2-1e63982abfc9 | -4.02051 | -38.31772 | 2024-10-02 03:28:00 | NPP-375D | PINDORETAMA | CEARÁ | Brasil | 2310852 | 23 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 1563835a-963c-34cf-a0b6-ede7eb326362 | -3.86538 | -40.78274 | 2024-10-02 03:28:00 | NPP-375D | MUCAMBO | CEARÁ | Brasil | 2309003 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| a2349174-fc77-3482-92dc-7dc10379f755 | -3.85992 | -40.78183 | 2024-10-02 03:28:00 | NPP-375D | MUCAMBO | CEARÁ | Brasil | 2309003 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| f1c07ab4-745d-343a-9684-535ba52d2bdb | -3.47258 | -43.35661 | 2024-10-02 03:28:00 | NPP-375D | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 47c3521a-cbfd-3e76-b873-a31a4526f50e | -3.47183 | -43.36041 | 2024-10-02 03:28:00 | NPP-375D | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 796bae0b-87fa-3ab3-96e5-062fd0db010c | -3.47165 | -43.36194 | 2024-10-02 03:28:00 | NPP-375D | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3faa7a59-a52a-37e2-b2b2-c2ceaf89c7dd | -3.46537 | -43.35922 | 2024-10-02 03:28:00 | NPP-375D | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| cbc4ac80-af5f-3031-9ced-c54d86f790d7 | -10.6762 | -46.14276 | 2024-10-02 03:30:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| eda75dc0-0488-3156-9af1-5a18681daa05 | -10.66661 | -44.505 | 2024-10-02 03:30:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 7b5e6941-907c-301a-bb28-1bd74037b4f6 | -10.66141 | -44.49888 | 2024-10-02 03:30:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 9bec2824-40fe-33da-bf04-9d8ca6e50a7a | -10.66046 | -44.50369 | 2024-10-02 03:30:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| dce3cafd-829a-3000-bd99-56be3370f802 | -10.6543 | -44.50241 | 2024-10-02 03:30:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f354363a-2477-3554-90f3-075fcae492db | -10.47313 | -37.87604 | 2024-10-02 03:30:00 | NPP-375D | PARIPIRANGA | BAHIA | Brasil | 2923803 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| be052980-c2b3-35a2-a3f9-10740ebe0637 | -7.09261 | -45.67049 | 2024-10-02 03:30:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| b2088995-eb06-312d-9e25-fd582bf78d34 | -8.15326 | -42.90862 | 2024-10-02 03:30:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 2a6a71da-30f9-335c-a1a9-a4c1fbc1a048 | -12.4811 | -47.50267 | 2024-10-02 03:30:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 5f4977b9-eaad-36ee-a13c-fa061e16a6f9 | -12.47696 | -47.50139 | 2024-10-02 03:30:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 7.2 |
| f58e8982-6f04-3f6d-ae7b-484da1048ef8 | -12.47402 | -47.50106 | 2024-10-02 03:30:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| fac03ede-e54e-3e93-936b-0c3c7bab4881 | -12.2933 | -47.64725 | 2024-10-02 03:30:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8aee91a5-7eb0-3921-b5ec-01ff7c2ffd13 | -12.29235 | -47.64538 | 2024-10-02 03:30:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 4b82f095-086a-3f55-b851-d61d5b32a690 | -12.29078 | -47.65274 | 2024-10-02 03:30:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 64634541-c088-3fd1-aadf-34e728219ed0 | -12.28924 | -47.65997 | 2024-10-02 03:30:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 995bb5b5-eb1d-3819-8a14-c6aed5a4c794 | -12.28614 | -47.6456 | 2024-10-02 03:30:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| b8b1d515-feb5-3d25-b843-a4e9bcc32c34 | -12.2852 | -47.6437 | 2024-10-02 03:30:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| ae6e64fa-77a2-341d-9e21-85c19ae4f8ba | -12.28458 | -47.65274 | 2024-10-02 03:30:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 0cd0b04a-8287-3f8c-99af-1cb3a6c993e7 | -12.28366 | -47.6509 | 2024-10-02 03:30:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 85ad0063-7066-3527-8a21-98de4eb7c435 | -12.28295 | -47.66016 | 2024-10-02 03:30:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 7.9 |
| de842cd0-cdc1-3c59-8ab7-e7300074536b | -12.28209 | -47.65827 | 2024-10-02 03:30:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 4615fb34-99e1-3278-a566-0e2f167fd7ff | -12.27746 | -47.65094 | 2024-10-02 03:30:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 66d8985d-eddf-314c-a578-9b1cb0be7abc | -10.989 | -46.56067 | 2024-10-02 03:30:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| cc5ca2f0-a724-3dec-872f-33850d049bd2 | -10.98213 | -46.55904 | 2024-10-02 03:30:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ceb2fd45-5484-34da-9a0f-9292bebb98f6 | -10.91902 | -46.3454 | 2024-10-02 03:30:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 881d4876-97a2-3715-bd5c-67fb8bede220 | -10.91304 | -46.33981 | 2024-10-02 03:30:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 6dce8ac6-c902-365d-8028-1a3db073c272 | -10.21746 | -46.82485 | 2024-10-02 03:30:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| c09c2678-63fc-372e-8e76-8083b82f9705 | -10.216 | -46.83205 | 2024-10-02 03:30:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 1cdc592d-5e8c-3bcf-9a54-675743f15342 | -10.21365 | -46.82351 | 2024-10-02 03:30:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| bbd184db-ec03-37db-9539-4dd611668db1 | -10.21216 | -46.83063 | 2024-10-02 03:30:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 89882abb-0b1b-3243-a17c-3c48abc2e475 | -9.5736 | -40.3447 | 2024-10-02 03:30:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 03bd9336-8275-349b-8e35-addbc02a85d3 | -9.46155 | -40.36612 | 2024-10-02 03:30:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 6b579756-272c-37a6-9f12-6e0280dce08f | -9.46058 | -40.37144 | 2024-10-02 03:30:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 2.1 |
| fff61f92-88c4-3fc5-bba0-638a87cafa50 | -9.4582 | -40.36858 | 2024-10-02 03:30:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 2.8 |
| ab974910-047d-3623-a832-49315eeebd99 | -9.45673 | -40.36524 | 2024-10-02 03:30:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 711b095d-1fca-3bcd-b514-010755c85128 | -9.43193 | -40.31993 | 2024-10-02 03:30:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 3.2 |
| e6d4bf19-dba3-3a5f-a954-d9d54f6eb365 | -9.01331 | -45.23263 | 2024-10-02 03:30:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| ecccb06d-a7df-3936-b736-8e33a1f4dd2c | -8.95595 | -35.54816 | 2024-10-02 03:30:00 | NPP-375D | JUNDIÁ | ALAGOAS | Brasil | 2703908 | 27 | 33 | nan | nan | nan | Mata Atlântica | 6.8 |
| f963718d-6caf-3bc4-b029-cebaef6ad205 | -8.95235 | -35.54759 | 2024-10-02 03:30:00 | NPP-375D | JUNDIÁ | ALAGOAS | Brasil | 2703908 | 27 | 33 | nan | nan | nan | Mata Atlântica | 10.6 |
| cf0ad691-f082-35de-b933-8d71ef1a2f08 | -8.69993 | -45.23441 | 2024-10-02 03:30:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 5dbebee2-31fd-364a-af48-989c72699acd | -8.69876 | -45.24046 | 2024-10-02 03:30:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8717307d-561f-3843-b590-dffb6af7bfbc | -8.69222 | -45.23854 | 2024-10-02 03:30:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 817c9aed-5ec6-32e8-97c4-4136ef2b1b92 | -8.64353 | -40.28436 | 2024-10-02 03:30:00 | NPP-375D | LAGOA GRANDE | PERNAMBUCO | Brasil | 2608750 | 26 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 2acbf045-f6b1-35b7-b1e5-307dc2e6350e | -8.63866 | -40.2835 | 2024-10-02 03:30:00 | NPP-375D | LAGOA GRANDE | PERNAMBUCO | Brasil | 2608750 | 26 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 3ab1763b-54b1-33a4-a72d-0ec19fe618bf | -8.63768 | -40.28895 | 2024-10-02 03:30:00 | NPP-375D | LAGOA GRANDE | PERNAMBUCO | Brasil | 2608750 | 26 | 33 | nan | nan | nan | Caatinga | 5.4 |
| b079e256-8fe0-3937-ba1c-6a8195f913c2 | -8.6334 | -44.06421 | 2024-10-02 03:30:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9549dd97-2443-3955-9b89-ca3179e29019 | -8.63249 | -44.06892 | 2024-10-02 03:30:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3511f97d-a024-3f70-b796-ee562a865619 | -8.50542 | -43.91682 | 2024-10-02 03:30:00 | NPP-375D | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| b93b5fea-1430-3eee-91dd-8186f2f4b112 | -8.50447 | -43.92182 | 2024-10-02 03:30:00 | NPP-375D | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 146dee63-9526-3f1c-a413-f3f4c78e4cca | -8.43556 | -41.93513 | 2024-10-02 03:30:00 | NPP-375D | CAPITÃO GERVÁSIO OLIVEIRA | PIAUÍ | Brasil | 2202455 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| c30c2d37-cede-3f79-ae50-620cdf317ad0 | -8.42959 | -41.93687 | 2024-10-02 03:30:00 | NPP-375D | CAPITÃO GERVÁSIO OLIVEIRA | PIAUÍ | Brasil | 2202455 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 9ba9c030-8bef-3ca5-afda-42d432fad123 | -8.21419 | -44.35822 | 2024-10-02 03:30:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 362d96e8-bc6e-3112-a349-06e23b5d78d4 | -8.20791 | -44.35651 | 2024-10-02 03:30:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 47e3e416-d155-3274-a69f-161553bd6a19 | -8.20689 | -44.36185 | 2024-10-02 03:30:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 7b57e8e9-039b-3fa3-9f01-7954c556fe37 | -8.20587 | -44.36718 | 2024-10-02 03:30:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| f0f83414-6b9c-3e6e-84ff-9e7b2939016c | -8.20061 | -44.36017 | 2024-10-02 03:30:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 3605a329-26f9-3b7a-b9f5-a8aabda20b64 | -8.19959 | -44.36548 | 2024-10-02 03:30:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 15d840d8-888e-3d1b-8b47-507b5b9b9016 | -8.17943 | -43.67938 | 2024-10-02 03:30:00 | NPP-375D | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 691fe694-7dd1-3d91-837d-01ee8152cfae | -8.17912 | -43.67582 | 2024-10-02 03:30:00 | NPP-375D | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9a66326d-7834-3056-94c0-99a0ec058f13 | -8.17826 | -43.68031 | 2024-10-02 03:30:00 | NPP-375D | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c925664c-f5ab-362f-b925-3a04cec9bbe3 | -8.1733 | -43.67827 | 2024-10-02 03:30:00 | NPP-375D | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 329d148a-e545-354f-a05e-63ba9012f3b7 | -8.17243 | -43.68298 | 2024-10-02 03:30:00 | NPP-375D | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 76776d61-b6e3-368a-949e-5e18bcd51c07 | -8.17155 | -43.6877 | 2024-10-02 03:30:00 | NPP-375D | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 45eca46b-43af-3e9b-910a-8706a812be5d | -8.17122 | -43.68396 | 2024-10-02 03:30:00 | NPP-375D | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| dd59631a-ca3d-35c0-b7b6-fb7cdf54c617 | -8.17031 | -43.68867 | 2024-10-02 03:30:00 | NPP-375D | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8189df05-3fb2-3be3-98a2-8dd352c6fe78 | -8.16543 | -43.68653 | 2024-10-02 03:30:00 | NPP-375D | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 513f7d83-680e-3fb0-a1a2-3cc465153e98 | -8.15932 | -43.68532 | 2024-10-02 03:30:00 | NPP-375D | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1a0fbbe8-9e27-3b10-b57a-394667599eea | -8.15841 | -43.69026 | 2024-10-02 03:30:00 | NPP-375D | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 08a43c74-b999-379b-ac30-7e4461ac7349 | -8.14748 | -42.90724 | 2024-10-02 03:30:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 4d25bf89-9f38-33e6-a5e6-6576647ad7a4 | -7.90831 | -43.17176 | 2024-10-02 03:30:00 | NPP-375D | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 006dbdd2-87c6-3c4c-9613-4c0ec744039f | -7.90233 | -43.17078 | 2024-10-02 03:30:00 | NPP-375D | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| e1c82c96-8f1b-3f32-b0e7-f45e394636f8 | -7.87556 | -42.67292 | 2024-10-02 03:30:00 | NPP-375D | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| ef252725-ec3d-34ce-a7f7-0a47cfc54afd | -7.86978 | -42.67189 | 2024-10-02 03:30:00 | NPP-375D | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| febf23ea-2acc-341c-87ca-08e0779c9239 | -7.8571 | -43.08414 | 2024-10-02 03:30:00 | NPP-375D | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| b53f9693-5174-3f09-91dc-5e858a4d7125 | -7.85626 | -43.0886 | 2024-10-02 03:30:00 | NPP-375D | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| be44efe8-1dc8-3708-9b99-5d0feaced66d | -7.8554 | -43.09314 | 2024-10-02 03:30:00 | NPP-375D | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| f741d890-e823-3209-84af-cf53dc5f3a44 | -7.85488 | -43.08192 | 2024-10-02 03:30:00 | NPP-375D | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 7fc0b3aa-2e88-36e1-a07f-e8cbd9d6f6da | -7.84898 | -43.08066 | 2024-10-02 03:30:00 | NPP-375D | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| b9d18363-7ff7-3d10-ab4f-d3a69b832781 | -7.83039 | -43.08175 | 2024-10-02 03:30:00 | NPP-375D | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| b46bb4b3-fe6d-3fe2-a26a-8b742cf93651 | -7.82955 | -43.08633 | 2024-10-02 03:30:00 | NPP-375D | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 8d5c7932-132f-323f-9d40-ab6cf4b5a01b | -7.82869 | -43.091 | 2024-10-02 03:30:00 | NPP-375D | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 5b39f06e-8fca-3e47-bf7a-a65db05689c9 | -7.82783 | -43.09568 | 2024-10-02 03:30:00 | NPP-375D | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| a1b89c70-1f6e-370c-840f-01bd656e3ae1 | -7.82361 | -43.08529 | 2024-10-02 03:30:00 | NPP-375D | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| d645a1a5-1d67-397d-b90a-966880d9fb04 | -7.76504 | -43.05311 | 2024-10-02 03:30:00 | NPP-375D | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |


[Clique aqui para ver as próximas entradas](README52.md)
