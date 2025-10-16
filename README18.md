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

## Dados Diários - Página 18

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 736b281d-0102-3c33-87c0-c84ec7138994 | -10.52201 | -43.36786 | 2025-10-16 03:28:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 32d278fe-dd4e-3626-809a-886ba68ce247 | -7.11089 | -44.72856 | 2025-10-16 03:28:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 9ed81081-039c-3c4b-a805-926efe3dfb34 | -10.82933 | -43.94727 | 2025-10-16 03:28:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2f6e5b52-b78c-3406-9159-ad36544ad624 | -10.69766 | -44.43296 | 2025-10-16 03:28:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 186f2e84-4418-38df-b9ec-125f1d338926 | -9.67983 | -44.50384 | 2025-10-16 03:28:00 | NPP-375D | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 14.8 |
| f8da8b4b-e46f-3c92-8f6e-6381849fe340 | -7.38814 | -44.75063 | 2025-10-16 03:28:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 3d6727cb-50f4-3e59-a79c-366e9e0fcfda | -13.65621 | -43.92986 | 2025-10-16 03:28:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 5.3 |
| f0da6356-62df-33ed-9962-e39294ad5b08 | -8.26606 | -43.35779 | 2025-10-16 03:28:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 9cb9d040-2af0-35f7-a976-0056a3fbe683 | -10.52739 | -43.37388 | 2025-10-16 03:28:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 23181fb4-7a5d-36fd-a064-4cd9e28e14f6 | -7.47159 | -42.76234 | 2025-10-16 03:28:00 | NPP-375D | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 5.4 |
| abd96b16-8b54-3b84-9a25-77d77fe50880 | -8.46417 | -44.18175 | 2025-10-16 03:28:00 | NPP-375D | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 18.9 |
| ca42dedf-0882-34a5-bde3-bb65061f39c1 | -9.26017 | -45.26291 | 2025-10-16 03:28:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 6ca4e508-b2e2-371c-9825-c38de535155d | -7.94663 | -44.14132 | 2025-10-16 03:28:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 92cc4651-e670-310c-b801-f8d5be4856b1 | -14.75103 | -42.37872 | 2025-10-16 03:28:00 | NPP-375D | JACARACI | BAHIA | Brasil | 2917409 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 6c0fa2a0-3e8d-3263-a777-7eea5a4b8859 | -8.29544 | -43.40875 | 2025-10-16 03:28:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 920238b2-7f1c-3ba1-b8ea-89065d0568aa | -10.124 | -44.55779 | 2025-10-16 03:28:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 74bfd84f-bf2c-30c7-807c-7c54cb5316e0 | -8.45596 | -44.186 | 2025-10-16 03:28:00 | NPP-375D | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 13.6 |
| 620a0663-5900-33a2-83dd-3949296fe12f | -10.0348 | -43.83466 | 2025-10-16 03:28:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2b72cf11-1412-3648-8864-56eec91b7a12 | -10.61102 | -42.31968 | 2025-10-16 03:28:00 | NPP-375D | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 3d4c7c12-e874-3716-9b6f-960c7ba9502c | -7.941 | -44.13363 | 2025-10-16 03:28:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 9330898b-51a2-36e8-b19f-72c1f8e95d76 | -14.07732 | -44.28381 | 2025-10-16 03:28:00 | NPP-375D | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 4a072042-a7b2-339b-b190-d459c876a39d | -7.48537 | -42.75953 | 2025-10-16 03:28:00 | NPP-375D | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 7.1 |
| a4799da7-8a58-3d3c-9ece-02cc79662be5 | -14.01268 | -42.14841 | 2025-10-16 03:28:00 | NPP-375D | LAGOA REAL | BAHIA | Brasil | 2918753 | 29 | 33 | nan | nan | nan | Caatinga | 11.1 |
| 174e25fd-dad4-3432-8121-ed014262191f | -10.63527 | -44.41835 | 2025-10-16 03:28:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8e5e0950-843e-361d-a3ea-9e2e7878f8e6 | -10.12005 | -44.57732 | 2025-10-16 03:28:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 0d560e3d-9d0d-33ac-8d15-08b0627b6ec2 | -11.58096 | -44.06617 | 2025-10-16 03:28:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| be3c9b71-af5b-3c07-ab6f-8cf09ccceb37 | -10.82817 | -43.95313 | 2025-10-16 03:28:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c9b1c660-7e40-3642-8c2b-8e3995894a11 | -7.40986 | -44.75381 | 2025-10-16 03:28:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 978ae1c3-5047-36ab-a306-6879a0e343b3 | -10.51566 | -43.36686 | 2025-10-16 03:28:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cfa35c18-e911-30d4-8c50-4bfb6050f1bc | -11.58367 | -44.08516 | 2025-10-16 03:28:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 5f5f9a38-4752-3d3a-9b25-c068216813da | -7.96036 | -44.14412 | 2025-10-16 03:28:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 662978c6-2e8c-33ae-91cb-d5c631856f5c | -7.40276 | -44.75203 | 2025-10-16 03:28:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 6132ca7c-8c75-3be5-971f-6db090121ce8 | -14.63879 | -42.39775 | 2025-10-16 03:28:00 | NPP-375D | LICÍNIO DE ALMEIDA | BAHIA | Brasil | 2919405 | 29 | 33 | nan | nan | nan | Caatinga | 2.0 |
| b7747205-8684-3a1a-86ba-8513170708b4 | -14.00832 | -42.1484 | 2025-10-16 03:28:00 | NPP-375D | LAGOA REAL | BAHIA | Brasil | 2918753 | 29 | 33 | nan | nan | nan | Caatinga | 5.0 |
| 2ec51680-32dc-3561-a5b5-378ffe281f23 | -12.35475 | -38.27943 | 2025-10-16 03:28:00 | NPP-375D | POJUCA | BAHIA | Brasil | 2925204 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 74869730-9988-32a1-bd72-a49187ab6435 | -11.50682 | -44.06699 | 2025-10-16 03:28:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 09161fc4-f71d-3447-b988-07846db248a3 | -12.22361 | -43.30832 | 2025-10-16 03:28:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d9817b52-5d80-3bc1-8fce-b0a117c10cae | -13.89701 | -45.57693 | 2025-10-16 03:28:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6e916abf-9751-3430-90f7-84aceea9f63f | -10.62159 | -45.25632 | 2025-10-16 03:28:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 5.6 |
| e2489104-f196-3c0a-889a-e62c3e10c281 | -13.04504 | -43.0271 | 2025-10-16 03:28:00 | NPP-375D | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 3683ebff-566b-3a46-bf3f-1cc116e3bb30 | -15.08705 | -42.12476 | 2025-10-16 03:28:00 | NPP-375D | CONDEÚBA | BAHIA | Brasil | 2908705 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 5625849d-54f9-34eb-80c0-5861b46387a1 | -8.46795 | -44.19726 | 2025-10-16 03:28:00 | NPP-375D | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 24.2 |
| 6927b552-1f35-3fc7-983e-f08b679e99ca | -9.68689 | -44.53763 | 2025-10-16 03:28:00 | NPP-375D | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 11.9 |
| ee7aa359-2be2-3106-b633-aa88bc5e41ae | -8.4612 | -44.19545 | 2025-10-16 03:28:00 | NPP-375D | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 14.5 |
| 740913f0-bebf-36f5-a89a-aab2205bc345 | -7.34811 | -43.85952 | 2025-10-16 03:28:00 | NPP-375D | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 463aafe5-326c-366d-9cfe-d3c7c50e7337 | -10.53083 | -44.51376 | 2025-10-16 03:28:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5bc9f7ee-6c11-39b1-b368-ba6b78ad12fd | -8.1984 | -43.32173 | 2025-10-16 03:28:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 4b7045a8-4e3f-32a1-9a53-9fa1f72b596b | -11.43982 | -44.17085 | 2025-10-16 03:28:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 1d9b87f9-4eaf-39e7-9986-335e8d6f33b5 | -8.44815 | -44.1913 | 2025-10-16 03:28:00 | NPP-375D | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 73e351c3-a6bb-3dd7-897e-e5b5254e26d8 | -9.15899 | -41.05968 | 2025-10-16 03:28:00 | NPP-375D | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 5.9 |
| 98549000-4da5-32d2-b321-edcd8c5ceaf5 | -8.25395 | -44.09343 | 2025-10-16 03:28:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 0f20af49-531b-3b27-a963-34122d11cd28 | -10.61561 | -42.31392 | 2025-10-16 03:28:00 | NPP-375D | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 8dd8c222-2221-30a3-8894-57a814594388 | -11.57451 | -44.06481 | 2025-10-16 03:28:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 5.9 |
| fa216119-9ec0-3f0b-a327-1fbd3f28662d | -7.54714 | -42.06263 | 2025-10-16 03:28:00 | NPP-375D | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 33de7a91-ff7d-3f11-a968-01f544448d26 | -9.14998 | -41.06488 | 2025-10-16 03:28:00 | NPP-375D | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 12.3 |
| 2b6c729c-e98a-34af-9756-dec5ab3db4ff | -10.50644 | -43.38046 | 2025-10-16 03:28:00 | NPP-375D | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fda465b5-4e27-38dc-bfc9-05b51be0b533 | -10.82936 | -44.00663 | 2025-10-16 03:28:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7dbcfcbf-55f8-357f-a645-8cda4a37de4f | -7.9696 | -44.13331 | 2025-10-16 03:28:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| e6b31a03-3613-3a58-b5f5-7090ec1f39e5 | -11.59124 | -44.08109 | 2025-10-16 03:28:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 531f1d7e-2852-3f96-918e-fc4cdb9bcb83 | -9.15271 | -41.06238 | 2025-10-16 03:28:00 | NPP-375D | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 5.9 |
| 49410d5f-6fea-36cb-addd-ad4851283254 | -10.0425 | -43.83017 | 2025-10-16 03:28:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 46026662-6489-327f-8eb3-418226f8a254 | -7.96271 | -44.13202 | 2025-10-16 03:28:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 69fbe252-fec3-3c4c-b154-62c849b98959 | -10.50802 | -43.38193 | 2025-10-16 03:28:00 | NPP-375D | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 021192fb-1e6c-3a33-b92c-fc54de79ece8 | -10.82286 | -43.94584 | 2025-10-16 03:28:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e5dffd38-a418-3b94-83d1-94cf8ee81ed9 | -11.58255 | -44.09062 | 2025-10-16 03:28:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 5ffbd0aa-5296-317b-bf84-c96b590a19c7 | -7.94539 | -44.14768 | 2025-10-16 03:28:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 14.3 |
| fcca1754-7872-35b1-b63e-1e135b58a0c4 | -8.21267 | -43.31798 | 2025-10-16 03:28:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 2b867522-303f-340b-a5e7-6890e6b4593a | -11.43556 | -44.1583 | 2025-10-16 03:28:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 07cec792-44ce-3ac9-9f1e-ca8666214e39 | -8.55343 | -44.58653 | 2025-10-16 03:28:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 8c6ea29e-b222-3d0b-9f72-73c10981a1b7 | -4.3874 | -43.3827 | 2025-10-16 03:30:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 381.3 |
| 89324f1c-80f1-3428-98ba-403d589f3afe | -4.4061 | -43.3816 | 2025-10-16 03:30:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 81.3 |
| 0cf8baab-354e-3cfb-8881-74c46f36fa59 | -4.4059 | -43.4049 | 2025-10-16 03:30:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 93.3 |
| 11c60e6b-9791-3ba5-bfef-274bed94160c | -4.6811 | -44.105 | 2025-10-16 03:30:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 69.2 |
| b6a436c0-df5d-337f-aefd-85baa05504c2 | -5.6821 | -45.0893 | 2025-10-16 03:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 63.0 |
| 25125dda-a9f4-3cef-98e2-9dc0ea6d5be6 | -4.6626 | -44.0832 | 2025-10-16 03:30:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 148.9 |
| f8393788-322c-32bb-b944-21a290362536 | -7.9439 | -44.1381 | 2025-10-16 03:30:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 61.4 |
| b2306ee0-950a-3d10-a87c-e4444e6d6ac2 | -4.116 | -48.0352 | 2025-10-16 03:30:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 101.0 |
| 555e2f0d-a936-3d94-a6ae-a6f47d442fc8 | -6.1534 | -40.8971 | 2025-10-16 03:30:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 94.0 |
| f140cd0f-0726-3c7e-8938-e75659914a52 | -5.4762 | -42.9367 | 2025-10-16 03:30:00 | GOES-19 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 56.3 |
| c0f4f99b-d376-3ae7-a28b-af5c2deeda9e | -7.3955 | -39.6845 | 2025-10-16 03:30:00 | GOES-19 | EXU | PERNAMBUCO | Brasil | 2605301 | 26 | 33 | nan | nan | nan | Caatinga | 66.5 |
| c43913c3-98c9-3239-ab94-c0c29c5a7a0d | -6.1532 | -40.9215 | 2025-10-16 03:30:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 53.4 |
| 1c0724b1-4c17-3418-9523-8e16095cb920 | -4.3872 | -43.406 | 2025-10-16 03:30:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 388.7 |
| d06b854e-5f53-3707-b72c-0045ca5f6b43 | -6.1112 | -47.2897 | 2025-10-16 03:30:00 | GOES-19 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 99.9 |
| d4234536-397b-39dd-8682-080eef3f4b70 | -12.6805 | -43.4235 | 2025-10-16 03:30:00 | GOES-19 | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 67.0 |
| df26d1af-0833-3c93-8fde-0fdb10bb5b7b | 1.8218 | -55.7431 | 2025-10-16 03:30:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 65.0 |
| 8e26ac48-a87a-368c-899f-88804a82181a | -6.1723 | -40.8954 | 2025-10-16 03:30:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 49.2 |
| 2e89d20f-c821-3c42-bfae-d867a15cc033 | -4.3687 | -43.3838 | 2025-10-16 03:30:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 345.7 |
| 55984b20-484a-3558-8677-ff426777c8aa | -8.4717 | -44.1746 | 2025-10-16 03:30:00 | GOES-19 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 80.8 |
| 014302e6-8503-3cff-8adc-a6cbbb078716 | -5.8802 | -43.8613 | 2025-10-16 03:30:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 39.2 |
| 80c4000d-92b7-305b-959a-661b252bc3db | -8.4714 | -44.1978 | 2025-10-16 03:30:00 | GOES-19 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 69.3 |
| 97dad719-f01b-395e-90ad-1f03e04e432c | -5.8799 | -43.8844 | 2025-10-16 03:30:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 43.7 |
| 17055d15-8416-3b76-b56f-41e33e70aa0b | -5.6819 | -45.112 | 2025-10-16 03:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 54.7 |
| a032082e-5980-315f-a0e0-7d754fab93f2 | -4.1161 | -48.0136 | 2025-10-16 03:30:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 141.3 |
| 85d34d35-90ba-398e-bb45-ec40015613e2 | -4.6813 | -44.082 | 2025-10-16 03:30:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 52.5 |
| e8166ba5-499b-3dd5-a794-8afc8b84528f | -8.1996 | -43.3189 | 2025-10-16 03:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 68.0 |
| e5fee78e-7a80-3e97-9505-15d9051fa85e | -3.0157 | -45.3903 | 2025-10-16 03:30:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 176.7 |
| 56348197-de96-3c67-8b43-20d032d946a9 | -4.6624 | -44.1062 | 2025-10-16 03:30:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 201.5 |
| 14227090-7840-3826-84e3-0735695541a4 | -2.9971 | -45.391 | 2025-10-16 03:30:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 46.4 |
| 6d0d1e5a-2085-306d-a1c2-7a8b8e417c84 | -3.0158 | -45.3679 | 2025-10-16 03:30:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 90.9 |
| bb88d1f0-dd0d-3303-9b88-dffe45998528 | -8.4528 | -44.1767 | 2025-10-16 03:30:00 | GOES-19 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 73.0 |


[Clique aqui para ver as próximas entradas](README19.md)
